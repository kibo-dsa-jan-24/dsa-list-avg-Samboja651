import unittest
from listavg import ListAverage

class TestListAverage(unittest.TestCase):
    def test_compute_avg(self):
        lavg = ListAverage([1, 2, 3])
        assert lavg.compute_avg() == 2.0

    def test_compute_avg_faster(self):
        lavg = ListAverage([1, 2, 3])
        assert lavg.compute_avg_faster() == 2.0    

    def test_compute_avg_faster_add(self):
        lavg = ListAverage([1, 2, 3])
        lavg.add(10)
        assert lavg.compute_avg_faster() == 4.0

    def test_compute_avg_add(self):
        lavg = ListAverage([1, 2, 3])
        lavg.add(10)
        assert lavg.compute_avg() == 4.0
    
    # add more unit tests below
