#visual.py

#import pandas as pd;
#import seaborn as sns;
#from random import randint, shuffle;
import numpy as np;
from math import log;

import matplotlib.pyplot as plt;
from matplotlib.animation import FuncAnimation;

from sort import *;

   
def sort_func(   selector = 0):
    lookup  =   [   quick_sort, merge_sort, bubble_sort, insertion_sort, heap_sort];
    title   =   [   "Quick Sort O(N LogN)", "Merge Sort O(N LogN)", "Bubble Sort O(N*N)", \
                    "Insertion Sort O(N*N)", "Heap Sort O(N LogN)" ];

    return lookup[selector], title[selector];

def generate_init_arr(    N = 20):
    X       =   np.array(   list(range(N)), dtype  =   'int32');
    Y       =   np.random.randint(  N+1,    size = N);
    #arr     =   [ randint(0, N) for _ in range(N)];
    return X,Y;

def sort_visual(    arr, iter_func, title):

    N = len(arr);

    ## Initialize the plot frame.
    #fig = plt.figure();
    fig, ax = plt.subplots();
    ax.set_title(   title);
    ax.set_ylabel(  "DATA");

    num_frames  =   N*N; #Number of frames.

    X   =   np.array(range(N), dtype =  'int32');
    Y   =   arr;

    barcollection = plt.bar(    X, Y, color = 'b',
                                #, align    =   'edge', width   =   0.5,
                            );
    
    IA, IB  =   [0], [0];
    sort_completed  =   [False];

    def animate(i):

        #global sort_completed;

        if not sort_completed[0]:

            if not i&1:
                barcollection[IA[0]].set_color('blue');
                barcollection[IB[0]].set_color('blue');
            
            else:

                try:
                    ia, a   =   next(iter_func);
                    ib, b   =   next(iter_func);

                    barcollection[ia].set_height(a);
                    barcollection[ib].set_height(b);

                    barcollection[ia].set_color('red');
                    barcollection[ib].set_color('red');

                    IA[0], IB[0]  =   ia, ib;
                
                except StopIteration:
                    sort_completed[0] = True;
                    IA[0] = 0;

        elif IA[0] < N:
            j = IA[0];
            barcollection[j].set_color('g');
            IA[0] += 1;
        
        #return barcollection;
        return;

    anim    =   FuncAnimation(      fig,
                                    animate,
                                    repeat = False,
                                    blit = False,
                                    frames = num_frames,
                                    interval = 12);

    #anim.save(  'test.html', writer = 'ffmpeg', fps = 20);
    plt.show();

    return;