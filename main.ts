// Поворот на лево
input.onButtonPressed(Button.A, function () {
    snake.turn(Direction.Right, 270)
})
// Поворот на право
input.onButtonPressed(Button.B, function () {
    snake.turn(Direction.Right, 90)
})
// Приветствие и спавн змейки
let apple: game.LedSprite = null
let snake: game.LedSprite = null
basic.showString("SNAKE")
basic.clearScreen()
basic.pause(200)
snake = game.createSprite(2, 2)
// Спавн яблок
basic.forever(function () {
    for (let index = 0; index < 1; index++) {
        apple = game.createSprite(randint(0, 4), randint(0, 4))
        basic.pause(6000)
    }
})
// "Если Змейка касается яблока, убрать яблоко и дать одно очко"
basic.forever(function () {
    if (snake.isTouching(apple)) {
        apple.delete()
        game.addScore(1)
        snake.change(LedSpriteProperty.X, 1)
    }
})
// Конец игры и подсчёт очков
basic.forever(function () {
    if (snake.isTouchingEdge()) {
        game.gameOver()
        basic.clearScreen()
        basic.showString("GAME OVER")
        basic.pause(1000)
        basic.clearScreen()
        basic.showString("" + (game.score()))
    }
})
// Передвижение Змейки
basic.forever(function () {
    for (let index = 0; index < 1; index++) {
        snake.move(1)
        basic.pause(500)
    }
})
