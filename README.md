# sudoku
Validates if a sudoku is valid or not.

## Usage
```bash
python3 -m pip install -U -r requirements.dev.txt
python3 sudoku.py # Will run tests in the tests directory
```

## Testing
Tests are run with Coverage, which uses PyTest, and the main `sudoku.py` also contains its own tests.
```bash
coverage run # OK
coverage report # Get report of test code coverage
python3 sudoku.py # OK
```
