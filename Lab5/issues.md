# Lab 5: Static Code Analysis — Issues Log

## Initial Analysis

### Issues Identified

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Dangerous mutable default argument | Code quality / Bug | 10 | A function uses an empty list as a default argument, which can be shared between calls. | Use `None` as the default and initialise a new list inside the function. |
| Bare exception handler | Code quality | 18 | An exception is caught without specifying its type. | Catch the appropriate specific exception. |
| Insecure temporary file creation | Security — Medium | 40 | `tempfile.mktemp()` can introduce a race condition when creating temporary files. | Use a safer temporary-file creation method. |
| Use of assert for validation | Security / Reliability — Low | 61 | An assertion is used to check whether assets exist, but assertions can be disabled in optimised execution. | Replace it with an explicit condition and suitable error handling. |
| Unused import | Code quality / Style | 2 | The `logging` module is imported but not used. | Remove the unused import or use it appropriately. |
| Missing docstrings | Code quality | Multiple | The module and functions lack documentation strings. | Add meaningful module and function docstrings. |
| File handling without context managers | Code quality | 34, 41 | Files are opened without using a `with` statement. | Use context managers to ensure files are closed properly. |
| Missing file encoding | Code quality | 34, 41 | File operations do not explicitly specify an encoding. | Specify an appropriate encoding, such as UTF-8. |
| Global statement | Code quality | 30 | A function modifies a global variable. | Refactor state management to avoid unnecessary global variables. |
| Inconsistent formatting | Style | Multiple | Blank lines and line length violate Flake8 conventions. | Apply PEP 8 formatting and rerun Flake8. |
| Non-snake_case function name | Style | 46 | `printAlerts` does not follow Python's snake_case naming convention. | Rename it to `print_alerts` and update its calls. |

## Verification Plan

After applying fixes, rerun Pylint, Bandit, and Flake8. Compare the final reports with the initial reports to verify which issues have been resolved.