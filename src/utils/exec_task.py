from time import time
from src.services.logger import Log
from src.settings import PROJECT


async def exec_task(task_function, params=None):
    start_time = time()
    try:
        exec_result = await task_function() if params is None else await task_function(params)

        Log().info(f'{PROJECT}_{task_function.__name__.upper()}_FINISH', f'Finished {task_function.__module__} table generation. Elapsed time: {time() - start_time}')

        return exec_result
    except BaseException as error:  # pylint: disable=broad-except
        Log().error(f'{PROJECT}_{task_function.__name__.upper()}_ERROR', f'Error on generate {task_function.__module__}', error)

        return None
