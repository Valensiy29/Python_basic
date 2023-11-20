class TaskManager:
    def new_task(self,name,steck):
        self.name = name
        self.steck = steck
        task = {}
        task[self.steck] = self.name

        print(task)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)