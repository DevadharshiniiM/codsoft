task_list=[]

def add_task():
    enter_task=input("Enter task:")
    task_list.append(enter_task)

def remove_task():
    rem_task=input("Enter task to remove:")
    if rem_task in task_list:               
        task_list.remove(rem_task)
    else:
        print("task doesn't exist")

def view_task():
     print(task_list)

     
while True:
    print("main menu")
    print("1.add task")
    print("2.remove  task")
    print("3.view task")
    print("4.exit")
    ch=int(input("enter  your choice :"))
    if ch==1:
        add_task()
    elif ch==2:
        remove_task()
    elif ch==3:
        view_task()
    elif ch==4:
        break
    else:
        print("invalid choice ,try again!")
