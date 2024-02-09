from collections import deque


class Task(object):
    def __init__(self, task_desc, has_priority=False):
        self.taskDesc = task_desc
        self.hasPriority = has_priority

    def __str__(self):
        return "Task: {0}, Priority: {1}".format(self.taskDesc, self.hasPriority)


task_queue = deque()


def add_task(task):
    if task.hasPriority:
        task_queue.appendleft(task)
    else:
        task_queue.append(task)


def do_task():
    return task_queue.popleft()


def print_tasks():
    for t in task_queue:
        print(str(t))


def main():
    add_task(Task("Make List"))
    add_task(Task("Make BreakFast"))
    add_task(Task("Respond to Email", True))
    print_tasks()
    print("*******************")
    print(do_task())
    print("*******************")
    print_tasks()
    print("*******************")
    print(do_task())
    print("*******************")
    print_tasks()

    # add code here
    return


if __name__ == "__main__":
    main()
