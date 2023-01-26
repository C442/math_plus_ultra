# the ultimate math game with feedback
from random import randint
import time


# idea of a class is there, it must be made, since it is the only way to make it good
def main():
    parameters = 3
    current_level_stats = getting_file_information()
    f = open("memory.txt", "a")
    # parameters which should be interchangable
    level, points = 3, 10
    # points should be affected by correct/incorrect answer(later made by player) & time for answer(automatic)
    print("are you ready?")
    while True:
        numbers = remember_number(level)
        start = time.time()
        points = exercise_calculating(level, points)
        time_total = round(time.time()-start, 3)
        points = check_if_remember(numbers, points)
        f.write(
            f"Points= {points} time= {time_total} level= {level}|")
        break
    f.close()


def setting_up_parameters(last_played_game_stats):
    level = last_played_game_stats["level="]
    memory, addition, substraction, multiplication, division = 1, 1, 1, 1, 1
    return level, memory, addition, substraction, multiplication, division


class level:
    def choosing_difficulty(self, level):
        pass


def take_input():
    button_pressed = input("Press button")


def remember_number(level):
    numbers = []

    print("try to remember: ")
    for i in range(level):
        x = randint(1, 20)
        numbers.append(x)
        print(f"{x}")
    return numbers


def exercise_calculating(level, points):
    for i in range(level):
        points = addition_q(level, points)
    return points


def check_if_remember(numbers, points):
    remember = input(numbers)
    if remember == "yes":
        pass
    else:
        points -= 1
    return points


def addition_q(level, points):
    # max number possible should change with level
    a, b = randint(1, 10), randint(1, 10)
    answer = int(input(f"{a}+{b}"))
    if answer == a + b:
        pass
    else:
        points -= 1
    return points

# independent of parameters


def getting_file_information():
    last_level_stats = {}
    f = open("memory.txt", "r")
    entire_file = f.read()
    sessions = entire_file.split("|")
    last_session = sessions[len(sessions)-1]
    if last_session == "":
        last_level_stats = {"Points": 10, "time": 0, "level": 1}
    else:
        all_remaining_elements = last_session.split(" ")
        for i in range(len(all_remaining_elements)):
            if i % 2 == 0:
                try:
                    last_level_stats[all_remaining_elements[i]
                                     ] = all_remaining_elements[i+1]
                except:
                    break
        f.close()
        return last_level_stats, sessions


main()
