from time import time
from src.services.logger import Log
from src.settings import PROJECT


def end_time_ms(start_time):
    return (time() - start_time) * 1000


async def exec_task(task_function, params=None):
    start_time = time()
    code = f'{PROJECT}_{task_function.__name__.upper()}'
    module = task_function.__module__

    try:
        return await task_function() if params is None else await task_function(params)
    except BaseException as error:  # pylint: disable=broad-except
        Log().error(f'{code}_ERROR', f'Error in module {module}', error)

        return None
    finally:
        Log().info(f'{code}_FINISH', f'Finished {module} execution. Elapsed time: {end_time_ms(start_time)}ms')
