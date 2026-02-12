# member_cleanup.py

import pandas as pd
import re

INPUT_FILE = "signups.xls"  # CSV disguised as .xls
FINAL_OUTPUT = "members_final.csv"
QUARANTINE_OUTPUT = "quarantine.csv"


def standardize_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^\w]", "", regex=True)
    )
    return df


def is_valid_email(email):
    if pd.isna(email):
        return False
    pattern = r"^[^@]+@[^@]+\.[^@]+$"
    return re.match(pattern, str(email).strip()) is not None


def is_low_quality(row):
    garbage_keywords = ["test", "dummy", "asdf", "qwerty", "fake", "abc", "1234"]

    combined = f"{row.get('name','')} {row.get('email','')}".lower()

    if any(word in combined for word in garbage_keywords):
        return True

    if not is_valid_email(row.get("email")):
        return True

    if pd.isna(row.get("signup_date")):
        return True

    return False


def process_file():
    # 🔥 Robust CSV Loader (handles broken rows safely)
    df = pd.read_csv(
        INPUT_FILE,
        engine="python",     # safer parser
        on_bad_lines="skip"  # skip malformed rows
    )

    df = standardize_columns(df)

    required_columns = {"email", "signup_date", "plan"}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"Missing required columns: {required_columns}")

    # Standardize date
    df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce")

    # Flag low quality
    df["is_low_quality"] = df.apply(is_low_quality, axis=1)

    quarantine_df = df[df["is_low_quality"]].copy()
    clean_df = df[~df["is_low_quality"]].copy()

    quarantine_df.to_csv(QUARANTINE_OUTPUT, index=False)

    # Sort by latest signup
    clean_df.sort_values("signup_date", ascending=False, inplace=True)

    # Multi-plan detection
    plan_counts = clean_df.groupby("email")["plan"].nunique().reset_index()
    multi_plan_emails = set(plan_counts[plan_counts["plan"] > 1]["email"])

    clean_df["is_multi_plan"] = clean_df["email"].isin(multi_plan_emails)

    # Keep most recent record
    final_df = clean_df.drop_duplicates(subset=["email"], keep="first").copy()

    # Format date
    final_df["signup_date"] = final_df["signup_date"].dt.strftime("%Y-%m-%d")

    final_df.drop(columns=["is_low_quality"], inplace=True)

    final_df.to_csv(FINAL_OUTPUT, index=False)

    print("✅ Cleaning completed successfully.")
    print("Generated members_final.csv")
    print("Generated quarantine.csv")


if __name__ == "__main__":
    process_file()
