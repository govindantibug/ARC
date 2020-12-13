# The Abstraction and Reasoning Corpus (ARC)

This repository contains the ARC task data, as well as a browser-based interface for humans to try their hand at solving the tasks manually.

*"ARC can be seen as a general artificial intelligence benchmark, as a program synthesis benchmark, or as a psychometric intelligence test. It is targeted at both humans and artificially intelligent systems that aim at emulating a human-like form of general fluid intelligence."*

A complete description of the dataset, its goals, and its underlying logic, can be found in: [The Measure of Intelligence](https://arxiv.org/abs/1911.01547).

As a reminder, a test-taker is said to solve a task when, upon seeing the task for the first time, they are able to produce the correct output grid for *all* test inputs in the task (this includes picking the dimensions of the output grid). For each test input, the test-taker is allowed 3 trials (this holds for all test-takers, either humans or AI).


## Task file format

The `data` directory contains two subdirectories:

- `data/training`: contains the task files for training (400 tasks). Use these to prototype your algorithm or to train your algorithm to acquire ARC-relevant cognitive priors.
- `data/evaluation`: contains the task files for evaluation (400 tasks). Use these to evaluate your final algorithm. To ensure fair evaluation results, do not leak information from the evaluation set into your algorithm (e.g. by looking at the evaluation tasks yourself during development, or by repeatedly modifying an algorithm while using its evaluation score as feedback).

The tasks are stored in JSON format. Each task JSON file contains a dictionary with two fields:

- `"train"`: demonstration input/output pairs. It is a list of "pairs" (typically 3 pairs).
- `"test"`: test input/output pairs. It is a list of "pairs" (typically 1 pair).

A "pair" is a dictionary with two fields:

- `"input"`: the input "grid" for the pair.
- `"output"`: the output "grid" for the pair.

A "grid" is a rectangular matrix (list of lists) of integers between 0 and 9 (inclusive). The smallest possible grid size is 1x1 and the largest is 30x30.

When looking at a task, a test-taker has access to inputs & outputs of the demonstration pairs, plus the input(s) of the test pair(s). The goal is to construct the output grid(s) corresponding to the test input grid(s), using 3 trials for each test input. "Constructing the output grid" involves picking the height and width of the output grid, then filling each cell in the grid with a symbol (integer between 0 and 9, which are visualized as colors). Only *exact* solutions (all cells match the expected answer) can be said to be correct.


## Usage of the testing interface

The testing interface is located at `apps/testing_interface.html`. Open it in a web browser (Chrome recommended). It will prompt you to select a task JSON file.

After loading a task, you will enter the test space, which looks like this:

![test space](https://arc-benchmark.s3.amazonaws.com/figs/arc_test_space.png)

On the left, you will see the input/output pairs demonstrating the nature of the task. In the middle, you will see the current test input grid. On the right, you will see the controls you can use to construct the corresponding output grid.

You have access to the following tools:

### Grid controls

- Resize: input a grid size (e.g. "10x20" or "4x4") and click "Resize". This preserves existing grid content (in the top left corner).
- Copy from input: copy the input grid to the output grid. This is useful for tasks where the output consists of some modification of the input.
- Reset grid: fill the grid with 0s.

### Symbol controls

- Edit: select a color (symbol) from the color picking bar, then click on a cell to set its color.
- Select: click and drag on either the output grid or the input grid to select cells.
    - After selecting cells on the output grid, you can select a color from the color picking to set the color of the selected cells. This is useful to draw solid rectangles or lines.
    - After selecting cells on either the input grid or the output grid, you can press C to copy their content. After copying, you can select a cell on the output grid and press "V" to paste the copied content. You should select the cell in the top left corner of the zone you want to paste into.
- Floodfill: click on a cell from the output grid to color all connected cells to the selected color. "Connected cells" are contiguous cells with the same color.

### Answer validation

When your output grid is ready, click the green "Submit!" button to check your answer. We do not enforce the 3-trials rule.

After you've obtained the correct answer for the current test input grid, you can switch to the next test input grid for the task using the "Next test input" button (if there is any available; most tasks only have one test input).

When you're done with a task, use the "load task" button to open a new task.

### PTAI Assignment 3

# Numpy features:
np.where()
We've made extensive use of where() method to find positions of matching cells, or cells having a particular color

np.unique()
 Gives unique values in an array. We used it to get unique colours present in a grid.
 
 np.reshape()
	Reshapes the array based on parameters. We used it to convert the array into 1D because it simplified the comparision task.
	
collections.Counter()
	Used to get values and their counts in an array.
	
np.transpose() 
 Transpose the npdarray , making then columns now rows and vice versa

# Tasks:
22eb0ac0:
#Input: Grid of size 10x10, where first and last cells of some rows are coloured
#Output: Grid of size 10x10, where entire row is recoloured with 'x' colour if both the first and last cell of that row are of color 'x'

1e32b0e9:
#Input: Grid of size 17x17, which can be divided into 9 sub-blocks by 4 straight lines
#Output: Grid of size 17x17, where the pattern in the first sub-block is copied to-
 -other 8 sub-blocks based on:
 1) If part of the pattern already exists in the sub-block,-
    - then complete the pattern using sub-block border colour
 2) If the pattern doesnt exist, then draw the entire pattern using border color 

23b5c85d:
#Input: A grid of dynamic size with blocks of different sizes
#Output: Extract a 4 sided shape with minimum size

09629e4f:
#Input: A grid of size 11x11, which is divided into 9 sub-blocks of size 3x3
#Output: A grid of size 11x11, which is formed based on:
 1) Find the sub-block in input grid with highest number of black cells,
      lets call it "X"
 2) X can be further divided into 9 cells, shaped 3x3
 3) For each cell in 'X', colour the corresponding sub-block in output grid with-
     -colour of that cell
   For example: if the colour of first cell in X is green, -
   -then the first sub-block in output grid should be Green

6430c8c4:
#Input: Grid of size 9x4, with a yellow row dividing it into 2 parts
#Output: Grid of size 4x4, with cells which are black in both parts coloured Green

a85d4709:
#Input: Grid of size 3x3, with each row having a Gray coloured cell
#Output: Grid of size 3x3, where entire row is recoloured based on position of Gray cell in the input Grid

7e0986d6 :
#input : a grid with a shape and few patched elements with some other color , refered to as outliers in the code
#ouput :matrix with correct color for the outliers

67385a82 :
#input : a grid with green elements
#output : a grid with all the green elements colored with turquoise color (8) if they have atleast 1 neighbour

dbc1a6ce :
#input : a grid with multiple blue points
#output :  a grid with all the intermediate spaces filled if there are two or more blue points in a row or column in a grid ,
#          color used to fill is turquoise

54d82841 :
#input : a grid with 5 elements 3 in a row and 2 in the next row. the elements in the next row are alligned to first and last
#        element of the upper row
#output : the last element of the column of the missing element is painted by the color 4


