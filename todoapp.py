import json
def main():
    while True:
        print('TODO app')
        print('1.) Display Todo Lists')
        print('2.) Insert Todo Task')
        print('3.) Mark Todo as completed')
        print('4.) Remove Todo Task')
        print('5.) Exit')
        
        choice = input("Choose any option ")
        
        if choice == "1":
            display_in_detail()
        elif choice == "2":
            task = input('Enter the TODO task: ')
            add_todo(task)
            print('Added Successfully')
        elif choice == "3":
            task = input('Enter the TODO no. to mark as checked: ')
            mark_as_complete(task)
        elif choice == "4":
            task = input('Enter id of task to remove: ')
            remove_todo(task)
        elif choice == "5":
            print('Ending Task App. Bye see you soon')
            

def display_in_detail():
    listvalue = get_all_todoList()
    print('\n================================')
    print('Your TODO list')
    print('================================\n')
    for value in listvalue:
        print(f"{value['id']}.) {value['title']} : {value['checked']}")
    print('\n================================\n')

def get_all_todoList():
    with open('todo.json','r') as file:
        data = json.load(file)
        return data

def add_todo(value):
    data = []
    with open('todo.json', 'r') as file:
        data = json.load(file)

    index = len(data) + 1        
    data.append({"title":value,"checked":False,"id":index})
    with open('todo.json', 'w') as file:
        json.dump(data, file,indent=4)
        
def mark_as_complete(id):
    list_of_tasks = get_all_todoList()
    new_data = []
    for task in list_of_tasks:
        if task['id'] == int(id):
            task['checked'] = True
        new_data.append(task)
        print(new_data)
    with open('todo.json', 'w') as file:
        json.dump(new_data, file,indent=4)
    
    
def remove_todo(id):
    list_of_tasks = get_all_todoList()
    new_data = [list for list in list_of_tasks if list['id'] != int(id)]
    with open('todo.json', 'w') as file:
        json.dump(new_data, file,indent=4)
    
        
if __name__ == "__main__":
    main()