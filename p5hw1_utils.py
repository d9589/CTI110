import time
import random


def is_time_left(end_time):
    current_time = time.time()
    if current_time >= end_time:
        return False
    return True


def create_lock_code():
    lock_dict = {}
    low_number = 0
    high_number = 9
    number_list = random.sample(range(low_number, high_number + 1), 4)
    for i in range(0, 4):
        lock_dict[f"pos_{i}"] = number_list.pop(0)
    return lock_dict


def create_player_lock():
    player_dict = {}
    for i in range(0, 4):
        player_dict[f"pos_{i}"] = None
    return player_dict
