from best_sum import best_sum, best_sum_memo

def test_0():
    assert sorted(best_sum(7, [5,3,4,7])) == sorted([7])
    assert sorted(best_sum(8, [2,3,5])) == sorted([3,5])
    assert sorted(best_sum(8, [1,4,5])) == sorted([4,4])

def test_1():
    assert sorted(best_sum_memo(7, [5,3,4,7], dict())) == sorted(best_sum(7, [5,3,4,7]))
    assert sorted(best_sum_memo(8, [2,3,5], dict())) == sorted(best_sum(8, [2,3,5]))
    assert sorted(best_sum_memo(8, [1,4,5], dict())) == sorted(best_sum(8, [1,4,5]))
