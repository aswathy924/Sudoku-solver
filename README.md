# Sudoku Solver

A clean, interactive Sudoku solver built with Python and Streamlit. The app accepts standard 9×9 grids, validates inputs against board constraints, and finds solutions using recursive depth-first backtracking.

---

## Project Structure

```text
Sudoku-solver/
├── app.py
├── requirements.txt
├── README.md
├── src/
│   └── solver.py
├── tests/
│   └── test_solver.py
└── examples/
    ├── easy.txt
    ├── medium.txt
    ├── hard.txt
    └── unsolvable.txt
```

---

## Setup & Installation

### Requirements
* Python 3.9+
* `pip`

### Step-by-Step Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aswathy924/Sudoku-solver.git
   cd Sudoku-solver
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv .venv
   ```

3. **Activate the environment:**
   * **Windows (PowerShell):**
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   * **macOS / Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the App

Launch the Streamlit interface:

```bash
streamlit run app.py
```

The terminal will print a local address (usually `http://localhost:8501`). Open it in your browser, paste your puzzle into the input box, and hit **Solve**.

---

## Input Format

Supply the board as 9 lines with 9 space-separated values per line:
* Digits `1`–`9` represent fixed clues.
* `0` denotes an empty cell.
* Every row must contain exactly 9 space-separated numbers.

### Example:

```text
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

---

## Features

* **Instant Solving:** Computes solutions for standard 9×9 puzzles.
* **Strict Validation:** Catches bad grid dimensions, non-digit characters, and duplicate values across rows, columns, and 3×3 blocks before solving.
* **Sample Grids:** Pre-packaged test files spanning easy, medium, hard, and edge-case unsolvable boards.
* **Automated Tests:** Comprehensive unit test coverage for validation rules and edge cases.

---

## Solving Logic (Backtracking)

The solver relies on standard depth-first search:

1. Scan the board for the next open cell (`0`).
2. Test candidate values from `1` through `9`.
3. Check row, column, and sub-grid constraints.
4. If valid, place the candidate and recurse to the next open cell.
5. If recursion hits a dead end (no valid candidates remaining), reset the cell to `0` and backtrack.
6. Terminate once every cell satisfies board rules or all permutations fail.

---

## Running Tests

Execute the test suite via `pytest`:

```bash
python -m pytest -v
```

The test suite covers:
* Correct solutions on solvable boards
* Malformed input (wrong row/column counts, out-of-range values)
* Immediate constraint violations (duplicate entries)
* Graceful exits on mathematically unsolvable boards

---

## Notes & Limitations

* Standard 9×9 grids only (no samurai, mini, or irregular variants).
* Worst-case runtime scales exponentially with puzzle complexity; adversarial grids may take longer to compute.
* Outputs the final board state directly does not supply human solving techniques, step-by-step reasoning, or hints.