class BaseCourse(object):

    def __init__(self):
        self.base_course = ["Programming", "Speaking Programming", "C"]

    def get_base_course(self):
        return self.base_course


class Course(BaseCourse):

    def __init__(self):
        super(Course, self).__init__()
        self.courses = list()
        self.courses.extend(self.get_base_course())

    def join_course(self, course_name):
        self.courses.append(course_name)

    def __str__(self):
        return "Working on "+",".join(self.courses)


course = Course()
course.join_course("Python")
course.join_course("Android")
print course