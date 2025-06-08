class Student:
    def __init__(self, roll_no, name, dept):
        self.roll_no = roll_no
        self.name = name
        self.dept = dept

    def __repr__(self):
        return f"{self.roll_no}| {self.name} ({self.dept})"

class HashTable:
    def __init__(self, size=3):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, key):
        return (key+3) % self.size 

    def add(self, student):
        index = self.hash_function(student.roll_no)
        self.buckets[index].append(student)

    def search(self, roll_no):
        index = self.hash_function(roll_no)
        for student in self.buckets[index]:
            if student.roll_no == roll_no:
                return student
        return None

    def display(self):
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}: {bucket}")

students = [
    Student(101, "Ilakkiya", "CSE"),
    Student(102, "Kaveri", "ME"),
    Student(103, "Ilamparithi", "EEE"),
    Student(104, "Yazhini", "CE"),
    Student(105, "Mani", "IT")
    ]

hash_table = HashTable(size=3)

for s in students:
    hash_table.add(s)

hash_table.display()

print("\nSearch for 103:", hash_table.search(103))
print("\nSearch for 105:", hash_table.search(105))

