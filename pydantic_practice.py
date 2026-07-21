from pydantic import BaseModel
class Student(BaseModel):
    name: str
    age: int
    single: bool
student = Student(
    name="BORZ",
    age="18",
    single=True
)
print(student)