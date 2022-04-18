from sys import argv, exit

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

debug = False

min_values = [
    1784.48,
    2.44,
    38.67,
    15.7,
    179.37,
    0.6,
    64.05,
    1036.86,
    63.69,
    0,
    0.04,
    27.27
]


class Application:
    def __init__(self):
        self.core = QApplication(argv)
        self.window = MainWindow()
        self.mainFunction = lambda x: 0

    def start(self):
        self.window.show()
        self.window.Start_Button.clicked.connect(lambda: self.startProcess())

    def startProcess(self):

        def check_values(d: dict):
            for v1, v2 in zip(min_values, d.values()):
                if v2 < v1 and not debug:
                    return False
            return True

        setup = self.getUserSetup()

        if check_values(setup):
            result = self.mainFunction(setup)
            self.window.result_Label.setText(str(result))
        else:
            QMessageBox.warning(self.window, "Ошибка ввода", "Данные вне допустимого диапазона!")

    def getUserSetup(self):
        setup = {
            "density": self.window.density_SB.value(),
            "elasticity": self.window.elasticity.value(),
            "hardener_quantity": self.window.amount_SB.value(),
            "groups_content": self.window.content_SB.value(),
            "temperature": self.window.temp_SB.value(),
            "surf_density": self.window.surf_density_SB.value(),
            "tensile module": self.window.mod_SB.value(),
            "tensile_edurance": self.window.endurance_SB.value(),
            "consumption": self.window.consumption_SB.value(),
            "corner": self.window.corner_CB.currentData(),
            "patch_step": self.window.step_SB.value(),
            "patch_density": self.window.patch_density_SB.value(),
        }

        return setup


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(250, 250, 610, 480)
        self.setFixedSize(610, 440)
        self.setWindowTitle("Program")

        self._SetupObjects()

    def _SetupObjects(self):
        dec = 2

        self.MainWidget = QtWidgets.QWidget(self)
        self.MainWidget.setGeometry(QtCore.QRect(0, 0, 610, 480))
        self.Title_Label = QtWidgets.QLabel(self.MainWidget)
        self.Title_Label.setGeometry(QtCore.QRect(0, 0, 611, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.Title_Label.setFont(font)
        self.line = QtWidgets.QFrame(self.MainWidget)
        self.line.setGeometry(QtCore.QRect(-10, 40, 741, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label = QtWidgets.QLabel(self.MainWidget)
        self.label.setGeometry(QtCore.QRect(30, 90, 231, 16))
        font = QtGui.QFont("Corbel", 10)
        self.label.setFont(font)
        self.label_2 = QtWidgets.QLabel(self.MainWidget)
        self.label_2.setGeometry(QtCore.QRect(30, 115, 231, 16))
        self.label_2.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.MainWidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 231, 16))
        self.label_3.setFont(font)
        self.label_4 = QtWidgets.QLabel(self.MainWidget)
        self.label_4.setGeometry(QtCore.QRect(30, 165, 231, 16))
        self.label_4.setFont(font)
        self.label_5 = QtWidgets.QLabel(self.MainWidget)
        self.label_5.setGeometry(QtCore.QRect(30, 190, 231, 16))
        self.label_5.setFont(font)
        self.label_6 = QtWidgets.QLabel(self.MainWidget)
        self.label_6.setGeometry(QtCore.QRect(30, 215, 231, 16))
        self.label_6.setFont(font)
        self.label_7 = QtWidgets.QLabel(self.MainWidget)
        self.label_7.setGeometry(QtCore.QRect(30, 290, 231, 16))
        self.label_7.setFont(font)
        self.label_8 = QtWidgets.QLabel(self.MainWidget)
        self.label_8.setGeometry(QtCore.QRect(30, 315, 231, 16))
        self.label_8.setFont(font)
        self.label_9 = QtWidgets.QLabel(self.MainWidget)
        self.label_9.setGeometry(QtCore.QRect(30, 340, 231, 16))
        self.label_9.setFont(font)
        self.label_10 = QtWidgets.QLabel(self.MainWidget)
        self.label_10.setGeometry(QtCore.QRect(30, 365, 231, 16))
        self.label_10.setFont(font)
        self.density_SB = QtWidgets.QDoubleSpinBox(self.MainWidget)
        self.density_SB.setGeometry(QtCore.QRect(280, 90, 81, 20))
        self.elasticity = QtWidgets.QDoubleSpinBox(self.MainWidget)
        self.elasticity.setGeometry(QtCore.QRect(280, 115, 81, 20))
        self.amount_SB = QtWidgets.QDoubleSpinBox(self.MainWidget)
        self.amount_SB.setGeometry(QtCore.QRect(280, 140, 81, 20))
        self.content_SB = QtWidgets.QDoubleSpinBox(self.MainWidget)
        self.content_SB.setGeometry(QtCore.QRect(280, 165, 81, 20))
        self.temp_SB = QtWidgets.QDoubleSpinBox(self.MainWidget)
        self.temp_SB.setGeometry(QtCore.QRect(280, 190, 81, 20))
        self.surf_density_SB = QtWidgets.QDoubleSpinBox(self.MainWidget)
        self.surf_density_SB.setGeometry(QtCore.QRect(280, 215, 81, 20))
        self.consumption_SB = QtWidgets.QDoubleSpinBox(self.MainWidget)
        self.consumption_SB.setGeometry(QtCore.QRect(280, 290, 81, 20))
        self.step_SB = QtWidgets.QDoubleSpinBox(self.MainWidget)
        self.step_SB.setGeometry(QtCore.QRect(280, 340, 81, 20))
        self.patch_density_SB = QtWidgets.QDoubleSpinBox(self.MainWidget)
        self.patch_density_SB.setGeometry(QtCore.QRect(280, 365, 81, 20))
        self.corner_CB = QtWidgets.QComboBox(self.MainWidget)
        self.corner_CB.setGeometry(QtCore.QRect(280, 315, 81, 20))
        self.corner_CB.setEditable(False)
        self.corner_CB.setFrame(True)
        self.corner_CB.addItem("", 0)
        self.corner_CB.addItem("", 1)
        self.label_21 = QtWidgets.QLabel(self.MainWidget)
        self.label_21.setGeometry(QtCore.QRect(400, 90, 131, 16))
        self.label_21.setStyleSheet("QLabel {color: rgba(0, 0, 0, 100)}")
        self.label_22 = QtWidgets.QLabel(self.MainWidget)
        self.label_22.setGeometry(QtCore.QRect(400, 115, 131, 16))
        self.label_22.setStyleSheet("QLabel {color: rgba(0, 0, 0, 100)}")
        self.label_23 = QtWidgets.QLabel(self.MainWidget)
        self.label_23.setGeometry(QtCore.QRect(400, 140, 131, 16))
        self.label_23.setStyleSheet("QLabel {color: rgba(0, 0, 0, 100)}")
        self.label_24 = QtWidgets.QLabel(self.MainWidget)
        self.label_24.setGeometry(QtCore.QRect(400, 165, 131, 16))
        self.label_24.setStyleSheet("QLabel {color: rgba(0, 0, 0, 100)}")
        self.label_25 = QtWidgets.QLabel(self.MainWidget)
        self.label_25.setGeometry(QtCore.QRect(400, 190, 131, 16))
        self.label_25.setStyleSheet("QLabel {color: rgba(0, 0, 0, 100)}")
        self.label_26 = QtWidgets.QLabel(self.MainWidget)
        self.label_26.setGeometry(QtCore.QRect(400, 215, 131, 16))
        self.label_26.setStyleSheet("QLabel {color: rgba(0, 0, 0, 100)}")
        self.label_43 = QtWidgets.QLabel(self.MainWidget)
        self.label_43.setGeometry(QtCore.QRect(400, 290, 131, 16))
        self.label_43.setStyleSheet("QLabel {color: rgba(0, 0, 0, 100)}")
        self.label_44 = QtWidgets.QLabel(self.MainWidget)
        self.label_44.setGeometry(QtCore.QRect(400, 345, 131, 16))
        self.label_44.setStyleSheet("QLabel {color: rgba(0, 0, 0, 100)}")
        self.label_63 = QtWidgets.QLabel(self.MainWidget)
        self.label_63.setGeometry(QtCore.QRect(400, 365, 131, 16))
        self.label_63.setStyleSheet("QLabel {color: rgba(0, 0, 0, 100)}")
        self.line_8 = QtWidgets.QFrame(self.MainWidget)
        self.line_8.setGeometry(QtCore.QRect(-10, 390, 731, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Start_Button = QtWidgets.QPushButton(self.MainWidget)
        self.Start_Button.setGeometry(QtCore.QRect(30, 410, 91, 23))
        self.label_64 = QtWidgets.QLabel(self.MainWidget)
        self.label_64.setGeometry(QtCore.QRect(150, 60, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        self.label_64.setFont(font)
        self.label_65 = QtWidgets.QLabel(self.MainWidget)
        self.label_65.setGeometry(QtCore.QRect(420, 60, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        self.label_65.setFont(font)
        self.label_66 = QtWidgets.QLabel(self.MainWidget)
        self.label_66.setGeometry(QtCore.QRect(170, 410, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        self.label_66.setFont(font)
        self.line_9 = QtWidgets.QFrame(self.MainWidget)
        self.line_9.setGeometry(QtCore.QRect(150, 400, 3, 61))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.result_Label = QtWidgets.QLabel(self.MainWidget)
        self.result_Label.setGeometry(QtCore.QRect(360, 410, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.result_Label.setFont(font)
        self.result_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.line_3 = QtWidgets.QFrame(self.MainWidget)
        self.line_3.setGeometry(QtCore.QRect(370, 90, 20, 291))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_11 = QtWidgets.QLabel(self.MainWidget)
        self.label_11.setGeometry(QtCore.QRect(30, 240, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_35 = QtWidgets.QLabel(self.MainWidget)
        self.label_35.setGeometry(QtCore.QRect(30, 265, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.mod_SB = QtWidgets.QDoubleSpinBox(self.MainWidget)
        self.mod_SB.setGeometry(QtCore.QRect(280, 240, 81, 20))
        self.endurance_SB = QtWidgets.QDoubleSpinBox(self.MainWidget)
        self.endurance_SB.setGeometry(QtCore.QRect(280, 265, 81, 20))
        self.label_47 = QtWidgets.QLabel(self.MainWidget)
        self.label_47.setGeometry(QtCore.QRect(400, 240, 131, 16))
        self.label_47.setStyleSheet("QLabel {color: rgba(0, 0, 0, 100)}")
        self.label_48 = QtWidgets.QLabel(self.MainWidget)
        self.label_48.setGeometry(QtCore.QRect(400, 265, 131, 16))
        self.label_48.setStyleSheet("QLabel {color: rgba(0, 0, 0, 100)}")
        self.density_SB.setMinimum(0)
        self.density_SB.setMaximum(2161.57)
        self.density_SB.setDecimals(dec)
        self.elasticity.setMinimum(0)
        self.elasticity.setMaximum(1649.42)
        self.elasticity.setDecimals(dec)
        self.amount_SB.setMinimum(0)
        self.amount_SB.setMaximum(181.83)
        self.amount_SB.setDecimals(dec)
        self.content_SB.setMinimum(0)
        self.content_SB.setMaximum(28.96)
        self.content_SB.setDecimals(dec)
        self.temp_SB.setMinimum(0)
        self.temp_SB.setMaximum(386.07)
        self.temp_SB.setDecimals(dec)
        self.surf_density_SB.setMinimum(0)
        self.surf_density_SB.setMaximum(1291.34)
        self.surf_density_SB.setDecimals(dec)
        self.consumption_SB.setMinimum(0)
        self.consumption_SB.setMaximum(359.05)
        self.consumption_SB.setDecimals(dec)
        self.step_SB.setMinimum(0)
        self.step_SB.setMaximum(13.73)
        self.step_SB.setDecimals(dec)
        self.patch_density_SB.setMaximum(0)
        self.patch_density_SB.setMaximum(86.01)
        self.patch_density_SB.setDecimals(dec)
        self.endurance_SB.setMaximum(0)
        self.endurance_SB.setMaximum(3848.44)
        self.endurance_SB.setDecimals(dec)
        self.mod_SB.setMaximum(0)
        self.mod_SB.setMaximum(82.68)
        self.mod_SB.setDecimals(dec)
        

        title = """
        <html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">
        Рекомендация показателя «Соотношение матрица-наполнитель»<br/>
        для композиционного материала «Базальтопластик»
        </span></p></body></html>
        """

        self.label.setText("Плотность, кг/м3")
        self.label_2.setText("Модуль упругости, ГПа")
        self.label_3.setText("Количество отвердителя, м.%")
        self.label_4.setText("Содержание эпоксидных групп, %_2")
        self.label_5.setText("Температура вспышки, С_2")
        self.label_6.setText("Поверхностная плотность, г/м2")
        self.label_7.setText("Потребление смолы, г/м2")
        self.label_8.setText("Угол нашивки, град")
        self.label_9.setText("Шаг нашивки")
        self.label_10.setText("Плотность нашивки")
        self.corner_CB.setItemText(0, "0°")
        self.corner_CB.setItemText(1, "90°")
        self.label_21.setText("1784,48 – 2161,57")
        self.label_22.setText("2,44 – 1649,42")
        self.label_23.setText("38,67 – 181,83")
        self.label_24.setText("15,70 – 28,96")
        self.label_25.setText("179,37 – 386,07")
        self.label_26.setText("0,60 – 1291,34")
        self.label_43.setText("63,69 – 359,05")
        self.label_44.setText("0,04 -13,73")
        self.label_63.setText("27,27 – 86,01")
        self.Start_Button.setText("Счёт")
        self.label_64.setText("Значение")
        self.label_65.setText("Диапазон")
        self.label_66.setText("Прогноз:")
        self.label_11.setText("Модуль упрогости при растяжении, ГПа")
        self.label_35.setText("Прочность при растяжении, МПа")
        self.label_47.setText("64,05 – 82,68")
        self.label_48.setText("1036,86 – 3848,44")
        self.Title_Label.setText(title)
