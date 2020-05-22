from . import handlers


def __getattr__(name):
    return getattr(handlers, name)
