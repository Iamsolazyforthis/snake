# Поворот на лево

def on_button_pressed_a():
    snake.turn(Direction.RIGHT, 270)
input.on_button_pressed(Button.A, on_button_pressed_a)

# Поворот на право

def on_button_pressed_b():
    snake.turn(Direction.RIGHT, 90)
input.on_button_pressed(Button.B, on_button_pressed_b)

# Приветствие и спавн змейки
apple: game.LedSprite = None
snake: game.LedSprite = None
basic.show_string("SNAKE")
basic.clear_screen()
basic.pause(200)
snake = game.create_sprite(2, 2)
# Спавн яблок

def on_forever():
    global apple
    for index in range(1):
        apple = game.create_sprite(randint(0, 4), randint(0, 4))
        basic.pause(6000)
basic.forever(on_forever)

# Передвижение Змейки

def on_forever2():
    for index2 in range(1):
        snake.move(1)
        basic.pause(500)
basic.forever(on_forever2)

def on_forever3():
    if snake.is_touching_edge():
        game.game_over()
        basic.clear_screen()
        basic.show_string("GAME OVER")
        basic.pause(1000)
        basic.clear_screen()
        basic.show_string("" + str((game.score())))
basic.forever(on_forever3)

# "Если Змейка касается яблока, убрать яблоко и дать одно очко"

def on_forever4():
    if snake.is_touching(apple):
        apple.delete()
        game.add_score(1)
        snake.change(LedSpriteProperty.X, 1)
basic.forever(on_forever4)
