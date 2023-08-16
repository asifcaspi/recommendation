import schedule
from functools import wraps
from croniter import croniter

def scheduled_task(cron_expression):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            iter = croniter(cron_expression)
            next_run = iter.get_next()
            schedule.every().second.do(func, *args, **kwargs).tag(next_run)
        return wrapper
    return decorator
