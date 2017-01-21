
class GuideLines(object):

    def __init__(self):
        self.tutors = list()
        self.tutors.append("Murthy")
        self.tutors.append("John")

    @staticmethod
    def course_guidelines():
        guide_lines = ["Start's at 8 AM IST", "Weekend will be on Saturday"]
        print "Guidelines ---\n"
        print ",\n".join(guide_lines)


    @staticmethod
    def course_faq():
        guide_lines = dict()
        guide_lines['How about I miss a day?'] = "You can access videos and course content"
        guide_lines['Whats the time in need to spend?'] = "70 min a day"
        print "FAQ ---\n"
        for key in guide_lines:
            print key,guide_lines[key]




GuideLines.course_guidelines()
GuideLines.course_faq()