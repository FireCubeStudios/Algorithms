from Sort import Sort

# TO DO Implementing my own MergeSort for learning purposes
class MergeSort(Sort):
    def __init__(self, count: int):
         Sort.__init__(self, count)

    # Sort the list with merge sort
    def Sort(self): return self.merge(0, len(self.grades) - 1)

    def merge(self, start: int, end: int):
        if(start == end): 
            sorted = [1] 
            sorted[0] = self.grades[start]
            return sorted
        else:
            list1 = self.merge(start, end / 2)
            list2 = self.merge(end / 2, end)
            sorted = [end - start]
    pass