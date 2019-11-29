"""
核心流程(建议用协成方式完成, yield与send的方式)
1. root -> child
2. child -> 获取父结点结果 ->  自身执行 -> 保存结果 -> 通知子结点
"""


class NodeBean():
    def __init__(self):
        self.state = False

    def ready(self):
        self.state = True

    def is_ready(self):
        return self.state == True

class JobBean(NodeBean):

    def __init__(self, is_root = False):
        self.parents = []
        self.childen = []
        self.is_root = is_root
        self.exec_result = None

        if is_root:
            self.ready()


    def add_child(self, child: NodeBean):
        self.childen.append(child)

    def add_parent(self, parent: NodeBean):
        if self.is_root:
            return

        self.parents.append(parent)

    def is_parent_ready(self):
        sum = 0
        size = len(self.parents)
        for parent in self.parents:
            if parent.is_ready():
                sum += 1

        if size == sum:
            return True

        return False

    def get_parents_result(self):
        result = {}
        for parent in self.parents:
            result[parent.name] = parent.exec_result

        return result

    def set_result(self, result):
        self.exec_result = result

    def execute(self):
        pass


class Pipe:
    """管道流"""

    def add_jobs(self):

class ChildCallBack():

    def execute(self, child_job):


        if not child_job.is_parent_ready():
            AsyMsg.send(child, delay = 5ms)
            return

        kwargs = child_job.get_parents_result()

        result = child_job.execute(kwargs)
        child_job.set_result(result)
        child_job.ready()
        AsyMsg.send('notify_child_to_execute', child_job)

class NotifyChildToExecCallBack():

    def execute(self, job):
        for child in job.child:
            AsyMsg.send(child)

