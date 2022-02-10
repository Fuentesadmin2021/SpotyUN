# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SpotyUNIomQXKt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1274, 647)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 40))
        self.frame_superior.setMaximumSize(QSize(16777215, 40))
        self.frame_superior.setStyleSheet(u"background-color:rgb(0, 0, 200)")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_menu = QPushButton(self.frame_superior)
        self.bt_menu.setObjectName(u"bt_menu")
        self.bt_menu.setMinimumSize(QSize(250, 32))
        font = QFont()
        font.setFamily(u"Georgia")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.bt_menu.setFont(font)
        self.bt_menu.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"background-color:rgb(0, 0, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px solid #rgb(255, 255, 255);\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        icon = QIcon()
        icon.addFile(u"imagenes/menus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_menu)

        self.horizontalSpacer = QSpacerItem(872, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.bt_ocultar = QPushButton(self.frame_superior)
        self.bt_ocultar.setObjectName(u"bt_ocultar")
        self.bt_ocultar.setMaximumSize(QSize(16777215, 35))
        self.bt_ocultar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"background-color:rgb(149, 183, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px solid #rgb(0, 0, 255);\n"
"background-color:rgb(0, 0, 255)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"imagenes/ocultarp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_ocultar.setIcon(icon1)
        self.bt_ocultar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_ocultar)

        self.bt_minimizar = QPushButton(self.frame_superior)
        self.bt_minimizar.setObjectName(u"bt_minimizar")
        self.bt_minimizar.setMaximumSize(QSize(16777215, 35))
        self.bt_minimizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"background-color:rgb(149, 183, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px solid #rgb(0, 0, 255);\n"
"background-color:rgb(0, 0, 255)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"imagenes/minimizarp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_minimizar.setIcon(icon2)
        self.bt_minimizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_minimizar)

        self.bt_maximizar = QPushButton(self.frame_superior)
        self.bt_maximizar.setObjectName(u"bt_maximizar")
        self.bt_maximizar.setMaximumSize(QSize(16777215, 35))
        self.bt_maximizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"background-color:rgb(149, 183, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px solid #rgb(0, 0, 255);\n"
"background-color:rgb(0, 0, 255)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"imagenes/maximizarp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_maximizar.setIcon(icon3)
        self.bt_maximizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_maximizar)

        self.bt_cerrar = QPushButton(self.frame_superior)
        self.bt_cerrar.setObjectName(u"bt_cerrar")
        self.bt_cerrar.setMaximumSize(QSize(16777215, 35))
        self.bt_cerrar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"background-color:rgb(149, 183, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px solid #rgb(165, 0, 0);\n"
"background-color:rgb(165, 0, 0)\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"imagenes/cerrarp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cerrar.setIcon(icon4)
        self.bt_cerrar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_cerrar)


        self.verticalLayout.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.centralwidget)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_lateral = QFrame(self.frame_inferior)
        self.frame_lateral.setObjectName(u"frame_lateral")
        self.frame_lateral.setMinimumSize(QSize(250, 0))
        self.frame_lateral.setMaximumSize(QSize(0, 16777215))
        self.frame_lateral.setStyleSheet(u"QFrame{\n"
"background-color:rgb(105, 105, 255)\n"
"}\n"
"\n"
"QPushButton{\n"
"background:qlineargradient(spread:pad, x1:0.0695224, y1:0.943, x2:0.825871, y2:0.745, stop:0.00497512 rgba(255, 255, 255, 255), stop:1 rgba(74, 68, 255, 255));\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font 75 12pt \"Arial Narrow\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 255, 255);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"font 75 12pt \"Arial Narrow\";\n"
"}")
        self.frame_lateral.setFrameShape(QFrame.StyledPanel)
        self.frame_lateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_lateral)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_inicio = QPushButton(self.frame_lateral)
        self.bt_inicio.setObjectName(u"bt_inicio")
        self.bt_inicio.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setFamily(u"Georgia")
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setWeight(75)
        self.bt_inicio.setFont(font1)
        self.bt_inicio.setLayoutDirection(Qt.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u"imagenes/Inicio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_inicio.setIcon(icon5)
        self.bt_inicio.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_inicio)

        self.bt_canciones = QPushButton(self.frame_lateral)
        self.bt_canciones.setObjectName(u"bt_canciones")
        self.bt_canciones.setMinimumSize(QSize(200, 40))
        font2 = QFont()
        font2.setFamily(u"Georgia")
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(75)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.bt_canciones.setFont(font2)
        self.bt_canciones.setLayoutDirection(Qt.RightToLeft)
        icon6 = QIcon()
        icon6.addFile(u"imagenes/musica.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_canciones.setIcon(icon6)
        self.bt_canciones.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_canciones)

        self.bt_planes = QPushButton(self.frame_lateral)
        self.bt_planes.setObjectName(u"bt_planes")
        self.bt_planes.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setFamily(u"Georgia")
        font3.setBold(True)
        font3.setWeight(75)
        self.bt_planes.setFont(font3)
        self.bt_planes.setLayoutDirection(Qt.LeftToRight)
        self.bt_planes.setAutoFillBackground(False)
        icon7 = QIcon()
        icon7.addFile(u"imagenes/coin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_planes.setIcon(icon7)
        self.bt_planes.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_planes)

        self.bt_cliente = QPushButton(self.frame_lateral)
        self.bt_cliente.setObjectName(u"bt_cliente")
        self.bt_cliente.setMinimumSize(QSize(0, 40))
        self.bt_cliente.setFont(font3)
        self.bt_cliente.setLayoutDirection(Qt.RightToLeft)
        icon8 = QIcon()
        icon8.addFile(u"imagenes/usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cliente.setIcon(icon8)
        self.bt_cliente.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_cliente)

        self.bt_pp_cliente = QPushButton(self.frame_lateral)
        self.bt_pp_cliente.setObjectName(u"bt_pp_cliente")
        self.bt_pp_cliente.setMinimumSize(QSize(0, 40))
        self.bt_pp_cliente.setFont(font3)
        self.bt_pp_cliente.setLayoutDirection(Qt.LeftToRight)
        icon9 = QIcon()
        icon9.addFile(u"imagenes/mas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_pp_cliente.setIcon(icon9)
        self.bt_pp_cliente.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_pp_cliente)

        self.bt_listas = QPushButton(self.frame_lateral)
        self.bt_listas.setObjectName(u"bt_listas")
        self.bt_listas.setMinimumSize(QSize(0, 40))
        self.bt_listas.setFont(font3)
        self.bt_listas.setLayoutDirection(Qt.RightToLeft)
        icon10 = QIcon()
        icon10.addFile(u"imagenes/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_listas.setIcon(icon10)
        self.bt_listas.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_listas)

        self.verticalSpacer = QSpacerItem(20, 268, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_program = QLabel(self.frame_lateral)
        self.label_program.setObjectName(u"label_program")
        self.label_program.setMinimumSize(QSize(0, 50))
        font4 = QFont()
        font4.setFamily(u"Baskerlle Old Face")
        font4.setPointSize(24)
        font4.setBold(False)
        font4.setWeight(50)
        self.label_program.setFont(font4)
        self.label_program.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0.0695224, y1:0.943, x2:0.825871, y2:0.745, stop:0.00497512 rgba(255, 255, 255, 255), stop:1 rgba(73, 69, 255, 255))")
        self.label_program.setScaledContents(False)
        self.label_program.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_program)


        self.horizontalLayout_3.addWidget(self.frame_lateral)

        self.frame_contenedor = QFrame(self.frame_inferior)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setMinimumSize(QSize(1000, 0))
        self.frame_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_contenedor)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_contenedor)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setStyleSheet(u"background:qlineargradient(spread:pad, x1:1, y1:0.892, x2:0, y2:0.761136, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(177, 175, 255, 255))")
        self.page_inicio = QWidget()
        self.page_inicio.setObjectName(u"page_inicio")
        self.verticalLayout_7 = QVBoxLayout(self.page_inicio)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.page_inicio)
        self.label.setObjectName(u"label")

        self.verticalLayout_7.addWidget(self.label)

        self.stackedWidget.addWidget(self.page_inicio)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_9 = QVBoxLayout(self.page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_table = QFrame(self.page)
        self.frame_table.setObjectName(u"frame_table")
        self.frame_table.setMaximumSize(QSize(0, 16777215))
        self.frame_table.setFrameShape(QFrame.StyledPanel)
        self.frame_table.setFrameShadow(QFrame.Raised)
#-----------
        self.verticalLayout_4 = QVBoxLayout(self.frame_table)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.table_canciones = QTableWidget(self.frame_table)
        self.table_canciones.setObjectName(u"table_canciones")

        self.verticalLayout_4.addWidget(self.table_canciones)

        self.progressBar = QProgressBar(self.frame_table)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 10))
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(0)

        self.verticalLayout_4.addWidget(self.progressBar)

        self.label_2 = QLabel(self.frame_table)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet("color: black; font-size: 20px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.hide()

        self.verticalLayout_4.addWidget(self.label_2)


        self.verticalLayout_9.addWidget(self.frame_table)

        self.frame_botones = QFrame(self.page)
        self.frame_botones.setObjectName(u"frame_botones")
        self.frame_botones.setFrameShape(QFrame.StyledPanel)
        self.frame_botones.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_botones)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(281, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.bt_canciones_2 = QPushButton(self.frame_botones)
        self.bt_canciones_2.setObjectName(u"bt_canciones_2")
        icon11 = QIcon()
        icon11.addFile(u"imagenes/buscarc.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_canciones_2.setIcon(icon11)
        self.bt_canciones_2.setIconSize(QSize(28, 28))

        self.horizontalLayout_4.addWidget(self.bt_canciones_2)

        self.bt_reproducir = QPushButton(self.frame_botones)
        self.bt_reproducir.setObjectName(u"bt_reproducir")
        self.bt_reproducir.setIcon(icon10)
        self.bt_reproducir.setIconSize(QSize(28, 28))

        self.horizontalLayout_4.addWidget(self.bt_reproducir)

        self.bt_pausar = QPushButton(self.frame_botones)
        self.bt_pausar.setObjectName(u"bt_pausar")
        icon12 = QIcon()
        icon12.addFile(u"imagenes/pausar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_pausar.setIcon(icon12)
        self.bt_pausar.setIconSize(QSize(28, 28))

        self.horizontalLayout_4.addWidget(self.bt_pausar)

        self.bt_detener = QPushButton(self.frame_botones)
        self.bt_detener.setObjectName(u"bt_detener")
        icon13 = QIcon()
        icon13.addFile(u"imagenes/detener.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_detener.setIcon(icon13)
        self.bt_detener.setIconSize(QSize(28, 28))

        self.horizontalLayout_4.addWidget(self.bt_detener)

        self.volumen = QSlider(self.frame_botones)
        self.volumen.setObjectName(u"volumen")
        self.volumen.setMinimumSize(QSize(0, 20))
        self.volumen.setMaximumSize(QSize(200, 16777215))
        self.volumen.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0.0695224, y1:0.943, x2:0.825871, y2:0.745, stop:0.00497512 rgba(255, 255, 255, 255), stop:1 rgba(73, 69, 255, 255))")
        self.volumen.setSliderPosition(50)
        self.volumen.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.volumen)

        self.horizontalSpacer_3 = QSpacerItem(235, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_9.addWidget(self.frame_botones)

        self.stackedWidget.addWidget(self.page)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_6 = QVBoxLayout(self.page_1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.p_planes = QPushButton(self.page_1)
        self.p_planes.setObjectName(u"p_planes")
        self.p_planes.setStyleSheet(u"background-color:rgb(0, 0, 127)")

        self.verticalLayout_6.addWidget(self.p_planes)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.p_clientes = QPushButton(self.page_2)
        self.p_clientes.setObjectName(u"p_clientes")
        self.p_clientes.setStyleSheet(u"background-color:rgb(0, 255, 255)")

        self.verticalLayout_3.addWidget(self.p_clientes)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.p_pp_clientes = QPushButton(self.page_3)
        self.p_pp_clientes.setObjectName(u"p_pp_clientes")
        self.p_pp_clientes.setStyleSheet(u"background-color:rgb(0, 170, 255)")

        self.verticalLayout_8.addWidget(self.p_pp_clientes)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_5 = QVBoxLayout(self.page_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.p_listas = QPushButton(self.page_4)
        self.p_listas.setObjectName(u"p_listas")
        self.p_listas.setStyleSheet(u"background-color:rgb(170, 85, 255)")

        self.verticalLayout_5.addWidget(self.p_listas)

        self.stackedWidget.addWidget(self.page_4)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.frame_contenedor)


        self.verticalLayout.addWidget(self.frame_inferior)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_menu.setText(QCoreApplication.translate("MainWindow", u"  MENU", None))
        self.bt_ocultar.setText("")
        self.bt_minimizar.setText("")
        self.bt_maximizar.setText("")
        self.bt_cerrar.setText("")
        self.bt_inicio.setText(QCoreApplication.translate("MainWindow", u"   \u00bfQue es SpotyUN?", None))
        self.bt_canciones.setText(QCoreApplication.translate("MainWindow", u"  CANCIONES   ", None))
        self.bt_planes.setText(QCoreApplication.translate("MainWindow", u"  PLANES    ", None))
        self.bt_cliente.setText(QCoreApplication.translate("MainWindow", u"  CLIENTE   ", None))
        self.bt_pp_cliente.setText(QCoreApplication.translate("MainWindow", u"   PLANES CLIENTE   ", None))
        self.bt_listas.setText(QCoreApplication.translate("MainWindow", u"  MI LISTA  ", None))
        self.label_program.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-style:italic; color:#000000; vertical-align:super;\">SpotyUN</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tempor voluptate ullamco consectetur magna sunt duis sint qui non anim elit. Amet officia laboris minim elit qui ad Lorem quis laborum consequat id in eu deserunt. Nisi aute cupidatat culpa aute deserunt pariatur.\n"
"\n"
"Pariatur cillum culpa nostrud proident quis id reprehenderit eu aute voluptate. Ullamco sunt occaecat nisi exercitation culpa enim in non dolor. Dolore aliqua aliqua mollit laboris voluptate.", None))
        self.label.setWordWrap(True)
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.bt_canciones_2.setText("")
        self.bt_reproducir.setText("")
        self.bt_pausar.setText("")
        self.bt_detener.setText("")
        self.p_planes.setText(QCoreApplication.translate("MainWindow", u"Planes", None))
        self.p_clientes.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.p_pp_clientes.setText(QCoreApplication.translate("MainWindow", u"Planes cliente", None))
        self.p_listas.setText(QCoreApplication.translate("MainWindow", u"Mi lista", None))
        self.message = QMessageBox(self.centralwidget)
        self.message.setGeometry(QRect(220, 520, 200, 25))
    # retranslateUi

