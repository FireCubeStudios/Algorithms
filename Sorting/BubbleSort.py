from Sort import Sort

class BubbleSort(Sort):
    def __init__(self):
         Sort.__init__(self)

    # Sort the list with bubble sort
    def Sort(self): 
        sorted = True
        while sorted:
            sorted = False
            for i in range(0, len(self.grades) - 1):
                if not (self.grades[i].isHigher(self.grades[i + 1])):
                   temp = self.grades[i] 
                   self.grades[i] = self.grades[i + 1]
                   self.grades[i + 1] = temp
                   sorted = True

        return self.grades