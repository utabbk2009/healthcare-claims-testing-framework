# Healthcare Claims Testing Framework

## Overview

This project demonstrates how Python and SQL can be used to automate healthcare claims data validation and quality testing.

The framework generates synthetic claims data, loads it into a database, executes automated SQL validation rules, and produces audit-ready PASS/FAIL testing reports.

## Technologies

- Python
- SQL
- SQLite
- Pandas
- Pytest

## Key Features

- Claims data generation
- Automated data quality testing
- Duplicate detection
- Missing data validation
- Invalid status detection
- Source-to-target reconciliation
- Automated reporting

## Sample Business Rules

- Member ID cannot be blank
- Claim IDs must be unique
- Paid Amount cannot be negative
- Claim Status must be PAID, DENIED, or PENDING

## Results

The framework intentionally injects defects into the warehouse dataset and successfully detects:

- Missing Member IDs
- Duplicate Claims
- Negative Payments
- Invalid Status Values
- Date Sequence Errors

## Skills Demonstrated

- Data Validation
- ETL Testing
- SQL Development
- Python Automation
- Healthcare Claims Analysis
- Quality Assurance

## Author

Bruce Knox II
BS Data Science
Healthcare Claims Analyst | Data Analyst | QA Analyst
