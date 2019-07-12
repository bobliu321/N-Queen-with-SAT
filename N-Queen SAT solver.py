import sys
import math
import os
import time

def exactly_one(X):
    const=""
    for i in X:
        const=const+str(i)+" "
    const=const+"0\n"
    const=const+at_most_one(X)
   

    return const

def at_most_one(X):
    const=""
    for i in X:
        for ii in X[X.index(i)+1:]:
            const=const+"-"+str(i)+" -"+str(ii)+" 0\n"
    return const






def make_queen_sat(N):
    const=""
    #row constraints
    for row in range(N):
        Array=[]
        for column in range(N):
             Array.append(row*N+column+1)
        const=const+exactly_one(Array)
    #column constraints
    for column in range(N):
        Array=[]
        for row in range(N):
             Array.append(row*N+column+1)
        const=const+exactly_one(Array)
    #diagonal constraints
    #top right triangle
    incRow=1
    column=N-3
    
    for count in range(1,N):
        Array=[]
        incRow=incRow+1
        for row in range(0,incRow,1):
            column=column+1
            Array.append(row*N+column+1)
        column=column-(count+2)
        const=const+at_most_one(Array)
    #bottom left triangle
    incCol=1
    row=N-3
    for count in range(1,N-1):
         Array=[]
         incCol=incCol+1
         for column in range(0,incCol,1):
             row=row+1
             Array.append(row*N+column+1)
         row=row-(count+2)
         const=const+at_most_one(Array)
    #Top Left triangle
    incRow=1
    column=2
    for count in range(1,N):
        Array=[]
        incRow=incRow+1
        for row in range(0,incRow,1):
            column=column-1
            Array.append(row*N+column+1)
        column=column+count+2
        const=const+at_most_one(Array)
    #Bottom right triangle
    incCol=-1
    row=0
    for count in range(N-1,1,-1):
         Array=[]
         incCol=incCol+1
         for column in range(N-1,incCol,-1):
             row=row+1
             Array.append(row*N+column+1)
         row=row-(count-1)
         const=const+at_most_one(Array)


    f=open("a3_q1.txt","w+")
    f.write('c ' + str(N)+"-queens problem\n")
    f.write('p cnf ' + str(N*N) + ' ' + str(const.count('\n')))
    f.write("\n")
    f.write(const)
    f.close()

    
    

def draw_queen_sat_sol(sol):

    split=sol.splitlines()
    if split[0]=="UNSAT":
        print("no solution")
        
    else:
        nums = [int(n) for n in split[1].split()]
        if math.sqrt(len(nums))>40:
            print("Too Big")
        else:
            display=""
            for i in range(len(nums)-1):
                if nums[i]<0:
                    display=display+". "
                else:
                    display=display+"Q "          

                if nums[i]%math.sqrt(len(nums)-1)==0:
                    display=display+"\n"
            print(display)


        
    
    
###main
MAX_N=2

while True:
   make_queen_sat(MAX_N)
   start = time.time()
   os.system('minisat a3_q1.txt out.txt')
   end = time.time()
   print("Solver running time:",end-start)
   print("MAX_N: ", MAX_N)
   f=open("out.txt","r")
   if f.mode == 'r':
       contents = f.read()
   draw_queen_sat_sol(contents)
   f.close()
   if end-start>10:
       break
   MAX_N=MAX_N+1






