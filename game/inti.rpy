init python:

    g = Gallery()

    # Указываем картинку для закрытых постеров.

    g.locked_button = "images/gallery/lock.jpg"

    # Добавляем кнопку и задаём ей название.

    g.button("ending1")

    # Условие, при котором кнопка активируется.

    g.condition("persistent.ending1")

    # картинка, который отображается при нажатии на кнопку.

    g.image("chapter1")

    # глава 2
    g.button("ending2")
    g.condition("persistent.ending2")
    g.image("chapter2")

init:
    define main_menu = "/audio/music/main_menu.mp3"