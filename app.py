import streamlit as st

from src.solver import solveSudoku

st.set_page_config(page_title="Sudoku Solver",layout="centered")

def clear_input():
    st.session_state["puzzleText"] = ""

st.title("Sudoku Solver")
st.caption("Enter the 9x9 grid. Leave empty cells as zero, then click on solve.")

puzzleText = st.text_area(
    "Enter Sudoku puzzle",
    height=250,
    placeholder=(
        "5 3 0 0 7 0 0 0 0\n"
        "6 0 0 1 9 5 0 0 0\n"
        "..."
    ),
    key="puzzleText"
)

solveClicked = st.button("Solve",type="primary",use_container_width=True)

if solveClicked:
    try:
        lines = [line.split() for line in puzzleText.strip().splitlines() if line.strip()]
        board = [[int(value) for value in row] for row in lines]

        if solveSudoku(board):
            st.success("Solution found")
            st.subheader("Solved Sudoku")
            st.code("\n".join(" ".join(map(str, row)) for row in board),language="text")   

        else:
            st.error("No solution exists for this puzzle.")

    except ValueError as error:
        st.error(f"Invalid puzzle: {error}")
    except (TypeError, IndexError) as error:
        st.error(f"Could not read the puzzle: {error}")

st.button("Clear", on_click=clear_input)
