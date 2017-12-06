#MIT License
#
#Copyright (c) 2017 Shreenandan Rajarathnam
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#___________________________________________________________________
#
#Simulation of Course Workload and Academic Pressure for U of I Students

class AcademicTask:
    '''
        A class that represents 1 academic task (assignment, project, research paper deliverable, exam and etc.) in a week.
    '''
    def __init__(self, type_of_task: str, difficulty_level: int, no_of_hours_of_work: int):
        self._type_of_task = type_of_task
        self._difficulty_level = difficulty_level
        self._no_of_hours_of_work = no_of_hours_of_work

class AcademicWeek:
    '''
        A class that represents 1 academic week (for a course) in a semester.
    '''
    #_tasks = {}
    
    def __init__(self, week_no: int):
        self._week_no = week_no

    def get_week_no(self):
        return self._week_no

class Course:
    '''
        A class that represents 1 course taken by a student in a semester.
    '''
    
    _academic_weeks = {}
    
    def __init__(self, course_name: str, course_code: str):
        self._course_name = course_name
        self._course_code = course_code

        for i in range(14): # 14 is the number of weeks in a semester (can be changed to a different value if needed)
            self._academic_weeks.update({i:AcademicWeek(i)})
            print(self._academic_weeks[i].get_week_no())

class Student:
    '''
        A class that represents the student.
    '''

    def __init__(self, student_name: str, netID: str, UIN: str):
        self._student_name = student_name
        self._netID = netID
        self._UIN = UIN

def main():
    c_obj = Course('CourseName','CourseCode')

if __name__ == "__main__":
    main()
