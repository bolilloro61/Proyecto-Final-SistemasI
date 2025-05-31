# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test2YzMvkD.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
from . import src_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(968, 594)
        palette = QPalette()
        brush = QBrush(QColor(61, 61, 61, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(169, 236, 250, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        brush2 = QBrush(QColor(170, 170, 255, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        brush3 = QBrush(QColor(170, 255, 255, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush3)
        brush4 = QBrush(QColor(85, 0, 255, 255))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush4)
        brush5 = QBrush(QColor(85, 85, 255, 255))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush5)
        brush6 = QBrush(QColor(60, 60, 60, 255))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush6)
        brush7 = QBrush(QColor(90, 90, 90, 255))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush7)
        brush8 = QBrush(QColor(255, 239, 252, 255))
        brush8.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush8)
        brush9 = QBrush(QColor(255, 229, 254, 255))
        brush9.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush9)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush3)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush4)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush5)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush6)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush7)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush8)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush9)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush3)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush5)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush9)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush9)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush9)
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        palette1 = QPalette()
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush6)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush8)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush9)
        brush10 = QBrush(QColor(167, 233, 247, 255))
        brush10.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
        brush11 = QBrush(QColor(249, 224, 248, 255))
        brush11.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush6)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush8)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush9)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush9)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush9)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.frame.setPalette(palette1)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.widget.setPalette(palette2)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        palette3 = QPalette()
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.frame_2.setPalette(palette3)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.img_Logo = QLabel(self.frame_2)
        self.img_Logo.setObjectName(u"img_Logo")
        palette4 = QPalette()
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.img_Logo.setPalette(palette4)
        self.img_Logo.setStyleSheet(u"image: url(:/icons/assets/Logo.png);")

        self.horizontalLayout_6.addWidget(self.img_Logo)

        self.widget_4 = QWidget(self.frame_2)
        self.widget_4.setObjectName(u"widget_4")
        palette5 = QPalette()
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.widget_4.setPalette(palette5)
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbUser = QLabel(self.widget_4)
        self.lbUser.setObjectName(u"lbUser")
        palette6 = QPalette()
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.lbUser.setPalette(palette6)

        self.verticalLayout_2.addWidget(self.lbUser)

        self.lbCompany = QLabel(self.widget_4)
        self.lbCompany.setObjectName(u"lbCompany")
        palette7 = QPalette()
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.lbCompany.setPalette(palette7)

        self.verticalLayout_2.addWidget(self.lbCompany)


        self.horizontalLayout_6.addWidget(self.widget_4)


        self.verticalLayout.addWidget(self.frame_2)

        self.btnProvider = QPushButton(self.widget)
        self.btnProvider.setObjectName(u"btnProvider")
        palette8 = QPalette()
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.btnProvider.setPalette(palette8)

        self.verticalLayout.addWidget(self.btnProvider)

        self.btnClient = QPushButton(self.widget)
        self.btnClient.setObjectName(u"btnClient")
        palette9 = QPalette()
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.btnClient.setPalette(palette9)

        self.verticalLayout.addWidget(self.btnClient)

        self.btnProduct = QPushButton(self.widget)
        self.btnProduct.setObjectName(u"btnProduct")
        palette10 = QPalette()
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.btnProduct.setPalette(palette10)

        self.verticalLayout.addWidget(self.btnProduct)

        self.btnComb = QPushButton(self.widget)
        self.btnComb.setObjectName(u"btnComb")
        palette11 = QPalette()
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.btnComb.setPalette(palette11)

        self.verticalLayout.addWidget(self.btnComb)

        self.btnSProv = QPushButton(self.widget)
        self.btnSProv.setObjectName(u"btnSProv")
        palette12 = QPalette()
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.btnSProv.setPalette(palette12)

        self.verticalLayout.addWidget(self.btnSProv)

        self.btnBase = QPushButton(self.widget)
        self.btnBase.setObjectName(u"btnBase")
        palette13 = QPalette()
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.btnBase.setPalette(palette13)

        self.verticalLayout.addWidget(self.btnBase)

        self.btnPed = QPushButton(self.widget)
        self.btnPed.setObjectName(u"btnPed")
        palette14 = QPalette()
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.btnPed.setPalette(palette14)

        self.verticalLayout.addWidget(self.btnPed)

        self.btnPaq = QPushButton(self.widget)
        self.btnPaq.setObjectName(u"btnPaq")
        palette15 = QPalette()
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.btnPaq.setPalette(palette15)

        self.verticalLayout.addWidget(self.btnPaq)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        palette16 = QPalette()
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.widget_3.setPalette(palette16)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btnLogOut = QPushButton(self.widget_3)
        self.btnLogOut.setObjectName(u"btnLogOut")
        palette17 = QPalette()
        palette17.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette17.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette17.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.btnLogOut.setPalette(palette17)

        self.horizontalLayout_5.addWidget(self.btnLogOut)

        self.btnClose = QPushButton(self.widget_3)
        self.btnClose.setObjectName(u"btnClose")
        palette18 = QPalette()
        palette18.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette18.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette18.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.btnClose.setPalette(palette18)

        self.horizontalLayout_5.addWidget(self.btnClose)


        self.verticalLayout.addWidget(self.widget_3)


        self.horizontalLayout_2.addWidget(self.widget)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        palette19 = QPalette()
        palette19.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette19.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette19.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.frame_3.setPalette(palette19)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stacked1Contenido = QStackedWidget(self.frame_3)
        self.stacked1Contenido.setObjectName(u"stacked1Contenido")
        palette20 = QPalette()
        brush12 = QBrush(QColor(255, 219, 254, 255))
        brush12.setStyle(Qt.BrushStyle.SolidPattern)
        palette20.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush12)
        palette20.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette20.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush12)
        palette20.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette20.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush12)
        palette20.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush12)
        palette20.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.stacked1Contenido.setPalette(palette20)
        self.stacked1Contenido.setLineWidth(-1)
        self.tbProvider = QWidget()
        self.tbProvider.setObjectName(u"tbProvider")
        self.verticalLayout_3 = QVBoxLayout(self.tbProvider)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_2 = QWidget(self.tbProvider)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.tableProvider = QTableWidget(self.tbProvider)
        if (self.tableProvider.columnCount() < 6):
            self.tableProvider.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableProvider.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableProvider.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableProvider.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableProvider.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableProvider.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableProvider.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableProvider.setObjectName(u"tableProvider")
        self.tableProvider.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableProvider.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableProvider.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.tableProvider)

        self.stacked1Contenido.addWidget(self.tbProvider)
        self.tbClient = QWidget()
        self.tbClient.setObjectName(u"tbClient")
        self.verticalLayout_5 = QVBoxLayout(self.tbClient)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_6 = QWidget(self.tbClient)
        self.widget_6.setObjectName(u"widget_6")
        palette21 = QPalette()
        palette21.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette21.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette21.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.widget_6.setPalette(palette21)
        self.horizontalLayout_8 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")
        palette22 = QPalette()
        palette22.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette22.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette22.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.label_2.setPalette(palette22)
        self.label_2.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_2)


        self.verticalLayout_5.addWidget(self.widget_6)

        self.tableClient = QTableWidget(self.tbClient)
        if (self.tableClient.columnCount() < 4):
            self.tableClient.setColumnCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableClient.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        if (self.tableClient.rowCount() < 1):
            self.tableClient.setRowCount(1)
        self.tableClient.setObjectName(u"tableClient")
        palette23 = QPalette()
        palette23.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette23.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette23.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.tableClient.setPalette(palette23)
        self.tableClient.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableClient.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableClient.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableClient.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.tableClient.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableClient.horizontalHeader().setCascadingSectionResizes(False)
        self.tableClient.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableClient.horizontalHeader().setStretchLastSection(True)
        self.tableClient.verticalHeader().setCascadingSectionResizes(False)
        self.tableClient.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableClient.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_5.addWidget(self.tableClient)

        self.stacked1Contenido.addWidget(self.tbClient)
        self.tbProduct = QWidget()
        self.tbProduct.setObjectName(u"tbProduct")
        self.verticalLayout_6 = QVBoxLayout(self.tbProduct)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_8 = QWidget(self.tbProduct)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_3 = QLabel(self.widget_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_3)


        self.verticalLayout_6.addWidget(self.widget_8)

        self.tableProduct = QTableWidget(self.tbProduct)
        if (self.tableProduct.columnCount() < 5):
            self.tableProduct.setColumnCount(5)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableProduct.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        self.tableProduct.setObjectName(u"tableProduct")
        self.tableProduct.setAutoFillBackground(False)
        self.tableProduct.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableProduct.setAlternatingRowColors(False)
        self.tableProduct.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableProduct.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableProduct.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_6.addWidget(self.tableProduct)

        self.stacked1Contenido.addWidget(self.tbProduct)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_22 = QVBoxLayout(self.page)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.stacked1Contenido_2 = QStackedWidget(self.page)
        self.stacked1Contenido_2.setObjectName(u"stacked1Contenido_2")
        self.tbProvider_2 = QWidget()
        self.tbProvider_2.setObjectName(u"tbProvider_2")
        self.verticalLayout_7 = QVBoxLayout(self.tbProvider_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_7 = QWidget(self.tbProvider_2)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.widget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_4)


        self.verticalLayout_7.addWidget(self.widget_7)

        self.tableProvider_2 = QTableWidget(self.tbProvider_2)
        if (self.tableProvider_2.columnCount() < 6):
            self.tableProvider_2.setColumnCount(6)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableProvider_2.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableProvider_2.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableProvider_2.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableProvider_2.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableProvider_2.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableProvider_2.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        self.tableProvider_2.setObjectName(u"tableProvider_2")
        self.tableProvider_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableProvider_2.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_7.addWidget(self.tableProvider_2)

        self.stacked1Contenido_2.addWidget(self.tbProvider_2)
        self.tbClient_2 = QWidget()
        self.tbClient_2.setObjectName(u"tbClient_2")
        self.verticalLayout_8 = QVBoxLayout(self.tbClient_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_9 = QWidget(self.tbClient_2)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_5 = QLabel(self.widget_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_10.addWidget(self.label_5)


        self.verticalLayout_8.addWidget(self.widget_9)

        self.tableClient_2 = QTableWidget(self.tbClient_2)
        if (self.tableClient_2.columnCount() < 4):
            self.tableClient_2.setColumnCount(4)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableClient_2.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableClient_2.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableClient_2.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableClient_2.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        if (self.tableClient_2.rowCount() < 1):
            self.tableClient_2.setRowCount(1)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableClient_2.setVerticalHeaderItem(0, __qtablewidgetitem25)
        self.tableClient_2.setObjectName(u"tableClient_2")
        self.tableClient_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableClient_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableClient_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableClient_2.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.tableClient_2.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableClient_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableClient_2.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableClient_2.horizontalHeader().setStretchLastSection(True)
        self.tableClient_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableClient_2.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableClient_2.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_8.addWidget(self.tableClient_2)

        self.stacked1Contenido_2.addWidget(self.tbClient_2)
        self.tbProduct_2 = QWidget()
        self.tbProduct_2.setObjectName(u"tbProduct_2")
        self.verticalLayout_9 = QVBoxLayout(self.tbProduct_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_10 = QWidget(self.tbProduct_2)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_6 = QLabel(self.widget_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_6)


        self.verticalLayout_9.addWidget(self.widget_10)

        self.tableComb = QTableWidget(self.tbProduct_2)
        if (self.tableComb.columnCount() < 4):
            self.tableComb.setColumnCount(4)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableComb.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableComb.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableComb.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableComb.setHorizontalHeaderItem(3, __qtablewidgetitem29)
        self.tableComb.setObjectName(u"tableComb")
        self.tableComb.setAutoFillBackground(False)
        self.tableComb.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableComb.setAlternatingRowColors(False)
        self.tableComb.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableComb.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableComb.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_9.addWidget(self.tableComb)

        self.stacked1Contenido_2.addWidget(self.tbProduct_2)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stacked1Contenido_2.addWidget(self.page_2)

        self.verticalLayout_22.addWidget(self.stacked1Contenido_2)

        self.stacked1Contenido.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_23 = QVBoxLayout(self.page_3)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.stacked1Contenido_3 = QStackedWidget(self.page_3)
        self.stacked1Contenido_3.setObjectName(u"stacked1Contenido_3")
        self.tbProvider_3 = QWidget()
        self.tbProvider_3.setObjectName(u"tbProvider_3")
        self.verticalLayout_10 = QVBoxLayout(self.tbProvider_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_11 = QWidget(self.tbProvider_3)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_7 = QLabel(self.widget_11)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_7)


        self.verticalLayout_10.addWidget(self.widget_11)

        self.tableProvider_3 = QTableWidget(self.tbProvider_3)
        if (self.tableProvider_3.columnCount() < 6):
            self.tableProvider_3.setColumnCount(6)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableProvider_3.setHorizontalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableProvider_3.setHorizontalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableProvider_3.setHorizontalHeaderItem(2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableProvider_3.setHorizontalHeaderItem(3, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableProvider_3.setHorizontalHeaderItem(4, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableProvider_3.setHorizontalHeaderItem(5, __qtablewidgetitem35)
        self.tableProvider_3.setObjectName(u"tableProvider_3")
        self.tableProvider_3.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableProvider_3.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_10.addWidget(self.tableProvider_3)

        self.stacked1Contenido_3.addWidget(self.tbProvider_3)
        self.tbClient_3 = QWidget()
        self.tbClient_3.setObjectName(u"tbClient_3")
        self.verticalLayout_11 = QVBoxLayout(self.tbClient_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_12 = QWidget(self.tbClient_3)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_8 = QLabel(self.widget_12)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_8)


        self.verticalLayout_11.addWidget(self.widget_12)

        self.tableClient_3 = QTableWidget(self.tbClient_3)
        if (self.tableClient_3.columnCount() < 4):
            self.tableClient_3.setColumnCount(4)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableClient_3.setHorizontalHeaderItem(0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableClient_3.setHorizontalHeaderItem(1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableClient_3.setHorizontalHeaderItem(2, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableClient_3.setHorizontalHeaderItem(3, __qtablewidgetitem39)
        if (self.tableClient_3.rowCount() < 1):
            self.tableClient_3.setRowCount(1)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableClient_3.setVerticalHeaderItem(0, __qtablewidgetitem40)
        self.tableClient_3.setObjectName(u"tableClient_3")
        self.tableClient_3.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableClient_3.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableClient_3.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableClient_3.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.tableClient_3.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableClient_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableClient_3.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableClient_3.horizontalHeader().setStretchLastSection(True)
        self.tableClient_3.verticalHeader().setCascadingSectionResizes(False)
        self.tableClient_3.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableClient_3.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_11.addWidget(self.tableClient_3)

        self.stacked1Contenido_3.addWidget(self.tbClient_3)
        self.tbProduct_3 = QWidget()
        self.tbProduct_3.setObjectName(u"tbProduct_3")
        self.verticalLayout_12 = QVBoxLayout(self.tbProduct_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_13 = QWidget(self.tbProduct_3)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_9 = QLabel(self.widget_13)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.horizontalLayout_14.addWidget(self.label_9)


        self.verticalLayout_12.addWidget(self.widget_13)

        self.tableSProv = QTableWidget(self.tbProduct_3)
        if (self.tableSProv.columnCount() < 6):
            self.tableSProv.setColumnCount(6)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableSProv.setHorizontalHeaderItem(0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableSProv.setHorizontalHeaderItem(1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableSProv.setHorizontalHeaderItem(2, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableSProv.setHorizontalHeaderItem(3, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableSProv.setHorizontalHeaderItem(4, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableSProv.setHorizontalHeaderItem(5, __qtablewidgetitem46)
        self.tableSProv.setObjectName(u"tableSProv")
        self.tableSProv.setAutoFillBackground(False)
        self.tableSProv.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableSProv.setAlternatingRowColors(False)
        self.tableSProv.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableSProv.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableSProv.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_12.addWidget(self.tableSProv)

        self.stacked1Contenido_3.addWidget(self.tbProduct_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stacked1Contenido_3.addWidget(self.page_4)

        self.verticalLayout_23.addWidget(self.stacked1Contenido_3)

        self.stacked1Contenido.addWidget(self.page_3)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_24 = QVBoxLayout(self.page_5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.stacked1Contenido_4 = QStackedWidget(self.page_5)
        self.stacked1Contenido_4.setObjectName(u"stacked1Contenido_4")
        self.tbProvider_4 = QWidget()
        self.tbProvider_4.setObjectName(u"tbProvider_4")
        self.verticalLayout_13 = QVBoxLayout(self.tbProvider_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_14 = QWidget(self.tbProvider_4)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_10 = QLabel(self.widget_14)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.horizontalLayout_15.addWidget(self.label_10)


        self.verticalLayout_13.addWidget(self.widget_14)

        self.tableProvider_4 = QTableWidget(self.tbProvider_4)
        if (self.tableProvider_4.columnCount() < 6):
            self.tableProvider_4.setColumnCount(6)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableProvider_4.setHorizontalHeaderItem(0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableProvider_4.setHorizontalHeaderItem(1, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableProvider_4.setHorizontalHeaderItem(2, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableProvider_4.setHorizontalHeaderItem(3, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableProvider_4.setHorizontalHeaderItem(4, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableProvider_4.setHorizontalHeaderItem(5, __qtablewidgetitem52)
        self.tableProvider_4.setObjectName(u"tableProvider_4")
        self.tableProvider_4.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableProvider_4.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_13.addWidget(self.tableProvider_4)

        self.stacked1Contenido_4.addWidget(self.tbProvider_4)
        self.tbClient_4 = QWidget()
        self.tbClient_4.setObjectName(u"tbClient_4")
        self.verticalLayout_14 = QVBoxLayout(self.tbClient_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_15 = QWidget(self.tbClient_4)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_11 = QLabel(self.widget_15)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.horizontalLayout_16.addWidget(self.label_11)


        self.verticalLayout_14.addWidget(self.widget_15)

        self.tableClient_4 = QTableWidget(self.tbClient_4)
        if (self.tableClient_4.columnCount() < 4):
            self.tableClient_4.setColumnCount(4)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableClient_4.setHorizontalHeaderItem(0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableClient_4.setHorizontalHeaderItem(1, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableClient_4.setHorizontalHeaderItem(2, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableClient_4.setHorizontalHeaderItem(3, __qtablewidgetitem56)
        if (self.tableClient_4.rowCount() < 1):
            self.tableClient_4.setRowCount(1)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableClient_4.setVerticalHeaderItem(0, __qtablewidgetitem57)
        self.tableClient_4.setObjectName(u"tableClient_4")
        self.tableClient_4.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableClient_4.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableClient_4.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableClient_4.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.tableClient_4.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableClient_4.horizontalHeader().setCascadingSectionResizes(False)
        self.tableClient_4.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableClient_4.horizontalHeader().setStretchLastSection(True)
        self.tableClient_4.verticalHeader().setCascadingSectionResizes(False)
        self.tableClient_4.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableClient_4.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_14.addWidget(self.tableClient_4)

        self.stacked1Contenido_4.addWidget(self.tbClient_4)
        self.tbProduct_4 = QWidget()
        self.tbProduct_4.setObjectName(u"tbProduct_4")
        self.verticalLayout_15 = QVBoxLayout(self.tbProduct_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_16 = QWidget(self.tbProduct_4)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_12 = QLabel(self.widget_16)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.horizontalLayout_17.addWidget(self.label_12)


        self.verticalLayout_15.addWidget(self.widget_16)

        self.tableBase = QTableWidget(self.tbProduct_4)
        if (self.tableBase.columnCount() < 3):
            self.tableBase.setColumnCount(3)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableBase.setHorizontalHeaderItem(0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableBase.setHorizontalHeaderItem(1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableBase.setHorizontalHeaderItem(2, __qtablewidgetitem60)
        self.tableBase.setObjectName(u"tableBase")
        self.tableBase.setAutoFillBackground(False)
        self.tableBase.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableBase.setAlternatingRowColors(False)
        self.tableBase.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableBase.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableBase.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_15.addWidget(self.tableBase)

        self.stacked1Contenido_4.addWidget(self.tbProduct_4)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.stacked1Contenido_4.addWidget(self.page_6)

        self.verticalLayout_24.addWidget(self.stacked1Contenido_4)

        self.stacked1Contenido.addWidget(self.page_5)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_25 = QVBoxLayout(self.page_7)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.stacked1Contenido_5 = QStackedWidget(self.page_7)
        self.stacked1Contenido_5.setObjectName(u"stacked1Contenido_5")
        self.tbProvider_5 = QWidget()
        self.tbProvider_5.setObjectName(u"tbProvider_5")
        self.verticalLayout_16 = QVBoxLayout(self.tbProvider_5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_17 = QWidget(self.tbProvider_5)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_13 = QLabel(self.widget_17)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.horizontalLayout_18.addWidget(self.label_13)


        self.verticalLayout_16.addWidget(self.widget_17)

        self.tableProvider_5 = QTableWidget(self.tbProvider_5)
        if (self.tableProvider_5.columnCount() < 6):
            self.tableProvider_5.setColumnCount(6)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableProvider_5.setHorizontalHeaderItem(0, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableProvider_5.setHorizontalHeaderItem(1, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableProvider_5.setHorizontalHeaderItem(2, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableProvider_5.setHorizontalHeaderItem(3, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableProvider_5.setHorizontalHeaderItem(4, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableProvider_5.setHorizontalHeaderItem(5, __qtablewidgetitem66)
        self.tableProvider_5.setObjectName(u"tableProvider_5")
        self.tableProvider_5.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableProvider_5.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_16.addWidget(self.tableProvider_5)

        self.stacked1Contenido_5.addWidget(self.tbProvider_5)
        self.tbClient_5 = QWidget()
        self.tbClient_5.setObjectName(u"tbClient_5")
        self.verticalLayout_17 = QVBoxLayout(self.tbClient_5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget_18 = QWidget(self.tbClient_5)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_14 = QLabel(self.widget_18)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.horizontalLayout_19.addWidget(self.label_14)


        self.verticalLayout_17.addWidget(self.widget_18)

        self.tableClient_5 = QTableWidget(self.tbClient_5)
        if (self.tableClient_5.columnCount() < 4):
            self.tableClient_5.setColumnCount(4)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableClient_5.setHorizontalHeaderItem(0, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableClient_5.setHorizontalHeaderItem(1, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tableClient_5.setHorizontalHeaderItem(2, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableClient_5.setHorizontalHeaderItem(3, __qtablewidgetitem70)
        if (self.tableClient_5.rowCount() < 1):
            self.tableClient_5.setRowCount(1)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableClient_5.setVerticalHeaderItem(0, __qtablewidgetitem71)
        self.tableClient_5.setObjectName(u"tableClient_5")
        self.tableClient_5.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableClient_5.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableClient_5.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableClient_5.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.tableClient_5.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableClient_5.horizontalHeader().setCascadingSectionResizes(False)
        self.tableClient_5.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableClient_5.horizontalHeader().setStretchLastSection(True)
        self.tableClient_5.verticalHeader().setCascadingSectionResizes(False)
        self.tableClient_5.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableClient_5.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_17.addWidget(self.tableClient_5)

        self.stacked1Contenido_5.addWidget(self.tbClient_5)
        self.tbProduct_5 = QWidget()
        self.tbProduct_5.setObjectName(u"tbProduct_5")
        self.verticalLayout_18 = QVBoxLayout(self.tbProduct_5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_19 = QWidget(self.tbProduct_5)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_15 = QLabel(self.widget_19)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.horizontalLayout_20.addWidget(self.label_15)


        self.verticalLayout_18.addWidget(self.widget_19)

        self.tablePed = QTableWidget(self.tbProduct_5)
        if (self.tablePed.columnCount() < 3):
            self.tablePed.setColumnCount(3)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tablePed.setHorizontalHeaderItem(0, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tablePed.setHorizontalHeaderItem(1, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tablePed.setHorizontalHeaderItem(2, __qtablewidgetitem74)
        self.tablePed.setObjectName(u"tablePed")
        self.tablePed.setAutoFillBackground(False)
        self.tablePed.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tablePed.setAlternatingRowColors(False)
        self.tablePed.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablePed.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tablePed.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_18.addWidget(self.tablePed)

        self.stacked1Contenido_5.addWidget(self.tbProduct_5)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.stacked1Contenido_5.addWidget(self.page_8)

        self.verticalLayout_25.addWidget(self.stacked1Contenido_5)

        self.stacked1Contenido.addWidget(self.page_7)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_26 = QVBoxLayout(self.page_9)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.stacked1Contenido_6 = QStackedWidget(self.page_9)
        self.stacked1Contenido_6.setObjectName(u"stacked1Contenido_6")
        self.tbProvider_6 = QWidget()
        self.tbProvider_6.setObjectName(u"tbProvider_6")
        self.verticalLayout_19 = QVBoxLayout(self.tbProvider_6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_20 = QWidget(self.tbProvider_6)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_16 = QLabel(self.widget_20)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.horizontalLayout_21.addWidget(self.label_16)


        self.verticalLayout_19.addWidget(self.widget_20)

        self.tableProvider_6 = QTableWidget(self.tbProvider_6)
        if (self.tableProvider_6.columnCount() < 6):
            self.tableProvider_6.setColumnCount(6)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tableProvider_6.setHorizontalHeaderItem(0, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableProvider_6.setHorizontalHeaderItem(1, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableProvider_6.setHorizontalHeaderItem(2, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableProvider_6.setHorizontalHeaderItem(3, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableProvider_6.setHorizontalHeaderItem(4, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableProvider_6.setHorizontalHeaderItem(5, __qtablewidgetitem80)
        self.tableProvider_6.setObjectName(u"tableProvider_6")
        self.tableProvider_6.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableProvider_6.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_19.addWidget(self.tableProvider_6)

        self.stacked1Contenido_6.addWidget(self.tbProvider_6)
        self.tbClient_6 = QWidget()
        self.tbClient_6.setObjectName(u"tbClient_6")
        self.verticalLayout_20 = QVBoxLayout(self.tbClient_6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_21 = QWidget(self.tbClient_6)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_17 = QLabel(self.widget_21)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.horizontalLayout_22.addWidget(self.label_17)


        self.verticalLayout_20.addWidget(self.widget_21)

        self.tableClient_6 = QTableWidget(self.tbClient_6)
        if (self.tableClient_6.columnCount() < 4):
            self.tableClient_6.setColumnCount(4)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableClient_6.setHorizontalHeaderItem(0, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableClient_6.setHorizontalHeaderItem(1, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tableClient_6.setHorizontalHeaderItem(2, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tableClient_6.setHorizontalHeaderItem(3, __qtablewidgetitem84)
        if (self.tableClient_6.rowCount() < 1):
            self.tableClient_6.setRowCount(1)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tableClient_6.setVerticalHeaderItem(0, __qtablewidgetitem85)
        self.tableClient_6.setObjectName(u"tableClient_6")
        self.tableClient_6.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableClient_6.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableClient_6.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableClient_6.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.tableClient_6.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableClient_6.horizontalHeader().setCascadingSectionResizes(False)
        self.tableClient_6.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableClient_6.horizontalHeader().setStretchLastSection(True)
        self.tableClient_6.verticalHeader().setCascadingSectionResizes(False)
        self.tableClient_6.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableClient_6.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_20.addWidget(self.tableClient_6)

        self.stacked1Contenido_6.addWidget(self.tbClient_6)
        self.tbProduct_6 = QWidget()
        self.tbProduct_6.setObjectName(u"tbProduct_6")
        self.verticalLayout_21 = QVBoxLayout(self.tbProduct_6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.widget_22 = QWidget(self.tbProduct_6)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_18 = QLabel(self.widget_22)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.horizontalLayout_23.addWidget(self.label_18)


        self.verticalLayout_21.addWidget(self.widget_22)

        self.tablePaq = QTableWidget(self.tbProduct_6)
        if (self.tablePaq.columnCount() < 3):
            self.tablePaq.setColumnCount(3)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tablePaq.setHorizontalHeaderItem(0, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tablePaq.setHorizontalHeaderItem(1, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tablePaq.setHorizontalHeaderItem(2, __qtablewidgetitem88)
        self.tablePaq.setObjectName(u"tablePaq")
        self.tablePaq.setAutoFillBackground(False)
        self.tablePaq.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tablePaq.setAlternatingRowColors(False)
        self.tablePaq.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablePaq.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tablePaq.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_21.addWidget(self.tablePaq)

        self.stacked1Contenido_6.addWidget(self.tbProduct_6)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.stacked1Contenido_6.addWidget(self.page_10)

        self.verticalLayout_26.addWidget(self.stacked1Contenido_6)

        self.stacked1Contenido.addWidget(self.page_9)

        self.verticalLayout_4.addWidget(self.stacked1Contenido)

        self.widget_5 = QWidget(self.frame_3)
        self.widget_5.setObjectName(u"widget_5")
        palette24 = QPalette()
        palette24.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette24.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette24.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.widget_5.setPalette(palette24)
        self.btnDeleteRow = QPushButton(self.widget_5)
        self.btnDeleteRow.setObjectName(u"btnDeleteRow")
        self.btnDeleteRow.setGeometry(QRect(170, 0, 111, 41))
        palette25 = QPalette()
        palette25.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette25.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette25.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.btnDeleteRow.setPalette(palette25)
        self.btnUpdateRow = QPushButton(self.widget_5)
        self.btnUpdateRow.setObjectName(u"btnUpdateRow")
        self.btnUpdateRow.setGeometry(QRect(300, 0, 111, 41))
        palette26 = QPalette()
        palette26.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette26.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette26.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.btnUpdateRow.setPalette(palette26)
        self.btnAdd = QPushButton(self.widget_5)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setGeometry(QRect(430, 0, 111, 41))
        palette27 = QPalette()
        palette27.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette27.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        palette27.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush11)
#endif
        self.btnAdd.setPalette(palette27)

        self.verticalLayout_4.addWidget(self.widget_5)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stacked1Contenido.setCurrentIndex(1)
        self.stacked1Contenido_2.setCurrentIndex(2)
        self.stacked1Contenido_3.setCurrentIndex(2)
        self.stacked1Contenido_4.setCurrentIndex(2)
        self.stacked1Contenido_5.setCurrentIndex(2)
        self.stacked1Contenido_6.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.img_Logo.setText("")
        self.lbUser.setText("")
        self.lbCompany.setText("")
        self.btnProvider.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        self.btnClient.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btnProduct.setText(QCoreApplication.translate("MainWindow", u"Sabores", None))
        self.btnComb.setText(QCoreApplication.translate("MainWindow", u"Combinaciones", None))
        self.btnSProv.setText(QCoreApplication.translate("MainWindow", u"Sabores por proveedor", None))
        self.btnBase.setText(QCoreApplication.translate("MainWindow", u"Bases", None))
        self.btnPed.setText(QCoreApplication.translate("MainWindow", u"Pedidos", None))
        self.btnPaq.setText(QCoreApplication.translate("MainWindow", u"Paquetes", None))
        self.btnLogOut.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.btnClose.setText(QCoreApplication.translate("MainWindow", u"Apagar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        ___qtablewidgetitem = self.tableProvider.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableProvider.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableProvider.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Contacto", None));
        ___qtablewidgetitem3 = self.tableProvider.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        ___qtablewidgetitem4 = self.tableProvider.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem5 = self.tableProvider.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Direccion", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        ___qtablewidgetitem6 = self.tableClient.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem7 = self.tableClient.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem8 = self.tableClient.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Preferencia de Sabor", None));
        ___qtablewidgetitem9 = self.tableClient.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Historial combinaciones", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sabores", None))
        ___qtablewidgetitem10 = self.tableProduct.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem11 = self.tableProduct.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem12 = self.tableProduct.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Intensidad", None));
        ___qtablewidgetitem13 = self.tableProduct.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem14 = self.tableProduct.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Fecha de Expiracion", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        ___qtablewidgetitem15 = self.tableProvider_2.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem16 = self.tableProvider_2.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem17 = self.tableProvider_2.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Contacto", None));
        ___qtablewidgetitem18 = self.tableProvider_2.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        ___qtablewidgetitem19 = self.tableProvider_2.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem20 = self.tableProvider_2.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Direccion", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        ___qtablewidgetitem21 = self.tableClient_2.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem22 = self.tableClient_2.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem23 = self.tableClient_2.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Preferencia de Sabor", None));
        ___qtablewidgetitem24 = self.tableClient_2.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Historial combinaciones", None));
        ___qtablewidgetitem25 = self.tableClient_2.verticalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Combinaciones", None))
        ___qtablewidgetitem26 = self.tableComb.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem27 = self.tableComb.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Chicle Base", None));
        ___qtablewidgetitem28 = self.tableComb.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Sabor", None));
        ___qtablewidgetitem29 = self.tableComb.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Polvo por porcion", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        ___qtablewidgetitem30 = self.tableProvider_3.horizontalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem31 = self.tableProvider_3.horizontalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem32 = self.tableProvider_3.horizontalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Contacto", None));
        ___qtablewidgetitem33 = self.tableProvider_3.horizontalHeaderItem(3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        ___qtablewidgetitem34 = self.tableProvider_3.horizontalHeaderItem(4)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem35 = self.tableProvider_3.horizontalHeaderItem(5)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Direccion", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        ___qtablewidgetitem36 = self.tableClient_3.horizontalHeaderItem(0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem37 = self.tableClient_3.horizontalHeaderItem(1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem38 = self.tableClient_3.horizontalHeaderItem(2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Preferencia de Sabor", None));
        ___qtablewidgetitem39 = self.tableClient_3.horizontalHeaderItem(3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Historial combinaciones", None));
        ___qtablewidgetitem40 = self.tableClient_3.verticalHeaderItem(0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Sabores por proveedor", None))
        ___qtablewidgetitem41 = self.tableSProv.horizontalHeaderItem(0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Sabor", None));
        ___qtablewidgetitem42 = self.tableSProv.horizontalHeaderItem(1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None));
        ___qtablewidgetitem43 = self.tableSProv.horizontalHeaderItem(2)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Precio", None));
        ___qtablewidgetitem44 = self.tableSProv.horizontalHeaderItem(3)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Fecha ultimo pedido", None));
        ___qtablewidgetitem45 = self.tableSProv.horizontalHeaderItem(4)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Cantidad comprada", None));
        ___qtablewidgetitem46 = self.tableSProv.horizontalHeaderItem(5)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Arribo ultimo pedido", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        ___qtablewidgetitem47 = self.tableProvider_4.horizontalHeaderItem(0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem48 = self.tableProvider_4.horizontalHeaderItem(1)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem49 = self.tableProvider_4.horizontalHeaderItem(2)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Contacto", None));
        ___qtablewidgetitem50 = self.tableProvider_4.horizontalHeaderItem(3)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        ___qtablewidgetitem51 = self.tableProvider_4.horizontalHeaderItem(4)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem52 = self.tableProvider_4.horizontalHeaderItem(5)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Direccion", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        ___qtablewidgetitem53 = self.tableClient_4.horizontalHeaderItem(0)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem54 = self.tableClient_4.horizontalHeaderItem(1)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem55 = self.tableClient_4.horizontalHeaderItem(2)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Preferencia de Sabor", None));
        ___qtablewidgetitem56 = self.tableClient_4.horizontalHeaderItem(3)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Historial combinaciones", None));
        ___qtablewidgetitem57 = self.tableClient_4.verticalHeaderItem(0)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Bases", None))
        ___qtablewidgetitem58 = self.tableBase.horizontalHeaderItem(0)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem59 = self.tableBase.horizontalHeaderItem(1)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o", None));
        ___qtablewidgetitem60 = self.tableBase.horizontalHeaderItem(2)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Formula", None));
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        ___qtablewidgetitem61 = self.tableProvider_5.horizontalHeaderItem(0)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem62 = self.tableProvider_5.horizontalHeaderItem(1)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem63 = self.tableProvider_5.horizontalHeaderItem(2)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"Contacto", None));
        ___qtablewidgetitem64 = self.tableProvider_5.horizontalHeaderItem(3)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        ___qtablewidgetitem65 = self.tableProvider_5.horizontalHeaderItem(4)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem66 = self.tableProvider_5.horizontalHeaderItem(5)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"Direccion", None));
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        ___qtablewidgetitem67 = self.tableClient_5.horizontalHeaderItem(0)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem68 = self.tableClient_5.horizontalHeaderItem(1)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem69 = self.tableClient_5.horizontalHeaderItem(2)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Preferencia de Sabor", None));
        ___qtablewidgetitem70 = self.tableClient_5.horizontalHeaderItem(3)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"Historial combinaciones", None));
        ___qtablewidgetitem71 = self.tableClient_5.verticalHeaderItem(0)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Pedidos", None))
        ___qtablewidgetitem72 = self.tablePed.horizontalHeaderItem(0)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem73 = self.tablePed.horizontalHeaderItem(1)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem74 = self.tablePed.horizontalHeaderItem(2)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Paquete", None));
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        ___qtablewidgetitem75 = self.tableProvider_6.horizontalHeaderItem(0)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem76 = self.tableProvider_6.horizontalHeaderItem(1)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem77 = self.tableProvider_6.horizontalHeaderItem(2)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"Contacto", None));
        ___qtablewidgetitem78 = self.tableProvider_6.horizontalHeaderItem(3)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        ___qtablewidgetitem79 = self.tableProvider_6.horizontalHeaderItem(4)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem80 = self.tableProvider_6.horizontalHeaderItem(5)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"Direccion", None));
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        ___qtablewidgetitem81 = self.tableClient_6.horizontalHeaderItem(0)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem82 = self.tableClient_6.horizontalHeaderItem(1)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem83 = self.tableClient_6.horizontalHeaderItem(2)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"Preferencia de Sabor", None));
        ___qtablewidgetitem84 = self.tableClient_6.horizontalHeaderItem(3)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"Historial combinaciones", None));
        ___qtablewidgetitem85 = self.tableClient_6.verticalHeaderItem(0)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Paquetes", None))
        ___qtablewidgetitem86 = self.tablePaq.horizontalHeaderItem(0)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem87 = self.tablePaq.horizontalHeaderItem(1)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"Chicle", None));
        ___qtablewidgetitem88 = self.tablePaq.horizontalHeaderItem(2)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"Sabor", None));
        self.btnDeleteRow.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.btnUpdateRow.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
    # retranslateUi

