# Title: 

#Simulation of Course Workload and Academic Pressure for U of I Students

## Team Member(s): Shreenandan Rajarathnam

# Monte Carlo Simulation Scenario & Purpose: 

The objective of this simulation is to check the study workload of students during a semester and predict the busiest for the students. The workload and pressure on students depend on multiple factors (or parameters) including but not restricted to the following:

No. of credits (or courses) taken per semester
No. of assignments, projects, and exams (and other tasks)
No. of tasks (assignments, exams, projects and etc.) that are pending or due at a given time period 
Difficulty level of each task (assignments, exams, projects and etc.) 

A combination of the aforementioned factors determines the amount of time and effort a student needs to put in at any time. If we divide the semester into 13 weeks (could be a different number), the number of tasks pending, the time required to be dedicated (cumulative of time required for all tasks due) and difficulty level of the tasks are random or can be assumed to be random for practical applications. The number of parameters involved makes this a complex system to understand. Therefore, a Monte Carlo simulation could be employed to simulate the system and predict or determine which weeks would be most hectic, in terms of academic workload. 

Assumptions:
There are certain assumptions and considerations, for example, the courses taken and department/program and/or level of courses could impact the difficulty level and time taken for tasks in a subject. For practical purposes of the study, we consider these random for simulation. 

### Hypothesis before running the simulation:

From my experience as a student, I believe that the finals week/s (last 1 or 2 weeks of the semester) and the middle week ( the mid-term week or the week just half-way through the semester) tend to be the most hectic. However, this is just a hypothesis. 

Actual simulation and other methods of data analysis could provide counter-intuitive results, for example, week 2 could be the busiest for some students. 

### Simulation's variables of uncertainty

The input variables or parameters of uncertainty would be the tasks pending or due per week (assignments, exams, projects and etc.), the difficulty levels of the tasks and time taken for each task. These depend on the number of credits (or courses) taken which is also an input variable, however, that is not random.

Ranges of the variables would be based on the pattern followed by the School of Information Sciences, UIUC (could be any other department as well). For probability distribution, real-world data will be analyzed/compared (sample of students and their course schedules) and considered for this project.

I believe using real-world data for analysis and/or comparison is a good representation of reality.  

## Instructions on how to use the program:

Firstly, the program takes the input values for the aforementioned parameters/variables.

The program then performs the simulation to check the busiest or most hectic week/s and checks if the hypothesis holds true.

The program also computes and compares the results of the data from the available dataset (a small sample of students from the School of Information Sciences) along with the simulation results.


## Sources Used:

For this project, I intend to use real-world data. The first step is to take a small sample of students from the School of Information Sciences (or any other department) and analyze their schedules and workload (for different combinations of courses). Next step would be to check if the hypothesis is validated or refuted, and also if the simulations provide a similar outcome. 

References:

[1] Thomas W. Armstrong, "Making Decisions with Uncertain Data Practical Examples of Monte Carlo Simulations"
Link: http://synergist.aiha.org/monte-carlo-risk-assessment

[2] Jim Frost, "Understanding Monte Carlo Simulation with an Example". The Minitab Blog, April 25
Link: http://blog.minitab.com/blog/adventures-in-statistics-2/understanding-monte-carlo-simulation-with-an-example

[3] "Monte Carlo Simulation". Palisade
Link: http://synergist.aiha.org/monte-carlo-risk-assessment

