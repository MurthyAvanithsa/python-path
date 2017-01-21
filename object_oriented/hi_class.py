
class Training(object):

    def __init__(self):
        self.default_duration = 90
        self.courses = list()

    def join(self, course_name):
        self.courses.append(course_name)

    def unsub(self, course_id):
        pass

    def __str__(self):
        return "Working on "+",".join(self.courses)



free_training = Training()

free_training.join("Basics")

python_training = Training()
python_training.join("Python-Basics")
python_training.join("Python-Advanced")


print free_training,id(free_training)

print python_training, id(python_training)




