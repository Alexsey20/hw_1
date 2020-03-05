#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if wall_is_above() and wall_is_on_the_left():
        while True:
            if not wall_is_on_the_right():
                move_right()
            else:
                break
            if not wall_is_beneath():
                move_down()
            else:
                break
    elif wall_is_above and wall_is_on_the_right():
        pass
    elif wall_is_beneath and wall_is_on_the_left():
        pass
    else:
        pass



if __name__ == '__main__':
    run_tasks()
