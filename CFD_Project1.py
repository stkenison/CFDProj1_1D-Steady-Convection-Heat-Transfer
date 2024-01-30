import numpy as np; import os;import matplotlib.pyplot as plt;
os.system('cls')
plt.rcParams['font.family'] = 'Times New Roman'

#define constants for problem
length = 0.5; Ta = 100; Tb = 500; k = 10; max_iter = 10000;max_error = 10e-4

#ask for dimensions of matrix to be solved
dim = int(input("Please enter dimensions/unknowns to be solved for: "))
print("Solving using jacobi iteration...\n")

#create matrixes to be solved
dx = length/(dim+1)
solution = np.hstack((Ta,np.full(dim,(Ta+Tb)/2),Tb)) #create solution matrix with all endpoints and middle values set to midpoint
working_solution = solution
print("dx =",dx)
print("starting solution = ",solution)

#create exact solution matrix
dTdx = (Tb-Ta)/length
exact_solution = np.hstack((Ta,np.zeros(dim),Tb))
for i in range(1,dim+1):
        exact_solution[i] = dTdx*i*dx+Ta
print("exact solution = ",exact_solution)

#create CFD algorithm constants
a_eorw = k/dx #constant for sides of finite control volume
print("a_e or a_w = ", a_eorw)
a_p = a_eorw*2 #constant for point in middle of control volume
print("a_point = ",a_p,"\n")

#iterate towards final solution
error = np.ones(dim+2)
error_array = np.zeros(max_iter)
solutions_array = np.zeros((max_iter,int(dim)))
for i in range(0,max_iter):
     for j in range(1,dim+1): #one iteration towards solution
        solutions_array[(i,j-1)] = working_solution[j]
        working_solution[j] = (solution[j-1]*a_eorw+solution[j+1]*a_eorw)/a_p #jacobi iteration
     solution = working_solution
     for k in range(0,dim+2): #check relative error of current solution iteration
         error[k] = (exact_solution[k]-solution[k])/exact_solution[k]
     e = np.max(np.abs(error)) #calculate max error
     error_array[i] = e
     if e<max_error: #break out of loop if sufficient accuracy is achieved
         break

print("iterations = ",i,)
print("end solution: ",solution,"\n")


#generate error plot
x_vals = np.arange(i+1)
plt.figure(1)
plt.title("Maximum Iteration Error")
plt.xlabel("Iterations");plt.ylabel("Relative Error")
plt.xlim(0,i)
plt.plot(x_vals+1,error_array[:i+1]) #Relative error is shifted by 1 to match iterations properly


#generate iterative solution plot
plt.figure(2)
plt.title("Iterative Solution")
plt.xlabel("Iterations");plt.ylabel("Solution Value (°C)")
for m in range(0,dim): #create legend as each line is plotted
     plt.plot(x_vals,solutions_array[:i+1,m],label='T{}'.format(m+1))
plt.legend(loc='upper right')
plt.show()



