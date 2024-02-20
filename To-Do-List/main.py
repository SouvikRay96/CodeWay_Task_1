import random

from tabulate import tabulate
import databaseConnectionModule as todolist

print("=====================================================================".center(140))
print("Welcome to the To-Do-List Application".center(140))
print("=====================================================================".center(140))

use = input("Do you want to use the Application(y/Y/n/N): ".center(140))
use = use.lower()
if use == 'n' or use == 'no':
    quit()
userid = ""
flag = 0 # This Flag Variable will be used for Checking Successfull Log-In, Sign-up and Log Out Operation

# =========================================================================================================
#User Login or Registration
while(True):
    print("========================================================================".center(140))
    print("Kindly Login or Signup to proceed with the application".center(140))
    print("1) Login".center(140))
    print("2) Signup".center(140))
    print("3) Exit the Application".center(140))
    print("========================================================================".center(140))
    ch = int(input("Enter your choice : ".center(140)))
    if ch == 1:
        """
            Login Implementation
            Prompting the user for entering the credentials i.e. UserId and Password
        """
        userid = input("Enter User Id : ")
        username = input("Enter the User Name : ")
        password = input("Enter Password : ")

        # First we need to create a dictionary which will store all the account details
        accountDetails = {
            "userid":userid,
            "username":username,
            "password":password
        }

        # Now we need to call the Login function 
        status = todolist.login_Account(accountDetails)
        if status == "success":
            print("===========================================================================".center(140))
            print("Dear {} ".format(username).center(140))
            print("You are successfully Logged-In to your account".center(140))
            print("===========================================================================".center(140))
            flag = 1
            break
        elif status == "failure":
            print("===========================================================================".center(140))
            print("Dear {} ".format(username).center(140))
            print("Please Provide Valid Username and Password".center(140))
            print("===========================================================================".center(140))
        elif status == "error":
            print("===========================================================================".center(140))
            print("Dear {} ".format(username).center(140))
            print("Some Error Occured While Logging in to the Account".center(140))
            print("===========================================================================".center(140))

        
    elif ch == 2:
        """
            Signup Implementation
            Prompting the user for entering the credentials i.e. UserName and Password
            After User has provided the credentials, an unique userId will be generated randomly
        """
        # Prompting User name and Password from the User
        username = input("Enter the User Name : ".center(140))
        password = input("Enter Password : ".center(140))

        # Generating UserId for the User
        r = random.randint(0,1000)
        userid = "USER"+str(r)

        # Duplication Check for the Generated UserId
        while todolist.checkDuplicateUserID(userid):
            r = random.randint(0,1000)
            userid = "USER"+str(r)
        
        # Displaying the UserID of the User
        print("The UserID {} is Successfully Generated.".format(userid).center(140))
        print("NOTE : Please try to remember this UserID as it will be required the next time you Login".center(140))

        
        # Creating Account for the User. This step include the following
            # First we need to create a dictionary which will store all the account details
        accountDetails = {
            "userid":userid,
            "username":username,
            "password":password
        }
            # 1) Inserting the Account details in the Accounts table of the database
            # 2) Creating an User table based on the UserID generated which will store all the task of the User
        if todolist.create_Acoount(accountDetails):
            print("===========================================================================".center(140))
            print("Dear {} Your Account has been created Succesfully".format(username).center(140))
            print("You are successfully Logged-In to your account".center(140))
            print("===========================================================================".center(140))
            flag = 1
            break
        else:
            print("===========================================================================".center(140))
            print("Dear {} Some Problem has been encountered while creating you Account".format(username).center(140))
            print("Kindly Try Again".center(140))
            print("===========================================================================".center(140))
            flag = 0
            continue




    elif ch == 3:
        quit()
#============================================================================================================


print("Registration Part Completed Successfully")


"""The Below part will be in while loop"""
#Displaying the Operations

while True:
    print("===============================================================================================".center(140))
    print("To-Do-List Operations".center(140))
    print("===============================================================================================".center(140))
    print("1) Insert Task into the To-Do-List".center(140))
    print("2) Update Task in the To-Do-List i.e. Completed or not".center(140))
    print("3) Delete Task from the To-Do-List".center(140))
    print("4) View the Full Task List".center(140))
    print("0) Log-Out from the Application".center(140))
    print("===============================================================================================".center(140))
    ch = int(input("Enter which Operation do you want to perform : "))
    if ch == 1:
        """
            Inserting of Task into the To-Do-List
            At first it will Prompt the User to enter the Task Name, The Starting Time and the Ending Time of the Task
        """
        taskname = input("Enter the Task Name : ")
        startTime = input("Enter the Starting Time of the Task (Enter the Starting Time in the Format (hh:mm:ss)) : ")
        endTime = input("Enter the Ending Time of the Task (Enter the Ending Time in the Format (hh:mm:ss)) : ")

        # By Default Completed will be No
        complete = "No"
        # to get the record Number
        taskid = todolist.fetchRecordNumber(userid)
        
        recordTuple = (taskid,taskname,startTime,endTime,complete)
        status = todolist.insert_Task(userid,recordTuple)
        if status == "success":
            print("===============================================================================================".center(140))
            print("Insertion of the Task is Succesfull".center(140))
            print("===============================================================================================".center(140))
        else:
            print("===============================================================================================".center(140))
            print("Insertion of the Task is Not Done. Some error Occured".center(140))
            print("===============================================================================================".center(140))

    elif ch == 2:
        """
            Update Task in the To-Do-List
            Here Updation means that the Task is completed or not
            It will first prompt the user to enter which Task to Update
            And then it will ask the user that the Task selected is Completed or not
        """

        records = todolist.taskList(userid)
        print(tabulate(records,headers=['TASK_ID','TASK','START_TIME','END_TIME']).center(140))

        taskid = int(input("Enter the Task id of the Task You want to Update: "))
        isCompleted = input("Is the Task Completed (Yes/No)? : ")
        if isCompleted == "No":
            print("===============================================================================================".center(140))
            print("There is no need for any Updation as Completed Status is By Default No".center(140))
            print("===============================================================================================".center(140))
            continue
        taskDetails = {"taskid":taskid,"compStatus":isCompleted,"userid":userid}
        if todolist.update_Task(taskDetails):
            print("===============================================================================================".center(140))
            print("Updation of the Task is Succesfull".center(140))
            print("===============================================================================================".center(140))
        else:
            print("===============================================================================================".center(140))
            print("Updation of the Task is Not Succesfull".center(140))
            print("===============================================================================================".center(140))



    elif ch == 3:
        """
            Deletion of the specified Task by the user from the To-Do-List of the User
            First it will promt the User to enter any Task which they want to delete and then it will delete the Task from the To-Do-List
        """

        print("===============================================================================================".center(140))
        print("The Task List As Follows : ".center(140))
        records = todolist.view_Task_List(userid)
        print(tabulate(records,headers=['TASK_ID','TASK','START_TIME','END_TIME','IS_COMPLETED']).center(140))
        print("===============================================================================================".center(140))
        taskid = int(input("Enter the Task you want to delete : ".center(140)))
        if todolist.delete_Task(taskid,userid):
            print("===============================================================================================".center(140))
            print("Deletion is Suuccessfully Done".center(140))
            print("===============================================================================================".center(140))
        else:
            print("===============================================================================================".center(140))
            print("Deletion is Not Suuccessfully Done".center(140))
            print("===============================================================================================".center(140))

    elif ch == 4:
        """
            After Clicking on this Option the User can View the Full To-Do-List in a Tabular format
        """
        print("===============================================================================================".center(140))
        print("The Task List As Follows : ".center(140))
        records = todolist.view_Task_List(userid)
        print(tabulate(records,headers=['TASK_ID','TASK','START_TIME','END_TIME','IS_COMPLETED']).center(140))
        print("===============================================================================================".center(140))

    elif ch == 0:
        """
            Logging Out from the Application
            Here Logging Out means just Closing the Application and the Connection Established with the Database
            And Displaying a Suitable Message of Logging Out
        """
        quit()



#Create an Option for Log out
#After Log out the Connection will be lost with the database
