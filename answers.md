# CMPS 2200 Reciation 5
## Answers

**Name:**______Joshua Sasson________


Place all written answers from `recitation-05.md` here for easier grading.







- **1b.**
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




- **1c.**
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
