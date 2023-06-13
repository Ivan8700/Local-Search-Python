from schedule import Schedule
import time
from random import randint
cnt_amount_of_moves = 0;

def TrivialSchedule(load_scheduling,jobs):
    for key,value in jobs.items():
        if (value % 2 == 0):
            load_scheduling.schedule[1][key] = value
            load_scheduling.load_of_each_machine[1]+=value
        else:
            load_scheduling.schedule[0][key] = value
            load_scheduling.load_of_each_machine[0]+=value # Scheduling trivialy the jobs - odd jobs on the first machine and even jobs on the second machine

def movingSingleEvenJob(load_scheduling,print_check):
    for index_machine in range(0,m):
        for key,value in sorted(load_scheduling.schedule[index_machine].items(),key=lambda item: item[1]):
            if(value % 2 == 0):
                for secondary_index_machine in range(0,m):
                    if(secondary_index_machine!=index_machine):
                        maximum_between_the_machines=max(load_scheduling.load_of_each_machine[index_machine],load_scheduling.load_of_each_machine[secondary_index_machine])
                        if(int(load_scheduling.load_of_each_machine[secondary_index_machine])+value<maximum_between_the_machines):
                            if(print_check==1):
                                print("Moving job (" + str(value) + ", " + str(key) + ") from machine number " + str(index_machine+1) + " to machine number " + str(secondary_index_machine+1));
                            load_scheduling.schedule[secondary_index_machine][key] = value
                            load_scheduling.load_of_each_machine[secondary_index_machine]+=value
                            del load_scheduling.schedule[index_machine][key]
                            load_scheduling.load_of_each_machine[index_machine]-=value
                            global cnt_amount_of_moves
                            cnt_amount_of_moves+=1;
                            return True
            if(value%2==0):
                break;
    return False # Trying to move an even job from some machine to another machine

def movingTwoOddJobs(load_scheduling,print_check): 
    for index_machine in range(0,m):
        for key,value in sorted(load_scheduling.schedule[index_machine].items(),key=lambda item: item[1]):
            if(value%2==1):
                for key_2,value_2 in sorted(load_scheduling.schedule[index_machine].items(),key=lambda item: item[1]):
                    if(key!=key_2 and (value_2)%2==1):
                        for secondary_machine in range(0,m):
                            maximum_between_the_machines=max(load_scheduling.load_of_each_machine[index_machine],load_scheduling.load_of_each_machine[secondary_machine])
                            if(load_scheduling.load_of_each_machine[secondary_machine]+value_2+value<maximum_between_the_machines):
                                if(print_check==1):
                                    print("Moving 2 odd jobs (" + str(value) + ", " + str(key) + ") and (" + str(value_2) + ", " + str(key_2) + ") from machine number " + str(index_machine+1) + " to machine number " + str(secondary_machine+1));
                                load_scheduling.load_of_each_machine[secondary_machine]+=(value+value_2);
                                load_scheduling.load_of_each_machine[index_machine]-= (value+value_2);
                                load_scheduling.schedule[secondary_machine][key]=value;
                                load_scheduling.schedule[secondary_machine][key_2] = value_2;
                                del load_scheduling.schedule[index_machine][key];
                                del load_scheduling.schedule[index_machine][key_2];
                                global cnt_amount_of_moves
                                cnt_amount_of_moves+=1;
                                return True; #Looking to move 2 odd jobs
                        break;
                break; #Trying to move 2 odd jobs to another machine
                    
def switchingAJob(load_scheduling,print_check):
    for index_machine in range(0,m-1):
        for key,value in load_scheduling.schedule[index_machine].items():
            for secondary_index_machine in range(index_machine+1,m):
                maximum_between_the_machines=max(load_scheduling.load_of_each_machine[index_machine],load_scheduling.load_of_each_machine[secondary_index_machine])
                for key_s,value_s in load_scheduling.schedule[secondary_index_machine].items():
                    if((value_s%2)==(value%2)):
                        if (load_scheduling.load_of_each_machine[index_machine]-value+value_s < maximum_between_the_machines and load_scheduling.load_of_each_machine[secondary_index_machine]+value-value_s<maximum_between_the_machines):
                            if(print_check==1):
                                print("Switching a job (" + str(value) + ", " + str(key) + ") from machine number " + str(index_machine+1) + " and job (" + str(value_s) + ", " + str(key_s) + ") from machine number " + str(secondary_index_machine+1))
                            load_scheduling.schedule[secondary_index_machine][key] = value;
                            load_scheduling.load_of_each_machine[secondary_index_machine] += (value-value_s);
                            load_scheduling.schedule[index_machine][key_s] = value_s;
                            load_scheduling.load_of_each_machine[index_machine] += (value_s-value);
                            del load_scheduling.schedule[index_machine][key];
                            del load_scheduling.schedule[secondary_index_machine][key_s];
                            global cnt_amount_of_moves
                            cnt_amount_of_moves+=1;
                            return True;
    return False; #Trying to switch even job for even and odd job for odd job between 2 machines

def switchingTwoJobsForOneEvenJob(load_scheduling,print_check):
    for index_machine in range(0,m):
        for key_1,value_1 in load_scheduling.schedule[index_machine].items():
            for key_2,value_2 in load_scheduling.schedule[index_machine].items():
                if(key_1 != key_2 and (value_1%2 == value_2%2)):
                    for secondary_index_machine in range(0,m):
                        if(secondary_index_machine!=index_machine):
                            maximum_between_the_machines=max(load_scheduling.load_of_each_machine[index_machine],load_scheduling.load_of_each_machine[secondary_index_machine])
                            for key_3,value_3 in load_scheduling.schedule[secondary_index_machine].items():
                                if(value_3 % 2 ==0 and (load_scheduling.load_of_each_machine[index_machine]-value_1-value_2+value_3 < maximum_between_the_machines) and (load_scheduling.load_of_each_machine[secondary_index_machine]-value_3+value_1+value_2 < maximum_between_the_machines)):
                                    if(print_check==1):
                                        print("Switching the jobs (" + str(value_1) + ", " + str(key_1) + ") and (" + str(value_2) + ", " + str(key_2) + ") from machine number " + str(index_machine+1) + " with job (" + str(value_3) + ", " + str(key_3) + ") from machine number " + str(secondary_index_machine+1));
                                    load_scheduling.load_of_each_machine[index_machine]+=(value_3-value_2-value_1);
                                    load_scheduling.load_of_each_machine[secondary_index_machine]+=(value_1+value_2-value_3);
                                    load_scheduling.schedule[index_machine][key_3]=value_3;
                                    del load_scheduling.schedule[index_machine][key_1];
                                    del load_scheduling.schedule[index_machine][key_2];
                                    load_scheduling.schedule[secondary_index_machine][key_1]=value_1;
                                    load_scheduling.schedule[secondary_index_machine][key_2]=value_2;
                                    del load_scheduling.schedule[secondary_index_machine][key_3];
                                    global cnt_amount_of_moves
                                    cnt_amount_of_moves+=1;
                                    return True;
    return False; #Trying to switch 2 even/odd jobs with 1 even job from another machine

def switchingTwoForTwo(load_scheduling,print_check):
    for index_machine in range(0,m-1):
        for key_1,value_1 in load_scheduling.schedule[index_machine].items():
            for key_2,value_2 in load_scheduling.schedule[index_machine].items():
                if(key_1 != key_2 and (value_1%2 == value_2%2)):
                    for secondary_index_machine in range(index_machine+1,m):
                        maximum_between_the_machines=max(load_scheduling.load_of_each_machine[index_machine],load_scheduling.load_of_each_machine[secondary_index_machine]);
                        for key_3,value_3 in load_scheduling.schedule[secondary_index_machine].items():
                            for key_4,value_4 in load_scheduling.schedule[secondary_index_machine].items():
                                if(key_3 != key_4 and (value_3 %2 == value_4 %2)):
                                    load_on_first_machine=load_scheduling.load_of_each_machine[index_machine];
                                    load_on_second_machine=load_scheduling.load_of_each_machine[secondary_index_machine];
                                    if((load_on_first_machine+value_3+value_4-value_1-value_2)<maximum_between_the_machines and (load_on_second_machine+value_1+value_2-value_3-value_4)<maximum_between_the_machines):
                                        if(print_check==1):
                                            print("Moving jobs (" + str(value_1) + ", " + str(key_1) + ") and (" + str(value_2) + ", " + str(key_2) + ") from machine number " + str(index_machine+1) + " with jobs (" + str(value_3) + ", " + str(key_3) + ") and (" + str(value_4) + ", " + str(key_4) + ") from machine number " + str(secondary_index_machine+1));
                                        #Tranfersing the jobs process
                                        load_scheduling.schedule[secondary_index_machine][key_1]=value_1;
                                        load_scheduling.schedule[secondary_index_machine][key_2]=value_2;
                                        load_scheduling.schedule[index_machine][key_3]=value_3;
                                        load_scheduling.schedule[index_machine][key_4]=value_4;
                                        load_scheduling.load_of_each_machine[secondary_index_machine]+=(value_1+value_2-value_3-value_4);
                                        load_scheduling.load_of_each_machine[index_machine]+=(value_3+value_4-value_1-value_2);
                                        #Removing the jobs
                                        del load_scheduling.schedule[index_machine][key_1];
                                        del load_scheduling.schedule[index_machine][key_2];
                                        del load_scheduling.schedule[secondary_index_machine][key_3];
                                        del load_scheduling.schedule[secondary_index_machine][key_4];
                                        global cnt_amount_of_moves
                                        cnt_amount_of_moves+=1;
                                        return True;
    return False; #Trying to switch 2 even/odd jobs for 2 even/odd jobs from another machine
                                        
def local_search_algorithm(load_scheduling,print_check): #Main Algorithm
    moving_single_job_bool = True; switching_a_job_bool = True; moving_2_odd_jobs_bool = True; switching_2_jobs_with_1_even_job_bool=True; switching_2_jobs_for_2_jobs_bool=True;
    while(moving_single_job_bool or switching_a_job_bool or moving_2_odd_jobs_bool or switching_2_jobs_with_1_even_job_bool or switching_2_jobs_for_2_jobs_bool):
        moving_single_job_bool = movingSingleEvenJob(load_scheduling,print_check)
        if(moving_single_job_bool): continue
        moving_2_odd_jobs_bool =  movingTwoOddJobs(load_scheduling,print_check);
        if(moving_2_odd_jobs_bool): continue;
        switching_a_job_bool = switchingAJob(load_scheduling,print_check);
        if(switching_a_job_bool): continue;
        switching_2_jobs_with_1_even_job_bool=switchingTwoJobsForOneEvenJob(load_scheduling,print_check);
        if(switching_2_jobs_with_1_even_job_bool): continue;
        switching_2_jobs_for_2_jobs_bool=switchingTwoForTwo(load_scheduling,print_check);
        if(switching_2_jobs_for_2_jobs_bool): continue;

start_time = time.time();
print_check=int(input("Would you like to print the moving of jobs ? 0 - no , 1 - yes : "));
input_option=int(input("How would you like to get the input? 0 - .txt file, 1 - manual insertion, 2 - randomization : "));
#Read from .txt file
if(input_option==0):
    input_from_text = open("inputs/input1.txt")
    m = int(input_from_text.readline())
    n = int(input_from_text.readline())
else: #specific input
    m = int(input("Enter amount of the machines\n")) ##in case you want to run
    n = int(input("Enter amount of jobs\n")) ##
indexes = []
job_values = []

cnt_odd = 0
if(input_option== 1 or input_option==2):
    print("Enter the jobs one by one (integer) : ")
for x in range(1,(n+1)): #create input of jobs
    indexes.append(x);
    if(input_option==0):
        k=(int(input_from_text.readline())) #if you want to read the jobs from a specific txt file.
        job_values.append(k);
    elif (input_option==1):
        k=(int(input())); #if you want to insert an input manually
        job_values.append(k);
    else:
        k=randint(21,60);
        job_values.append(k); # if you want to random the input
    if(k%2==1):
        cnt_odd+=1;
if(cnt_odd % 2 == 1): #if the amount of odd jobs is odd, there can't be any solution for this input. instead it increases by 1 some odd job.
    cnt=0;
    for x in job_values:
        if(x%2==1): 
            print("Job with value " + str(job_values[cnt]) + " will be changed to " + str(job_values[cnt]+1) + " Since number of odd jobs is odd");
            job_values[cnt]+=1;
            break;
        cnt+=1;
    #print("Odd amount of odd jobs, there is no solution")
    #exit(0)
jobs = dict(zip(indexes,job_values))
load_scheduling = Schedule(m)
TrivialSchedule(load_scheduling,jobs)
local_search_algorithm(load_scheduling,print_check)
load_scheduling.print_schedule();
print("Amount of moves the algorithm did is : " + str(cnt_amount_of_moves));
print("Time taken is {} seconds" .format(time.time() - start_time))


