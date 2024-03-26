def display_menu():
    print("Todo List Menu:")
    print("1. View Todo List")
    print("2. Add Item to Todo List")
    print("3. Mark Item as Done")
    print("4. Remove Item from Todo List")
    print("5. Exit")

def view_todo_list(todo_list):
    if todo_list:
        print("Todo List:")
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Todo List is empty.")

def add_item(todo_list):
    item = input("Enter the todo item: ")
    todo_list.append(item)
    print("Item added to todo list.")

def mark_item_done(todo_list):
    view_todo_list(todo_list)
    index = int(input("Enter the index of the item to mark as done: ")) - 1
    if 0 <= index < len(todo_list):
        print(f"Marking '{todo_list[index]}' as done.")
        todo_list.pop(index)
    else:
        print("Invalid index.")

def remove_item(todo_list):
    view_todo_list(todo_list)
    index = int(input("Enter the index of the item to remove: ")) - 1
    if 0 <= index < len(todo_list):
        removed_item = todo_list.pop(index)
        print(f"Removed '{removed_item}' from todo list.")
    else:
        print("Invalid index.")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_item(todo_list)
        elif choice == '3':
            mark_item_done(todo_list)
        elif choice == '4':
            remove_item(todo_list)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
