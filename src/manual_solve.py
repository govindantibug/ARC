#!/usr/bin/python

import os, sys
import json
import numpy as np
import re
import itertools
### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.
# def solve_54d82841(x):
#     missing_indices = []
#     for arr in x:
#         for i in range(len(arr) - 2): 
#             if arr[i] == arr[i + 1] and arr[i + 1] == arr[i + 2] and arr[i] != 0 : 
#                 missing_indices.append(i+1)
    
#     for index in missing_indices:
#         x[-1][index] = 4
#     return x

# def solve_dbc1a6ce(x):
#     def fill_rows (x):
#         for arr in x :
#             unique, counts = np.unique(arr, return_counts=True)
#             count_1 = 0
#             for u ,c in zip (unique,counts):
#                 if u == 1:
#                     count_1 =  c
#                 if count_1 > 1:
#                     indices = [index for index, element in enumerate(arr) if element == 1]
#                     min_idx = min(indices)
#                     max_idx = max(indices)
#                     new_arr = arr
#                     for i in range(min_idx,max_idx+1):
#                         if new_arr[i] == 0:
#                             new_arr[i] = 8
#                     np.where(x==arr, new_arr, x) 
#         return x
#     x = fill_rows(x)
#     x = np.transpose(x)
#     x = fill_rows(x)
#     x = np.transpose(x)
#     return x

# def solve_67385a82(x):
#     indices = np.where(x == 3)
#     i_values = indices[0]
#     j_values = indices[1]
#     points = []
#     for i,j in zip(i_values,j_values):
#         points.append((i,j))
#     for p1,p2 in itertools.combinations(points, 2):
#         x1,y1 = p1
#         x2,y2 = p2
#         if (x1 == x2 and abs(y1-y2) == 1) or (y1 == y2 and abs(x1-x2) == 1):
#             if x[x1][y1] != 8:
#                 x[x1][y1] = 8
#             if x[x2][y2] != 8:
#                 x[x2][y2] = 8
#     return x

# def solve_776ffc46(x):
#     indices = np.where(x == 5)
#     i_values = indices[0]
#     j_values = indices[1]
#     points = []
#     squares = []
#     for i,j in zip(i_values,j_values):
#         points.append((i,j))
#     count = len(points)   
#     min_point = None
#     min_x = 10000
#     min_y = 10000
#     while (count != 0):
#     if (min_point == None):
#         for point in points:
#             x1, y1 = point
#             if x1 <= min_x and y1 <= min_y and point not in squares:
#                 min_point = point
#                 min_x =  x1
#                 min_y = y1
#     print (min_point)
    
#     is_square = True
#     side_len = 0
#     x_dir = True
#     y_dir = True
#     while(x_dir == True ):
#         side_len += 1
#         if x_dir:
#             if (min_x + side_len , min_y) in points :
#                 continue
#             else : 
#                 x_dir = False
#     print (side_len)
#     x_max = x_min + side_len
#     y_max = y_min + side_len
#     for y1 in range(side_len) :
#         if (x_min,y_min + y1) and (x_max, y_max - y1) in points : 
#             continue
#         else : 
#             is_square = False
#         square_list.append((x_min,y_min + y1))
#         square_list.append((x_max, y_max - y1))
#     for x1 in range (side_len) : 
#         if (x_min + x1 , y_min) and (x_max - x1 , y_max) in points :
#             continue
#         else :
#             is_square = False
#         square_list.append((x_min + x1 , y_min))
#         square_list.append( (x_max - x1 , y_max))
    
#     if is_square :
#         count -= len(square_list)
#     squares.append(square_list)
        
        
        
#     return x


def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)
    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    # if yhat has the right shape, then (y == yhat) is a bool array
    # and we test whether it is True everywhere. if yhat has the wrong
    # shape, then y == yhat is just a single bool.
    print(np.all(y == yhat))

if __name__ == "__main__": main()

