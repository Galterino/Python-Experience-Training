import random
import time
from math import ceil

def update_character_stats(actor):
    actor['cur_vit'] = actor['vit'] + actor['health_boost'] + actor['pos_vit']
    actor['cur_dex'] = actor['dex'] + actor['dex_boost'] + actor['pos_dex']
    actor['cur_force'] = actor['force'] + actor['force_boost'] + actor['pos_force']
    actor['cur_def'] = actor['protect_boost'] + actor['def'] + actor['pos_def']
    actor['current_max_health'] = (actor['max_health_start'] + (actor['cur_vit'] * 12)) + actor['permanent_bonus_hp']
    actor['force_damage_current'] = actor['force_damage_start'] + (actor['cur_force'] * 3)
    actor['miss_damage_chance'] = (actor['cur_dex']  / 100)
    actor['crit_damage_chance'] = (actor['cur_dex'] * 0.007)
    actor['damage_crit'] = actor['force_damage_current'] * 1.8
    actor['xp_required'] = int(90 * (actor['current_level'] ** 1.5) + (actor['current_level'] * 30))


def update_dungeon_eq(level_part, actor):
    reward = dungeon_rewards[level_part]
    actor['health_boost'] += reward['health_boost']
    actor['force_boost'] += reward['force_boost']
    actor['dex_boost'] += reward['dex_boost']
    actor['protect_boost'] += reward['protect_boost']



def event_choice(scene):

    sudden_event_chance = scene['probability_sudden']
    attack_event_chance = scene['probability_attack']

    event_chance = random.random()

    if event_chance <= attack_event_chance:
        return 'attack'
    elif attack_event_chance < event_chance < sudden_event_chance + attack_event_chance:
        return 'sudden'
    else:
        return 'nothing'

def check_input():

    choice_user = input('\n>>> 1, 2, 3, 4, 5, 6: ').strip()

    while choice_user not in ('1', '2', '3', '4', '5', '6'):
        print('---->[Ошибка ввода]<----')

        choice_user = input('\n>>> 1, 2, 3, 4, 5, 6: ').strip()

    return choice_user

def step_print():

    actions = ['Повернуть налево', "Повернуть направо", "Осмотреться", "Идти вперед"]
    random.shuffle(actions)
    actions.extend(['5: проверить статистику', '6: Подлечиться'])
    print()
    for action in actions:
        print(f"{action}", end=' | ')

def print_stats(actor):
    actor['current_health'] = round(actor['current_health'])
    print("\n>>>ТЕКУЩИЕ ХАРАКТЕРИСТИКИ ПЕРСОНАЖА<<<"
          "\n\t"
          f"\n>>>Имя: {actor['name']}"
          f"\n>>>Текущее/максимальное hp: {actor['current_health']}/{actor['current_max_health']}"
          f"\n>>>Урон: {actor['force_damage_start']} + {actor['force']} * 3 = {actor['force_damage_current']}"
          f"\n>>>Ловкость: {actor['cur_dex']} + ({actor['dex_boost']} от снаряжения)"
          f"\n>>>Сила: {actor['cur_force']} + ({actor['force_boost']} от снаряжения)"
          f"\n>>>Живучесть: {actor['cur_vit']} + ({actor['health_boost']} от снаряжения)"
          f"\n>>>Защита: {actor['cur_def']} + ({actor['protect_boost']} от снаряжения)"
          f"\n>>>---------------------------------------------------------------<<<"
          f"\n>>>Текущий/Максимальный уровень: {actor['current_level']}/{actor['max_level']}"
          f"\n>>>Опыта до следующего уровня: {actor["exp_current"]}/{actor['xp_required']}"
          f"\n>>>Количество монет: {actor["money"]}"
          f"\n>>>Количество бутылок со здоровьем: {actor['hp_bottles']}"
          f"\n>>>---------------------------------------------------------------<<<"
          f"\n>>>Вероятность уклонения: {actor['miss_damage_chance']:.2%}"
          f"\n>>>Вероятность нанесения крит урона: {actor['crit_damage_chance']:.2%}"
          f"\n>>>---------------------------------------------------------------<<<")

def hp_bottle_boost(actor):

    actor['current_health'] = round(actor['current_health'])
    hp_boost = 50

    if actor['hp_bottles'] > 0:

        if actor['current_health'] == actor['current_max_health']:
            print('\n>>>[Предупреждение] Вам нет необходимости восстанавливать здоровье')
        elif actor['current_health'] + hp_boost < actor['current_max_health']:
            print(f"\n>>>[Действие] Восстановлено {hp_boost} здоровья")
            actor['current_health'] += hp_boost
            actor['hp_bottles'] -= 1
        elif actor['current_health'] + hp_boost > actor['current_max_health']:
            print(f"\n>>>[Действие] Восстановлено {actor['current_max_health'] - actor['current_health']} здоровья")
            actor['current_health'] += actor['current_max_health'] - actor['current_health']
            actor['hp_bottles'] -= 1
    else:

        print('\n>>>[Предупреждение]У вас нет бутылочек здоровья!')

        print(f"\nТекущее/максимальное hp: {actor['current_health']}/{actor['current_max_health']}")

def check_lvl_up(actor):

    if actor['exp_current'] >= actor['xp_required'] and actor['current_level'] < actor['max_level']:
        actor['current_level'] += 1
        actor['exp_current'] = actor['exp_current'] - actor['xp_required']
        update_character_stats(actor)
        level_up(actor)

def level_up(actor):

    print('\n>>>>> **** ПОВЫШЕНИЕ УРОВНЯ **** <<<<<')

    print(f'>>>[Информация] В вашем распоряжении: {actor['points']} очка, распределите их по нужным характеристикам')

    time.sleep(1)

    for _ in range(actor['points']):



        print(
            '\n1. Живучесть: + 12 hp к максимальному за каждое очко'
            '\n2. Ловкость: +1% к увороту и +0.7% к шансу крита за каждое очко'
            '\n3. Защита: поглощает 1% урона за каждое очко.'
            '\n4. Сила: + 3 урона за каждое очко'
        )

        user_choice = input('\n>>> 1,2,3,4: ').lower().strip()

        while user_choice not in ('1', '2', '3', '4'):
            print("Ошибка ввода, попробуйте еще раз: ")
            user_choice = input('\n>>> 1,2,3,4: ').lower().strip()

        if user_choice == '1':
            actor['pos_vit'] += 1

        elif user_choice == '2':
            actor['pos_dex'] += 1

        elif user_choice == '3':
            actor['pos_def'] += 1

        elif user_choice == '4':
            actor['pos_force'] += 1

    actor['current_health'] = actor['current_max_health']
    update_character_stats(actor)

def is_dead(actor):
    return actor['current_health'] <= 0

def sudden_event(events, actor):

    event_cur = random.choice(events['events_tuple'])

    print(events[event_cur]['desc'])
    print(events[event_cur]['choice_desc'])

    user_choice = input('\nВы согласны? Да/Нет: ').lower().strip()

    if event_cur == 'mysterious_stranger' and user_choice == "да":

        actor['current_max_health'] += events[event_cur]['increase']
        actor['current_health'] -= events[event_cur]['reduce']

        actor['current_health'] = round(actor['current_health'])
        print(f'\n>>>[Информация] Текущее максимальное здоровье: {actor['current_max_health']}')
        print(f'>>>[Информация] Текущее здоровье: {actor['current_health']}')
        actor['permanent_bonus_hp'] += events[event_cur]['increase']

    elif event_cur == 'the_chamber_0f_secrets' and user_choice == "да":

        random_choice = round(random.random(), 2)

        print(random_choice)

        if random_choice < 0.5:

            print(f'\n>>>[Действие] Вы получили {50} монет')
            actor['money'] += events[event_cur]['increase']

        else:

            print(f'\n>>>[Действие] Вы потеряли {50} здоровья')
            actor['current_health'] -= events[event_cur]['reduce']

    elif event_cur == 'fountain_of_knowledge' and  user_choice == "да":

        actor['current_health'] = actor['current_max_health']

        print(f"\n>>>[Информация]Текущее/максимальное hp: {actor['current_health']}/{actor['current_max_health']}")

    elif event_cur == 'nothing' and  user_choice == "да":

        actor['hp_bottles'] += 1

        print("\n>>>[Действие] Вы получили 1 бутылек здоровья!")

    elif event_cur == 'trader' and  user_choice == "да":

        count_bottles = actor['money'] // events[event_cur]['cost']

        print(f'\n>>>[Информация] Вы можете приобрести: {count_bottles} бутылочек.\nВаши средства: {actor['money']}')

        if actor['money'] < events[event_cur]['cost']:

            print('>>>[Информация] К сожалению, у вас недостаточно монет')

        else:

            user_bottles = input("\nСколько желаете приобрести: ").strip()

            while True:

                if user_bottles.isdigit():
                    if int(user_bottles) <= count_bottles:
                        break

                user_bottles = input("\n>>>[Ошибка ввода] Сколько желаете приобрести: ").strip()

            actor['hp_bottles'] += int(user_bottles)

            print("\n>>>[Действие] Успешная покупка!")
            actor['money'] -= int(user_bottles) * events[event_cur]['cost']

    else:

        print("\n>>>[Информация] Вы, решившись не рисковать, прошли мимо.")


def fight_final_boss(scene, level_part, actor):
    count_act = 1
    health_enemy = scene[level_part]['enemies']['enemy_boss_health']
    current_health_enemy = health_enemy
    enemy_reward = scene[level_part]['enemies']['enemy_boss_reward']
    character_def = actor['cur_def'] / 100
    enemy_def = scene[level_part]['enemies']['protect_boss'] / 100

    while current_health_enemy > 0:

        time.sleep(1)

        print(f'\n>>>[Информация] Здоровье Босса: {current_health_enemy:.1f}/{health_enemy}')

        time.sleep(1)

        if count_act % 2 == 0:
            print('\n>>>[Информация] Ход врага: ')

            time.sleep(1)

            crit_chance = round(random.random(), 2)
            miss_chance = round(random.random(), 2)
            ability_chance = round(random.random(), 2)

            if ability_chance <= scene[level_part]['enemies']['ability_boss_chance_total']:

                print(scene[level_part]['enemies']["ability_boss_chance_total_desc"])

                actor['current_health'] -= 100000

            elif crit_chance <= scene[level_part]['enemies']['enemy_boss_crit']:
                crit_damage_decs = scene[level_part]['enemies']['enemy_boss_crit_desc']

                if miss_chance <= actor['miss_damage_chance']:
                    miss_damage_decs = random.choice(actor['miss_damage_tuple'])
                    print(actor[miss_damage_decs])
                else:
                    damage_enemy = random.randint(scene[level_part]['enemies']['enemy_boss_damage'][0],
                                                  scene[level_part]['enemies']['enemy_boss_damage'][1])
                    print(crit_damage_decs)
                    damage = round((damage_enemy * 1.5) - (damage_enemy * 1.5 * character_def), 1)
                    actor['current_health'] -= damage
                    print(f'\n>>>[Нанесено {damage} критического урона по вам]<<<')
            else:
                if miss_chance <= actor['miss_damage_chance']:
                    miss_damage_decs = random.choice(actor['miss_damage_tuple'])
                    print(actor[miss_damage_decs])
                else:
                    damage_enemy = random.randint(scene[level_part]['enemies']['enemy_boss_damage'][0],
                                                  scene[level_part]['enemies']['enemy_boss_damage'][1])
                    damage = round(damage_enemy - (damage_enemy * character_def), 1)
                    actor['current_health'] -= damage
                    print(f'\n>>>[Нанесено {damage} обычного урона по вам]<<<')

        elif count_act % 2 != 0:

            time.sleep(1)

            print('\n>>>>[Информация] Ваш ход: ')

            crit_chance = round(random.random(), 2)
            miss_chance = round(random.random(), 2)

            while True:
                actor_act = input("\n1. Атаковать | 2. Подлечиться | 3. Проверить здоровье: ")

                if actor_act in ('1', '2'):
                    break
                elif actor_act == '3':
                    actor['current_health'] = round(actor['current_health'])
                    print(f"\n>>>[Информация]Текущее/максимальное hp: {actor['current_health']}/{actor['current_max_health']}")

            if actor_act == '1':

                if crit_chance <= actor['crit_damage_chance']:
                    crit_damage_decs = random.choice(actor['crit_damage_tuple'])

                    if miss_chance <= scene[level_part]['enemies']['miss_damage_boss']:
                        miss_damage_decs = scene[level_part]['enemies']['miss_damage_boss_desc']
                        print(miss_damage_decs)
                    else:
                        print(actor[crit_damage_decs])
                        damage = round(actor['damage_crit'] - (enemy_def * actor['damage_crit']), 1)
                        current_health_enemy -= damage
                        print(f'\n>>>[Нанесено {damage} критического урона]<<<')
                else:
                    if miss_chance <= scene[level_part]['enemies']['miss_damage_boss']:
                        miss_damage_decs = scene[level_part]['enemies']['miss_damage_boss_desc']
                        print(miss_damage_decs)
                    else:
                        damage = round(actor['force_damage_current'] - (enemy_def * actor['force_damage_current']), 1)
                        current_health_enemy -= damage
                        print(f'\n>>>[Нанесено {damage} обычного урона]<<<')

            elif actor_act == '2':
                hp_bottle_boost(actor)

        if is_dead(actor):
            break

        count_act += 1

    else:
        print(f'\n>>>[Информация] Вы успешно одержали победу над {scene[level_part]['enemies']['enemy_boss_name']}')
        actor['exp_current'] += scene[level_part]['enemies']['enemy_boss_exp']
        print(f'>>>[Информация] Вы получили {scene[level_part]['enemies']['enemy_boss_exp']} опыта!')
        actor['money'] += enemy_reward
        print(f'>>>[Информация] Вы получили {enemy_reward} золота!')

        time.sleep(2)

def fight_process(pattern_enemy, actor):
    count_act = 1
    appearance_desc = random.choice(pattern_enemy['appearance_desc_tuple'])
    print()
    print(pattern_enemy[appearance_desc].format(name=pattern_enemy['name']))
    health_enemy = random.randint(pattern_enemy['health'][0], pattern_enemy['health'][1])
    current_health_enemy = health_enemy
    enemy_reward = random.randint(pattern_enemy['reward'][0], pattern_enemy['reward'][1])
    character_def = actor['def'] / 100
    enemy_def = pattern_enemy['protect'] / 100 if pattern_enemy['protect'] > 0 else 0

    while current_health_enemy > 0:

        time.sleep(1)

        print(f'\n>>>[Информация] Здоровье врага: {current_health_enemy:.1f}/{health_enemy}')

        time.sleep(1)

        if count_act % 2 == 0:
            print('\n>>>[Информация] Ход врага: ')

            time.sleep(1)

            crit_chance = round(random.random(), 2)
            miss_chance = round(random.random(), 2)

            if crit_chance <= pattern_enemy['crit']:
                crit_damage_decs = pattern_enemy['crit_desc']

                if miss_chance <= actor['miss_damage_chance']:
                    miss_damage_decs = random.choice(actor['miss_damage_tuple'])
                    print(actor[miss_damage_decs])
                else:
                    damage_enemy = random.randint(pattern_enemy['damage'][0], pattern_enemy['damage'][1])
                    print(crit_damage_decs)
                    damage = round((damage_enemy * 1.5) - (damage_enemy * 1.5 * character_def), 1)
                    actor['current_health'] -= damage
                    print(f'\n>>>[Нанесено {damage} критического урона по вам]<<<')
            else:
                if miss_chance <= actor['miss_damage_chance']:
                    miss_damage_decs = random.choice(actor['miss_damage_tuple'])
                    print(actor[miss_damage_decs])
                else:
                    damage_enemy = random.randint(pattern_enemy['damage'][0], pattern_enemy['damage'][1])
                    damage = round(damage_enemy - (damage_enemy * character_def), 1)
                    actor['current_health'] -= damage
                    print(f'\n>>>[Нанесено {damage} обычного урона по вам]<<<')

        elif count_act % 2 != 0:

            time.sleep(1)

            print('\n>>>>[Информация] Ваш ход: ')

            crit_chance = round(random.random(), 2)
            miss_chance = round(random.random(), 2)

            while True:
                actor_act = input("\n1. Атаковать | 2. Подлечиться | 3. Проверить здоровье: ")

                if actor_act in ('1', '2'):
                    break
                elif actor_act == '3':
                    actor['current_health'] = round(actor['current_health'])
                    print(f"\n>>>[Информация]Текущее/максимальное hp: {actor['current_health']}/{actor['current_max_health']}")

            if actor_act == '1':

                if crit_chance <= actor['crit_damage_chance']:
                    crit_damage_decs = random.choice(actor['crit_damage_tuple'])

                    if miss_chance <= pattern_enemy['miss_damage']:
                        miss_damage_decs = pattern_enemy['miss_damage_desc']
                        print(miss_damage_decs)
                    else:
                        print(actor[crit_damage_decs])
                        damage = round(actor['damage_crit'] - (enemy_def * actor['damage_crit']), 1)
                        current_health_enemy -= damage
                        print(f'\n>>>[Нанесено {damage} критического урона]<<<')
                else:
                    if miss_chance <= pattern_enemy['miss_damage']:
                        miss_damage_decs = pattern_enemy['miss_damage_desc']
                        print(miss_damage_decs)
                    else:
                        damage = round(actor['force_damage_current'] - (enemy_def * actor['force_damage_current']), 1)
                        current_health_enemy -= damage
                        print(f'\n>>>[Нанесено {damage} обычного урона]<<<')

            elif actor_act == '2':
                hp_bottle_boost(actor)

        if is_dead(actor):
            print('\n>>>[Информация] Вы потерпели поражение! ')
            break

        count_act += 1

    else:
        print(f'\n>>>[Информация] Вы успешно одержали победу над {pattern_enemy['name']}')
        actor['exp_current'] += pattern_enemy['exp']
        print(f'>>>[Информация] Вы получили {pattern_enemy['exp']} опыта!')
        actor['money'] += enemy_reward
        print(f'>>>[Информация] Вы получили {enemy_reward} золота!')

        time.sleep(2)


def fight(scene_all, level_part, actor):
    random_choice_enemy = round(random.random(), 2)

    probability_boss = scene_all['probability_attack_boss']

    if random_choice_enemy <= probability_boss:
        pattern = boss_enemy_pattern(scene_all, level_part)

        fight_process(pattern, actor)

    elif random_choice_enemy > probability_boss:
        pattern = common_enemy_pattern(scene_all, level_part)

        fight_process(pattern, actor)

def common_enemy_pattern(scene, level_part):

    enemy_pattern = {
        'name':scene[level_part]['enemies']['name_enemy_common'],
        'damage':scene[level_part]['enemies']['damage_enemy_common'],
        'reward':scene[level_part]['enemies']['reward_enemy_common'],
        'health':scene[level_part]['enemies']['health_enemy_common'],
        'exp':scene[level_part]['enemies']['exp_enemy_common'],
        'protect':scene[level_part]['enemies']['protect_common'],
        'crit':scene[level_part]['enemies']['crit_enemy_common'],
        'crit_desc':scene[level_part]['enemies']['crit_enemy_common_desc'],
        'miss_damage':scene[level_part]['enemies']['miss_damage_common'],
        'miss_damage_desc': scene[level_part]['enemies']['miss_damage_common_desc'],
        'appearance_desc_1': "\n>>>[УГРОЗА] Из-за угла выскакивает {name}! Он явно настроен враждебно и готов к атаке.",
        'appearance_desc_2': "\n>>>[УГРОЗА] Не успеваете вы сделать и шага, как из темноты на вас бросается {name}!"
                             "\nКажется, вы потревожили его покой",
        'appearance_desc_3': "\n>>>[УГРОЗА] Из-за груды камней появляется {name}."
                             "\nЕго взгляд полон агрессии, и он явно не рад вашему вторжению.",
        'appearance_desc_4': "\n>>>[УГРОЗА] То, что вы приняли за безобидный предмет, вдруг оживает!"
                             "\nЭто {name}, и он недружелюбно настроен.",
        'appearance_desc_tuple':('appearance_desc_1', 'appearance_desc_2', 'appearance_desc_3', 'appearance_desc_4')
    }

    return enemy_pattern

def boss_enemy_pattern(scene, level_part):

    enemy_pattern = {
        'name': scene[level_part]['enemies']['enemy_boss_name'],
        'damage':scene[level_part]['enemies']['enemy_boss_damage'],
        'reward': scene[level_part]['enemies']['enemy_boss_reward'],
        'health': scene[level_part]['enemies']['enemy_boss_health'],
        'exp': scene[level_part]['enemies']['enemy_boss_exp'],
        'protect': scene[level_part]['enemies']['protect_boss'],
        'crit': scene[level_part]['enemies']['enemy_boss_crit'],
        'crit_desc': scene[level_part]['enemies']['enemy_boss_crit_desc'],
        'miss_damage': scene[level_part]['enemies']['miss_damage_boss'],
        'miss_damage_desc': scene[level_part]['enemies']['miss_damage_boss_desc'],
        'appearance_desc_1':"\n>>>[УГРОЗА] То, что вы принимали за каменную статую, вдруг начинает двигаться."
                            "\nГлыба камня превращается в грозного воина. «Я – {name}. Ты потревожил мой тысячелетний сон!",
        'appearance_desc_2':"\n>>>[УГРОЗА] С потолка обрушивается массивная фигура, от удара которой дрожит земля."
                            "\n«Я – {name}! Покажи мне, на что ты способен, жалкий неудачник!",
        'appearance_desc_3':"\n>>>[УГРОЗА] «Ищешь меня?» – раздается голос сзади. Вы оборачиваетесь и видите улыбающееся существо."
                            "\n« Я - {name}, это будет твой последний бой.»",
        'appearance_desc_4':"\n>>>[УГРОЗА] Воздух мерцает, и перед вами материализуется покрытая рунами фигура."
                            "«Я – {name}, страж этого этажа. Твое путешествие закончится здесь.",
        'appearance_desc_tuple':('appearance_desc_1', 'appearance_desc_2', 'appearance_desc_3', 'appearance_desc_4')
    }

    return enemy_pattern


character = {

    'force_damage_start': 7,
    'force_damage_current': 0,
    'max_health_start': 100,
    'current_max_health':0,
    'current_health': 0,
    'force': 5,
    'dex': 5,
    'vit': 5,
    'def': 2,
    'money': 25,
    'exp_current': 0,
    'current_level': 1,
    'max_level': 20,
    'protect_boost': 0,
    'force_boost': 0,
    'dex_boost': 0,
    'health_boost': 0,
    'points': 3,
    'hp_bottles': 0,
    'permanent_bonus_hp': 0,
    'pos_force': 0,
    'pos_dex': 0,
    'pos_vit': 0,
    'pos_def': 0,


    'miss_damage_desc_1':"\n>>>[УВОРОТ] Резким рывком в сторону вы уворачиваетесь от удара, заставляя врага промахнуться и потерять равновесие.",
    'miss_damage_desc_2':"\n>>>[УВОРОТ] Вы пригибаетесь, и лезвие просвистело у вас над головой. Мгновенная реакция спасла вас!",
    'miss_damage_desc_3':"\n>>>[УВОРОТ] Взгляд противника выдал его намерение. Вы были готовы и с легкостью уклонились от предсказуемого удара.",
    'miss_damage_tuple':('miss_damage_desc_1', 'miss_damage_desc_2', 'miss_damage_desc_3'),

    'crit_damage_desc_1':'\n>>>[КРИТ]Молниеносная атака! Вы наносите серию быстрых, точных ударов, с которыми враг не может справиться.',
    'crit_damage_desc_2':'\n>>>[КРИТ]Противник открывается на долю секунды — и этого достаточно. Ваше оружие вонзается точно в цель.',
    'crit_damage_desc_3': '\n>>>[КРИТ]Вы вкладываете всю свою ярость в один идеальный удар! Раздается оглушительный хруст, и враг отлетает назад.',
    'crit_damage_tuple': ('crit_damage_desc_1', 'crit_damage_desc_2', 'crit_damage_desc_3') ,

}

dungeon_rewards = {

    1: {

        'name':"Поношенные Ботфорты",
        'protect_boost': 2,
        'force_boost': 0,
        'dex_boost': 0,
        'health_boost': 0,

    },

    2: {

        'name': "Кожаный нагрудник",
        'protect_boost': 3,
        'force_boost': 0,
        'dex_boost': 0,
        'health_boost': 0

    },

    3: {

        'name': "Перчатки Студенческого Труда",
        'protect_boost': 0,
        'force_boost': 2,
        'dex_boost': 0,
        'health_boost': 0

    },

    4: {

        'name': "Плащ Шепчущей Тени",
        'protect_boost': 0,
        'force_boost': 0,
        'dex_boost': 3,
        'health_boost': 0

    },

    5: {

        'name': "Амулет Ясного Ума",
        'protect_boost': 0,
        'force_boost': 0,
        'dex_boost': 2,
        'health_boost': 0

    },

    6: {

        'name': "Сапоги Скользящего Времени",
        'protect_boost': 0,
        'force_boost': 0,
        'dex_boost': 3,
        'health_boost': 0

    },

    7: {

        'name': "Кольцо Фитнеса",
        'protect_boost': 0,
        'force_boost': 0,
        'dex_boost': 0,
        'health_boost': 3

    },

    8: {

        'name': "Шлем Просветления",
        'protect_boost': 0,
        'force_boost': 2,
        'dex_boost': 0,
        'health_boost': 2

    },

    9: {

        'name': "Наручи Железной Воли",
        'protect_boost': 2,
        'force_boost': 3,
        'dex_boost': 2,
        'health_boost': 2

    },

    10: {

        'name': "Зачетка Юлии Игоревны",
        'protect_boost': 10,
        'force_boost': 10,
        'dex_boost': 10,
        'health_boost': 10

    },



}

sudden_events = {

    'mysterious_stranger':{

        'desc':"\n>>>[Событие] В тусклом свете вы замечаете фигуру в потрепанной мантии, сидящую на обломке колонны."
               "\n Его лицо скрыто в тени, но вы чувствуете на себе его пронзительный взгляд."
               "\n'Подойди, искатель знаний,' — раздается его хриплый шепот."
               "\n'Я могу дать тебе силу, но всё в этом мире имеет свою цену.'",

        'choice_desc':'\n[+20 к макс. здоровью (но -40 к текущему)]',
        
        'increase':20,
        'reduce':40,

    },

    'the_chamber_0f_secrets': {

        'desc': "\n>>>[Событие] За подвижной панелью вы обнаруживаете узкую потайную комнату. "
                "\nВоздух здесь спертый и пыльный. В центре на простом каменном постаменте стоит небольшой сундук."
                "\nОн выглядит подозрительно нетронутым.",

        'choice_desc': '\n[50/50 либо - 50 к текущему здоровью, либо + 50 золота]',

        'increase':50,
        'reduce':50,

    },

    'fountain_of_knowledge': {

        'desc': "\n>>>[Событие] Вы выходите в небольшой грот, где из стены бьет кристально чистый родник."
                "\nВода стекает в чашу, высеченную в камне, и излучает едва заметное мягкое свечение."
                "\nВозле него вы чувствуете невероятный прилив бодрости и ясности мыслей.",

        'choice_desc': '\n[Восстанавливает все здоровье]',

    },

    'nothing': {

        'desc': "\n>>>[Событие] В небольшой нише, почти скрытый в тени, вы замечаете забытый кем-то стеклянный пузырёк."
                "\nАккуратный, без пыли, будто его оставили здесь совсем недавно."
                "\nВнутри переливается знакомая красноватая жидкость. Похоже, сегодня вам просто повезло",

        'choice_desc': '\n[Вы нашли 1 бутылек здоровья]',



    },

    'trader': {

        'desc': "\n>>>[Событие] В небольшом тупичке, прижавшись к стене, сидит хмурый гном в заляпанном фартуке."
                "\n Перед ним на разложенном одеяле аккуратно расставлены пузырьки с красноватой жидкостью."
                "\n'Зелья здоровья, свежие!' — бурчит он, не глядя на вас."
                "\n'Бери, не пожалеешь. В этих стенах лишняя капля жизни не помешает.'",

        'choice_desc': '\n[Цена 1 бутылек: 25 золотых]',

        'cost': 25

    },

    'events_tuple':('mysterious_stranger', 'the_chamber_0f_secrets', 'fountain_of_knowledge', 'nothing', 'trader'),


}


scenes = {

    "Actions":{'1. Повернуть налево', "2. Повернуть направо", "3. Осмотреться", "4. Идти вперед"},

    'probability_attack_boss': 0.25,
    'probability_attack_common': 0.75,
    'probability_attack': 0.30,
    'probability_sudden': 0.35,

    'nothing_desc_1':'\n[Ничего не произошло] Вы продолжаете свой путь по тихому коридору.'
                     '\nКажется, на этом участке подземелья царит необычное спокойствие.'
                     '\nЛишь эхо ваших шагов нарушает гнетущую тишину.'
                     '\nВозможно, это последняя передышка перед новыми испытаниями.',

    'nothing_desc_2': '\n[Ничего не произошло] Перед вами очередной ничем не примечательный коридор.'
                      '\nКаменные стены, пыльный пол, потрескавшиеся своды.'
                      '\nНи врагов, ни сокровищ.'
                      '\nПросто еще один отрезок пути в глубины подземелья.',

    'nothing_desc_3': '\n[Ничего не произошло] Вы заходите в камеру, которая кажется тупиком.'
                      '\nНесколько минут осмотра не приносят результатов - здесь действительно нечего делать.'
                      '\nПридется возвращаться и искать другой путь.',

    'nothing_desc_4': '\n[Ничего не произошло] Вы замедляете шаг, ожидая подвоха. Но ничего не происходит.'
                      '\nЛишь холодный воздух подземелья обжигает легкие. '
                      '\nИногда отсутствие опасности настораживает куда больше, чем сама опасность.',

    'nothing_desc_5': '\n[Ничего не произошло] На несколько минут в подземелье воцаряется идиллия.'
                      '\nНи звука, ни движения. Вы почти начинаете расслабляться, но затем вспоминаете,'
                      '\nв этих стенах расслабляться смертельно опасно. Лучше двигаться дальше.',

    'nothing_tuple_acts':('nothing_desc_1', 'nothing_desc_2', 'nothing_desc_3', 'nothing_desc_4', 'nothing_desc_5'),

    1: {

        'name_dungeon': "Заброшенный холл",

        'description':"\n>>> Воздух пыльный и неподвижный. Свет, исходящий от потускневших люминесцентных ламп на высоком потолке,"
                      "\nмерцает, отбрасывая длинные, пляшущие тени."
                      "\nСтены когда-то были обшиты дубом, но теперь панели потрескались и покрыты паутиной."
                      "\nРазбросанные по полу обрывки конспектов и сломанные стулья намекают на то,"
                      "\nчто здесь когда-то кипела академическая жизнь, ныне забытая."
                      "\nВпереди — массивная дверь, ведущая вглубь.",
        
        'enemies': {

            "name_enemy_common":'Пыльный Шептун',
            "damage_enemy_common":(5, 10),
            "reward_enemy_common":(5, 10),
            "health_enemy_common":(40, 50),
            "exp_enemy_common": 35,
            'protect_common': 0,
            "crit_enemy_common": 0.06,
            "crit_enemy_common_desc": '\t\n>>>[КРИТ ПО ВАМ] Шепот переходит в пронзительный визг! Вы получили Критический удар!',
            "miss_damage_common": 0.04,
            "miss_damage_common_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Пыльный шептун растворяется в облаке пыли",
            
            "enemy_boss_name":"Старший Конспект",
            "enemy_boss_damage":(7, 12),
            "enemy_boss_reward":(7, 12),
            "enemy_boss_health":(50, 60),
            "enemy_boss_exp": 40,
            'protect_boss': 1,
            "enemy_boss_crit": 0.06,
            "enemy_boss_crit_desc": '\t\n>>>[КРИТ ПО ВАМ] Формулы на листке вспыхивают алым пламенем! Вы получили Критический удар!',
            "miss_damage_boss": 0.04,
            "miss_damage_boss_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Чернильный фантом расплывается, уходя от клинка",

            "mobs_case_key": ("name_enemy_common", "enemy_boss_name"),

        },

        'dungeon_reward':dungeon_rewards[1],

    },

    2: {

        'name_dungeon': "Библиотека забытых томов",

        'description': "\n>>> Бесконечные стеллажи, уходящие в темноту, заставлены книгами в одинаковых кожаных переплетах без названий."
                       "\nТишина стоит звенящая, нарушаемая лишь шелестом страниц, который издает не ветер.",

        'enemies': {

            "name_enemy_common": 'Блуждающий Фолиант',
            "damage_enemy_common": (8, 13),
            "reward_enemy_common": (8, 13),
            "health_enemy_common": (60, 70),
            "exp_enemy_common": 50,
            'protect_common': 1,
            "crit_enemy_common": 0.07,
            "crit_enemy_common_desc": '\t\n>>>[КРИТ ПО ВАМ] Книга раскрывается на странице с сокрушительным заклятьем! Крит!',
            "miss_damage_common": 0.05,
            "miss_damage_common_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Тяжелый переплет книги с грохотом захлопывается,"
                                       "\t\nиспользуя свой корешок как щит.",

            "enemy_boss_name": "Чернильный Фантом",
            "enemy_boss_damage": (10, 15),
            "enemy_boss_reward": (10, 15),
            "enemy_boss_health": (65, 75),
            "enemy_boss_exp": 60,
            "enemy_boss_crit": 0.05,
            'protect_boss': 2,
            "enemy_boss_crit_desc": '\t\n>>>[КРИТ ПО ВАМ] Чернильная клякса превращается в острейшую иглу! Критическое попадание!',
            "miss_damage_boss": 0.05,
            "miss_damage_boss_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Фантом на мгновение теряет форму, превращаясь в чернильную лужу.",

            "mobs_case_key": ("name_enemy_common", "enemy_boss_name"),

        },

        'dungeon_reward_2': dungeon_rewards[2],

    },

    3: {

        'name_dungeon': "Лаборатория алхимика",

        'description': "\n>>> Резкий запах реактивов бьет в нос. Столы заставлены колбами и ретортами,"
                       "\nв некоторых до сих пор кипят разноцветные жидкости."
                       "\nПо полу разлиты лужи неизвестного происхождения, которые лучше не трогать.",

        'enemies': {

            "name_enemy_common": 'Сбежавший Реагент',
            "damage_enemy_common": (12, 17),
            "reward_enemy_common": (12, 17),
            "health_enemy_common": (80, 90),
            "exp_enemy_common": 65,
            'protect_common': 1,
            "crit_enemy_common": 0.08,
            "crit_enemy_common_desc": '\t\n>>>[КРИТ ПО ВАМ] Реагент вскипает с взрывной силой!',
            "miss_damage_common": 0.06,
            "miss_damage_common_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Реагент с шипением выкипает, и ваша атака попадает в едкий пар.",

            "enemy_boss_name": "Булькающий Слизень",
            "enemy_boss_damage": (15, 18),
            "enemy_boss_reward": (10, 15),
            "enemy_boss_health": (90, 100),
            "enemy_boss_exp": 80,
            'protect_boss': 3,
            "enemy_boss_crit": 0.08,
            "enemy_boss_crit_desc": '\t\n>>>[КРИТ ПО ВАМ] Слизень выплевывает сгусток невероятной едкости! Крит!',
            "ability_boss_chance": 0.1,
            "miss_damage_boss": 0.06,
            "miss_damage_boss_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Слизень сжимается в упругий шар и отскакивает от слова, уворачиваясь.",

            "mobs_case_key": ("name_enemy_common", "enemy_boss_name"),

        },

        'dungeon_reward': dungeon_rewards[3],

    },

    4: {

        'name_dungeon': "Бальный зал призраков",

        'description': "\n>>> Огромное помещение с хрустальной люстрой, затянутой паутиной."
                       "\nПыльные зеркала вдоль стен отражают не вас, а тени давно минувших балов."
                       "\nЭхо ваших шагов смешивается с призрачными звуками вальса.",

        'enemies': {

            "name_enemy_common": 'Тень Кавалера',
            "damage_enemy_common": (16, 20),
            "reward_enemy_common": (16, 20),
            "health_enemy_common": (100, 120),
            "exp_enemy_common": 90,
            'protect_common': 2,
            "crit_enemy_common": 0.09,
            "crit_enemy_common_desc": '\t\n>>>[КРИТ ПО ВАМ] Теневой клинок наносит удар нечеловеческой точности! Критический удар!',
            "miss_damage_common": 0.07,
            "miss_damage_common_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Тень исполняет фигуру высшего пилотажа, отступая с невероятной грацией.",

            "enemy_boss_name": "Маэстро Призрачного Бала",
            "enemy_boss_damage": (28, 32),
            "enemy_boss_reward": 65,
            "enemy_boss_health": 180,
            "enemy_boss_exp": 200,
            "enemy_boss_crit": 0.09,
            'protect_boss': 4,
            "enemy_boss_crit_desc": '\t\n>>>[КРИТ ПО ВАМ] Дирижерская палочка Маэстро выписывает смертельную арпеджио! Крит!',
            "ability_boss_chance": 0.11,
            "miss_damage_boss": 0.07,
            "miss_damage_boss_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Маэстро исполняет пируэт, и его полупрозрачная форма ускользает от лезвия.",

            "mobs_case_key": ("name_enemy_common", "enemy_boss_name"),

        },

        'dungeon_reward': dungeon_rewards[4],

    },

    5: {

        'name_dungeon':"Лабиринт иллюзий",

        'description': "\n>>> Стены здесь состоят из дыма и тумана, постоянно меняя свою форму."
                       "\nВам чудится, что вы уже были в этом месте пять минут назад.",

        'enemies': {

            "name_enemy_common": 'Мираж-Обманщик',
            "damage_enemy_common": (18, 24),
            "reward_enemy_common": (18, 24),
            "health_enemy_common": (120, 140),
            "exp_enemy_common": 110,
            'protect_common': 2,
            "crit_enemy_common": 0.1,
            "crit_enemy_common_desc": '\t\n>>>[КРИТ ПО ВАМ] Иллюзия на мгновение становится смертоносной реальностью! Критическое попадание!',
            "miss_damage_common": 0.08,
            "miss_damage_common_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Ваше оружие проходит сквозь мираж, не встречая сопротивления.",

            "enemy_boss_name": "Властитель Иллюзий",
            "enemy_boss_damage": (32, 36),
            "enemy_boss_reward": 80,
            "enemy_boss_health": 220,
            "enemy_boss_exp": 300,
            "enemy_boss_crit": 0.1,
            'protect_boss': 5,
            "enemy_boss_crit_desc": '\t\n>>>[КРИТ ПО ВАМ] Властитель манипулирует самой реальностью, и пространство разрывает вас! Крит!',
            "ability_boss_chance": 0.11,
            "miss_damage_boss": 0.08,
            "miss_damage_boss_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Властитель исчезает и появляется за вашей спиной, усмехаясь.",

            "mobs_case_key": ("name_enemy_common", "enemy_boss_name"),

        },

        'dungeon_reward': dungeon_rewards[5],

    },

    6: {

        'name_dungeon': "Чертежные комнаты",

        'description': "\n>>> Помещение завалено свитками и чертежами с невероятными механизмами."
                       "\nЦиркули и линейки лежат в идеальном порядке.",

        'enemies': {

            "name_enemy_common": 'Живой Циркуль',
            "health_enemy_common": (140, 160),
            "damage_enemy_common": (22, 27),
            "reward_enemy_common": (22, 27),
            'protect_common': 3,
            "exp_enemy_common": 130,
            "crit_enemy_common": 0.11,
            "crit_enemy_common_desc": '\t\n>>>[КРИТ ПО ВАМ] Циркуль с идеальной точностью вонзается в вас! Критический удар!',
            "miss_damage_common": 0.09,
            "miss_damage_common_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Циркуль отступает по идеальной дуге, отклоняя атаку.",

            "enemy_boss_name": "Чертежный Дракон",
            "enemy_boss_health": 270,
            "enemy_boss_damage": (35, 40),
            'protect_boss': 6,
            "enemy_boss_reward": 400,
            "enemy_boss_exp": 230,
            "enemy_boss_crit": 0.11,
            "enemy_boss_crit_desc": '\t\n>>>[КРИТ ПО ВАМ] Дракон вычисляет траекторию вашего разрушения! Сокрушительный крит!',
            "ability_boss_chance": 0.11,
            "miss_damage_boss": 0.09,
            "miss_damage_boss_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Дракон складывается в идеальный чертеж, двухмерный и неуязвимый.",

            "mobs_case_key": ("name_enemy_common", "enemy_boss_name"),

        },

        'dungeon_reward': dungeon_rewards[6],

    },

    7: {

        'name_dungeon': "Оранжерея ядовитых знаний",

        'description': "\n>>> В этой теплой, влажной комнате растут странные растения,"
                       "\nчьи лепестки напоминают пергамент. Воздух густой и сладковатый.",

        'enemies': {

            "name_enemy_common": 'Плющ-Памфлет',
            "health_enemy_common": (160, 180),
            "damage_enemy_common": (26, 30),
            "reward_enemy_common": (26, 30),
            'protect_common': 3,
            "exp_enemy_common": 170,
            "crit_enemy_common": 0.12,
            "crit_enemy_common_desc": '\t\n>>>[КРИТ ПО ВАМ] Ядовитые шипы плюща пронзают вас с невероятной силой! Крит!',
            "miss_damage_common": 0.10,
            "miss_damage_common_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Плющ стремительно отдергивает свои побеги.",

            "enemy_boss_name": "Древний Хранитель Рощи",
            "enemy_boss_health": 320,
            "enemy_boss_damage": (40, 45),
            'protect_boss': 7,
            "enemy_boss_reward": 120,
            "enemy_boss_exp": 450,
            "enemy_boss_crit": 0.12,
            "enemy_boss_crit_desc": '\t\n>>>[КРИТ ПО ВАМ] Древний голос Хранителя произносит слово смерти! Критический удар!',
            "ability_boss_chance": 0.11,
            "miss_damage_boss": 0.10,
            "miss_damage_boss_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Хранитель уходит под землю, и ваша атака бьет по пустому месту.",

            "mobs_case_key": ("name_enemy_common", "enemy_boss_name"),

        },

        'dungeon_reward': dungeon_rewards[7],

    },

    8: {

        'name_dungeon': "Зал испытующего взгляда",

        'description': "\n>>> Длинный, абсолютно белый коридор без дверей и окон."
                       "\n Каждый ваш шаг отдается эхом в голове, заставляя вспоминать все ошибки",

        'enemies': {

            "name_enemy_common": 'Воплощение Страха',
            "health_enemy_common": (180, 200),
            "damage_enemy_common": (30, 35),
            "reward_enemy_common": (30, 35),
            'protect_common': 4,
            "exp_enemy_common": 190,
            "crit_enemy_common": 0.13,
            "crit_enemy_common_desc": '\t\n>>>[КРИТ ПО ВАМ] Ваш худший кошмар наносит сокрушающий удар! Крит!',
            "miss_damage_common": 0.11,
            "miss_damage_common_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Страх пульсирует, и его форма искажается.",

            "enemy_boss_name": "Кошмар наяву",
            "enemy_boss_health": 380,
            "enemy_boss_damage": (45, 50),
            'protect_boss': 8,
            "enemy_boss_reward": 140,
            "enemy_boss_exp": 500,
            "enemy_boss_crit": 0.13,
            "enemy_boss_crit_desc": '\t\n>>>[КРИТ ПО ВАМ] Кошмар материализует вашу самую страшную фобию! Критический ужас!',
            "ability_boss_chance": 0.11,
            "miss_damage_boss": 0.11,
            "miss_damage_boss_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Кошмар искажает пространство, и вы атакуете мимо.",

            "mobs_case_key": ("name_enemy_common", "enemy_boss_name"),

        },

        'dungeon_reward': dungeon_rewards[8],

    },

    9: {

        'name_dungeon': "Аудитория вечного экзамена",

        'description': "\n>>> Ряды парт, за которыми сидят сгорбленные,"
                       "\n полупрозрачные фигуры и пишут что-то на бесконечных листах.",

        'enemies': {

            "name_enemy_common": 'Вечный Студент',
            "health_enemy_common": (200, 220),
            "damage_enemy_common": (34, 38),
            "reward_enemy_common": (34, 38),
            'protect_common': 4,
            "exp_enemy_common": 290,
            "crit_enemy_common": 0.14,
            "crit_enemy_common_desc": '\t\n>>>[КРИТ ПО ВАМ] Отчаяние студента выливается в яростный, точный удар! Крит!',
            "miss_damage_common": 0.12,
            "miss_damage_common_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Сгорбленная фигура студента внезапно падает на пол.",

            "enemy_boss_name": "Тьютор Ада",
            "enemy_boss_health": 450,
            "enemy_boss_damage": (50, 55),
            'protect_boss': 9,
            "enemy_boss_reward": 700,
            "enemy_boss_exp": 400,
            "enemy_boss_crit": 0.14,
            "enemy_boss_crit_desc": '\t\n>>>[КРИТ ПО ВАМ] Печать Тьютора обжигает вашу душу! Сокрушительный крит!',
            "ability_boss_chance": 0.11,
            "miss_damage_boss": 0.12,
            "miss_damage_boss_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Тьютор читает указ, и защитное поле останавливает вашу атаку",

            "mobs_case_key": ("name_enemy_common", "enemy_boss_name"),

        },

        'dungeon_reward': dungeon_rewards[9],

    },

    10: {

        'name_dungeon': "Кабинет Юлии Игоревны",

        'description': "\n>>> Вы замираете на пороге. Это – та самая комната."
                       "\nЗнакомая до боли, но теперь все в ней доведено до сюрреалистичного абсолюта."
                       "\nСтеллажи с конспектами и методичками уходят в заоблачную высь, теряясь где-то в районе потолка,"
                       "\nпревращенного в звездную карту из светящихся оценок."
                       "\nВ воздухе медленно плавают, как осенние листья, зачетки и листки с долгами."
                       "\nВоздух густой, настоянный на аромате старой бумаги, строгого парфюма и несданных вовремя работ."
                       "\n\nЗа массивным учительским столом, заваленным кипами тестов, сидит Она. Спиной к вам. "
                       "\nВ ее руке – красная ручка, которая с мертвой точки выводит замысловатые узоры на полях чьей-то судьбы."
                       "\nТишина стоит такая, что слышно, как муха пролетает где-то на 15 этаже."
                       "\nСтул с глухим скрипом поворачивается."
                       "\nИ вот ее взгляд, тот самый, от которого у целого потока студентов стынет кровь, устремляется на вас."
                       "\nНа губах играет едва заметная, но безжалостная улыбка."
                       '\n\n«Ну что же, — раздается голос, холодный и четкий, как формулировка в билете.'
                       '\n— Я так понимаю, это ваша пересдача?'
                       '\nЧто ж, давайте проверим, чему вы все-таки научились за время своего... академического отпуска».',

        'enemies': {

            "enemy_boss_name": "Юлия Игоревна",
            "enemy_boss_health": 1500,
            "enemy_boss_damage": (70, 85),
            'protect_boss': 20,
            "enemy_boss_reward": 1000,
            "enemy_boss_exp": 2000,
            "enemy_boss_crit": 0.20,
            "enemy_boss_crit_desc": "\n>>>[КРИТ ПО ВАМ] Юлия Игоревна поднимает бровь."
                                    "\n'Это что за примитивный подход? На третьем курсе уже так не мыслят!'"
                                    "\n — ее замечание обрушивается на вас как удар молотка по неподготовленному домашнему заданию."
                                    "\n СОКРУШИТЕЛЬНЫЙ КРИТИЧЕСКИЙ УРОН!",
            "miss_damage_boss": 0.15,
            "miss_damage_boss_desc": "\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Вы яростно атакуете,"
                                     "\nно Юлия Игоревна просто поправляет платок в нагрудном кармане"
                                     "\nи делает шаг в сторону с грацией кошки, обходящей лужу."
                                     "\n'Не туда, не туда... Сначала подумайте, потом действуйте'. Ваша атака проходит мимо!",
            "ability_boss_chance_total": 0.05,
            "ability_boss_chance_total_desc": "\n>>>[Активация способности - смертельная атака]<<< "
                                              "\nВнезапно ее глаза вспыхивают."
                                              "\n'А теперь — ВНЕПЛАНОВАЯ КОНТРОЛЬНАЯ! Без подготовки!"
                                              "\nНа всю оставшуюся жизнь!' Она щелкает пальцами,"
                                              "\nи пространство вокруг вас сжимается от ужаса перед чистым листом.",

        },

        'dungeon_reward': dungeon_rewards[10],

    },

}


user_name = input("Введите имя игрового персонажа: ")
character["name"] = user_name
update_character_stats(character)
character['current_health'] = character['current_max_health']
steps_for_level = 15

for level in range(1, 11):
    print(f'\n\t<---> Этаж - ({level}) {scenes[level]['name_dungeon']} <--->')
    print(scenes[level]['description'])

    if level == 10:

        fight_final_boss(scenes, level, character)
        check_lvl_up(character)

    else:
        for step in range(1, steps_for_level + 1):
            print(f'\n\t\t\t --------------Ход:{step}/{steps_for_level}--------------')

            while True:
                step_print()
                choice = check_input()

                if choice in ('1', '2', '3', '4'):
                    break
                elif choice == '5':
                    print_stats(character)
                elif choice == '6':
                    hp_bottle_boost(character)

            event = event_choice(scenes)

            if event == 'attack':
                fight(scenes, level, character)
                if is_dead(character):
                    break
                check_lvl_up(character)
            elif event == 'sudden':
                sudden_event(sudden_events, character)
            elif event == 'nothing':

                nothing_desc = random.choice(scenes['nothing_tuple_acts'])

                print(scenes[nothing_desc])

            if is_dead(character):
                break

    if is_dead(character):
        print("\n--->ВЫ ПОГИБЛИ, ИГРА ОКОНЧЕНА<---")
        break

    print(f"\n>>>[Действие] Вы получили награду за прохождение этажа: {dungeon_rewards[level]['name']}")
    update_dungeon_eq(level, character)
    update_character_stats(character)

    input('Enter: Чтобы продолжить...')

input('\nНажмите любую клавишу чтобы выйти: ')






