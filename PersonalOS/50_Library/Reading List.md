# Reading List

A curated library to feed the *Doctorate* archetype—deeply learning philosophy, productivity, business frameworks, and technology to refine your life steering, startup execution, and communication.

---

## 🗂️ Master Reading Ledger

| Book Title | Author | Genre | Status | Rating | Summary Link |
|---|---|---|---|---|---|
| **Meditations** | Marcus Aurelius | Philosophy | Wishlist | — | [Link](file:///Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/PersonalOS/50_Library/Clients/) |
| **Atomic Habits** | James Clear | Productivity | Wishlist | — | — |
| **The Personal MBA** | Josh Kaufman | Business | Wishlist | — | — |
| **Zero to One** | Peter Thiel | Business / Startups | Wishlist | — | — |
| **Principles** | Ray Dalio | Philosophy / Business | Wishlist | — | — |
| **Deep Work** | Cal Newport | Productivity | Wishlist | — | — |

---

## 📚 Curated Shelves & Recommendations

### 1. Philosophy & Mindset
*Focus: Staying humble like Lord Hanuman, training the mind, developing resilience.*
- **Meditations** by Marcus Aurelius *(Stoicism, self-discipline, steering under pressure)*
- **Bhagavad Gita** *(Duty without attachment, focus on actions over fruits of labor)*
- **Man's Search for Meaning** by Viktor Frankl *(Finding purpose in constraints)*

### 2. Business Thinking & Venture Building
*Focus: Finding deep USPs, scaling systems, running startups.*
- **The Personal MBA** by Josh Kaufman *(Comprehensive mental models of business)*
- **Zero to One** by Peter Thiel *(Creating proprietary technology, vertical progress, moats)*
- **The Lean Startup** by Eric Ries *(Hypothesis testing, fast execution)*
- **Good to Great** by Jim Collins *(Disciplined people, disciplined thought, disciplined action)*

### 3. Productivity & Discipline
*Focus: Building routines like an Army Officer, maximizing deep focus.*
- **Atomic Habits** by James Clear *(Compounding small positive routines, environment design)*
- **Deep Work** by Cal Newport *(Sustained cognitive focus, eliminating shallow distraction)*
- **The 5 AM Club** by Robin Sharma *(Structured morning routines and performance optimization)*

### 4. Technical Stack & AI Systems
*Focus: Mastering custom APIs, robotics, data layers, and orchestration.*
- **Designing Data-Intensive Applications** by Martin Kleppmann *(System design, database engines)*
- **Enterprise Integration Patterns** by Gregor Hohpe *(Messaging, workflow integration routing)*

---

## 🔮 Dynamic Reading Log (Dataview)

> [!NOTE]
> Once you install the **Dataview** community plugin in Obsidian, the query below will automatically generate a dynamic table of all books in your `50_Library/` system that are marked as `Wishlist`, `Reading`, or `Completed` in their frontmatter.

```dataview
TABLE author AS "Author", genre AS "Genre", status AS "Status", rating AS "Rating"
FROM "50_Library"
WHERE file.name != "Reading List" AND file.name != "Book Notes Template"
SORT status DESC
```
