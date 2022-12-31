init python:

    g = Gallery()

    # Указываем картинку для закрытых постеров.
    g.locked_button = "images/gallery/lock.jpg"

    # Добавляем кнопку и задаём ей название.
    g.button("ending1")

    # Условие, при котором кнопка активируется.
    g.condition("persistent.ending1")

    # картинка, которая отображается при нажатии на кнопку.
    g.image("chapter1")

    # глава 2
    g.button("ending2")
    g.condition("persistent.ending2")
    g.image("chapter2")

    # глава 3
    g.button("ending3")
    g.condition("persistent.ending3")
    g.image("chapter3")

    # глава 4
    g.button("ending4")
    g.condition("persistent.ending4")
    g.image("chapter4")

init:
    #музыка главного меню
    define main_menu = "/audio/music/main_menu.mp3"

    #стиль текста для гиперссылок
    style hyperlink_text:
        bold True
        underline False
        size gui.text_size
        idle_color "#7A5660"
        hover_color "#E0A366"
    
    #стиль заголовка в разделе об игре
    style about_text:
        line_spacing -15
        size gui.text_size
    style about_label is gui_label
    style about_label_text:
        size 50
        bold True
        idle_color "#7A5660"
        hover_color "#7A5660"
    
    #стиль названия клавиш в разделе помощь
    style help_label_text:
        bold True
        idle_color "#7A5660"
        hover_color "#7A5660"

    style slot_time_text:
        line_spacing 30

init python:
    define.move_transitions("ease", 0.7)