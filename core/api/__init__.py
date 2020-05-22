from . import handlers


class Project:
    """
        Project handler class
        create, update
    """

    def create(self, project):
        pass

    def update(self, project):
        pass


class Task:
    """
        Task handler class
        create, update
    """

    def create(self, task):
        pass

    def update(self, task):
        pass


class User:
    """
        User handler class
        create, update
    """

    def create(self, task):
        pass

    def update(self, task):
        pass


def __getattr__(name):
    return getattr(handlers, name)
