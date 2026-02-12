Member Cleanup Script
📌 Overview

This project cleans messy signup data exported from multiple landing pages and generates a CRM-ready “Golden Record” file.

The dataset contained inconsistent date formats, duplicate users, fake/test entries, invalid emails, and malformed rows. The script processes this data and produces clean, structured output files.

Main script: 

member_cleanup

🎯 Objective

To transform raw, inconsistent signup data into:

A clean and deduplicated CRM-ready dataset

A separate quarantine file for low-quality or suspicious leads

📂 Input File

signups.xls (CSV data disguised as .xls)

📤 Output Files

members_final.csv

Cleaned data

Standardized dates (YYYY-MM-DD)

No duplicates

Multi-plan users flagged

quarantine.csv

Fake/test entries

Invalid emails

Corrupted or incomplete rows

🛠 Cleaning Logic Applied
1️⃣ Date Standardization

All signup dates are converted into YYYY-MM-DD format for consistency and accurate reporting.

2️⃣ Deduplication

Email is used as a unique identifier.
If a user appears multiple times:

The most recent signup is kept

Older records are removed

3️⃣ Low-Quality Lead Detection

Records are flagged as low-quality if:

Name contains test/dummy keywords

Email format is invalid

Signup date is missing

These rows are moved to quarantine.csv.

4️⃣ Multi-Plan Handling

If a user signed up for both Plan A and Plan B:

Only the most recent signup is kept

A flag is_multi_plan = True is added

⚙️ Technologies Used

Python 3.x

Pandas

Regular Expressions (re module)

▶️ How to Run
1. Install dependencies
pip install pandas

2. Run the script
python member_cleanup.py

3. Generated Files

After execution:

members_final.csv
quarantine.csv

💼 Business Impact

This script ensures:

High-quality CRM data

No duplicate customer records

Improved sales productivity

More accurate marketing analytics

Better decision-making based on clean data

📚 Key Learnings

Real-world data is often messy and inconsistent

Data validation is critical before CRM ingestion

Business rules must be carefully preserved during deduplication

Data quality is more important than data quantity
