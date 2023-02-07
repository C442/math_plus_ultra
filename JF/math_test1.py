# the ultimate math game with feedback
from random import randint
import time
from gpio_lcd import GpioLcd
from machine import Pin

lcd = GpioLcd(rs_pin=Pin(16),
              enable_pin=Pin(17),
              d4_pin=Pin(18),
              d5_pin=Pin(19),
              d6_pin=Pin(20),
              d7_pin=Pin(21),
              num_lines=2, num_columns=16)


def main():
    f = open("memory.txt", "a")

    # points should be affected by correct/incorrect answer(later made by player) & time for answer(automatic)
    while True:
        numbers = remember_number(current_level.level)
        start = time.time()
        points = exercise_calculating(
            current_level.level, current_level.points, current_level.add_sub_paramters)
        time_total = round(time.time()-start, 3)
        points = check_if_remember(numbers, points)
        f.write(
            f"|level= {current_level.level} points= {points} time= {time_total}")
    f.close()


def remember_number(level):
    numbers = []
    lcd.putstr("try to remember: ")
    for i in range((level+1) % 5+1+int(level//5)):
        x = randint(1, 100)
        numbers.append(x)
    lcd.putstr(str(numbers))
    time.sleep(3)
    lcd.clear()
    return numbers


def exercise_calculating(level, points, parameters):
    num_questions = current_level.max_questions
    parameters_add_sub = current_level.add_sub_paramters
    parameters_mult_div = current_level.mult_div_parameters
    for i in range(num_questions):
        x = randint(1, 2)
        if parameters_mult_div[0] and parameters_add_sub[0]:
            pass
        elif parameters_add_sub[0]:
            if x == 1:
                points += current_level.addition_or_sub_q(
                    level, points, parameters, "addition")
            else:
                points += current_level.addition_or_sub_q(
                    level, points, parameters, "substraction")
        elif parameters_mult_div[0]:
            if x == 1:
                pass
            else:
                pass
    return points


def check_if_remember(numbers, points):
    remember = input("\n"+str(numbers))
    if remember == "yes":
        pass
    else:
        points -= 1
    return points


# independent of parameters


def getting_file_information():
    last_level_stats = {}
    f = open("memory.txt", "a")
    f = open("memory.txt", "r")
    entire_file = f.read()
    sessions = entire_file.split("|")
    last_session = sessions[len(sessions)-1]
    if not "level=" in entire_file:
        last_level_stats = {"level=": 10, "points=": 0, "time=": 0}
        return last_level_stats, sessions
    else:
        all_remaining_elements = last_session.split(" ")
        print(all_remaining_elements)
        for i in range(len(all_remaining_elements)):
            if i % 2 == 0:
                try:
                    last_level_stats[all_remaining_elements[i]
                                     ] = all_remaining_elements[i+1]
                except:
                    break
        return last_level_stats, sessions


class current_level:
    current_level_stats, sessions = getting_file_information()
    level = int(list(current_level_stats.values())[0])
    points = int(list(current_level_stats.values())[1])
    if level > 20:
        # true: yes, substraction and addition |(4,4): max length of digits and termes|False:
        add_sub_paramters = [True, (4, 4)]
        mult_div_parameters = [True, (2, 4)]
        max_questions = 20
    elif level > 15:
        add_sub_paramters = [True, (4, 4)]
        mult_div_parameters = [True, (2, 4)]
        max_questions = 15
    elif level > 10:
        add_sub_paramters = [True, (4, 4)]
        mult_div_parameters = [True, (2, 4)]
        max_questions = 10
    elif level > 5:
        add_sub_paramters = [True, (4, 4)]
        mult_div_parameters = [False, (2, 4)]
        max_questions = 5
    elif level <= 5:
        add_sub_paramters = [True, (2, 3)]
        mult_div_parameters = [False, (False, False)]
        max_questions = 5

    def addition_or_sub_q(self, points, add_sub_parameters, kind):
        if kind == "addition":
            sign = "+"
        else:
            sign = "-"

        # max number possible should change with level
        list_of_termes = []
        number_length_digit = 10
        solved = 0
        question = ""
        length_of_digits, number_of_terms = add_sub_parameters[1]
        # getting transformation of paramters
        x = randint(1, length_of_digits)
        if x != 1:
            for i in range(x):
                if i == 0:
                    pass
                else:
                    number_length_digit *= 10
        for i in range(randint(2, number_of_terms)):
            chosen_number = randint(3, number_length_digit)
            if chosen_number in list_of_termes:
                chosen_number += randint(2, (number_length_digit-1)//2)
            list_of_termes.append(chosen_number)
        max_termes = len(list_of_termes)
        for element in list_of_termes:
            if kind == "addition":
                solved += int(element)
            else:
                solved -= int(element)
            if element == list_of_termes[0]:
                question += f"{element} "

            elif element == list_of_termes[max_termes-1]:
                question += f"{sign} {element} ="

            else:
                question += f"{sign} {element} "

        lcd.putstr(question)
        time.sleep(3)        
        lcd.putstr(str(solved))
        lcd.clear()

        return points


main()
