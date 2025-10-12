from bubble_sort import bubble_sort

def test_bubble_sort_basico():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]

if __name__ == '__main__':
    test_bubble_sort_basico()
    print('Todos os testes passaram.')
