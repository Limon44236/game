from random import randint
from random import uniform
from time import sleep

player = {
    'name': '', # имя
    'armor': 0.95, # броня 
    'hp': 100, # здоровье
    'attack': 5, # атака
    'luck': 10, # удача
    # 'money': 10000, # монеты
    # 'inventory': [] # инвертарь 
}

# список врагов
enemies = [
    {
        'name': 'Волк', 
        'hp': 10,
        'attack': 10,
        'script': 'Зачем ты здесь? Ты не сможешь меня победить. Принцесса больше не твоя, а чья - не твоя забота. Уходи, пока можешь.',
        'win': 'Ты - достойный противник, но до принцессы тебе всё равно никогда не добраться.',
        'loss': 'Ха! Я же говорил - тебе меня не одолеть. Уходи и не возвращайся.'
    },
    {
        'name': 'Змей Горыныч',
        'hp': 20,
        'attack': 25,
        'script': 'Не ожидал меня встретить? Я, если честно, тоже не думал, что здесь окажусь. После богатырей остаётся только фрилансить, в этот раз сказали защищать долину на пути к замку. В любом случае, ААААААрхрхрархгрх!! Ты не пройдёшь!',
        'win': 'На самом деле, я даже рад, что ты меня победил. Мой босс - дуралей, принцессу не заслужил. Иди дальше. Не зубадь там замолвить за меня словечко. Скажи, что я сражался как лев. Нет.. Как дракон!!',
        'loss': 'Могли бы просто побеседовать. Ты же и сам знал, что у тебя не получится меня убить.. Возвращайся как-нибудь, здесь довольно одиноко.'
    },
    {
        'name': 'Доминик Торетто',
        'hp': 200,
        'attack': 50,
        'script': 'Как ты смог добраться до сюда?! Как ты вообще посмел думать, что можешь со мной сражаться? Ты слаб! Принцесса будет моей, а ты уйдёшь ни с чем. Да будет битва! Самое важное - семья.',
        'win': 'Ты меня убил, но я точно появлюсь в следующей части',
        'loss': 'Прощай..'
    }
]

# записывает игрока
name = input('Введи своё имя, путник: ')
player['name'] = name

# рандомно выбираем врага
current_enemy = randint(0, 2)

# рандомное число 1 или 2
round = randint(1, 2)

# записали врага в enemy
enemy = enemies[current_enemy]

# записываем хп врага в перменную enemy_hp 
enemy_hp = enemies[current_enemy]['hp']

print(f'Противник - {enemy["name"]}: {enemy["script"]}')
input('Enter чтобы продолжить')
print()


while True:
    action = int(input(f'Выберите действие: \n1. Бой \n2. Тренировка'))
    print()
    if action == 1:
        # пока хп есть и у игрока и у врага
        while player['hp'] > 0 and enemy_hp > 0:
            # если не четное аттакует игрок
            if round % 2 == 1:
                print(f'{player["name"]} атакует {enemy["name"]}.')
                # у врага отнимается жизнь, равная аттаке игрока
                rand_luck = randint(5, 20)
                if player['luck'] == rand_luck:
                    print(f'Вам повезло! Ваша аттака увеличена на 3 и составляет:{player["attack"]*3}')
                    enemy_hp -= player['attack'] * 3
                else:
                    enemy_hp -= player['attack']
                sleep(1)
                # пишем сколько хп у игрока и врага
                print(f'''{player['name']} - {player['hp']}
        {enemy['name']} - {enemy_hp}''')
                print()
                sleep(1)
            # если не четное аттакует враг
            else:
                # аттакует враг
                print(f'{enemy["name"]} атакует {player["name"]}.')
                # у игрока отнимается жизнь, равная аттаке врага
                player['hp'] -= enemy['attack'] * player['armor'] # поглатили 5% урона с броней
                sleep(1)
                # пишем сколько хп у игрока и врага
                print(f'''{player['name']} - {player['hp']}
        {enemy['name']} - {enemy_hp}''')
                print()
                sleep(1)
            round += 1

        # пишем кто победил
        if player['hp'] > 0:
            print(f'Противник - {enemy["name"]}: {enemy["win"]}')
        else:
            print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
    elif action == 2:
        choise = int(input(f'Что будем тренировать? \n1. Броня \n2. Аттаку'))
        print()
        for i in range(0, 101, 20):
            print(f'Тренировака завершена на {i}%')
            sleep(1)
        if choise == 1:
            new_ar = uniform(0, 0.3)
            player['armor'] -= new_ar
            print(f'Ваша броня после тренировки: {100 - player["armor"] * 100}')
        elif choise == 2:
            new_at = randint(1, 5)
            player['attack'] += new_at
            print(f'Ваша аттака после тренировки: {player["attack"]}')
        


