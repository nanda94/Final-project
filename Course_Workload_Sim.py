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
import texttable as tt
import matplotlib.pyplot as plt

#the following are variables to hold cumulative values across multiple weeks for multiple courses and hence global as they are larger than the scope of the individual classes
total_tasks = []
total_no_of_hours = []
sum_weighted_difficulty = [] # Note that this variable holds the summation and not the final values for weighted difficulty(refer to 4th comment on main, after declaring Student object)

class AcademicTask:
    '''
        A class that represents 1 academic task (exam, assignment, project deliverable, quiz and etc.) in a week.
    '''
    def __init__(self, type_of_task: str, difficulty_level: int, no_of_hours_of_work: int):
        '''
            Initializer for AcademicTask class.
            :param type_of_task: Type of task (Exam, assignment, project deliverable or quiz)
            :param difficulty_level: Difficulty level for the task (on a scale of 10)
            :param no_of_hours_of_work: No. of hours of work required for completing the task (per academic week)
        '''
        
        self._type_of_task = type_of_task
        self._difficulty_level = difficulty_level
        self._no_of_hours_of_work = no_of_hours_of_work

    def get_no_of_hours_of_work(self):
            return self._no_of_hours_of_work

    def get_difficulty(self):
        return self._difficulty_level

class AcademicWeek:
    '''
        A class that represents 1 academic week (for a course) in a semester.
    '''
    _tasks = {}
    
    def __init__(self, week_no: int, has_exam: bool = False, has_project: bool = False, has_assignment: bool = False, has_quiz: bool = False):
        '''
            Initializer for AcademicWeek class.
            :param week_no: Academic week number in the semester (1-14)
            :param has_exam: True or False corresponding to whether or not the AcademicWeek has an exam
            :param has_project: True or False corresponding to whether or not the AcademicWeek has a project deliverable due
            :param has_assignment: True or False corresponding to whether or not the AcademicWeek has an assignment
            :param has_quiz: True or False corresponding to whether or not the AcademicWeek has a quiz
        '''
        
        self._week_no = week_no
        self._has_exam = has_exam
        self._has_project = has_project
        self._has_assignment = has_assignment
        self._has_quiz = has_quiz
    
        if has_exam == True:
            exam_difficulty = 0
            exam_duration = 0
            
            exam_difficulty = int(round(np.random.normal(7,1,1)[0])) # As per my experience at iSchool, UIUC, the difficulty of exams would mostly be around 6-8 (on a scale of 10), sometimes as low as 5 or high as 9, and rarely 4 or 10
            exam_duration = round(np.random.random()) + 2 # Exam duration is mostly either 2 hours, or 3 hours
            
            self._tasks.update({'Exam':AcademicTask('Exam', exam_difficulty, exam_duration)})

        if has_project == True:
            project_difficulty = 0
            project_duration = 0
            
            project_difficulty = int(round(np.random.normal(7,1,1)[0])) # As per my experience at iSchool, UIUC, the difficulty of projects would mostly be around 6-8 (on a scale of 10), sometimes as low as 5 or high as 9, and rarely 4 or 10
            project_duration = int(round(np.random.normal(7,1,1)[0])) # No. of hours required per week for project is similar to difficulty (overall duration is high)
            
            self._tasks.update({'Project':AcademicTask('Project', project_difficulty, project_duration)})

        if has_assignment == True:
            assignment_difficulty = 0
            assignment_duration = 0
            
            assignment_difficulty = int(round(np.random.triangular(1,5,10,1)[0])) # As per my experience at iSchool, UIUC, the difficulty of assignments would mostly be anywhere between 1-10 with 7 most likely
            assignment_duration = int(round(np.random.triangular(1,5,10,1)[0])) # As per my experience at iSchool, UIUC, the no. of hours required per week for assignments would mostly be anywhere between 1-10 with 5 most likely
            
            self._tasks.update({'Assignment':AcademicTask('Assignment', assignment_difficulty, assignment_duration)})

        if has_quiz == True:
            quiz_difficulty = 0
            quiz_duration = 0
            
            quiz_difficulty = int(round(np.random.triangular(1,5,10,1)[0])) # As per my experience at iSchool, UIUC, the difficulty of assignments would mostly be anywhere between 1-10 with 5 most likely
            quiz_duration = int(round(np.random.triangular(1,2,3,1)[0])) # As per my experience at iSchool, UIUC, the no. of hours required per week for assignments would mostly be anywhere between 1-3 with 2 most likely
            
            self._tasks.update({'Quiz':AcademicTask('Quiz', quiz_difficulty, quiz_duration)})

    def get_weekly_stats(self):
        '''
            Function to get weekly statistics (total no. of tasks per week, total no. of hours of work per week, total weighted difficulty per week).
            :return (self._week_no, no_of_tasks, no_of_hours, weighted_difficulty): Returns tuple containing the academic week number, total no. of tasks per week, total no. of hours of work per week, total weighted difficulty per week
        '''
        no_of_tasks = 0
        no_of_hours = 0
        weighted_difficulty = 0.0
        for task_name, task_details in self._tasks.items():
            no_of_tasks = no_of_tasks + 1
            no_of_hours = no_of_hours + task_details.get_no_of_hours_of_work()
            weighted_difficulty = weighted_difficulty + (task_details.get_difficulty() * task_details.get_no_of_hours_of_work())
    
        if no_of_hours != 0:
                weighted_difficulty = weighted_difficulty / no_of_hours
        return (self._week_no, no_of_tasks, no_of_hours, weighted_difficulty)

class Course:
    '''
        A class that represents 1 course taken by a student in a semester.
    '''
    
    _academic_weeks = {}
    # for printing weekly tasks statistics for the course in table form
    tab = tt.Texttable()
    
    def __init__(self, course_name: str, course_code: str):
        '''
            Initializer for Course class.
            :param course_name: Name of the course (for future use, if program requires taking user input)
            :param course_code: Course code for the given course
        '''
        self._course_name = course_name
        self._course_code = course_code

        has_exams = round(np.random.random()) # I assume likelyhood of having (or not having) exams in a course to be equal, as per my experience at iSchool, UIUC
        has_project = round(np.random.random()) # I assume likelyhood of having (or not having) a project in a course to be equal, as per my experience at iSchool, UIUC
        has_quiz = round(np.random.random()) # likelihood of having (or not having) quizzes
        
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
        
        self.tab = tt.Texttable()
        heading = ['Week No.', 'No. of Tasks', 'Total no. of Hours', 'Weighted Difficulty',]
        self.tab.header(heading)
        
        if has_exams == 1:
            mid_term_exam = int(round(np.random.triangular(5,7,8,1)[0])) # mid-term exam scheduled sometime between weeks 5-8 with most likelihood of week 7
            final_exam = int(round(np.random.triangular(12,14,14,1)[0])) # mid-term exam scheduled sometime between weeks 12-14 with most likelihood of week 14 (finals week)
        
        if has_project == 1:
            mid_project_deliverable = int(round(np.random.triangular(5,7,8,1)[0])) # mid-term project deliverable scheduled sometime between weeks 5-8 with most likelihood of week 7
            final_project_deliverable = int(round(np.random.triangular(12,14,14,1)[0])) # final project deliverable scheduled sometime between weeks 12-14 with most likelihood of week 14 (finals week)
        
        week_no_list = []
        no_of_hours_list = []
        no_of_tasks_list = []
        weighted_difficulty_list = []
        
        
        for i in range(1,15): # 14 is the number of weeks in a semester (can be changed to a different value if needed)
            arg_exam = False
            arg_project = False
            arg_assignment = False
            arg_quiz = False
            quiz_this_week = 0
            
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
        
            if has_quiz == 1:
                quiz_this_week = round(np.random.random())
                if quiz_this_week == 1:
                    arg_quiz = True
        
            if i in assignment_weeks:
                arg_assignment = True
            
            self._academic_weeks.update({i:AcademicWeek(i, arg_exam, arg_project, arg_assignment, arg_quiz)})

            # Gets the details for the tasks for each week
            week_no, no_of_tasks, no_of_hours, weighted_difficulty = self._academic_weeks[i].get_weekly_stats()

            # for adding rows in the table
            row = [week_no, no_of_tasks, no_of_hours, weighted_difficulty]
            self.tab.add_row(row)
            week_no_list.append(week_no)
            weighted_difficulty_list.append(weighted_difficulty)
            no_of_tasks_list.append(no_of_tasks)
            no_of_hours_list.append(no_of_hours)
            
            # the following takes cumulative across various courses, and are for adding to the global variables initialized in the main
            total_tasks[i - 1] = total_tasks[i - 1] + no_of_tasks # i - 1 because i ranges from 1 to 15
            total_no_of_hours[i - 1] = total_no_of_hours[i - 1] + no_of_hours
            sum_weighted_difficulty[i - 1] = sum_weighted_difficulty[i - 1] + (weighted_difficulty * no_of_hours)
    
        s = self.tab.draw()
        print('\n')
        print(s)

        # for plotting charts for No. of tasks per week, no. of hours required per week and weighted difficulty per week, for 1 course

        plt.figure(figsize=(10,8))
        fig = plt.gcf()
        fig.canvas.set_window_title(self._course_name + ' (' + self._course_code + ')')
        plt.subplots_adjust(hspace = 0.4)

        plt.subplot(3, 1, 1)
        plt.plot(week_no_list, no_of_hours_list)
        plt.ylabel('No. of Hours Required')
        plt.xlabel('Week')

        plt.subplot(3, 1, 2)
        plt.plot(week_no_list, no_of_tasks_list)
        plt.ylabel('No. of Tasks')
        plt.xlabel('Week')

        plt.subplot(3, 1, 3)
        plt.plot(week_no_list, weighted_difficulty_list)
        plt.ylabel('Weighted Difficulty')
        plt.xlabel('Week')
        
        plt.show()

class Student:
    '''
        A class that represents the student.
    '''
    
    _courses = {}
    
    def __init__(self, student_name: str, netID: str, UIN: str):
        '''
            Initializer for Student class.
            :param student_name: Name of the student (for future use, if program requires taking user input)
            :param netID: NetID of the student
            :param UIN: UIN of the student
        '''
        self._student_name = student_name
        self._netID = netID
        self._UIN = UIN
        no_of_courses = 0
        
        try:
            no_of_courses = int(input('\nEnter the number of courses taken this semester: '))
        except ValueError:
            print("\nInvalid input!")
            exit(0)

        if no_of_courses not in range(1,11): # I assume the no. of courses that can be taken is between 1 to 10 (there might be exceptions as well, but those are not taken for the sake of simplicity)
            print('\nNot a practical input for number of courses!')
            exit(0)

        for i in range(1,no_of_courses + 1):
            print('\nCourse Name: CourseName' + str(i) + '\nCourse Code: CourseCode0' + str(i))
            self._courses.update({i:Course('CourseName' + str(i), 'CourseCode0' + str(i))}) # for future if program would take course name and course codes, as of now that is beyond the scope of the simulation

def main():
    """
        Take user input for number of courses to simulate. Then create object of type Student and calculate total workload for the entire semester for the student (along with plotting a graph).
    """
    global total_tasks
    global total_no_of_hours
    global sum_weighted_difficulty
    total_weighted_difficulty = []
    week_no_list = []
    tab = tt.Texttable()
    heading = ['Week No.', 'No. of Tasks', 'Total no. of Hours', 'Weighted Difficulty',]
    tab.header(heading)
    
    # initial setting up
    for i in range(1,15): # 14 is the number of weeks in a semester (can be changed to a different value if needed)
        total_tasks.append(0)
        total_no_of_hours.append(0)
        sum_weighted_difficulty.append(0.0)
    # total_weighted_difficulty.append(0.0)
    s_obj = Student('StudentName','NetID','UIN') # can take user input, but that is beyond the scope of this simulation project

    # for calculating the total weighted difficulty from summation of weighted difficulty (Formula: ( Σ (Difficulty * No_of_hours) /  Σ No_of_hours ))
    for i in range(1,15):
        total_weighted_difficulty.append(sum_weighted_difficulty[i - 1] / total_no_of_hours[i - 1])
        week_no_list.append(i)
        row = [i, total_tasks[i - 1], total_no_of_hours[i - 1], total_weighted_difficulty[i - 1]]
        tab.add_row(row)

    print('\nTotal course workload for the entire semester: ')
    s = tab.draw()
    print('\n')
    print(s)

    plt.figure(figsize=(10,8))
    fig = plt.gcf()
    fig.canvas.set_window_title('Total Workload For The Semester')
    plt.subplots_adjust(hspace = 0.4)
        
    plt.subplot(3, 1, 1)
    plt.plot(week_no_list, total_no_of_hours)
    plt.ylabel('No. of Hours Required')
    plt.xlabel('Week')
        
    plt.subplot(3, 1, 2)
    plt.plot(week_no_list, total_tasks)
    plt.ylabel('No. of Tasks')
    plt.xlabel('Week')
    
    plt.subplot(3, 1, 3)
    plt.plot(week_no_list, total_weighted_difficulty)
    plt.ylabel('Weighted Difficulty')
    plt.xlabel('Week')
        
    plt.show()

if __name__ == "__main__":
    main()
