# L6_L7_08 — Ski Resort Pass

**Course:** Software Engineering Lab\
**Application:** Ski Resort Pass\
**Student:** Ankita S\
**SRN:** PES1UG24CS066\
**Institution:** PES University

## Objective

Analyse the code coverage and branch coverage of the Ski Resort Pass
application using Python, Pytest, and Coverage.py. The test suites are
designed to exercise application statements, conditional branches,
boundary values, and invalid-input scenarios.

## Tools and Technologies

  Tool             Purpose
  ---------------- -------------------------------------------
  Python 3.12.6    Programming language
  Pytest           Test execution framework
  Coverage.py      Statement and branch coverage measurement
  VS Code          Code editing
  Git and GitHub   Version control and submission

## Project Files

The Lab 6 folder should contain the following files:

  ----------------------------------------------------------------------------
  File                                     Description
  ---------------------------------------- -----------------------------------
  `ski_resort_pass.py`                     Application source code being
                                           tested

  `test_ski_resort.py`                     Original/provided test file, if
                                           required

  `CodeCoverageTest_08_application.py`     Additional tests maintained for
                                           code coverage

  `BranchCoverageTest_08_application.py`   Additional tests maintained for
                                           branch coverage

  `CodeCoverage_08.png`                    Screenshot of the final code
                                           coverage report

  `BranchCoverage_08.png`                  Screenshot of the final branch
                                           coverage report

  `README.md`                              Lab documentation
  ----------------------------------------------------------------------------

## Setup

Open a terminal in the `Lab 6` directory and install the required
packages:

``` bash
python -m pip install pytest coverage
```

## Running the Tests

### 1. Code coverage

Run the code coverage test file:

``` bash
coverage erase
coverage run -m pytest CodeCoverageTest_08_application.py
coverage report -m
```

Save a terminal screenshot showing the test result and final coverage
percentage as:

``` text
CodeCoverage_08.png
```

### 2. Branch coverage

Run the branch coverage test file with branch measurement enabled:

``` bash
coverage erase
coverage run --branch -m pytest BranchCoverageTest_08_application.py
coverage report --branch -m
```

Save a terminal screenshot showing the test result and final branch
coverage percentage as:

``` text
BranchCoverage_08.png
```

> Run the code coverage and branch coverage commands separately.
> `coverage erase` clears the previous run's data so the two reports are
> independent.

## Sample Results

The sample report prepared for this lab displays the following
illustrative results:

  Coverage type       Tests passed   Sample coverage
  ----------------- -------------- -----------------
  Code coverage                 18              100%
  Branch coverage               23              100%

**Important:** These percentages and the terminal-style images in the
dummy report are examples. Replace them with the results and screenshots
from your own actual test execution before submitting the lab.

## Methodology

1.  Set up the Python environment and install Pytest and Coverage.py.
2.  Run the initial tests to identify statements and branches that are
    not exercised.
3.  Add test cases for valid inputs, invalid inputs, boundary values,
    and conditional outcomes.
4.  Run the code coverage tests and generate a statement coverage
    report.
5.  Run the branch coverage tests with branch measurement enabled.
6.  Capture the final terminal output and record the coverage
    percentages.

## Submission Checklist

-   [ ] Application source file is present.
-   [ ] `CodeCoverageTest_08_application.py` is included.
-   [ ] `BranchCoverageTest_08_application.py` is included.
-   [ ] Code coverage screenshot is included and shows the actual final
    percentage.
-   [ ] Branch coverage screenshot is included and shows the actual
    final percentage.
-   [ ] Both test suites have been executed successfully.
-   [ ] README and required deliverables are committed and pushed to
    GitHub.

## Conclusion

The two test suites are intended to measure statement coverage and
branch coverage for the Ski Resort Pass application. The final submitted
screenshots should be captured from the actual terminal execution and
should clearly show the resulting coverage percentages.
