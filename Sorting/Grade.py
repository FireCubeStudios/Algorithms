class Grade:
    def __init__(self, name, grade: str):
        self.name = name
        self.grade: int = self.convert(grade)

    # Convert a grade to an int value for comparing in sorting
    def convert(self, grade: str) -> int:
        dict = { "A": 100, "B": 200, "C": 300, "D": 400, "E": 500, "FX": 600, "F": 700 }
        value = dict.get(grade[:2] if len(grade) > 1 and grade[1] == 'X' else grade[0])
        for c in grade:
            if(c == '+'): value -= 1
            elif(c == '-'): value += 1
        return value
    
    # Return true if this grade is higher than the other grade
    def isHigher(self, grade) -> bool:
        if(self.grade == grade.grade): 
            for i in range(len(self.name)):
                if i > len(grade.name) - 1: return False # Shorter names come first so return false
                elif(ord(self.name[i]) != ord(grade.name[i])): return ord(self.name[i]) < ord(grade.name[i])
            return True
        else: return (self.grade < grade.grade) # Lower grade int value is a higher grade
