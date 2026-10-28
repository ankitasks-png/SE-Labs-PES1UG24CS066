# Reflection — Lab 5: Static Code Analysis

## 1. What did you learn from static code analysis?

I learned that static code analysis tools can identify code-quality, security, and formatting issues without requiring the program to be executed. Pylint helped improve code quality, Bandit identified potential security risks, and Flake8 detected style violations.

## 2. Which tool was most useful, and why?

Pylint was useful for identifying code-quality problems such as missing docstrings, duplicate function definitions, and the use of a global statement. Bandit helped identify unsafe temporary-file handling, while Flake8 helped enforce consistent formatting.

## 3. What challenges did you face while fixing the issues?

I encountered duplicate function definitions, indentation errors, and blank-line violations. I resolved these issues by reviewing the code, correcting the function definitions and indentation, and rerunning the tools to verify the changes.

## 4. How did the final results differ from the initial results?

Initially, Pylint rated the code 6.55/10, Bandit reported potential security issues, and Flake8 reported formatting violations. After making improvements, Pylint rated the code 10.00/10, Bandit reported zero issues, and Flake8 produced no violations.
