import random, time
import tabulate
import sys
sys.setrecursionlimit(100000)

def ssort(L):
    ### selection sort
    if (len(L) == 1):
        return(L)
    else:
        m = L.index(min(L))
        print('selecting minimum %s' % L[m])       
        L[0], L[m] = L[m], L[0]
        print('recursively sorting L=%s\n' % L[1:])
        return [L[0]] + ssort(L[1:])
        
def random_piv(a):
    if len(a) < 2:
        return 0
    else:
        l = len(a)
        pivot_index = random.randint(0, l-1)
    return pivot_index
def fixed_piv(a):
    return 0

def qsort(a, pivot_fn):
    pivot = pivot_fn(a)
    if len(a) <=1:
        return a
    right_array = []
    left_array = []
    for i in a:
        if i<a[pivot]:
            left_array.append(i)
        if i>a[pivot]:
            right_array.append(i)

    return qsort(left_array,pivot_fn) + [a[pivot]] +qsort(right_array, pivot_fn)

    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[1,10,100, 200, 500, 1000, 1100, 2000, 5000, 10000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    qsort_fixed_pivot = lambda a: qsort(a, fixed_piv)
    qsort_random_pivot = lambda a: qsort(a, random_piv)
    tim_sort = sorted
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
            time_search(tim_sort,mylist)
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()
