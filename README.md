# CSV Cleaning Pipeline (GitHub Actions)

This project automatically cleans uploaded CSV files using GitHub Actions. It's a serverless, cloud-free alternative to AWS Lambda for data cleaning.

## 📌 What It Does

- Watches the `raw/` folder for new CSV files
- Cleans the data:
  - Removes duplicates
  - Filters invalid rows
  - Keeps only `id` and `score` columns
  - Ensures `score` is between 0 and 100
- Saves cleaned files to the `processed/` folder

All cleaning happens **automatically** using a GitHub Actions workflow.

---

## 📁 Folder Structure

csv-cleaner/
│
├── raw/                  # Put test.csv here
│
├── processed/            # Cleaned files will go here
│
├── clean_csv.py          # The actual cleaner code
│
├── .github/
│   └── workflows/
│       └── clean.yml     # GitHub Action config
│
├── requirements.txt      # Dependencies (only if needed)