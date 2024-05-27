from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QFormLayout, QWidget, QComboBox, QMessageBox)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import random

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle('График')
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)

        cental_widget = QWidget()
        layout = QFormLayout()
        cental_widget.setLayout(layout)

        layout.addWidget(self.canvas)

        self.setCentralWidget(cental_widget)

        self.plot_button1 = QPushButton('Нарисовать график')
        self.plot_button1.clicked.connect(self.plot_data)

        self.check_point = QPushButton('Проверить точку')
        self.check_point.clicked.connect(self.proverka)

        self.random_point = QPushButton('Случайная точка')
        self.random_point.clicked.connect(self.random_points)

        self.range_label = QLabel('Диапазон:')
        self.range_start_input = QLineEdit('0')
        self.range_end_input = QLineEdit('1')
        self.range_start_input.setFixedSize(50, 25)
        self.range_end_input.setFixedSize(50,25)

        self.point_range = QLabel('Координаты точки')
        self.start_point_range = QLineEdit()
        self.end_point_range = QLineEdit()
        self.start_point_range.setFixedSize(50, 25)
        self.end_point_range.setFixedSize(50, 25)

        self.add_function_button1 = QPushButton('Добавить функцию')
        self.function_input1 = QLineEdit(' Введите функцию для добавление в список ')
        self.function_label1 = QLabel('Список функций')
        self.function_widget1 = QComboBox()
        self.function_widget1.addItems(['x', '2*x', 'x**2', 'x**3'])
        self.add_function_button1.clicked.connect(self.add_function)

        self.hl_widget1 = QComboBox()
        self.hl_widget1.addItems(['ВЫШЕ', 'НИЖЕ'])

        self.clear_button = QPushButton('Очистить график')
        self.clear_button.clicked.connect(self.clear_plot)

        self.error_message = QMessageBox()
        self.error_message.setText("Функция введена неверно!")
        self.error_message.setWindowTitle('Ошибка!')
        self.list_vector = []
        self.hl_vector = []

        layout.addRow(self.function_label1)
        layout.addWidget(self.function_widget1)
        layout.addWidget(self.plot_button1)
        layout.addWidget(self.hl_widget1)
        layout.addRow(self.range_label)
        layout.addRow(self.range_start_input, self.range_end_input)
        layout.addRow(self.point_range)
        layout.addRow(self.start_point_range, self.end_point_range)
        layout.addWidget(self.check_point)
        layout.addWidget(self.clear_button)
        layout.addRow(self.add_function_button1, self.function_input1)
        layout.addWidget(self.random_point)

    def vectors(self):
        try:
            expression = self.function_widget1.currentText()
        except NameError:
            expression = 'x'

        try:
            range_start = float(self.range_start_input.text())
            range_end = float(self.range_end_input.text())
        except ValueError:
            range_start = 0
            range_end = 1
        functions = {}
        try:
            exec(f'def f(x): return {expression}', functions)
            x = np.linspace(range_start, range_end)
            function = functions['f']
            y = [function(value) for value in x]
            return x, y

        except NameError:
            self.error_message.show()
            return 0
        except SyntaxError:
            self.error_message.show()
            return 0

    def plot_data(self):
        if self.vectors() != 0:
            x, y = self.vectors()
            axes = plt.subplot()
            axes.plot(x, y)
            plt.grid(True)
            plt.xlabel('x')
            plt.ylabel('y')
            expression = self.function_widget1.currentText()
            self.list_vector.append(expression)
            hl = self.hl_widget1.currentText()
            self.hl_vector.append(hl)
            self.centralWidget().layout().itemAt(0).widget().draw()

    def check_points(self):
        y_point_str = self.end_point_range.text()
        x_point_str = self.start_point_range.text()
        functions = {}
        cnt = 0
        for i in range(len(self.list_vector)):
            expression = self.list_vector[i]
            try:
                exec(f'def f(x): return {expression}', functions)
                function = functions['f']
                x_point = float(x_point_str)
                func = function(float(x_point))
                y_point = float(y_point_str)
            except NameError:
                return False
            except SyntaxError:
                return False

            hl = self.hl_vector[i]
            if hl == 'ВЫШЕ':
                if y_point >= func:
                    cnt += 1
            else:
                if y_point <= func:
                    cnt += 1

        if cnt == len(self.hl_vector):
            return True
        else:
            return False

    def proverka(self):
        g = self.check_points()

        x_point = float(self.start_point_range.text())
        y_point = float(self.end_point_range.text())

        if g != 0:
            plt.scatter(x_point, y_point, color='green')
        else:
            plt.scatter(x_point, y_point, color='red')

        self.canvas.draw()

    def clear_plot(self):
        for ax in self.fig.axes:
            ax.clear()
        plt.grid(True)
        self.canvas.draw()
        self.hl_vector = []
        self.list_vector = []

    def add_function(self):
        text_x = self.function_input1.text()
        self.function_widget1.addItems([text_x])

    def random_points(self):
        a1 = float(self.range_start_input.text())
        a2 = float(self.range_end_input.text())
        a = str(random.uniform(a1, a2))[0:4]
        b = str(random.uniform(a1, a2))[0:4]
        self.start_point_range.setText(a)
        self.end_point_range.setText(b)
        self.proverka()

app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec()

