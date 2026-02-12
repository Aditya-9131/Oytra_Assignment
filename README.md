# Member Cleanup Assignment

## Overview
The Member Cleanup Assignment is designed to streamline and optimize the management of user data within our application. As our user base grows, it becomes increasingly important to maintain clean and accurate member records. This assignment focuses on implementing a cleanup mechanism that removes inactive or unwanted members from the database while ensuring the integrity of the remaining data.

## Objectives
- To implement a systematic approach for identifying and removing inactive members.
- To enhance the performance of our application by reducing the amount of data stored.
- To ensure compliance with data protection regulations by effectively managing personal user information.

## Detailed Cleaning Logic
1. **Identification of Inactive Members**: Members will be flagged as inactive based on their last login date or activity within the application. A configurable threshold (e.g., 90 days of inactivity) will determine this status.
2. **Data Backup**: Before removal, a backup of the member data will be created to prevent accidental data loss.
3. **User Confirmation**: Inactive members will be notified via email about their impending removal, giving them an option to reactivate their accounts within a specified period.
4. **Cleanup Execution**: After the grace period, inactive members will be permanently removed from the database.

## Technologies
- **Programming Language**: Python
- **Web Framework**: Flask
- **Database**: PostgreSQL
- **Task Scheduler**: Celery or a cron job for regular cleanup tasks

## Usage Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Aditya-9131/Oytra_Assignment.git
   cd Oytra_Assignment
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure the application settings including database credentials in `config.py`.
4. Run the cleanup task manually or set it to run at scheduled intervals.
   ```bash
   python cleanup_script.py
   ```

## Examples
- Example of running the cleanup manually:
   ```bash
   python cleanup_script.py
   ```
- Example of a member receiving a notification:
   An email notification will be sent to inactive members informing them about their account status.

## Output Explanations
The output of the cleanup process will include:
- A log of members who were flagged as inactive.
- A summary of actions taken (e.g., removed, notified).
- Data backups will be stored securely for audit purposes.

## Business Impact
Implementing the Member Cleanup Assignment will lead to:
- Improved application performance due to a leaner database.
- Enhanced user engagement as members are encouraged to remain active.
- Compliance with regulations and reduced risk of data breaches or fines for data mismanagement.