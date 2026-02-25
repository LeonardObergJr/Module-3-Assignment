# Task class to represent a task with title, description, difficulty, and status
class Task:

    #constructor to initialize task
    def __init__(self, title=None, description=None, difficulty=None, status=None):
        self.title = title
        self.description = description
        self.difficulty = difficulty
        self.status = status

    #method to edit the task details
    def editTask(self, newTitle, newDescription, newDifficulty):

        if (newTitle == None or newDifficulty < 0): 
            print("Invalid input")

        else:
            self.title = newTitle
            self.description = newDescription
            self.difficulty = newDifficulty
            print("Task updated successfully")

    #method to mark the task as complete
    def markComplete(self):

        self.status = "Complete"
        print("Task marked as complete")

# Mood class to represent a person's mood
class Mood:

    #constructor to initialize mood
    def __init__(self, currentMood=None):
        self.currentMood = currentMood

    #method to set the current mood
    def setMood(self, newMood):

        if (newMood == None): 
            print("Invalid input")
            return

        if (newMood not in ["Happy", "Sad", "Neutral"]):
            print("Invalid mood")
            return

        else:
            self.currentMood = newMood
            print("Mood updated successfully")

    #method to get recommended tasks based on the current mood
    def getRecommendedTasks(self, TaskList):

        recommendedTasks = []

        for task in TaskList:
            if (task.difficulty == 3 and self.currentMood == "Happy"):
                recommendedTasks.append(task)
                
            elif (task.difficulty == 1 and self.currentMood == "Sad"):
                recommendedTasks.append(task)

            elif (task.difficulty == 2 and self.currentMood == "Neutral"):
                recommendedTasks.append(task)
        
        return recommendedTasks

class TaskManager:

    #constructor to initialize task manager
    def __init__(self):
        self.TaskList = []

    #method to add a task to the task list
    def addTask(self, newTask):

        if (newTask == None): 
            print("Invalid input")
            return

        else:
            self.TaskList.append(newTask)
            print("Task added successfully")

    #method to remove a task from the task list
    def removeTask(self, taskToRemove):

        if (taskToRemove == None): 
            print("Invalid input")
            return

        elif (taskToRemove not in self.TaskList):
            print("Task not found")
            return

        else:
            self.TaskList.remove(taskToRemove)
            print("Task removed successfully")


# Test class for non-interactive demo
class Test:

    @staticmethod
    def run():
        print("===== TASK MANAGEMENT SYSTEM (DEMO) =====\n")

        # Create task manager and mood tracker
        manager = TaskManager()
        mood = Mood()

        # Create tasks with different attributes
        print("--- Creating Tasks ---")
        task1 = Task("Study Math", "Complete chapter 5 exercises", 3, "Incomplete")
        task2 = Task("Write Essay", "Write 500 word essay on history", 2, "Incomplete")
        task3 = Task("Read Article", "Read news article about technology", 1, "Incomplete")

        # Add tasks to manager
        print("\n--- Adding Tasks to Manager ---")
        manager.addTask(task1)
        manager.addTask(task2)
        manager.addTask(task3)

        # Display all tasks and their attributes
        print("\n--- Current Tasks in List ---")
        for i, task in enumerate(manager.TaskList, 1):
            print(f"Task {i}: Title='{task.title}', Description='{task.description}', Difficulty={task.difficulty}, Status='{task.status}'")

        # Edit a task
        print("\n--- Editing Task 1 ---")
        task1.editTask("Study Advanced Math", "Complete chapter 5-6 exercises", 3)

        # Mark task as complete
        print("\n--- Marking Task 2 as Complete ---")
        task2.markComplete()

        # Display updated tasks
        print("\n--- Updated Tasks in List ---")
        for i, task in enumerate(manager.TaskList, 1):
            print(f"Task {i}: Title='{task.title}', Description='{task.description}', Difficulty={task.difficulty}, Status='{task.status}'")

        # Test Mood functionality
        print("\n--- Testing Mood System ---")
        mood.setMood("Happy")
        print(f"Current mood set to: {mood.currentMood}")

        print("\n--- Recommended Tasks for Happy Mood (Difficulty 3) ---")
        recommended = mood.getRecommendedTasks(manager.TaskList)
        if recommended:
            for task in recommended:
                print(f"  - {task.title} (Difficulty: {task.difficulty})")
        else:
            print("  No recommended tasks")

        # Test removing a task
        print("\n--- Removing Task 3 from List ---")
        manager.removeTask(task3)

        # Final task list
        print("\n--- Final Task List ---")
        for i, task in enumerate(manager.TaskList, 1):
            print(f"Task {i}: Title='{task.title}', Description='{task.description}', Difficulty={task.difficulty}, Status='{task.status}'")

        print("\n===== END OF DEMO =====")


# Main class now provides a simple interactive menu and delegates the demo to Test
class Main:

    # method to run the interactive menu for task management
    @staticmethod
    def run():
        print("===== TASK MANAGEMENT SYSTEM (INTERACTIVE) =====\n")

        # Create a TaskManager and Mood tracker used by the interactive session
        manager = TaskManager()
        mood = Mood()

        # Main interactive loop: present options and handle user commands
        while True:
            print("Options:\n  1) Run demo (non-interactive)\n  2) Add task\n  3) List tasks\n  4) Edit task\n  5) Mark task complete\n  6) Remove task\n  7) Set mood\n  8) Show recommended tasks\n  9) Exit")
            choice = input("Enter choice (1-9): ").strip()

            # Run the demo version of the workflow
            if choice == '1':
                Test.run()

            # Add a new task: collect title, description, difficulty and append
            elif choice == '2':
                title = input("Title: ").strip()
                description = input("Description: ").strip()
                try:
                    difficulty = int(input("Difficulty (1-3): ").strip())
                except Exception:
                    print("Invalid difficulty — must be an integer")
                    continue
                if difficulty < 1 or difficulty > 5:
                    print("Difficulty should be a positive integer (recommended 1-3)")
                    continue
                new_task = Task(title, description, difficulty, "Incomplete")
                manager.addTask(new_task)

            # List current tasks with basic details
            elif choice == '3':
                if not manager.TaskList:
                    print("No tasks in the list")
                else:
                    for i, task in enumerate(manager.TaskList, 1):
                        print(f"{i}) Title='{task.title}', Description='{task.description}', Difficulty={task.difficulty}, Status='{task.status}'")

            # Edit an existing task by selecting its index then updating fields
            elif choice == '4':
                if not manager.TaskList:
                    print("No tasks to edit")
                    continue
                for i, task in enumerate(manager.TaskList, 1):
                    print(f"{i}) {task.title} (Difficulty {task.difficulty})")
                try:
                    idx = int(input("Enter task number to edit: ").strip()) - 1
                except Exception:
                    print("Invalid number")
                    continue
                if idx < 0 or idx >= len(manager.TaskList):
                    print("Task number out of range")
                    continue
                new_title = input("New title: ").strip()
                new_desc = input("New description: ").strip()
                try:
                    new_diff = int(input("New difficulty (1-3): ").strip())
                except Exception:
                    print("Invalid difficulty")
                    continue
                manager.TaskList[idx].editTask(new_title, new_desc, new_diff)

            # Mark a task as complete by index
            elif choice == '5':
                if not manager.TaskList:
                    print("No tasks to mark complete")
                    continue
                for i, task in enumerate(manager.TaskList, 1):
                    print(f"{i}) {task.title} - {task.status}")
                try:
                    idx = int(input("Enter task number to mark complete: ").strip()) - 1
                except Exception:
                    print("Invalid number")
                    continue
                if idx < 0 or idx >= len(manager.TaskList):
                    print("Task number out of range")
                    continue
                manager.TaskList[idx].markComplete()

            # Remove a task by index
            elif choice == '6':
                if not manager.TaskList:
                    print("No tasks to remove")
                    continue
                for i, task in enumerate(manager.TaskList, 1):
                    print(f"{i}) {task.title}")
                try:
                    idx = int(input("Enter task number to remove: ").strip()) - 1
                except Exception:
                    print("Invalid number")
                    continue
                if idx < 0 or idx >= len(manager.TaskList):
                    print("Task number out of range")
                    continue
                manager.removeTask(manager.TaskList[idx])

            # Set current mood for recommendations
            elif choice == '7':
                new_mood = input("Set mood (Happy/Sad/Neutral): ").strip()
                mood.setMood(new_mood)

            # Show recommended tasks based on current mood
            elif choice == '8':
                recommended = mood.getRecommendedTasks(manager.TaskList)
                if recommended:
                    print("Recommended tasks:")
                    for task in recommended:
                        print(f"  - {task.title} (Difficulty: {task.difficulty})")
                else:
                    print("No recommended tasks for current mood or no tasks available")

            # Exit the interactive loop
            elif choice == '9' or choice.lower() in ('q', 'quit', 'exit'):
                print("Exiting. Goodbye!")
                break

            else:
                print("Invalid choice — please enter a number from the menu")


if __name__ == "__main__":
    Main.run()