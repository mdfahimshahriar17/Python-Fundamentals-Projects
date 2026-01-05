class Student:
    university = "FS University" #class variable

    def __init__(self, name, score):
        self.name = name #instance variable
        self.score = score


    def __str__(self):
        return f"Name: {self.name}, Score: {self.score}"
    
    
    def __repr__(self):
        return f"Name: {self.name}, Score: {self.score}"

class Result:
    def __init__(self):
        self.results = []

    def add(self, result):
        if result:
            self.results.append(result)

    def show_result(self):
        print(Student.university)
        for result in self.results:
            print(f"Name : {result.name} -- Score : {result.score}")


std1 = Student("Rahim", 99)
std2 = Student("Fahim", 90)
std3 = Student("Karim", 92)

rslt = Result()

rslt.add(std1)
rslt.add(std2)
rslt.add(std3)


rslt.show_result()

print(std1.__str__())
print(rslt.results)