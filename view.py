import random

from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton
from PyQt6.QtGui import QPixmap, QPainter, QPen, QBrush
from PyQt6.QtCore import Qt

from model import Model


class View(QMainWindow):
    '''Класс для создания объекта окна приложения'''

    def __init__(self):
        super(View, self).__init__()

        self.setGeometry(800, 200, 417, 684)

        self.setWindowTitle("My App")

        self.to_update = False

    def label_1(self):
        self.label1 = QLabel(self)
        self.label1.setText(" - Веревочка с колокольчиком")
        self.label1.move(102, 366)
        self.label1.adjustSize()

    def label_2(self):
        self.label2 = QLabel(self)
        self.label2.setText(" - Детектор протоплазмы")
        self.label2.move(102, 405)
        self.label2.adjustSize()

    def button_1(self):
        self.button1 = QPushButton(self)
        self.button1.setText("Стереть траектории")
        self.button1.move(60, 452)
        self.button1.setFixedSize(294, 27)
    
    def button_2(self):
        self.button2 = QPushButton(self)
        self.button2.setText("Перетасовать ловушки")
        self.button2.move(60, 485)
        self.button2.setFixedSize(294, 27)
        

    def button_3(self):
        self.button3 = QPushButton(self)
        self.button3.setStyleSheet('QPushButton {color: blue;}')
        self.button3.setText("Запустить кошку")
        self.button3.move(60, 543)
        self.button3.setFixedSize(294, 27)

    def button_4(self):
        self.button4 = QPushButton(self)
        self.button4.setStyleSheet('QPushButton {color: green;}')
        self.button4.setText("Запустить вампуса")
        self.button4.move(60, 576)
        self.button4.setFixedSize(294, 27)

    def button_5(self):
        self.button5 = QPushButton(self)
        self.button5.setStyleSheet('QPushButton {color: yellow;}')
        self.button5.setText("Запустить преведение")
        self.button5.move(60, 609)
        self.button5.setFixedSize(294, 27)

    def pictore_box_1(self):
        self.labelImage1 = QLabel(self)
        self.pixmap1 = QPixmap("./rope.png")
        self.labelImage1.setGeometry(60, 355, 36, 35)
        self.pixmap1 = self.pixmap1.scaled(36, 35)
        self.labelImage1.setPixmap(self.pixmap1)

    def pictore_box_2(self):
        self.labelImage2 = QLabel(self)
        self.pixmap2 = QPixmap("./detector.png")
        self.labelImage2.setGeometry(60, 394, 36, 35)
        self.pixmap2 = self.pixmap2.scaled(36, 35)
        self.labelImage2.setPixmap(self.pixmap2)

    def pictore_box_3(self, picutre, qp): #1
        self.pixmap3 = QPixmap(f"./{picutre}.png")
        self.pixmap3 = self.pixmap3.scaled(100, 100)
        qp.drawPixmap(60, 45, 100, 100, self.pixmap3)

    def pictore_box_4(self, picutre, qp): #2
        self.pixmap4 = QPixmap(f"./{picutre}.png")
        self.pixmap4 = self.pixmap4.scaled(100, 100)
        qp.drawPixmap(157, 45, 100, 100, self.pixmap4)

    def pictore_box_5(self, picutre, qp): #3
        self.pixmap5 = QPixmap(f"./{picutre}.png")
        self.pixmap6 = self.pixmap5.scaled(100, 100)
        qp.drawPixmap(254, 45, 100, 100, self.pixmap5)

    def pictore_box_6(self, picutre, qp):#4
        self.pixmap6 = QPixmap(f"./{picutre}.png")
        self.pixmap6 = self.pixmap6.scaled(100, 100)
        qp.drawPixmap(60, 142, 100, 100, self.pixmap6)
    
    def pictore_box_7(self, picutre, qp): #5
        self.pixmap7 = QPixmap(f"./{picutre}.png")
        self.pixmap7 = self.pixmap7.scaled(100, 100)
        qp.drawPixmap(157, 142, 100, 100, self.pixmap7)

    def pictore_box_8(self, picutre, qp): #6
        self.pixmap8 = QPixmap(f"./{picutre}.png")
        self.pixmap8 = self.pixmap8.scaled(100, 100)
        qp.drawPixmap(254, 142, 100, 100, self.pixmap8)
    
    def pictore_box_9(self, picutre, qp): #7
        self.pixmap9 = QPixmap(f"./{picutre}.png")
        self.pixmap9 = self.pixmap9.scaled(100, 100)
        qp.drawPixmap(60, 239, 100, 100, self.pixmap9)

    def pictore_box_10(self, picutre, qp): #8
        self.pixmap10 = QPixmap(f"./{picutre}.png")
        self.pixmap10 = self.pixmap10.scaled(100, 100)
        qp.drawPixmap(157, 239, 100, 100, self.pixmap10)

    def pictore_box_11(self, picutre, qp): #9
        self.pixmap11 = QPixmap(f"./{picutre}.png")
        self.pixmap11 = self.pixmap11.scaled(100, 100)
        qp.drawPixmap(254, 239, 100, 100, self.pixmap11)


    def paintEvent(self, e):
        '''Метод для создания графики'''

        self.qp = QPainter()
        self.qp.begin(self)
        self.create_field()
        self.draw_traps()
        self.draw_cat(Model.cat_coords)
        self.draw_vampus(Model.vampus_coords)
        self.draw_ghost(Model.ghost_coords)
        self.qp.end()

    def create_field(self):
        '''Метод, генерирующий основное поле'''

        if Model.update_field:
            random.shuffle(Model.traps_on_the_field)

        for idx, value in enumerate(Model.traps_on_the_field, start=3):
                eval(f"self.pictore_box_{idx}")(value, self.qp)

        Model.update_field = False

    def draw_cat(self, coords):
        '''Метод, отображающий траекторию кота'''

        if coords:
            pen = QPen(Qt.GlobalColor.blue, 7, Qt.PenStyle.SolidLine)
            
            first_point, second_point = 0, 1
            while second_point <= len(coords) - 1:
                first_coord = coords[first_point]
                second_coord = coords[second_point]

                self.qp.setPen(pen)
                self.qp.drawLine(first_coord[0], first_coord[1], second_coord[0], second_coord[1])
                first_point += 1
                second_point += 1
    
    def draw_vampus(self, coords):
        '''Метод, отображающий траекторию вампуса'''

        if coords:
            pen = QPen(Qt.GlobalColor.green, 7, Qt.PenStyle.SolidLine)
            
            first_point, second_point = 0, 1
            while second_point <= len(coords) - 1:
                first_coord = coords[first_point]
                second_coord = coords[second_point]
                self.qp.setPen(pen)
                self.qp.drawLine(first_coord[0], first_coord[1], second_coord[0], second_coord[1])
                first_point += 1
                second_point += 1

    def draw_ghost(self, coords):
        '''Метод, отображающий траекторию приведения'''

        if coords:
            pen = QPen(Qt.GlobalColor.yellow, 7, Qt.PenStyle.SolidLine)
        
            first_point, second_point = 0, 1
            while second_point <= len(coords) - 1:
                first_coord = coords[first_point]
                second_coord = coords[second_point]
                self.qp.setPen(pen)
                self.qp.drawLine(first_coord[0], first_coord[1], second_coord[0], second_coord[1])
                first_point += 1
                second_point += 1
    
    def draw_traps(self):
        '''Метод, отображающий сработавшие ловушки'''

        pen = QPen(Qt.GlobalColor.red, 7, Qt.PenStyle.SolidLine)
        self.qp.setPen(pen)
        brush = QBrush()
        self.qp.setBrush(brush)
        for trap in Model.triggered_traps:
            cell = Model.cells_coords[trap]
            self.qp.drawRect(cell[0], cell[1], 100, 100)
