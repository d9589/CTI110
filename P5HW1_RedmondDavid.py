# David Redmond
# 14 July 2025
# P5 LAB1
# Purpose: To create a game with the current lessons learned.

import time
from p5hw1_utils import is_time_left, create_lock_code, create_player_lock


def main():
    print("welcome To The Escape Room.")
    print(
        "🔐 Unlock the 4 digit pin to escape before the cops blame you for the heist! 💰"
    )
    print("🕐 Hurry Up! Time Starts Now! 🕐")

    end_time = time.time() + 300

    lock_dict = create_lock_code()
    player_lock = create_player_lock()

    solved_numbers = 0

    while solved_numbers < 4:
        time_left = is_time_left(end_time)
        if not time_left:
            break
        try:
            player_number = int(input("Which number would you like to guess?: "))
        except Exception:
            print("You did not enter an integer.")
            continue
        if player_number < 0 or player_number > 9:
            print("Number not in range of 0 through 9. Try again!")
            continue
        for k, v in lock_dict.items():
            if player_number == v:
                player_lock[k] = v
                lock_dict.pop(k)
                print("You guessed a number right!")
                print(f"Your progress is now: {player_lock}")
                solved_numbers += 1
                break
            else:
                print("Incorrect guess! Try again!")
                break

    if not time_left:
        print("You have run out of time. Try again next time!")
    else:
        print("Congratulations! You escaped and won't be blamed for the heist!!")


if __name__ == "__main__":
    main()
