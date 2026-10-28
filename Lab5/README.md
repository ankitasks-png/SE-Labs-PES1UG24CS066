# Lab 5 — Static Code Analysis: Warehouse Asset Maintenance Registry

## Overview

This lab applies static code analysis tools to a Python-based warehouse asset maintenance system. The program registers assets, tracks service dates, identifies overdue inspections, and exports maintenance reports.

## Tools Used

- **Pylint:** Checks code quality and reports potential issues.
- **Bandit:** Checks for potential security vulnerabilities.
- **Flake8:** Checks Python style and formatting.

## Files

| File | Description |
|---|---|
| `maintenance_system.py` | Revised Python program |
| `issues.md` | Documented issues identified during analysis |
| `reflection.md` | Lab reflection |
| `pylint_report_before.txt` | Initial Pylint report |
| `bandit_report_before.txt` | Initial Bandit report |
| `flake8_report_before.txt` | Initial Flake8 report |
| `pylint_report_after.txt` | Final Pylint report |
| `bandit_report_after.txt` | Final Bandit report |
| `flake8_report_after.txt` | Final Flake8 report |

## Final Results

- **Pylint:** 10.00/10
- **Bandit:** Zero reported issues
- **Flake8:** No style violations reported

## Run the Program

Activate the virtual environment and run:

```powershell
python maintenance_system.py
```

## Run the Analysis Tools

Run Pylint:

```powershell
python -m pylint maintenance_system.py
```

Run Bandit:

```powershell
python -m bandit -r maintenance_system.py
```

Run Flake8:

```powershell
python -m flake8 maintenance_system.py
```

## Generate Final Reports

```powershell
python -m pylint maintenance_system.py > pylint_report_after.txt
python -m bandit -r maintenance_system.py > bandit_report_after.txt
python -m flake8 maintenance_system.py > flake8_report_after.txt
```
