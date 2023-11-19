
def singleton(_class):
    def _init(*args, **kwargs):
        if not hasattr(_class, 'instance'):
            setattr(_class, 'instance', _class(*args, **kwargs))
        return getattr(_class, 'instance')
    return _init
