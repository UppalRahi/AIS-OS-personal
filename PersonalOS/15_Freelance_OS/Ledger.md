# Freelance OS Ledger

A master registry of all custom automation, consulting, and GTM integration client projects.

---

## 📊 Summary Statistics

- **Total Revenue (INR)**: ₹30,000+
- **Total Revenue (USD)**: $290+
- **Total Completed Projects**: 2
- **Active Clients**: 0 (Amply is tracked under main [Finance & Assets](file:///Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/PersonalOS/10_Life_OS/Finance%20&%20Assets.md))

---

## 🗂️ Master Projects Database

| Client | Project Name | Period | Revenue | Hours | Status | Tech Moat |
|---|---|---|---|---|---|---|
| [PMAPS](file:///Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/PersonalOS/15_Freelance_OS/Clients/PMAPS.md) | LinkedIn BDR Automation | Mar – Apr | ₹30,000 | 10 | Completed | Unipile API + n8n BDR scheduling logic |
| [HeyReach](file:///Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/PersonalOS/15_Freelance_OS/Clients/HeyReach.md) | n8n Partner Templates | Oct – Nov | $290 USD | 2 | Completed | n8n Creator authority |

---

## 🔮 Dynamic Vault Query (Dataview)

> [!NOTE]
> Once you install the **Dataview** community plugin in Obsidian, the query below will automatically generate a dynamic table of all your client files inside the `15_Freelance_OS/Clients/` folder based on their frontmatter metadata.

```dataview
TABLE period AS "Period", revenue AS "Revenue", hours_spent AS "Hours Spent", status AS "Status"
FROM "15_Freelance_OS/Clients"
SORT file.name ASC
```
