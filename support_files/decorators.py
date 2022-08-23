# This is a list of decorators being used in the project

def catchErrors(errors=(Exception,), default_value=''):
    def decorator(func):
        def new_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except errors as e:
                print('Got error! ', repr(e))
                return default_value
        return new_func
    return decorator
