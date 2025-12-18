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
    task = input("Enter a task: ")

    priority = input("Enter priority (High / Medium / Low): ").capitalize()
    if priority not in ["High", "Medium", "Low"]:
        priority = "Medium"

    tasks.append({
        "task": task,
        "done": False,
        "priority": priority
    })

    save_tasks(tasks)
    print("✅ Task added successfully.")



def list_tasks(tasks):
    if not tasks:
        print("📭 No tasks found.")
        return

    priority_order = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    sorted_tasks = sorted(
        tasks,
        key=lambda task: priority_order.get(task.get("priority", "Medium"), 2)
    )

    for i, task in enumerate(sorted_tasks, start=1):
        status = "✔" if task["done"] else "✘"
        priority = task.get("priority", "Medium")
        print(f"{i}. {task['task']} [{priority}] [{status}]")




def delete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"🗑 Task deleted: {removed['task']}")
    except (ValueError, IndexError):
        print("❌ Invalid task number.")


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
    print("5. Exit")


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
            print("👋 Exiting application...")
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
