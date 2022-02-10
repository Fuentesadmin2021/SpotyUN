import sys
from SpotyUNI import *
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtCore import pyqtSlot

# from PySide2 import QtCore
# from PySide2 import QtCore, QtGui, QtWidgets
# from PySide2.QtCore import QPropertyAnimation # paquete necesario para crear el menu lateral desplegable

from PyQt5 import QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation  # paquete necesario para crear el menu lateral desplegable
from pygame import mixer
import mutagen
from canciones import Canciones


lista_canciones = Canciones()
lista_canciones = lista_canciones.get_lista_canciones()


class SpotyUNI(QtWidgets.QMainWindow):
    def __init__(self, lista_informacion):
        super().__init__()
        self.lista_informacion = lista_informacion
        self.step = 0
        self.timer = QBasicTimer()
        mixer.init()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.table_canciones.setRowCount(len(lista_informacion))
        self.ui.table_canciones.setColumnCount(len(lista_informacion[0]) - 2)
        self.ui.table_canciones.setHorizontalHeaderLabels(('ID', 'NOMBRE CANCIÓN', 'GENERO', 'ALBUM', 'INTERPRETE'))
        self.ui.table_canciones.setVerticalHeaderLabels(('' for i in range(len(lista_informacion))))

        self.ui.table_canciones.setHorizontalHeader(self.ui.table_canciones.horizontalHeader().setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold)))
        self.ui.table_canciones.setStyleSheet("QHeaderView::section { background-color: #1e7eff; color: white; }")

        self.ui.table_canciones.setHorizontalHeader(self.ui.table_canciones.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch))
        row = 0
        for tup in self.lista_informacion:
            col = 0
            for item in tup[:5]:
                cellinfo = QTableWidgetItem(str(item))
                cellinfo.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.ui.table_canciones.setItem(row, col, cellinfo)
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                col += 1
            row += 1

        self.ui.table_canciones.resizeColumnToContents(0)
        self.ui.table_canciones.setSortingEnabled(True)
        self.ui.table_canciones.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.ui.table_canciones.itemSelectionChanged.connect(self.on_selec_change)

        # eliminar barra y de titulo - opacidad
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # SizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # mover ventana
        self.ui.frame_superior.mouseMoveEvent = self.mover_ventana

        # acceder a las paginas
        self.ui.bt_inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_inicio))
        self.ui.bt_canciones.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.bt_planes.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.bt_cliente.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.bt_pp_cliente.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.bt_listas.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))

        # control barra de titulos
        self.ui.bt_ocultar.clicked.connect(self.control_bt_ocultar)
        self.ui.bt_minimizar.clicked.connect(self.control_bt_normal)
        self.ui.bt_maximizar.clicked.connect(self.control_bt_maximizar)
        self.ui.bt_cerrar.clicked.connect(lambda: self.close())

        # control barra de reprodcucción
        # self.ui.bt_canciones_2.cliked.connect(self.no_exite)
        self.ui.bt_reproducir.clicked.connect(self.control_bt_reproducir)
        self.ui.bt_pausar.clicked.connect(self.control_bt_pausar)
        # self.ui.bt_reanudar.clicked.connect(self.control_bt_reanudar)
        self.ui.bt_detener.clicked.connect(self.control_bt_detener)
        self.ui.volumen.valueChanged.connect(self.control_volumen)

        self.ui.bt_ocultar.hide()

        # menu lateral
        self.ui.bt_menu.clicked.connect(self.mover_menu)
        self.ui.bt_canciones_2.clicked.connect(self.mover_table)

    def know_time(self):
        time = mutagen.File(ruta)
        return time.info.length * 1000 - 1

    @QtCore.pyqtSlot()
    def on_selec_change(self):
        global index
        row = self.ui.table_canciones.currentRow()
        item = self.ui.table_canciones.item(row, 0)
        index = int(item.text()) - 1
        return index

    def control_bt_reproducir(self):
        if self.step != 0:
            mixer.music.unpause()
            valor = self.know_time()
            self.timer.start(int(valor / 100), self)

        else:
            global ruta
            try:
                nombre = self.lista_informacion[index][1]
                cancion = self.lista_informacion[index][6]
                ruta = f"../SpotyUN_Lista/Canciones/{nombre}.mp3"
                print(ruta, nombre)
                with open(ruta, 'wb') as file:
                    file.write(cancion)

                mixer.music.load(ruta)

            except:
                self.ui.message.warning(self, 'Error de reproducción', "Escoge una canción")

            else:
                mixer.music.play()
                self.ui.progressBar.setValue(0)
                valor = self.know_time()
                self.timer.start(int(valor / 100), self)
                if self.timer.isActive():
                    cadena = self.know_text()
                    # self.ui.label_2.setGeometry(QtCore.QRect(0, 550, 600, 25))
                    self.ui.label_2.setVisible(True)
                    self.ui.label_2.setText(cadena)

    def know_text(self):
        nombre, interprete, genero, album = (lista_canciones[index][1:5])
        cadena2 = '- {} - {} - {} - {} -'.format(nombre, interprete, genero, album)
        return str(cadena2)

    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.step = 0
            self.ui.progressBar.setValue(0)
            mixer.music.stop()
            return

        self.step += 1
        self.ui.progressBar.setValue(self.step)

    def control_bt_pausar(self):
        mixer.music.pause()
        self.timer.stop()

    def control_bt_detener(self):
        mixer.music.stop()
        self.timer.stop()
        self.step = 0
        self.ui.progressBar.setValue(0)
        self.ui.label_2.hide()

    def control_volumen(self):
        value = self.ui.volumen.value()
        mixer.music.set_volume(value / 100)

    # -------------------------------------------------------------

    def control_bt_ocultar(self):
        self.showMinimized()

    def control_bt_normal(self):
        self.showNormal()
        self.ui.bt_ocultar.hide()
        self.ui.bt_maximizar.show()

    def control_bt_maximizar(self):
        self.showMaximized()
        self.ui.bt_maximizar.hide()
        self.ui.bt_ocultar.show()

    def mover_menu(self):
        if True:
            width = self.ui.frame_lateral.width()
            normal = 0
            if width == 0:
                extender = 250
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.ui.frame_lateral, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()

    def mover_table(self):
        if True:
            width = self.ui.frame_table.width()
            normal = 0
            if width == 0:
                extender = 1000
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.ui.frame_table, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()

    ## SizeGrip
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    ## mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):
        if self.isMaximized() == False:
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()

        if event.globalPos().y() <= 20:
            self.showMaximized()
        else:
            self.showNormal()


if __name__ == "__main__":
    program = QApplication(sys.argv)
    my_program = SpotyUNI(lista_canciones)
    my_program.show()
    sys.exit(program.exec_())
