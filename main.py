def sum_of_squares(a):
	sum = 0
    for i in a:
        mid = i * i
        sum = sum + mid
    pass

def test_one():
    assert sum_of_squares([1,2,3]) == 14

test_one()