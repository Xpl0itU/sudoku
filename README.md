# sudoku
Validates if a sudoku is valid or not.

## Usage
```bash
python3 sudoku.py # Will run tests in the tests directory
```

## Testing
Each file must be run from its own directory, tests are in the `tests` directory.
```bash
python3 sudoku.py # OK
python3 src/check_columns.py # NOT OK
cd src
python3 check_columns.py # OK
```