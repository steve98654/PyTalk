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
import numpy as np 
#import pandas as pd
from cffi import FFI

def cast_matrix(matrix,ffi):
    ap = ffi.new("double* [%d]" % (matrix.shape[0]))
    ptr = ffi.cast("double *",matrix.ctypes.data)
    for i in range(matrix.shape[0]):
        ap[i] = ptr + i*matrix.shape[1]
    return ap

ffi2 = FFI()
ffi2.cdef("""
        double sum1(double**,int,int,int,int);
        """)
C1 = ffi2.verify("""
        #include<stdio.h>
        double sum1(double** mat, int x, int y, int nrow, int ncol){
        int i,j,k;
        double tmpsm = 0;
        double mxval = 0;
        for (i=0; i<x-ncol+1; i++){
            for (j=0; j<y; j++){
                //tmpsm =0;
                printf("val %f",mat[i][j]);

                if(i==0)
                {
                    tmpsm =0;
                    for (k=0; k<ncol; k++){
                        tmpsm += mat[i+k][j];     
                    }
                    printf("tmpsm %f",tmpsm);
                    mat[i][j] = tmpsm;
                }
                else
                {
                    mat[i][j] = tmpsm - mat[i-1][j] + mat[i+ncol-1][j];
                    printf("tmpsm %f",tmpsm);
                }
            }
        }
        for (i=0; i<x; i++){
            for (j=0; j<y-nrow+1; j++){
                tmpsm =0;
                printf("val2 %f",mat[i][j]);
                if(j==0)
                {
                    for (k=0; k<nrow; k++){
                        tmpsm += mat[i][j+k];     
                    }
                    printf("tmpsm2 %f",tmpsm);
                    mat[i][j] = tmpsm;
                }
                else
                {
                    mat[i][j] = tmpsm - mat[i][j-1] + mat[i][j+nrow-1];
                    printf("tmpsm2 %f",tmpsm);
                }
                if(mat[i][j]>mxval)
                {
                    mxval = mat[i][j];
                    //printf("mxval %f",mxval);
                }
            }
        }
        return(mxval);
        }
        """)

#print int(pd.DataFrame(m).rolling(w_nrows).sum().rolling(w_ncols,axis=1).sum().max().max())

def find_densest(m, w_ncols, w_nrows):
    if len(m) < w_nrows or len(m[0]) < w_ncols:
        return 'None'
    else:
        m = np.array(m).astype(float)
        m_p = cast_matrix(m, ffi2)
        return int(C1.sum1(m_p, m.shape[0], m.shape[1],w_ncols,w_nrows))


#def find_densest(m, w_ncols, w_nrows):
#    """Finds the densest window of size w_nrows by w_ncols.

#    Args:
#        m: 2D matrix of positive integers as list of lists
#        w_ncols: width of window
#        w_nrows: height of window

#    Returns:
#       Sum of integers in the densest window if it exists, otherwise None
#    """
#    # Implement your solution here.

#    if len(m) < w_nrows or len(m[0]) < w_ncols:
#        return 'None'
#    else:
#        return int(pd.DataFrame(m).rolling(w_nrows).sum().rolling(w_ncols,axis=1).sum().max().max())
    

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

