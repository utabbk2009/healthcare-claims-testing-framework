# Healthcare Claims Testing Framework

## Overview

This project demonstrates how Python and SQL can be used to automate healthcare claims data validation and quality testing.

The framework generates synthetic claims data, loads it into a SQLite database, executes automated SQL validation rules, and produces audit-ready PASS/FAIL reports.

## Business Problem

Healthcare organizations rely on accurate claims data for payment processing, member services, provider reporting, and analytics. Poor data quality can result in claim errors, payment delays, reporting inaccuracies, and compliance risks.

This project simulates a real-world healthcare claims testing process by identifying data quality issues before data reaches downstream systems.

## Technologies Used

- Python
- SQL
- SQLite
- Pandas
- Pytest
- Data Validation
- Quality Assurance Testing

## Project Workflow

Claims Data
↓
Python Data Generation
↓
SQLite Database
↓
SQL Validation Rules
↓
Automated Testing
↓
PASS / FAIL Report

## Validation Rules

The framework automatically validates:

- Missing Member IDs
- Duplicate Claim IDs
- Negative Payment Amounts
- Invalid Claim Status Values
- Invalid Date Sequences
- Source-to-Target Record Counts
- Missing Claim IDs

## Test Results

The warehouse dataset intentionally contains data quality defects to verify that validation rules successfully detect errors.

Results generated:

- 8 Data Validation Rules Executed
- 2 Rules Passed
- 6 Rules Failed
- Defects Successfully Identified

## Pytest Automation Results

The framework was tested using pytest to verify validation logic and execution.

Result:

- 2 Automated Tests Passed
- 0 Automated Tests Failed

## Screenshots

### Validation Report

screenshots/validation_report.png

### Pytest Results

screenshots/pytest_results.png

## Skills Demonstrated

- Python Programming
- SQL Development
- Healthcare Claims Analysis
- Data Quality Testing
- ETL Validation
- Software Testing
- Automation
- Analytics

## Resume Summary

Built an automated healthcare claims testing framework using Python, SQL, SQLite, pandas, and pytest. Developed reusable validation rules to identify duplicates, missing values, claim-status issues, payment anomalies, and source-to-target discrepancies while generating audit-ready test reports.

## Author

Bruce Knox II
BS Data Science
Healthcare Claims Analyst | Data Analyst | QA Analyst
