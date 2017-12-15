# Title: Simulation of Course Workload and Academic Pressure for U of I Students

## Team Member(s): Shreenandan Rajarathnam

# Monte Carlo Simulation Scenario & Purpose: 

The objective of this simulation is to check the study workload of students during a semester and predict the busiest for the students. The workload and pressure on students depend on multiple factors (or parameters) including but not restricted to the following:

No. of courses (or credits) taken per semester

No. of assignments, project deliverables, and exams (and other tasks)

No. of tasks (assignments, exams, projects and etc.) that are pending or due at a given time period 

Difficulty level of each task (assignments, exams, projects and etc.) 

A combination of the aforementioned factors determines the amount of time and effort a student needs to put in at any time. If we divide the semester into 14 weeks (could be a different number), the number of tasks pending, the time required to be dedicated (cumulative of time required for all tasks due) and difficulty level of the tasks are random or can be assumed to be random for practical applications. The number of parameters involved makes this a complex system to understand. Therefore, a Monte Carlo simulation could be employed to simulate the system and predict or determine which weeks would be most hectic, in terms of academic workload. 

Assumptions:
There are certain assumptions and considerations, for example, the courses taken and department/program and/or level of courses could impact the difficulty level and time taken for tasks in a subject. For practical purposes of the study, we consider these random for simulation. 

### Hypothesis before running the simulation:

From my experience as a student, I believe that the finals week/s (last 1 or 2 weeks of the semester) and the middle week ( the mid-term week or the week just half-way through the semester) tend to be the most hectic. However, this is just a hypothesis. 

Actual simulation and other methods of data analysis could provide counter-intuitive results, for example, week 2 could be the busiest for some students. 

### Simulation's variables of uncertainty

The input variables or parameters of uncertainty would be the tasks pending or due per week (assignments, exams, projects and etc.), the difficulty levels of the tasks and time taken for each task. These depend on the number of coursess (or credits) taken which is also an input variable, however, that is not random.

Ranges of the variables would be based on the pattern followed by the School of Information Sciences, UIUC (could be any other department as well). For probability distribution, real-world data will be analyzed/compared (sample of students and their course schedules) and considered for this project.

Multiple distributions (Normal distribution and Triangular distribution) have been used according to context (see comments in the code).

I believe using real-world data for analysis and/or comparison is a good representation of reality. Therefore, an example course from the School of Information Sciences, UIUC has been considered for comparison (check Real_Courses.pdf).

## Instructions on how to use the program:

For an illustrative walkthrough, check the Conclusion.pdf file, which contains sample input along with screenshots of terminal output and graphs. The analysis has been explained with conclusion. 

Instructions:
Enter user input for number of courses. The program runs simulation and displays output graphs for each course, followed by a graphical representation of total workload (across all courses for the semester). 

# Conclusion:

We can conclude that the hypothesis does not always hold true (based on multiple simulation runs). Sometimes, the most hectic time for students could be weeks other than the mid-term and finals weeks.

(for a detailed explanation, refer to Conclusion.pdf file)


## Sources Used:

For this project, an example course from the School of Information Sciences, UIUC has been considered for comparison (check Real_Courses.pdf). 

References:

[1] Thomas W. Armstrong, "Making Decisions with Uncertain Data Practical Examples of Monte Carlo Simulations"
Link: http://synergist.aiha.org/monte-carlo-risk-assessment

[2] Jim Frost, "Understanding Monte Carlo Simulation with an Example". The Minitab Blog, April 25
Link: http://blog.minitab.com/blog/adventures-in-statistics-2/understanding-monte-carlo-simulation-with-an-example

[3] "Monte Carlo Simulation". Palisade
Link: http://synergist.aiha.org/monte-carlo-risk-assessment

