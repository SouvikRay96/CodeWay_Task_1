"""
    This Module will only interact with the Database MySQL
    This Module will be acting as a Communication channel between the user interface and database
"""

import mysql.connector as sqltor

mydb = sqltor.connect(host = "localhost",
                      user = "root",
                      password = "tojosoumili12",
                      database = "todolist",
                      auth_plugin = "mysql_native_password"
                    )#establishing connection

mycur = mydb.cursor()#Creating cursor instance

# Checking the Connection with the database is established or not
# if mydb.is_connected():
#     print("Connection Established")
# else:
#     print("Connection Not Established")

# Method for checking Duplicate UserId in the database
def checkDuplicateUserID(userid):
    """
        This method will first fetch all the userId from the table called accounts
        And from there it will check if the generated UserId is present or not
    """
    mycur.execute("SELECT USER_ID FROM ACCOUNTS")
    userids = mycur.fetchall()
    # userids = [(101),(102),.....]
    if (userid,) not in userids:
        return False
    else:
        return True
    
def fetchRecordNumber(userid):
    mycur.execute("SELECT TASK_ID FROM {}".format(userid))
    records = mycur.fetchall()
    #print(records)
    l = len(records)
    if l == 0:
        return 1
    else:
        return l+1




# Function for Creating User Account i.e. Creating a Seperate database and a table within it 
# The Table will contain all the task inserted/modified in the To-Do-List
def create_Acoount(accountDetails):
    """
        This Method will create a Database for the User based on the Account ID of the User
        Along with that will create a table in the User Database Created.
        The table will contain all the Task which will be inserted in the To-Do-List
        The Parameter accountDetails is a dictionary whcih will contain all the Account details
        including UserID,UserName, Password for the user.
    """
    records = (accountDetails["userid"],accountDetails["username"],accountDetails["password"])
    try:
        stringQuery = "INSERT INTO ACCOUNTS VALUES{records}".format(records=records)
        mycur.execute(stringQuery)
        mydb.commit()

        table_parameters = "TASK_ID INT PRIMARY KEY,TASK VARCHAR(30),START_TIME TIME,END_TIME TIME,IS_COMPLETED CHAR(5)"
        
        stringQuery = "CREATE TABLE {table_name}({table_parameters})".format(table_name=accountDetails["userid"],table_parameters=table_parameters)
        mycur.execute(stringQuery)
        mydb.commit()
        return True
    except:
        return False
    
def login_Account(accountDetails):
    """
        This method will be used for Login into the User Account
    """
    userid = accountDetails["userid"]
    try:
        stringQuery = "SELECT * FROM ACCOUNTS WHERE USER_ID='{}'".format(userid) # Creation of String Query
        mycur.execute(stringQuery) # Execution of the String Query in MySQL
        record = mycur.fetchall()[0] 
        # [("123","Samayita","paswd")]
        username = record[1]
        password = record[2]
        if username == accountDetails["username"] and password == accountDetails["password"]:
            return "success"
        else:
            return "failure"
    except:
        return "error"

def delete_Account(accountId):
    """
        This Method will delete/Drop the User database 
        i.e. delete the User Account Credentials along with the User Database
    """
    pass

def insert_Task(accountId,taskDetails):
    """
        This Method will insert a Task entered by the user 
        And store it in the User's Database created based on the AccountId
    """
    try:
        stringQuery = "INSERT INTO {tablename} VALUES{taskdetails}".format(tablename=accountId,taskdetails=taskDetails)
        mycur.execute(stringQuery)
        mydb.commit()
        return "success"
    except:
        return "failure"
    


def update_Task(taskDetails):
    """
        This method will update the Task in the Task List of the User 
        such as the Starting Time of the Task, Ending Time of the Task, Duration of the Task or 
        Description of the Task to be Done and many more
    """
    query = "UPDATE {tablename} SET IS_COMPLETED='{value}' WHERE TASK_ID={taskid}".format(
        tablename=taskDetails["userid"],
        value=taskDetails["compStatus"],
        taskid=taskDetails["taskid"]
    )
    try:
        mycur.execute(query)
        mydb.commit()
        return True
    except:
        return False

def delete_Task(taskid,accountId):
    """
        This Method will be deleting the task based on the TaskId from the Task List of the User
    """
    try:
        mycur.execute("delete from {tablename} where TASK_ID={taskid}".format(tablename=accountId,taskid=taskid))
        mydb.commit()
        return True
    except:
        return False
    pass

def view_Task_List(accountId):
    """
        This Method will display the full Task List of the User that the User needs to follow
        with Credentials of Starting Time,Ending Time, Duration of the Task, Description of the Task
        along with Task is Completed or not
    """
    mycur.execute("select * from {}".format(accountId))
    record = mycur.fetchall()
    return record
    

def taskList(accountid):
    mycur.execute("select TASK_ID,TASK,START_TIME,END_TIME from {}".format(accountid))
    record = mycur.fetchall()
    return record