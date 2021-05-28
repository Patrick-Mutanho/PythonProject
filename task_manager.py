import linecache
from datetime import *
from datetime import datetime as dt


print("This is test")
#register user function
def reg_user(username):
    #open the user file
    user_file= open('user.txt','r+')
    lis=[]
    if username == "admin":
        access=False
        while access == False:
            #ask user to input username
            add_user_name=input("Please enter your username: ")
            # ask user to enter password
            add_user_password=input("Please enter your username: ")
            
            #add information to the userfile
            for line in user_file:
                #declare two variables for theusername and password on each line of the file
                valid_username, valid_password=line.split(", ")
                #check to see if credentials entered are true and set login access
                user_name=valid_username.strip("\n")
                lis.append(user_name) 
                
            if add_user_name in lis:
                print("Username already exists!, please start over!") 
                access=False
                   
            if add_user_name not in lis:
                #add information to the userfile
                user_file.write(f"{add_user_name}, {add_user_password}\n")
                access=True                
    else:
        print("Access Denied")
    user_file.seek(0,0)
    user_file.close()
    return 0

#add task function
def add_task():
     #open the user file
        tasks= open('tasks.txt','a+')
        #admin, Assign initial tasks, Use taskManager.py to assign each team member with appropriate tasks, 10 Oct 2019, 25 Oct 2019, No
        
        #ask user to enter assign user for the task
        assign_user= input("Enter a user for the task: ")
        #ask user to enter tittle of the task
        task_title = input("Enter a title for the task: ")
        #ask user to enter task description
        task_description = input("Enter a title for the task: ")
        #ask user for start date
        start_date= input("Enter start date for the task: ")
        #ask user to enter end date
        end_date= input("Enter end date for the task: ")
        #ask user if task is complete
        task_status=input("Is the task completed?: ")
        #write to tasks file
        tasks.write(f"\n{assign_user}, {task_title}, Use taskManager.py to {task_description}, {start_date}, {end_date}, {task_status}")
        #close the file
        tasks.close()
        return 0

#view all tasks function
def view_all_tasks():
     #open the user file
        tasks= open('tasks.txt','r')
        for line in tasks:
            #unpack the line and asign it to respective values
            assign_user, task_title, task_description, start_date, end_date, task_status= line.split(", ")
            #print out the information
            print(f"""
        Assign User      :  {assign_user}
        Task Title       :  {task_title}
        Task Description :  {task_description}
        Start Date       :  {start_date}
        End Date         :  {end_date}
        Task completed   :  {task_status}
              """)
        #close task file
        tasks.close()
        return 0

#view the user tasks     
def view_my_tasks(username):
    
    #open the file
    data_file=open("tasks.txt","r")
    #read all the contents in the file to a list
    data=data_file.readlines()
    #close the file
    data_file.close()
    
    #make relevant variables used throughout the function
    task_number=0
    track_list=[]
    u={}
    line_number=-1
    count=-1
    
    #open the tasks file
    tasks= open('tasks.txt','r')
    for line in tasks:
        #store the line number of the file
        line_number+=1
        #unpack the variables of each sentence
        assign_user, task_title, task_description, start_date, end_date, task_status= line.split(", ")
        #if the user name is the same as the assigned user name then proceed
        if username == assign_user:
            #count the number of tasks assined to the user
            task_number+=1
            #assigne the line number to a new varible
            c_line_number=line_number
            #store the variable in a dictionary
            u.update( {task_number : c_line_number} )
            #print the information
            print(f"""
        Task Number      :  {task_number}          
        Assign User      :  {assign_user}
        Task Title       :  {task_title}
        Task Description :  {task_description}
        Start Date       :  {start_date}
        End Date         :  {end_date}
        Task completed   :  {task_status}
              """) 
    #close te tasks file   
    tasks.close()
    
    #open the tasks file in read mode 
    tasks= open('tasks.txt','r')
    #ask the user to return to the main menu or to make changes to a task
    choice=int(input("""
        Enter the task number to edit that task or change its status
        Enter -1 to return to the main menu:                       
        """))
   
    #return to the main menu
    if choice == -1:  
        return -1
    # select the chosen task in the dictionary by its key
    elif choice in u.keys():
        #store which line the task is on the file
        line_in_tasks=u.get(choice)
        for line in tasks:
            #increase the value of count
            count+=1
            #find the line on the file which is to be changed
            if line_in_tasks==count:
                #unpack the the information
               assign_user, task_title, task_description, start_date, end_date, task_status= line.split(", ")
                #allow user to select what they want to edit 
               selected_choice=int(input("""
                Please chose from the following options:
                1->Edit the task
                2->Change the task status        
                             """))
        # check if the choice selected iss edit tasks and the task is not complete
        if selected_choice==1 and task_status.lower().strip("\n") != 'yes':
            #check the task status
           if task_status.lower().strip("\n") == 'no':
              #change the task status 
              task_status=input("Please enter new task status: ")
        # check if user wants to change the task and if the task is not yet complete
        elif selected_choice==2  and task_status.lower().strip("\n") != 'yes':
            #Change the user_name
            assign_user=input("Please enter the revised assigned username for the task: ")
            #change the deadline
            end_date = input("Please enter the revised due date of the task: ")
            #copy the line with the changed info to a string
            sen= (f"{assign_user}, {task_title},Use taskManager.py to {task_description}, {start_date}, {end_date}, {task_status}")
            #remove one value from the value of p so as to start the file pointer at the correct line number
            required_fline=line_in_tasks-1
            #change the contents of the list
            data[required_fline]=sen
            #close the tasks file
            tasks.close()
            
            #open the tasks file in write mode
            tasks=open('tasks.txt','w')
            #write the contents of the list to the file tasks
            for item in data:
                tasks.write("%s" % item)
                #close the file
            tasks.close()
        return 0 
    #notify the user they need to make the correct choie       
    else:
        tasks.close()
        print("Enter valid option")
        return 0
    #close task file
    tasks.close()

#view the stats for the user
def stats(username):
    #make the relevant variables
    count_user=0
    total_num_tasks=0
    count=0
    incomplete_tasks=0
    num_completed_tasks=0
    num_ncompleted_tasks=0
    task_status=" "
    incomplete_otasks=0
    overdue_tasks=0
    count_user_tasks=0
    assigned_tasks_completed=0
    assigned_tasks_ncompleted=0
    assigned_tasks_n_o_completed=0
    num_no_completed_tasks=0

    #count the number of users
    user_file=open('user.txt','r')
    for line in user_file:
        count_user+=1
        assign_user, password, = line.split(", ")
        
    #count the number of tasks
    tasks=open('tasks.txt','r')
    for line in tasks:
        total_num_tasks+=1 
        assign_user, task_title, task_description, start_date, end_date, task_status= line.split(", ")
        #count incomplete tasks
        if  task_status.lower() == "no":
            incomplete_tasks=incomplete_tasks+1
        #get the current date 
        curr_date= datetime.today()
        #get the date from the file in the correct order
        objDate = datetime.strptime(end_date, '%d %b %Y')
        #check to see if deadline is not passed
        if curr_date<objDate:
            print("still have time to complete task")
            #check to see if deadline hasnt been passed and count overdue tasks
        if  curr_date>objDate:
            print("task is overdue")
            overdue_tasks+=1
        #check to see if the tasks is over due and not complete and count these tasks
        if curr_date>objDate and task_status.lower()== "no":
            incomplete_otasks+=1
        #count number of tasks assigned to the user
        if  assign_user == username:
            count_user_tasks+=1
        #count number of complete tasks
        if  task_status.lower()== "yes":
            num_completed_tasks+=1
        #count the number of tasks completed which are assigned to them
        if  assign_user == username and task_status.lower()== "yes" :
            assigned_tasks_completed+=1
        # count number of tasks assigned to the user and are not complete 
        if  assign_user == username and task_status.lower()== "no" :
            assigned_tasks_ncompleted+=1
        # count tasks overdue and not complete
        if  curr_date>objDate and task_status.lower() == "no" :
            assigned_tasks_n_o_completed+=1  
        
    #calculate percentage of assigned user tasks
    user_assigned_task_percentage= round((100*(count_user_tasks/total_num_tasks)),2)
    #calculate the percentage of overdue tasks
    tasks_incomplete= round((100*(overdue_tasks/total_num_tasks)),2)
    #calculate the percentage of completed assigned user tasks
    user_assigned_task_completed_percentage=round((100*(assigned_tasks_completed/count_user_tasks)),2)
    #calculate the percentage of incomplete tasks assigned to the user
    user_assigned_task_ncompleted_percentage=round((100*(assigned_tasks_ncompleted/count_user_tasks)),2)
    #calculate the percentage of tasks not overdue and assigned to the user
    user_assigned_task_not_ovr_percentage=round((100*(assigned_tasks_n_o_completed/count_user_tasks)),2)
    #calculate the percentage of incomplete tasks 
    uncomplete_tasks_percentage=round((100*(incomplete_tasks/total_num_tasks)),2)
    #calculate the percentage of incomplete tasks
    overdue_tasks_percentage=round((100*(overdue_tasks/total_num_tasks)),2) 
    
    #open a new file user_over_view
    user_over_view=open('user_over_view.txt','w')
     #open a new file tasks_over_view
    tasks_over_view=open('tasks_over_view.txt','w')
    
    #write  all the variables to the user over view file
    user_over_view.write(f"""The total number of users registered are {count_user}\n
    The total number of tasks tracked are {total_num_tasks}\n
    {username} was assigned  {user_assigned_task_percentage}%  of the available tasks\n
    {username} has completed {user_assigned_task_completed_percentage}% of the tasks assigned to them\n
    {username} still has {user_assigned_task_ncompleted_percentage}% of their to tasks still to be completed\n
    {username} has {user_assigned_task_not_ovr_percentage}% of their tasks still to be completed and are overdue.\n
    """)
    
    
    #write  all the variables to the tasks over view file
    tasks_over_view.write(f"""The total number of task generated is {total_num_tasks}\n
    The total number of task completed is is {num_completed_tasks}\n
    The total number of task uncompleted and are overdue  is {incomplete_otasks}\n  
    {tasks_incomplete}% of tasks registered are not complete\n
    {overdue_tasks_percentage}% of tasks registered are overdue for completion\n 
    """)
    
    
    #print all the variables form the user over view file to the console
    print(f"""The total number of users registered are {count_user}
    The total number of tasks tracked are {total_num_tasks}
    The total number of tasks assigned to {username} is {count_user_tasks}
    {username} was assigned  {user_assigned_task_percentage}%  of the available tasks
    {username} has completed {user_assigned_task_completed_percentage}% of the tasks assigned to them
    {username} still has {user_assigned_task_ncompleted_percentage}% of their to tasks still to be completed
    {username} has {user_assigned_task_not_ovr_percentage}% of their tasks still to be completed and are overdue.\n
    """)
    
    #print all the variables form the tasks over view file to the console
    print(f"""The total number of task generated is {total_num_tasks}
    The total number of task completed is is {num_completed_tasks}
    The total number of task not completed is is {incomplete_tasks}
    The total number of task uncompleted and are overdue  is {incomplete_otasks}
    {tasks_incomplete}% of tasks registered are not complete
    {overdue_tasks_percentage}% of tasks registered are overdue for completion
    """)
   
    #close tasks_over_view file
    tasks_over_view.close()
    #close user_over_view file
    user_over_view.close()
    #close tasks file
    tasks.close()
    return 0
    

#open the user file
user_file= open('user.txt','r')
#create login boolean variable to False
log_in=False
#for loop to iterate over the lines of the user file
while log_in == False:
    #ask user for username
    username=input("Please enter your Username: ")
    password=input("Please enter your Password: ")
    
    for line in user_file:
         #declare two variables for theusername and password on each line of the file
         valid_username, valid_password=line.split(", ")
         #check to see if credentials entered are true and set login access
         if username==valid_username.strip("\n") and password==valid_password.strip("\n"):
            log_in=True         
    if log_in==False:
        print("Please enter a valid Username and Password ") 
        log_in=False   
             
    user_file.seek(0,0)
#close userfile   
user_file.close()

#decloare the count variables
menu_choice=-1 

while menu_choice == -1:
    if log_in == True:
        #ask user to select options
        user_choice=input("""
            Enter a choice from the following:

            r->  Register User
            a->  Add Task
            va-> View all Tasks
            gr-> Generate a report 
            vm-> View my Tasks
            e->  Exit            
                            """)
        

        #make input lower case
        user_input_choice = user_choice.lower()
            
        #if user wants to register someone
        if user_input_choice =="r":
            reg_user(username)
                
        elif user_input_choice =="a":
            add_task()
            
        #reading all the tasks in the file
        elif user_input_choice =="va":
            view_all_tasks()
                
        elif user_input_choice =="vm":
            menu_choice=view_my_tasks(username)
            
        elif user_input_choice == "gr":
            count_user=0
            count_tasks=0 
            stats(username)
        elif user_input_choice =="e":
            pass
        else:
            print("Please enter a valid choice")




