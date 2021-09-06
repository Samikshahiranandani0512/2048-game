import pygame
import sys
import random

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
yellow = (252, 247, 135)
black = (0, 0, 0)
grey = (117, 117, 117)
color2 = (255, 223, 211)
color4 = (254, 200, 216)
color8 = (210, 145, 188)
color16 = (149, 125, 173)
color32 = (224, 187, 228)
othercolor = yellow


class Board_2048(object):
    """
    This is the main game class which sets the board and updates the
    configuration based on past configuration and new user input.
    """

    def __init__(self):
        self.grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0]]
        self.state = "INITIALIZED"
        self.score = 0
        print(self.grid)

    def create_rect(self, s, center, font_color, box_color):
        text = self.font.render(s, True, font_color, box_color)
        textRect = text.get_rect()
        textRect.center = center
        self.display_surface.blit(text, textRect)

    def draw(self):

        colors = {2: color2, 4: color4, 8: color8,
                  16: color16, 32: color32, 64: othercolor, 128: othercolor, 256: othercolor, 512: othercolor}

        # assigning values to X and Y variable
        X = 400
        Y = 400

        # create the display surface object
        # of specific dimension..e(X, Y).
        self.display_surface = pygame.display.set_mode((X, Y))

        # set the pygame window name
        pygame.display.set_caption('2048')

        self.font = pygame.font.Font('freesansbold.ttf', 32)

        while True:

            # completely fill the surface object with grey color
            self.display_surface.fill(grey)

            self.font = pygame.font.Font('freesansbold.ttf', 16)

            self.create_rect("Join the numbers and get to the 2048 tile!",
                             (200, 80), black, grey)
            self.create_rect("Press arrow keys up, down, right, left",
                             (200, 100), black, grey)

            self.font = pygame.font.Font('freesansbold.ttf', 32)

            self.create_rect(" 2048 ", (70, 50), black, yellow)

            self.create_rect(" Score : " + str(self.score) + " ",
                             (240, 50), black, yellow)

            x_start = 125
            y_start = 100
            positions = []

            for x in range(150, 350, 50):
                row = []
                for y in range(125, 300, 50):
                    row.append((y, x))
                positions.append(row)

            for row in range(len(self.grid)):
                for col in range(len(self.grid[0])):
                    if self.grid[row][col] != 0:
                        self.create_rect(
                            (f"{str(self.grid[row][col]).center(4)}"), positions[row][col], black, colors[self.grid[row][col]])

            for event in pygame.event.get():

                # if event object type is QUIT
                # then quitting the pygame
                # and program both.
                if event.type == pygame.QUIT:

                    # deactivates the pygame library
                    pygame.quit()

                    # quit the program.
                    quit()

                    # Draws the surface object to the screen.
            pygame.display.update()
            break

    def add_new_tile(self):
        # make a list of all empty spaces
        # choose one at random to add randomly a 2 or a 4
        empty = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 0:
                    empty.append((i, j))

        if len(empty) == 0:
            self.state = "FINISHED"
            return

        random_index = (random.randint(0, len(empty) - 1))

        position = empty[random_index]

        random_number = random.randint(0, 1)

        if random_number == 0:
            value = 2
        else:
            value = 4
        self.grid[position[0]][position[1]] = value

    def is_valid_move(self):
        pass

    def update_grid(self):
        pass

    def handle_up(self):
        """
        Changes board state after the player has pressed up key
        """

        # cover gaps

        for col in range(len(self.grid)):
            column = []
            for row in range(len(self.grid)):
                if self.grid[row][col] != 0:
                    column.append(self.grid[row][col])
            print("Column", column)
            print("col,", col)
            for row in range(len(column)):
                self.grid[row][col] = column[row]
            for row in range(len(self.grid) - len(column)):
                self.grid[row + len(column)][col] = 0
            print(self.grid)

        # combining numbers if seen

        for col in range(len(self.grid)):
            column = []
            for row in range(len(self.grid) - 1):
                # starting from up
                if self.grid[row][col] == self.grid[row + 1][col] and self.grid[row][col] != 0:
                    self.grid[row + 1][col] = 0
                    self.grid[row][col] *= 2
                    self.score += 1
                    print("Increasing score")
                    break
        # looking at each column
        for col in range(len(self.grid)):
            column = []
            for row in range(len(self.grid)):
                if self.grid[row][col] != 0:
                    column.append(self.grid[row][col])
            print("Column", column)
            print("col,", col)
            for row in range(len(column)):
                self.grid[row][col] = column[row]
            for row in range(len(self.grid) - len(column)):
                self.grid[row + len(column)][col] = 0
            print(self.grid)

    def handle_down(self):
        """
        Changes board state after the player has pressed up key
        """

        # cover gaps

        for col in range(len(self.grid)):
            column = []
            for row in range(len(self.grid)):
                if self.grid[row][col] != 0:
                    column.append(self.grid[row][col])
            offset = len(self.grid) - len(column)
            for row in range(len(column)):
                self.grid[row + offset][col] = column[row]
            for row in range(offset):
                self.grid[row][col] = 0

        # combining numbers if seen

        for col in range(len(self.grid)):
            column = []
            for row in range(len(self.grid) - 1):
                # starting from down
                row_num = len(self.grid) - 1 - row
                if self.grid[row_num][col] == self.grid[row_num - 1][col] and self.grid[row_num][col] != 0:
                    self.grid[row_num][col] = 0
                    self.grid[row_num - 1][col] *= 2
                    self.score += 1
                    break

        # cover gaps

        for col in range(len(self.grid)):
            column = []
            for row in range(len(self.grid)):
                if self.grid[row][col] != 0:
                    column.append(self.grid[row][col])
            offset = len(self.grid) - len(column)
            for row in range(len(column)):
                self.grid[row + offset][col] = column[row]
            for row in range(offset):
                self.grid[row][col] = 0

    def handle_right(self):
        """
        Changes board state after the player has pressed up key
        """

        # cover gaps

        for row in range(len(self.grid)):
            full_row = []
            for col in range(len(self.grid)):
                if self.grid[row][col] != 0:
                    full_row.append(self.grid[row][col])
            offset = len(self.grid) - len(full_row)
            for col in range(len(full_row)):
                self.grid[row][col + offset] = full_row[col]
            for col in range(offset):
                self.grid[row][col] = 0

        # combining numbers if seen

        for row in range(len(self.grid)):
            for col in range(len(self.grid) - 1):
                # starting from right
                col_num = len(self.grid) - 1 - col
                if self.grid[row][col_num] == self.grid[row][col_num - 1] and self.grid[row][col_num] != 0:
                    self.grid[row][col_num] = 0
                    self.grid[row][col_num - 1] *= 2
                    print(self.grid)
                    self.score += 1
                    break

        # cover gaps

        for row in range(len(self.grid)):
            full_row = []
            for col in range(len(self.grid)):
                if self.grid[row][col] != 0:
                    full_row.append(self.grid[row][col])
            offset = len(self.grid) - len(full_row)
            for col in range(len(full_row)):
                self.grid[row][col + offset] = full_row[col]
            for col in range(offset):
                self.grid[row][col] = 0

    def handle_left(self):
        """
        Changes board state after the player has pressed left key
        """

        # cover gaps

        for row in range(len(self.grid)):
            full_row = []
            for col in range(len(self.grid)):
                if self.grid[row][col] != 0:
                    full_row.append(self.grid[row][col])
            offset = len(self.grid) - len(full_row)
            for col in range(len(full_row)):
                self.grid[row][col] = full_row[col]
            for col in range(offset):
                self.grid[row][col + len(full_row)] = 0

        # combining numbers if seen

        for row in range(len(self.grid)):
            for col in range(len(self.grid) - 1):
                # starting from left
                if self.grid[row][col] == self.grid[row][col + 1] and self.grid[row][col] != 0:
                    self.grid[row][col] = 0
                    self.grid[row][col + 1] *= 2
                    print(self.grid)
                    self.score += 1
                    break

        # cover gaps

        for row in range(len(self.grid)):
            full_row = []
            for col in range(len(self.grid)):
                if self.grid[row][col] != 0:
                    full_row.append(self.grid[row][col])
            offset = len(self.grid) - len(full_row)
            for col in range(len(full_row)):
                self.grid[row][col] = full_row[col]
            for col in range(offset):
                self.grid[row][col + len(full_row)] = 0

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print("Key Down")
                if event.key == pygame.K_UP:
                    self.handle_up()
                    print(self.grid)
                elif event.key == pygame.K_DOWN:
                    self.handle_down()
                    print("Caught down")
                elif event.key == pygame.K_LEFT:
                    self.handle_left()
                    print("Caught left")
                elif event.key == pygame.K_RIGHT:
                    self.handle_right()
                    print("Caught right")
                self.add_new_tile()

    def draw_gameover(self):
        self.create_rect("Game Over", (200, 200), black, grey)


def main():
    pygame.init()

    clock = pygame.time.Clock()

    board = Board_2048()

    while (True):
        clock.tick(1)
        board.handle_keys()
        board.draw()
        if board.state == "FINISHED":
            print("finished")
            while (True):
                board.draw_gameover()
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()


main()
