import unittest
import random
import timeit

from CS03Final import *


class SortPerformanceTestCase(unittest.TestCase):
    sort_func = None

    def setUp(self):
        random.seed(3)  # ensure reproducibility

    def helpTestPerformance(self, sample):
        duration = timeit.timeit(lambda: self.__class__.sort_func(sample), number=1)
        print(f"{self.__class__.sort_func.__name__} on {len(sample)} items takes {duration:.6f} seconds")

    def testPerformance(self):
        for length in range(1000, 20001, 1000):
            sample = random.sample(range(1000000), length)
            self.helpTestPerformance(sample)


class ICantBelieveItCanSortPerformanceTestCase(SortPerformanceTestCase):
    sort_func = i_cant_believe_it_can_sort


class BubbleSortPerformanceTestCase(SortPerformanceTestCase):
    sort_func = bubble_sort


class InsertionSortPerformanceTestCase(SortPerformanceTestCase):
    sort_func = insertion_sort

class ShellSortPerformanceTestCase(SortPerformanceTestCase):
    sort_func = shell_sort


