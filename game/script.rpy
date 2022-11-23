﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define p = Character('Павел', color="#FEECB6",who_outlines=[ (3, "#592116") ], what_outlines=[ (2, "#466743") ], what_color="#BCE3B9",) # variable value

# Звуки и музыка
define audio.alarm = "audio/sounds/alarm.mp3"
define audio.wholegame = "audio/music/wholegame.mp3"

label splashscreen:
    $ renpy.movie_cutscene('video/intro.ogv')
    return

# Игра начинается здесь:
label start:

    play music wholegame fadeout 2.0 fadein 2.0

    scene bg transition
    with fade
    
    "Я давно хотел работать с техникой, еще с малых лет."
    
    scene bg radio
    with fade

    "Помню дед при мне пытался чинить свое старенькое радио советского производства. А я помогал. Ну как помогал, пытался светить в нужное место динамо фонарем, то и дело роняя его из-за усталости кисти."

    "{size=-2}Помимо ругани в его словах мелькали интересные подробности работы сие дивного устройства. А я слушал и запоминал, мечтал тоже встать когда-то у какого-нибудь навороченного аппарата и нажимать светящиеся кнопки с умным видом и крестовой отверткой за пазухой.{/size}"

    scene bg computer off
    with fade

    "{size=-2}В какой-то степени моя мечта осуществилась. После горы переломанных бытовых приборов и множества часов стояния в углу, родители сжалились и купили мне компьютер, взяв с меня обещание, что я его точно не разберу по винтикам к концу недели.{/size}"
    
    scene bg computer loading
    with fade

    p "Nothing"

    "Вообще они купили мне его для учебы. Но об учебе я в тот момент не думал."
    
    scene bg buying a disc
    with fade

    "Первым делом я разбил свою маленькую копилку, соскреб все свои пожитки в кучу и пошел в магазин дисков."

    scene bg computer heroes three
    with fade

    "Счастья моему не было придела, когда я тайком от сидящего на диване отца и готовящей ужин на кухне матери пронес под курткой свой первый диск с Третьими героями."

    scene bg thinking
    with fade

    "{size=-2}Вдоволь наигравшись, я в силу своего любознательного характера начал задумываться: если компьютер работает из-за микросхем и транзисторов и выполняет четко указанную цель, как могут так волшебно двигаться эти картинки на экране?{/size}"
    
    "Ведь не проводов, ни лампочек в диске не было. Так началась моя вторая глава изучения компьютера – неосязаемая; понять как работает все внутри, а главное – почему."
    
    window hide

    scene bg chapter1
    with fade

    pause

    $ persistent.ending1 = True

    play sound alarm fadeout 1.0 fadein 1.0
    
    $ persistent.ending2 = True
   

    return