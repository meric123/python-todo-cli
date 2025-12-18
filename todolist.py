import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


def add_task(tasks):
    task_desc = input("Enter a task: ")

    priority = input("Enter priority (High / Medium / Low): ").capitalize()
    if priority not in ["High", "Medium", "Low"]:
        priority = "Medium"

    tasks.append({
        "id": len(tasks) + 1,
        "task": task_desc,
        "priority": priority,
        "done": False
    })

    save_tasks(tasks)
    print("✅ Task added successfully.")



def list_tasks(tasks):
    if not tasks:
        print("❌ No tasks found.")
        return

    priority_order = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    sorted_tasks = sorted(
        tasks,
        key=lambda task: (
            task["done"],  # False (not done) first, True (done) last
            priority_order.get(task["priority"], 99)
        )
    )

    for task in sorted_tasks:
        status = "✔" if task["done"] else "✘"
        print(f'{task["id"]}. {task["task"]} [{task["priority"]}] [{status}]')





def delete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"🗑 Task deleted: {removed['task']}")
    except (ValueError, IndexError):
        print("❌ Invalid task number.")

def change_priority(tasks):
    if not tasks:
        print("⚠ No tasks available.")
        return

    list_tasks(tasks)

    try:
        task_id = int(input("Enter task ID: "))

        for task in tasks:
            if task["id"] == task_id:
                new_priority = input("Select new priority (High / Medium / Low): ").capitalize()

                if new_priority not in ["High", "Medium", "Low"]:
                    print("❌ Invalid priority.")
                    return

                task["priority"] = new_priority
                save_tasks(tasks)
                print("✅ Priority updated.")
                return

        print("❌ Task ID not found.")

    except ValueError:
        print("❌ Please enter a valid number.")





def mark_done(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("🎉 Task marked as completed.")
    except (ValueError, IndexError):
        print("❌ Invalid task number.")


def menu():
    print("\n--- TODO LIST ---")
    print("1. List Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Change task priority")
    print("6. Exit")



def main():
    tasks = load_tasks()

    while True:
        menu()
        choice = input("Select an option: ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            change_priority(tasks)
        elif choice == "6":
            print("👋 Exiting application...")
    

            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
