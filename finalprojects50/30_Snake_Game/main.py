# snake_game.py

import curses
import random
import time

class Snake:
    def __init__(self, win):
        self.body = [[10, 10], [10, 9], [10, 8]]
        self.direction = curses.KEY_RIGHT
        self.win = win

    def move(self, food):
        head = self.body[0][:]
        if self.direction == curses.KEY_UP:
            head[0] -= 1
        elif self.direction == curses.KEY_DOWN:
            head[0] += 1
        elif self.direction == curses.KEY_LEFT:
            head[1] -= 1
        elif self.direction == curses.KEY_RIGHT:
            head[1] += 1

        self.body.insert(0, head)
        if head == food:
            return True  # Food eaten
        else:
            self.body.pop()
            return False

    def change_direction(self, new_direction):
        # Prevent 180-degree turns
        opposites = {
            curses.KEY_UP: curses.KEY_DOWN,
            curses.KEY_DOWN: curses.KEY_UP,
            curses.KEY_LEFT: curses.KEY_RIGHT,
            curses.KEY_RIGHT: curses.KEY_LEFT
        }
        if new_direction != opposites.get(self.direction, None):
            self.direction = new_direction

    def check_collision(self, height, width):
        head = self.body[0]
        return (
            head in self.body[1:] or
            head[0] in [0, height-1] or
            head[1] in [0, width-1]
        )

    def draw(self):
        for segment in self.body:
            self.win.addch(segment[0], segment[1], '#')

def food_generator(height, width, snake_body):
    while True:
        food = [random.randint(1, height - 2), random.randint(1, width - 2)]
        if food not in snake_body:
            yield food

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    height, width = 20, 60
    win = curses.newwin(height, width, 0, 0)
    win.border()

    snake = Snake(win)
    food_gen = food_generator(height, width, snake.body)
    food = next(food_gen)
    score = 0

    win.addch(food[0], food[1], '*')

    while True:
        win.clear()
        win.border()
        win.addstr(0, 2, f'Score: {score}')
        snake.draw()
        win.addch(food[0], food[1], '*')
        win.refresh()

        try:
            key = win.getch()
            if key != -1:
                snake.change_direction(key)

            if snake.move(food):
                score += 1
                food = next(food_gen)

            if snake.check_collision(height, width):
                msg = f"Game Over! Final Score: {score}"
                win.addstr(height // 2, (width - len(msg)) // 2, msg)
                win.refresh()
                time.sleep(2)
                break
        except Exception as e:
            break

if __name__ == "__main__":
    curses.wrapper(main)

