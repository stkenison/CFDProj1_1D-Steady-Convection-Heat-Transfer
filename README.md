# CFD Project 1 | 1-D Steady Convection Heat Transfer

"CFD_Project1.py" is a python script written by Spencer Kenison
to solve a 1-D, steady heat conduction problem. It was written 
for MAE 5440 at Utah State University

The script was written using Python 3.11 interpreter but any similar 
version should function normally.

The script requires the following libraries to be installed:
- numpy
- matplotlib.pyplot
using PIP or other package-management system.

Run the "CFD_Project1.py" file using Python interpreter. Can be run
in terminal using "python CFD_Project1.py" command or from IDE such
as VSCode.

After running command to start python script, the terminal will ask for 
number of desired dimensions/unknowns for simulation. Enter the number of 
desired dimensions/unknowns and hit "Enter" to run numerical solver.

The python program will generate various information in the terminal for 
reference, including the step size between temperature values, the initial 
temperature values, and coefficient used for calulations. 

Following the running of the program, 2 plots will be generated showing 
temperature values and relative error of each iteration. The terminal will
display the number of iterations and the final iterative solution.

PLEASE NOTE: The script is written with a maximum number of iterations of 10,000.
If solutions with more than 99 unknowns are desired, more than 10,000 iterations 
may be required and this limit can be modified.
