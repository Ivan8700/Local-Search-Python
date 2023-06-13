import math;
class Schedule(object):
    """This class will show the status of the schedule on the machines, including the load of each machine"""

    def __init__(self,m):
        self.schedule=[];
        self.load_of_each_machine = [];
        self.m=m;
        for machine_index in range(0,m):
            self.schedule.append({});
            self.load_of_each_machine.append(0);

    def print_schedule(self):
        print("\n");
        sum=0; makespan=0;
        for machine_index in range(0,self.m):
            if (self.load_of_each_machine[machine_index] > makespan):
                makespan=self.load_of_each_machine[machine_index];
            output_string='';
            print("Machine number " + str(machine_index+1));
            output_string+= "{";
            for key,value in self.schedule[machine_index].items():
               output_string+="(" + str(value) + ", " + str(key) + ") ";
            output_string+="}"
            print(output_string);
            del output_string;
            print("load of the machine is {}\n".format(self.load_of_each_machine[machine_index]));
            sum += self.load_of_each_machine[machine_index];
        print("The makespan is " + str(makespan));
        OPT=math.ceil(sum/self.m);
        if (OPT%2==1): OPT +=1;
        print("The OPT bound is {} ".format(OPT));
        print("The sum of jobs is " + str(sum));
