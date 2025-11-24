dungeon_rewards = {

    1: {

        'id_worn_out_boots_name':"Поношенные Ботфорты",
        'protect_boost': 1,

    }

}

sudden_events = {



}


scenes = {

    "Actions":(),

    'sudden_events':(),

    1: {

        'name_dungeon': "Заброшенный холл",

        'description':"\n[Воздух пыльный и неподвижный. Свет, исходящий от потускневших люминесцентных ламп на высоком потолке,"
                      "\n мерцает, отбрасывая длинные, пляшущие тени."
                      "\n Стены когда-то были обшиты дубом, но теперь панели потрескались и покрыты паутиной."
                      "\n Разбросанные по полу обрывки конспектов и сломанные стулья намекают на то,"
                      "\n что здесь когда-то кипела академическая жизнь, ныне забытая."
                      "\n Впереди — массивная дверь, ведущая вглубь.]",
        
        'enemies': {

            "name_enemy_common":'Пыльный Шептун',
            "damage_enemy_common":(5, 10),
            "reward_enemy_common":(5, 10),
            "health_enemy_common":(40, 50),
            "exp_enemy_common": 25,
            'protect_common': 0,
            "crit_enemy_common": 0.06,
            "crit_enemy_common_desc": '\t\n>>>[КРИТ ПО ВАМ] Шепот переходит в пронзительный визг! Вы получили Критический удар!',
            "miss_damage_common": 0.04,
            "miss_damage_common_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Пыльный шептун растворяется в облаке пыли",
            
            "enemy_boss_name":"Старший Конспект",
            "enemy_boss_damage":(7, 12),
            "enemy_boss_reward":(7, 12),
            "enemy_boss_health":(50, 60),
            "enemy_boss_exp": 30,
            'protect_boss': 1,
            "enemy_boss_crit": 0.06,
            "enemy_boss_crit_desc": '\t\n>>>[КРИТ ПО ВАМ] Формулы на листке вспыхивают алым пламенем! Вы получили Критический удар!',
            "miss_damage_boss": 0.04,
            "miss_damage_boss_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Чернильный фантом расплывается, уходя от клинка",
            "appearance_boss_chance": 0.20,

            "mobs_case_key": ("name_enemy_common", "enemy_boss_name"),

        },

        'dungeon_reward':dungeon_rewards[1],

    },

    2: {

        'name_dungeon': "Библиотека забытых томов",

        'description': "\n[Бесконечные стеллажи, уходящие в темноту, заставлены книгами в одинаковых кожаных переплетах без названий."
                       "\n Тишина стоит звенящая, нарушаемая лишь шелестом страниц, который издает не ветер.]",

        'enemies': {

            "name_enemy_common": 'Блуждающий Фолиант',
            "damage_enemy_common": (8, 13),
            "reward_enemy_common": (8, 13),
            "health_enemy_common": (60, 70),
            "exp_enemy_common": 35,
            'protect_common': 1,
            "crit_enemy_common": 0.07,
            "crit_enemy_common_desc": '\t\n>>>[КРИТ ПО ВАМ] Книга раскрывается на странице с сокрушительным заклятьем! Крит!',
            "miss_damage_common": 0.05,
            "miss_damage_common_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Тяжелый переплет книги с грохотом захлопывается,"
                                       "\t\nиспользуя свой корешок как щит.",

            "enemy_boss_name": "Чернильный Фантом",
            "enemy_boss_damage": (10, 15),
            "enemy_boss_reward": (10, 15),
            "enemy_boss_health": (70, 80),
            "enemy_boss_exp": 40,
            "enemy_boss_crit": 0.05,
            'protect_boss': 2,
            "enemy_boss_crit_desc": '\t\n>>>[КРИТ ПО ВАМ] Чернильная клякса превращается в острейшую иглу! Критическое попадание!',
            "miss_damage_boss": 0.05,
            "miss_damage_boss_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Фантом на мгновение теряет форму, превращаясь в чернильную лужу.",
            "appearance_boss_chance": 0.20,

            "mobs_case_key": ("name_enemy_common", "enemy_boss_name"),

        },

        'dungeon_reward_2': dungeon_rewards[2],

    },

    3: {

        'name_dungeon': "Лаборатория алхимика",

        'description': "\n[Резкий запах реактивов бьет в нос. Столы заставлены колбами и ретортами,"
                       "\n в некоторых до сих пор кипят разноцветные жидкости."
                       "\n По полу разлиты лужи неизвестного происхождения, которые лучше не трогать.]",

        'enemies': {

            "name_enemy_common": 'Сбежавший Реагент',
            "damage_enemy_common": (12, 17),
            "reward_enemy_common": (12, 17),
            "health_enemy_common": (80, 90),
            "exp_enemy_common": 45,
            'protect_common': 1,
            "crit_enemy_common": 0.08,
            "crit_enemy_common_desc": '\t\n>>>[КРИТ ПО ВАМ] Реагент вскипает с взрывной силой!',
            "miss_damage_common": 0.06,
            "miss_damage_common_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Реагент с шипением выкипает, и ваша атака попадает в едкий пар.",

            "enemy_boss_name": "Булькающий Слизень",
            "enemy_boss_damage": (15, 18),
            "enemy_boss_reward": (10, 15),
            "enemy_boss_health": (90, 100),
            "enemy_boss_exp": 40,
            'protect_boss': 3,
            "enemy_boss_crit": 0.08,
            "enemy_boss_crit_desc": '\t\n>>>[КРИТ ПО ВАМ] Слизень выплевывает сгусток невероятной едкости! Крит!',
            "ability_boss_chance": 0.1,
            "miss_damage_boss": 0.06,
            "miss_damage_boss_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Слизень сжимается в упругий шар и отскакивает от слова, уворачиваясь.",
            "appearance_boss_chance": 0.20,

            "mobs_case_key": ("name_enemy_common", "enemy_boss_name"),

        },

        'dungeon_reward': dungeon_rewards[3],

    },

    4: {

        'name_dungeon': "Бальный зал призраков",

        'description': "\n[Огромное помещение с хрустальной люстрой, затянутой паутиной."
                       "\n Пыльные зеркала вдоль стен отражают не вас, а тени давно минувших балов."
                       "\n Эхо ваших шагов смешивается с призрачными звуками вальса.]",

        'enemies': {

            "name_enemy_common": 'Тень Кавалера',
            "damage_enemy_common": (16, 20),
            "reward_enemy_common": (16, 20),
            "health_enemy_common": (100, 120),
            "exp_enemy_common": 55,
            'protect_common': 2,
            "crit_enemy_common": 0.09,
            "crit_enemy_common_desc": '\t\n>>>[КРИТ ПО ВАМ] Теневой клинок наносит удар нечеловеческой точности! Критический удар!',
            "miss_damage_common": 0.07,
            "miss_damage_common_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Тень исполняет фигуру высшего пилотажа, отступая с невероятной грацией.",

            "enemy_boss_name": "Маэстро Призрачного Бала",
            "enemy_boss_damage": (28, 32),
            "enemy_boss_reward": 65,
            "enemy_boss_health": 180,
            "enemy_boss_exp": 150,
            "enemy_boss_crit": 0.09,
            'protect_boss': 4,
            "enemy_boss_crit_desc": '\t\n>>>[КРИТ ПО ВАМ] Дирижерская палочка Маэстро выписывает смертельную арпеджио! Крит!',
            "ability_boss_chance": 0.11,
            "miss_damage_boss": 0.07,
            "miss_damage_boss_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Маэстро исполняет пируэт, и его полупрозрачная форма ускользает от лезвия.",
            "appearance_boss_chance": 0.20,

            "mobs_case_key": ("name_enemy_common", "enemy_boss_name"),

        },

        'dungeon_reward': dungeon_rewards[4],

    },

    5: {

        'name_dungeon':"Лабиринт иллюзий",

        'description': "\n[Стены здесь состоят из дыма и тумана, постоянно меняя свою форму."
                       "\n Вам чудится, что вы уже были в этом месте пять минут назад.]",

        'enemies': {

            "name_enemy_common": 'Мираж-Обманщик',
            "damage_enemy_common": (18, 24),
            "reward_enemy_common": (18, 24),
            "health_enemy_common": (120, 140),
            "exp_enemy_common": 55,
            'protect_common': 2,
            "crit_enemy_common": 0.1,
            "crit_enemy_common_desc": '\t\n>>>[КРИТ ПО ВАМ] Иллюзия на мгновение становится смертоносной реальностью! Критическое попадание!',
            "miss_damage_common": 0.08,
            "miss_damage_common_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Ваше оружие проходит сквозь мираж, не встречая сопротивления.",

            "enemy_boss_name": "Властитель Иллюзий",
            "enemy_boss_damage": (32, 36),
            "enemy_boss_reward": 80,
            "enemy_boss_health": 220,
            "enemy_boss_exp": 190,
            "enemy_boss_crit": 0.1,
            'protect_boss': 5,
            "enemy_boss_crit_desc": '\t\n>>>[КРИТ ПО ВАМ] Властитель манипулирует самой реальностью, и пространство разрывает вас! Крит!',
            "ability_boss_chance": 0.11,
            "miss_damage_boss": 0.08,
            "miss_damage_boss_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Властитель исчезает и появляется за вашей спиной, усмехаясь.",
            "appearance_boss_chance": 0.20,

            "mobs_case_key": ("name_enemy_common", "enemy_boss_name"),

        },

        'dungeon_reward': dungeon_rewards[5],

    },

    6: {

        'name_dungeon': "Чертежные комнаты",

        'description': "\n[Помещение завалено свитками и чертежами с невероятными механизмами."
                       "\n Циркули и линейки лежат в идеальном порядке.]",

        'enemies': {

            "name_enemy_common": 'Живой Циркуль',
            "health_enemy_common": (140, 160),
            "damage_enemy_common": (22, 27),
            "reward_enemy_common": (22, 27),
            'protect_common': 3,
            "exp_enemy_common": 75,
            "crit_enemy_common": 0.11,
            "crit_enemy_common_desc": '\t\n>>>[КРИТ ПО ВАМ] Циркуль с идеальной точностью вонзается в вас! Критический удар!',
            "miss_damage_common": 0.09,
            "miss_damage_common_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Циркуль отступает по идеальной дуге, отклоняя атаку.",

            "enemy_boss_name": "Чертежный Дракон",
            "enemy_boss_health": 270,
            "enemy_boss_damage": (35, 40),
            'protect_boss': 6,
            "enemy_boss_reward": 100,
            "enemy_boss_exp": 230,
            "enemy_boss_crit": 0.11,
            "enemy_boss_crit_desc": '\t\n>>>[КРИТ ПО ВАМ] Дракон вычисляет траекторию вашего разрушения! Сокрушительный крит!',
            "ability_boss_chance": 0.11,
            "miss_damage_boss": 0.09,
            "miss_damage_boss_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Дракон складывается в идеальный чертеж, двухмерный и неуязвимый.",
            "appearance_boss_chance": 0.20,

            "mobs_case_key": ("name_enemy_common", "enemy_boss_name"),

        },

        'dungeon_reward': dungeon_rewards[6],

    },

    7: {

        'name_dungeon': "Оранжерея ядовитых знаний",

        'description': "\n[В этой теплой, влажной комнате растут странные растения,"
                       "\n чьи лепестки напоминают пергамент. Воздух густой и сладковатый.]",

        'enemies': {

            "name_enemy_common": 'Плющ-Памфлет',
            "health_enemy_common": (160, 180),
            "damage_enemy_common": (26, 30),
            "reward_enemy_common": (26, 30),
            'protect_common': 3,
            "exp_enemy_common": 85,
            "crit_enemy_common": 0.12,
            "crit_enemy_common_desc": '\t\n>>>[КРИТ ПО ВАМ] Ядовитые шипы плюща пронзают вас с невероятной силой! Крит!',
            "miss_damage_common": 0.10,
            "miss_damage_common_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Плющ стремительно отдергивает свои побеги.",

            "enemy_boss_name": "Древний Хранитель Рощи",
            "enemy_boss_health": 320,
            "enemy_boss_damage": (40, 45),
            'protect_boss': 7,
            "enemy_boss_reward": 120,
            "enemy_boss_exp": 280,
            "enemy_boss_crit": 0.12,
            "enemy_boss_crit_desc": '\t\n>>>[КРИТ ПО ВАМ] Древний голос Хранителя произносит слово смерти! Критический удар!',
            "ability_boss_chance": 0.11,
            "miss_damage_boss": 0.10,
            "miss_damage_boss_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Хранитель уходит под землю, и ваша атака бьет по пустому месту.",
            "appearance_boss_chance": 0.20,

            "mobs_case_key": ("name_enemy_common", "enemy_boss_name"),

        },

        'dungeon_reward': dungeon_rewards[7],

    },

    8: {

        'name_dungeon': "Зал испытующего взгляда",

        'description': "\n[Длинный, абсолютно белый коридор без дверей и окон."
                       "\n Каждый ваш шаг отдается эхом в голове, заставляя вспоминать все ошибки.]",

        'enemies': {

            "name_enemy_common": 'Воплощение Страха',
            "health_enemy_common": (180, 200),
            "damage_enemy_common": (30, 35),
            "reward_enemy_common": (30, 35),
            'protect_common': 4,
            "exp_enemy_common": 95,
            "crit_enemy_common": 0.13,
            "crit_enemy_common_desc": '\t\n>>>[КРИТ ПО ВАМ] Ваш худший кошмар наносит сокрушающий удар! Крит!',
            "miss_damage_common": 0.11,
            "miss_damage_common_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Страх пульсирует, и его форма искажается.",

            "enemy_boss_name": "Кошмар наяву",
            "enemy_boss_health": 380,
            "enemy_boss_damage": (45, 50),
            'protect_boss': 8,
            "enemy_boss_reward": 140,
            "enemy_boss_exp": 330,
            "enemy_boss_crit": 0.13,
            "enemy_boss_crit_desc": '\t\n>>>[КРИТ ПО ВАМ] Кошмар материализует вашу самую страшную фобию! Критический ужас!',
            "ability_boss_chance": 0.11,
            "miss_damage_boss": 0.11,
            "miss_damage_boss_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Кошмар искажает пространство, и вы атакуете мимо.",
            "appearance_boss_chance": 0.20,

            "mobs_case_key": ("name_enemy_common", "enemy_boss_name"),

        },

        'dungeon_reward': dungeon_rewards[8],

    },

    9: {

        'name_dungeon': "Аудитория вечного экзамена",

        'description': "\n[Ряды парт, за которыми сидят сгорбленные,"
                       "\n полупрозрачные фигуры и пишут что-то на бесконечных листах.]",

        'enemies': {

            "name_enemy_common": 'Вечный Студент',
            "health_enemy_common": (200, 220),
            "damage_enemy_common": (34, 38),
            "reward_enemy_common": (34, 38),
            'protect_common': 4,
            "exp_enemy_common": 105,
            "crit_enemy_common": 0.14,
            "crit_enemy_common_desc": '\t\n>>>[КРИТ ПО ВАМ] Отчаяние студента выливается в яростный, точный удар! Крит!',
            "miss_damage_common": 0.12,
            "miss_damage_common_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Сгорбленная фигура студента внезапно падает на пол.",

            "enemy_boss_name": "Тьютор Ада",
            "enemy_boss_health": 450,
            "enemy_boss_damage": (50, 55),
            'protect_boss': 9,
            "enemy_boss_reward": 170,
            "enemy_boss_exp": 400,
            "enemy_boss_crit": 0.14,
            "enemy_boss_crit_desc": '\t\n>>>[КРИТ ПО ВАМ] Печать Тьютора обжигает вашу душу! Сокрушительный крит!',
            "ability_boss_chance": 0.11,
            "miss_damage_boss": 0.12,
            "miss_damage_boss_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Тьютор читает указ, и защитное поле останавливает вашу атаку",
            "appearance_boss_chance": 0.20,

            "mobs_case_key": ("name_enemy_common", "enemy_boss_name"),

        },

        'dungeon_reward': dungeon_rewards[9],

    },

    10: {

        'name_dungeon': "Кабинет Юлии Игоревны",

        'description': "\n[Вы замираете на пороге. Это – та самая комната."
                       " \nЗнакомая до боли, но теперь все в ней доведено до сюрреалистичного абсолюта."
                       " \nСтеллажи с конспектами и методичками уходят в заоблачную высь, теряясь где-то в районе потолка,"
                       " \nпревращенного в звездную карту из светящихся оценок."
                       " \nВ воздухе медленно плавают, как осенние листья, зачетки и листки с долгами."
                       " \nВоздух густой, настоянный на аромате старой бумаги, строгого парфюма и несданных вовремя работ."
                       " \n\nЗа массивным учительским столом, заваленным кипами тестов, сидит Она. Спиной к вам. "
                       " \nВ ее руке – красная ручка, которая с мертвой точки выводит замысловатые узоры на полях чьей-то судьбы."
                       " \nТишина стоит такая, что слышно, как муха пролетает где-то на 15 этаже."
                       " \nСтул с глухим скрипом поворачивается."
                       " \nИ вот ее взгляд, тот самый, от которого у целого потока студентов стынет кровь, устремляется на вас."
                       " \nНа губах играет едва заметная, но безжалостная улыбка."
                       '\n\n«Ну что же, — раздается голос, холодный и четкий, как формулировка в билете.'
                       ' \n— Я так понимаю, это ваша пересдача?'
                       ' \nЧто ж, давайте проверим, чему вы все-таки научились за время своего... академического отпуска».]',

        'enemies': {

            "enemy_boss_name": "ЮЛИЯ ИГОРЕВНА",
            "enemy_boss_health": 1500,
            "enemy_boss_damage": (70, 85),
            'protect_boss': 20,
            "enemy_boss_reward": 1000,
            "enemy_boss_exp": 2000,
            "enemy_boss_crit": 0.20,
            "enemy_boss_crit_desc": "\t\n>>>[КРИТ ПО ВАМ] Юлия Игоревна поднимает бровь."
                                    "\n'Это что за примитивный подход? На третьем курсе уже так не мыслят!'"
                                    "\n — ее замечание обрушивается на вас как удар молотка по неподготовленному домашнему заданию."
                                    "\n СОКРУШИТЕЛЬНЫЙ КРИТИЧЕСКИЙ УРОН!",
            "miss_damage_boss": 0.15,
            "miss_damage_boss_desc": "\t\n>>>[УВОРОТ ВРАГА ОТ УДАРА] Вы яростно атакуете,"
                                     "\nно Юлия Игоревна просто поправляет платок в нагрудном кармане"
                                     "\nи делает шаг в сторону с грацией кошки, обходящей лужу."
                                     "\n'Не туда, не туда... Сначала подумайте, потом действуйте'. Ваша атака проходит мимо!",
            "appearance_boss_chance": 0.20,
            "ability_boss_chance_total": 0.10,
            "ability_boss_chance_total_desc": "\n\t >>> [Активация способности - смертельная атака] <<< "
                                              "\nВнезапно ее глаза вспыхивают."
                                              "\n'А теперь — ВНЕПЛАНОВАЯ КОНТРОЛЬНАЯ! Без подготовки!"
                                              "\nНа всю оставшуюся жизнь!' Она щелкает пальцами,"
                                              "\nи пространство вокруг вас сжимается от ужаса перед чистым листом.",

            "mobs_case_key": ("name_enemy_common", "enemy_boss_name"),
            "ability_boss_chance_quest": 0.25,
            "ability_boss_chance_quest_desc": "\n\t >>> [Активация способности - Вопрос на засыпку] <<< "
                                              "\n'А сюда вы посмотреть не хотели?'"
                                              "\nЮлия Игоревна указывает красной ручкой на единственную строчку в методичке,"
                                              "\nкоторую вы благополучно проигнорировали."
                                              "\nОсознание собственной некомпетентности ранит больнее любого клинка.",

        },

        'dungeon_reward': dungeon_rewards[10],

    },

}

character = {}

trader = {}