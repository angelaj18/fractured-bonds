##task manager file yayyyy

init python:
    # Ensure persistent variables exist and are lists
    if not hasattr(persistent, "task_list") or persistent.task_list is None:
        persistent.task_list = []
    
    if not hasattr(persistent, "task_completed") or persistent.task_completed is None:
        persistent.task_completed = []
    

    class TaskManager:
        def __init__(self):
            self.task_list = persistent.task_list  # Load tasks from persistent storage
            self.task_completed = persistent.task_completed  
            self.help_count = persistent.help_count  

        def add_task(self, newtask):
            """Adds a new task if it's not already in the list."""
            if self.task_list is None:
                self.task_list = []
                persistent.task_list = self.task_list  

            if newtask not in self.task_list:
                self.task_list.append(newtask)
                persistent.task_list = self.task_list  # Save to persistent storage

        def mark_task_completed(self, task_name, helper=None):
            """Marks a task as completed and updates the help count based on who helped."""
            if self.task_list is None:
                self.task_list = []
                persistent.task_list = self.task_list  

            if self.task_completed is None:
                self.task_completed = []
                persistent.task_completed = self.task_completed  

            if task_name in self.task_list:
                self.task_list.remove(task_name)
                self.task_completed.append(task_name)

                # Update persistent storage
                persistent.task_list = self.task_list
                persistent.task_completed = self.task_completed


        def get_tasks(self):
            """Returns the list of current tasks."""
            return self.task_list

        def get_completed_tasks(self):
            """Returns the list of completed tasks."""
            return self.task_completed


    # Create an instance of TaskManager
    task_manager = TaskManager()
