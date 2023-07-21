import random
import sys

from PyQt6.QtWidgets import QApplication

from view import View
from model import Model


class Controller:
    '''Класс для управелния приложением'''

    def __init__(self):
        self._app = QApplication(sys.argv)
        self.view = View()

    def create_field(self):
        '''Метод, инициализирующий интерфейс'''

        self.view.label_1()
        self.view.label_2()
        self.view.button_1()
        self.view.button1.clicked.connect(self.erase_lines)
        self.view.button_2()
        self.view.button2.clicked.connect(self.remake_fild)
        self.view.button_3()
        self.view.button3.clicked.connect(self.make_cat)
        self.view.button_4()
        self.view.button4.clicked.connect(self.make_vampus)
        self.view.button_5()
        self.view.button5.clicked.connect(self.make_ghost)
        self.view.pictore_box_1()
        self.view.pictore_box_2()

    def make_cat(self):
        '''Метод для рассчета траектории кота'''

        Model.cat_coords.append([207, 192])

        tmp = [207, 192]
        current_position = 5

        Model.cat_trajectory.append(tuple([current_position, Model.traps_on_the_field[current_position-1]]))

        while True:
            direction = random.choice(Model.directions)

            if direction == "left":
                current_position -= 1
                tmp[0] = tmp[0] - 100
                if 60 < tmp[0] < 354:
                    Model.cat_coords.append(tuple(tmp))
                    Model.cat_trajectory.append(tuple([current_position, Model.traps_on_the_field[current_position-1]]))
                else:
                    tmp[0] = tmp[0] + 50
                    Model.cat_coords.append(tuple(tmp))
                    break

            elif direction == "right":
                current_position += 1
                tmp[0] = tmp[0] + 100
                if 60 < tmp[0] < 354:
                    Model.cat_coords.append(tuple(tmp))
                    Model.cat_trajectory.append(tuple([current_position, Model.traps_on_the_field[current_position-1]]))

                else:
                    tmp[0] = tmp[0] - 50
                    Model.cat_coords.append(tuple(tmp))
                    break

            elif direction == "up":
                current_position -= 3
                tmp[1] = tmp[1] - 100
                if 45 < tmp[1] < 339:
                    Model.cat_coords.append(tuple(tmp))
                    Model.cat_trajectory.append(tuple([current_position, Model.traps_on_the_field[current_position-1]]))

                else:
                    tmp[1] = tmp[1] + 50
                    Model.cat_coords.append(tuple(tmp))
                    break

            else:
                current_position += 3
                tmp[1] = tmp[1] + 100
                if 45 < tmp[1] < 339:
                    Model.cat_coords.append(tuple(tmp))
                    Model.cat_trajectory.append(tuple([current_position, Model.traps_on_the_field[current_position-1]]))
                else:
                    tmp[1] = tmp[1] - 50
                    Model.cat_coords.append(tuple(tmp))
                    break

        self.check_traps(creature="cat")
        self.view.button3.setEnabled(False)
        self.view.update()

    def make_vampus(self):
        '''Метод для рассчета траектории вампуса'''

        Model.vampus_coords.append([207, 192])
    
        current_position = 5

        Model.vampus_trajectory.append(tuple([current_position, Model.traps_on_the_field[current_position-1]]))
        tmp = [207, 192]
        while True:
            direction = random.choice(Model.directions)

            if direction == "left":
                current_position -= 1
                tmp[0] = tmp[0] - 100
                if 60 < tmp[0] < 354:
                    Model.vampus_coords.append(tuple(tmp))
                    Model.vampus_trajectory.append(tuple([current_position, Model.traps_on_the_field[current_position-1]]))

                else:
                    tmp[0] = tmp[0] + 50
                    Model.vampus_coords.append(tuple(tmp))

                    break

            elif direction == "right":
                current_position += 1
                tmp[0] = tmp[0] + 100
                if 60 < tmp[0] < 354:
                    Model.vampus_coords.append(tuple(tmp))
                    Model.vampus_trajectory.append(tuple([current_position, Model.traps_on_the_field[current_position-1]]))

                else:
                    tmp[0] = tmp[0] - 50
                    Model.vampus_coords.append(tuple(tmp))

                    break

            elif direction == "up":
                current_position -= 3
                tmp[1] = tmp[1] - 100
                if 45 < tmp[1] < 339:
                    Model.vampus_coords.append(tuple(tmp))
                    Model.vampus_trajectory.append(tuple([current_position, Model.traps_on_the_field[current_position-1]]))

                else:
                    tmp[1] = tmp[1] + 50
                    Model.vampus_coords.append(tuple(tmp))

                    break

            else:
                current_position += 3
                tmp[1] = tmp[1] + 100
                if 45 < tmp[1] < 339:
                    Model.vampus_coords.append(tuple(tmp))
                    Model.vampus_trajectory.append(tuple([current_position, Model.traps_on_the_field[current_position-1]]))

                else:
                    tmp[1] = tmp[1] - 50
                    Model.vampus_coords.append(tuple(tmp))

                    break

        self.check_traps(creature="vampus")
        self.view.button4.setEnabled(False)
        self.view.update()

    def make_ghost(self):
        '''Метод для рассчета траектории приведения'''

        Model.ghost_coords.append([207, 192])

        current_position = 5

        Model.ghost_trajectory.append(tuple([current_position, Model.traps_on_the_field[current_position-1]]))

        tmp = [207, 192]
        while True:
            direction = random.choice(Model.directions)

            if direction == "left":
                current_position -= 1
                tmp[0] = tmp[0] - 100
                if 60 < tmp[0] < 354:
                    Model.ghost_coords.append(tuple(tmp))
                    Model.ghost_trajectory.append(tuple([current_position, Model.traps_on_the_field[current_position-1]]))

                else:
                    tmp[0] = tmp[0] + 50
                    Model.ghost_coords.append(tuple(tmp))
                    

                    break

            elif direction == "right":
                current_position += 1
                tmp[0] = tmp[0] + 100
                if 60 < tmp[0] < 354:
                    Model.ghost_coords.append(tuple(tmp))
                    Model.ghost_trajectory.append(tuple([current_position, Model.traps_on_the_field[current_position-1]]))

                else:
                    tmp[0] = tmp[0] - 50
                    Model.ghost_coords.append(tuple(tmp))

                    break

            elif direction == "up":
                current_position -= 3
                tmp[1] = tmp[1] - 100
                if 45 < tmp[1] < 339:
                    Model.ghost_coords.append(tuple(tmp))
                    Model.ghost_trajectory.append(tuple([current_position, Model.traps_on_the_field[current_position-1]]))

                else:
                    tmp[1] = tmp[1] + 50
                    Model.ghost_coords.append(tuple(tmp))

                    break

            else:
                tmp[1] = tmp[1] + 100
                current_position += 3
                if 45 < tmp[1] < 339:
                    Model.ghost_coords.append(tuple(tmp))
                    Model.ghost_trajectory.append(tuple([current_position, Model.traps_on_the_field[current_position-1]]))

                else:
                    tmp[1] = tmp[1] - 50
                    Model.ghost_coords.append(tuple(tmp))

                    break

        self.check_traps(creature="ghost")
        self.view.button5.setEnabled(False)
        self.view.update()

    def check_traps(self, creature):
        '''Метод, проверяющий какие ловушки сработали'''

        if creature == "cat":
            cells_list = [i[0] for i in Model.cat_trajectory]
            for step in Model.cat_trajectory:
                if cells_list.count(step[0]) >= 2 and step[1] != "none":
                    Model.triggered_traps.append(step[0])
        elif creature == "vampus":
            for step in Model.vampus_trajectory:
                if step[1] == "rope":
                    Model.triggered_traps.append(step[0])
        else:
            for step in Model.ghost_trajectory:
                if step[1] == "detector":
                    Model.triggered_traps.append(step[0])

    def erase_lines(self):
        '''Метод для удаления линий с поля'''
        
        Model.cat_coords = []
        Model.vampus_coords = []
        Model.ghost_coords = []
        Model.triggered_traps = []
        Model.cat_coords = []
        Model.cat_trajectory = []
        Model.vampus_trajectory = []
        Model.ghost_trajectory = []
        self.view.button3.setEnabled(True)
        self.view.button4.setEnabled(True)
        self.view.button5.setEnabled(True)
        self.view.update()

    def remake_fild(self):
        '''Метод для перетосовки ловушек на поле'''

        Model.cat_coords = []
        Model.vampus_coords = []
        Model.ghost_coords = []
        Model.triggered_traps = []
        Model.cat_coords = []
        Model.cat_trajectory = []
        Model.vampus_trajectory = []
        Model.ghost_trajectory = []
        Model.update_field = True
        self.view.button3.setEnabled(True)
        self.view.button4.setEnabled(True)
        self.view.button5.setEnabled(True)
        self.view.update()

    def run(self):
        self.create_field()
        self.view.show()
        return self._app.exec()

if __name__ == "__main__":
    c = Controller()
    c.run()
