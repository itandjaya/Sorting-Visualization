## main.py
## Main function to test sort functions.
from random import randint, shuffle;
from sort import *;
from visual import *;

## Visualization library.



def main():

    N = 100;
    X, arr  =   generate_init_arr(N);
    validation_arr  =   sorted(arr);

    selector    =   2;      #0: quick sort, 1: merge sort, 2: bubble sort.
    func, title =   sort_func(  selector);

    iter_sort   =   func(arr);
    sort_visual(    arr, iter_sort, title);

    #check_result    =   arr == validation_arr;
    assert  arr == validation_arr,  "Wrong Sort Result: {}".format(arr);

    return 0;


main()      if __name__ == "__main__"       else None;