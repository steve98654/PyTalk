"""
Boilerplate code for your convenience. Feel free to modify as you want.

Testing your implemention:
    cat inputs/input0.txt | python solution.py
    cat inputs/input1.txt | python solution.py
    cat inputs/input2.txt | python solution.py
    cat inputs/input3.txt | python solution.py

    Check if your output matches the corresponding outputs in 'outputs' folder.
"""
import sys
import pandas as pd

#@jit
def find_densest(m, w_ncols, w_nrows):
    """Finds the densest window of size w_nrows by w_ncols.

    Args:
        m: 2D matrix of positive integers as list of lists
        w_ncols: width of window
        w_nrows: height of window

    Returns:
       Sum of integers in the densest window if it exists, otherwise None
    """
    # Implement your solution here.

    if len(m) < w_nrows or len(m[0]) < w_ncols:
        return 'None'
    else:
        return int(pd.DataFrame(m).rolling(w_nrows).sum().rolling(w_ncols,axis=1).sum().max().max())
    

def read_problem_instances(ifile):
    """Reads problem instances from given file.

    See readme.md for file format.

    Returns:
        A generator that gives a tuple of (2D array, RECTANGLE_ROWS, RECTANGLE_COLUMNS)
    """
    N = int(ifile.readline().strip())

    for i in range(N):
        w_nrows, w_ncols = [int(x.strip()) for x in ifile.readline().strip().split(' ')]
        nrows, ncols = [int(x.strip()) for x in ifile.readline().strip().split(' ')]
        m = []
        for r in range(nrows):
            line = ifile.readline()
            line = line.strip()
            m.append([int(x.strip()) for x in line.split(' ')])
        yield m, w_nrows, w_ncols

if __name__ == '__main__':
    for m, w_nrows, w_ncols in read_problem_instances(sys.stdin):
        print(find_densest(m, w_nrows=w_nrows, w_ncols=w_ncols))

