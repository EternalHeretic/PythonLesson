# Создайте новый проект или продолжите работу в текущем проекте.
# Напишите код, который форматирует строки для следующих сценариев.
# Укажите переменные, которые должны быть вставлены в каждую строку:
#
# Использование %:
#
# Переменные: количество участников первой команды (team1_num).
# Пример итоговой строки: "В команде Мастера кода участников: 5 ! "
#
# Переменные: количество участников в обеих командах (team1_num, team2_num).
# Пример итоговой строки: "Итого сегодня в командах участников: 5 и 6 !"
#
# Использование format():
# Переменные: количество задач решённых командой 2 (score_2).
# Пример итоговой строки: "Команда Волшебники данных решила задач: 42 !"
#
# Переменные: время за которое команда 2 решила задачи (team1_time).
# Пример итоговой строки: " Волшебники данных решили задачи за 18015.2 с !"
#
# Использование f-строк:
# Переменные: количество решённых задач по командам: score_1, score_2
# Пример итоговой строки: "Команды решили 40 и 42 задач.”
#
# Переменные: исход соревнования (challenge_result).
# Пример итоговой строки: "Результат битвы: победа команды Мастера кода!"
#
# Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
# Пример итоговой строки: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!."
#
# Комментарии к заданию:
# В русском языке окончания слов меняются (1 участник, 2 участника), пока что давайте не обращать на это внимания.
# Переменные challenge_result, tasks_total, time_avg можно задать вручную или рассчитать. Например, для challenge_result:
# if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
# result = ‘Победа команды Мастера кода!’
# elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
# result = ‘Победа команды Волшебники Данных!’
# else:
# result = ‘Ничья!’

team1_name = 'Мастера кода'
team1_num = 5
team1_score = 40
team1_time = 1552.512

team2_name = 'Волшебники данных'
team2_num = 6
team2_score = 42
team2_time = 2153.31451

def teams_num(name1, num1, name2, num2):
    print('В команде "%s" участников: %d !' % (name1, num1))
    print('В команде "%s" участников: %d !' % (name2, num2))
    print('Итого сегодня в командах участников: %d и %d !' % (num1, num2))

def challenge_result(name1, score1, time1, name2, score2, time2):
    print('Команда "{name}" решила задач: {score} !'.format(name=name1, score=score1))
    print('{} решили задачи за {} с !'.format(name1, time1))
    print(f'В среднем, по {time1 / score1} секунды на задачу')
    print('\nКоманда "{name}" решила задач: {score} !'.format(name=name2, score=score2))
    print('{} решили задачи за {} с !'.format(name2, time2))
    print(f'В среднем, по {time2 / score2} секунды на задачу')
    print(f'\nСегодня было решено {score1 + score2} задач, '
          f'в среднем по {(time1 + time2) / (score1 + score2)} секунды на задачу!')

    if score1 > score2 or score1 == score2 and time1 < time2:
        win = name1
    elif score1 < score2 or score1 == score2 and time1 > time2:
        win = name2
    else:
        win = 0
    print('\n\nРезультат битвы: {}'.format(f'{f'Победа команды: "{win}"' if win != 0 else 'Ничья!'}'))

teams_num(name1=team1_name, num1=team1_num, name2=team2_name, num2=team2_num)
print()
challenge_result(name1=team1_name, score1=team1_score, time1=team1_time,
                 name2=team2_name, score2=team2_score, time2=team2_time)