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

import numpy as np

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
    
    def __init__(self, week_no: int, has_exam: bool = False, has_project: bool = False, has_assignment: bool = False):
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

        has_exams = round(np.random.random()) # I assume likelyhood of having (or not having) exams in a course to be equal, as per my experience at iSchool, UIUC
        has_project = round(np.random.random()) # I assume likelyhood of having (or not having) a project in a course to be equal, as per my experience at iSchool, UIUC
        
        # Assignments generally tend to be either weekly, or bi-weekly (fortnightly)
        
        assignments_frequency = round(np.random.random()) # if 0 -> weekly assingments, else 1 -> bi-weekly (fortnightly) assignments
        assignment_starting_week = round(np.random.random()) # may start either from week 1 (if 0), or week 2 (if 1)
        
        assignment_weeks = []
        if assignments_frequency == 0:
            if assignment_starting_week == 0:
                assignment_weeks = [1,2,3,4,5,6,7,8,9,10,11,12,13]
            elif assignment_starting_week == 1:
                assignment_weeks = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        elif assignments_frequency == 1:
            if assignment_starting_week == 0:
                assignment_weeks = [1,3,5,7,9,11,13]
            elif assignment_starting_week == 1:
                assignment_weeks = [2,4,6,8,10,12,14]
        
        # I assume that a course may have either 2 exams (mid. and final or none), or no exams. Similarly for project deliverables.
        mid_term_exam = 0 # week of mid-term exam
        final_exam = 0 # week of final exam
        mid_project_deliverable = 0 # week when mid-term deliverable is due
        final_project_deliverable = 0 # week when final deliverable is due
        
        if has_exams == 1:
            mid_term_exam = int(round(np.random.triangular(5,7,8,1)[0])) # mid-term exam scheduled sometime between weeks 5-8 with most likelihood of week 7
            final_exam = int(round(np.random.triangular(12,14,14,1)[0])) # mid-term exam scheduled sometime between weeks 12-14 with most likelihood of week 14 (finals week)
        
        for i in range(1,15): # 14 is the number of weeks in a semester (can be changed to a different value if needed)
            arg_exam = False
            arg_project = False
            arg_assignment = False
            
            if has_exams == 1:
                if i == mid_term_exam:
                    arg_exam = True
                elif i == final_exam:
                    arg_exam = True
                        
            if has_project == 1:
                if i == mid_project_deliverable:
                    arg_project = True
                elif i == final_project_deliverable:
                    arg_project = True
        
            if i in assignment_weeks:
                arg_assignment = True
            
            self._academic_weeks.update({i:AcademicWeek(i, arg_exam, arg_project, arg_assignment)})
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
