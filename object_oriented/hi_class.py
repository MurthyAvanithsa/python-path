
class Course(object):

    def __init__(self):
        self.courses = list()

    def join_course(self,course_name):
        self.courses.append(course_name)

    def __str__(self):
        return "Working on "+",".join(self.courses)

course = Course()
course.join_course("Python")
course.join_course("Android")

print course