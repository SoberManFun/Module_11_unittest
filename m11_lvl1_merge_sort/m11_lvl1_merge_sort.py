import unittest

def item_check(arr):
    type_item: annotate_arr = arr
    correct_item = True
    for item in type_item:
        if isinstance(item, int):
            correct_item = True
            continue
        else:
            correct_item = False    
            break
    return(correct_item)
            
def merge_sort(arr):
#функция сортировки слиянием
    if item_check(arr) == True:
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            merge_sort(left_half)
            merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        return arr


class TestMergeSort(unittest.TestCase):
#тесты для функции сортировки слиянием
    
    def test1_sort(self):
        test_array = [-3, 5, 9, 1, 23]
        self.assertTrue(merge_sort(test_array), test_array.sort())    

    def test2_empty_array(self):
        self.assertFalse(merge_sort([]))

    def test3_reverse_array(self):
        test_array = merge_sort([-3, 5, 9, 1, 23])
        test_array.reverse()
        self.assertTrue(test_array, [23, 9, 5, 1, -3])

    def test4_correct_type_int(self):
        self.assertFalse(merge_sort([-3, 5, 9.65, '1', 23, True, {'id': 13}]))    

unittest.main()

