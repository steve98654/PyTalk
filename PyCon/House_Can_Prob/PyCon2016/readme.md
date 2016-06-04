![HouseCanary: Powered by Python](https://i.imgsafe.org/79930d4.jpg)

# HouseCanary PyCon 2016 Coding Challenge

### The Challenge

In the search for great Software Engineers, HouseCanary is hosting a coding challenge for the attendees of PyCon 2016!

This is also an opportunity for job seekers. If you’d like to be considered for a career at HouseCanary, please attach a resume along with your submission. Take a look at our [job openings](http://housecanary.com/careers) and see if you’re a match.

### Prizes

 * Fastest Solution: $500 Amazon Gift Card
   (Should pass all provided test cases within 1 minute)

 * Pass The First Two Test Cases: HouseCanary T-shirt

### The Problem

You are given a 2D array of integers 'M'. The value M[x][y] is an
integer corresponding to the number of homes located in row 'x' and column 'y'.
You can assume value of each cell in 'M' is a positive integer <= 100.

Find the largest number of homes inside the 2D array 'M' that
can be contained in a rectangle of size 'a' rows and 'b' columns -- let's call
this the 'search rectangle'. Both a and b are positive integers, and will be
provided per problem instance you are asked to solve.

You can assume that the sum of values in the 2D array 'M' will fit in a 32-bit
signed integer.

Example Problem Instance

Location Array 'M':

    [[0, 3, 1, 6],
    [6, 9, 9, 0],
    [2, 8, 9, 2],
    [8, 8, 8, 5]]
Each cell value indicates number of homes located in that cell location.

Three examples of problem cases with search rectangle a x b:

    1. a=3, b=3
    2. a=2, b=2
    3. a=1, b=2

Solution:

    1. Search rectangle of size 3 by 3 with largest number of homes:

    [[6, 9, 9],
    [2, 8, 9],
    [8, 8, 8]]

    Number of homes: 67

    2. Search rectangle of size 2 by 2 with largest number of homes:

    [[9, 9],
     [8, 9]]

    Number of homes: 35

    3. Search rectangle of size 1 by 2 with largest number of homes:

    [[9, 9]]

    Number of homes: 18


### Input File Format

    N
    SEARCH_RECTANGLE_ROWS SEARCH_RECTANGLE_COLUMNS
    NUM_ROWS NUM_COLUMNS
    DATA (NUM_ROWS by NUM_COLUMNS)

First line in input file is the number of problem instances to solve (N).

Second line contains two space separated integers corresponding to number of rows
and columns in the search rectangle.

Third line contains two space separated integers corresponding to number of rows
and columns in location array 'M'.

The next NUM_ROWS lines contain NUM_COLUMNS space-separated integers each. These
lines correspond to rows and columns in location array 'M'.

For example, the following contains two problem instances (file inputs/input0.txt):

    3
    2 3
    3 8
    1 2 3 4 80 20 0 5
    5 8 20 0 0 0 0 1
    9 1 1 2 3 5 5 9
    4 5
    4 9
    0 0 2 4 8 2 0 5 1
    1 8 20 5 0 0 0 1 2
    7 1 0 2 3 5 5 9 5
    0 1 1 4 3 5 5 9 0
    20 3
    3 8
    0 2 3 4 80 20 0 5
    1 8 20 0 0 0 0 1
    2 1 1 2 3 5 5 9

The file [solution.py](./solution.py) already has a method to read input file for you, but feel free to
use your own if you want.

### Output format

For each problem instance print an integer equivalent to the
maximum number of homes possible in the search rectangle, followed by a new
line character '\n'. If no solution exists, print the word 'None' (without quotes)
followed by the new line character '\n'.

For the sample input above, the output should be:

    107
    75
    None

### How to implement your solution
Modify the `find_densest` function in [solution.py](./solution.py). Feel free to modify the provided boilerplate code.

The expected output for the input data in *inputs* folder has been provided for you in *outputs* folder.

Test your code as follows (assuming you used the provided boilerplate code):

```
cat inputs/input0.txt | python solution.py
cat inputs/input1.txt | python solution.py
cat inputs/input2.txt | python solution.py
cat inputs/input3.txt | python solution.py
```

Check that your solution matches the contents of corresponding file in *outputs* folder.

### Testing Environment
The test machine is a Macbook with a 2.2 GHz i7 processor and 16GB of RAM. Your code will be run in a VM with:

* Your choice of Python 2.7.11 or 3.5.1
* Numpy installed
* Any packages you need that can be pip installed

Your solution will be tested against similar input data as provided in *inputs* folder.
Your solution will get up to 1 minute to process each test file.

### Submitting

Copy your `solution.py` into a secret [GitHub Gist](https://gist.github.com/) and send the link to challenge@housecanary.com. Include a comment in the code describing which version of Python (2.7.11 or 3.5.1) and which additional packages should be pip installed, if any.

Make sure to attach your resume if you’re interested in a career at [HouseCanary](http://housecanary.com/careers).

After we run the code locally, we’ll send you an email with directions to the HouseCanary booth where you can pick up your prize.

## The Fine Print

Prizes are while supplies last. Code must be the entrant's original work, and HouseCanary may refuse prizes for detected plagiarism. T-shirt prizes must be picked up at the HouseCanary booth before 1pm on Wednesday June 1st. Contest for 1st place ends at end of day on Friday, June 3rd. 1st place winner will be announced in this repo on Monday, June 6th. Entrants must be attendees of PyCon 2016.

