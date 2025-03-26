# CMPS 2200 Recitation 5

In this recitation, we'll look at randomness in computation.

**To make grading easier, please place all written solutions directly in `answers.md`, rather than scanning in handwritten work or editing this file.**

All coding portions should go in `main.py` as usual.


## Determinism versus Randomization in Quicksort

In lecture we saw that adding a random choice of pivot reduced the
probability of worst-case behavior for any given input in
selection. Let's look at how pivot choices affect Quicksort. For this
question, refer to the code in `main.py` 

**1a)**

Complete the implementations of `qsort` and `compare_sort` stubs. Feel
free to take from code given in the lectures to  help you perform list
partitioning. Note that the pivot choice function is input to `qsort`,
so you will have to curry `qsort` to test different methods of
choosing pivots. Implement variants of `qsort` that correspond to
selecting the first element of the input list as the pivot, and to
selecting a random pivot.
.  
.  
.  
.  


**1b)**

Compare running times using `compare-sort` between variants of
Quicksort and the
provided implementation of selection sort (`ssort`). Perform two
different comparisons: a comparison between sorting methods using
random permutations of the specified sizes, and a comparison using
already sorted permutations. How do the running times compare to the
asymptotic bounds? How does changing the type of input list change the
relative performance of these algorithms? Note that you may have to
modify the list sizes based on your system memory; compare at least 10
different list sizes. The `print_results` function in `main.py` gives
a table of results, but feel free to use code from Lab 1 to plot
the results as well. 

When a list is sorted fixed pivot is faster than using random pivots. When a list is unsorted random pivot is faster 
than fixed pivot.
The asymptotic bounds of q_sort when picking a good pivot is O(nlgn) and when picking a bad pivot it is O(n^2)
The run times of the unsorted_lists agree with this good pivot asymptotic time analysis.
When sorted lists are used the random_pivot is much slower than the fixed_pivot and when unsorted lists are used the 
random_pivot is faster than the fixed_pivot agreeing with the above asymptotic analysis 
Sorted lists:
|--n---|----random_piv-----------|------fixed_piv--------------|
|     1 |               0.001 |                0.000 |
|    10 |               0.004 |                0.006 |
|   100 |               0.191 |                0.066 |
|   200 |               0.752 |                0.122 |
|   500 |               4.569 |                0.425 |
|  1000 |              15.503 |                0.743 |
|  1100 |              18.587 |                0.843 |
|  2000 |              61.603 |                1.546 |
|  5000 |             410.311 |                3.988 |
| 10000 |            1666.180 |                9.496 |


Unsorted lists:
|----n---|---------random_piv---------|--------fixed_piv------------|
|     1 |               0.000 |                0.001 |
|    10 |               0.005 |                0.004 |
|   100 |               0.041 |                0.063 |
|   200 |               0.094 |                0.129 |
|   500 |               0.266 |                0.355 |
|  1000 |               0.565 |                0.758 |
|  1100 |               0.623 |                0.831 |
|  2000 |               1.267 |                1.794 |
|  5000 |               3.227 |                4.285 |
| 10000 |               6.888 |                8.830 |



**1c)**

Python uses a sorting algorithm called [*Timsort*](https://en.wikipedia.org/wiki/Timsort), designed by Tim Peters. Compare the fastest of your sorting implementations to the Python
sorting function `sorted`, conducting the tests in 1b above. 

Sorted lists:
When using sorted lists the work is O(nlgn) for the best case and the work of tim_sort seems to be O(lgn) tim sort is faster.
|--n----|-----random_piv--|-----fixed_piv-------|------tim_sort----------------|
|     1 |    0.001 |               0.000 |                0.001 |
|    10 |    0.004 |               0.007 |                0.000 |
|   100 |    0.200 |               0.058 |                0.001 |
|   200 |    0.733 |               0.138 |                0.000 |
|   500 |    4.257 |               0.401 |                0.002 |
|  1000 |   15.703 |               0.755 |                0.003 |
|  1100 |   18.492 |               0.855 |                0.003 |
|  2000 |   60.390 |               1.558 |                0.007 |
|  5000 |  404.916 |               4.151 |                0.021 |
| 10000 | 1669.407 |               8.842 |                0.036 |

Unsorted lists:
When using unsorted lists the work is O(nlgn) for the best case and the work of tim_sort seems to be O(lgn) tim sort is faster.
|--n----|-----random_piv--|-----fixed_piv-------|------tim_sort----------------|
|     1 | 0.001 |               0.000 |                0.001 |
|    10 | 0.004 |               0.006 |                0.000 |
|   100 | 0.047 |               0.070 |                0.005 |
|   200 | 0.101 |               0.142 |                0.011 |
|   500 | 0.316 |               0.392 |                0.036 |
|  1000 | 0.603 |               0.814 |                0.096 |
|  1100 | 0.765 |               0.922 |                0.075 |
|  2000 | 1.286 |               1.767 |                0.147 |
|  5000 | 3.428 |               4.824 |                0.410 |
| 10000 | 7.661 |               9.794 |                0.899 |

