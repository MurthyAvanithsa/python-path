class Training(object):

    course_title = "Python-Path"

    def __init__(self, init_course):
        self.default_duration = 90
        self.courses = list()
        self.course_title = init_course

    def join(self, course_name, course_duration):
        self.courses.append(course_name)

    def unsub(self, course_id):
        pass

    def __str__(self):
        return "Working on "+",".join(self.courses)


training = Training("Go")

training2 = Training("Python")

# instance variable
print training.course_title

print training2.course_title

training.join(course_name="JSON",course_duration=3)

# class variables
print Training.course_title