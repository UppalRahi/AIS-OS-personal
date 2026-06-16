#!/usr/bin/env python3
"""
Send NRF Campaign Emails via Gmail SMTP
--------------------------------------
Loads the prepared batch of 10 leads from batch_10_leads.csv.
Replaces placeholders with actual recipient information.
Connects to smtp.gmail.com and sends Email 1 using a Gmail App Password.
"""

import csv
import os
import sys
import time
import getpass
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

BATCH_CSV = '/Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/nrf_campaign/batch_10_leads.csv'
DEFAULT_SENDER = 'er.rahiuppal@gmail.com'

def replace_placeholders(text, first_name, company_name):
    """Replaces placeholders like [First Name] and [Company Name] with actual values."""
    if not text:
        return ""
    
    # Replace first name variants
    text = re_replace(r'\[\s*first\s*name\s*\]|\{\{\s*first_name\s*\}\}|\[\s*recipient\s*name\s*\]', first_name, text)
    # Replace company name variants
    text = re_replace(r'\[\s*company\s*name\s*\]|\{\{\s*company_name\s*\}\}', company_name, text)
    
    # Dynamically change "this year" to "this week" to make outreach timely (NRF is running right now!)
    text = re_replace(r'\bthis year\b', 'this week', text)
    
    return text

def re_replace(pattern, replacement, text):
    """Helper to perform case-insensitive regex replacements."""
    import re
    return re.sub(pattern, replacement, text, flags=re.IGNORECASE)

def main():
    print("=========================================================")
    print("      NRF Outreach - Send via Personal Email (Gmail)    ")
    print("=========================================================\n")

    if not os.path.exists(BATCH_CSV):
        print(f"Error: Batch file not found at {BATCH_CSV}")
        print("Please run `python3 send_batch.py --dry-run` first to generate the batch.")
        sys.exit(1)

    # Load leads
    leads = []
    with open(BATCH_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            leads.append(row)

    if not leads:
        print("Error: No leads found in batch_10_leads.csv.")
        sys.exit(1)

    print(f"Loaded {len(leads)} leads from batch_10_leads.csv.")
    
    print("\n--- Quick List of Target Emails ---")
    for l in leads:
        print(f" - {l.get('email', '').strip()}")
    print("-----------------------------------\n")

    sender_email = os.environ.get('GMAIL_SENDER', '').strip()
    if not sender_email:
        sender_email_input = input(f"Enter your Gmail address (default: {DEFAULT_SENDER}): ").strip()
        sender_email = sender_email_input if sender_email_input else DEFAULT_SENDER

    app_password = os.environ.get('GMAIL_APP_PASSWORD', '').strip()
    if not app_password:
        print("\nTo send emails via Gmail SMTP, you need a 'Gmail App Password'.")
        print("If you don't have one, create it in Google Account Settings -> Security -> 2-Step Verification -> App Passwords.")
        app_password = getpass.getpass("Enter your Gmail App Password (hidden): ").strip()
        
    if not app_password:
        print("Error: App password is required.")
        sys.exit(1)

    # Test SMTP Connection
    print("\nConnecting to Gmail SMTP server (smtp.gmail.com:587)...")
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.quit()
        print("SMTP Authentication successful!\n")
    except Exception as e:
        print(f"Failed to authenticate with Gmail SMTP: {e}")
        sys.exit(1)

    send_all_mode = os.environ.get('AUTO_SEND', 'false').lower() == 'true'

    for idx, lead in enumerate(leads):
        first_name = lead.get('first_name', '').strip()
        last_name = lead.get('last_name', '').strip()
        company_name = lead.get('company_name', '').strip()
        recipient_email = lead.get('email', '').strip()
        
        # Format display name
        recipient_name = f"{first_name} {last_name}".strip()
        if not recipient_name:
            recipient_name = "there"

        # Parse subject and body
        raw_subject = lead.get('email_1_subject', 'NRF follow-up gap')
        raw_body = lead.get('email_1_body', '')

        subject = replace_placeholders(raw_subject, first_name, company_name)
        body = replace_placeholders(raw_body, first_name, company_name)

        print("---------------------------------------------------------")
        print(f"Lead #{idx+1} of {len(leads)}:")
        print(f"  Recipient: {recipient_name} <{recipient_email}>")
        print(f"  Company:   {company_name}")
        print(f"  Subject:   {subject}")
        print("  Body Preview:")
        body_lines = body.split('\n')
        preview_body = '\n'.join(body_lines[:6])
        print(f"    {preview_body.replace(chr(10), chr(10)+'    ')}...")
        print("---------------------------------------------------------")

        if not send_all_mode:
            choice = input("Send this email? [y (yes) / n (skip) / a (send all remaining) / q (quit)]: ").strip().lower()
            if choice == 'q':
                print("Exiting. No further emails will be sent.")
                break
            elif choice == 'n':
                print(f"Skipped email to {recipient_name}.")
                continue
            elif choice == 'a':
                send_all_mode = True
                print("Send All remaining mode activated. Sending emails...")
            elif choice != 'y' and choice != '':
                print("Invalid option. Skipping lead.")
                continue

        # Send email
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, app_password)

            msg = MIMEMultipart()
            msg['From'] = f"Rahi Uppal <{sender_email}>"
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            server.sendmail(sender_email, recipient_email, msg.as_string())
            server.quit()
            print(f"✓ Successfully sent email to {recipient_name} ({recipient_email})")
            
            # Record the successfully sent email to prevent duplicates in future batches
            with open('/Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/nrf_campaign/sent_log.txt', 'a', encoding='utf-8') as flog:
                flog.write(recipient_email + '\n')
            
            # Sleep between requests to respect rate limits
            if idx < len(leads) - 1:
                time.sleep(3.0)

        except Exception as e:
            print(f"✗ Failed to send email to {recipient_name}: {e}")
            if send_all_mode:
                cont = input("An error occurred. Continue with remaining leads? [y/n]: ").strip().lower()
                if cont != 'y':
                    break

    print("\nFinished outreach process.")

if __name__ == '__main__':
    main()
