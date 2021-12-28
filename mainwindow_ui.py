# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/icons/icons/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.open_action = QAction(MainWindow)
        self.open_action.setObjectName(u"open_action")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/file-image.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_action.setIcon(icon1)
        self.open_action.setVisible(True)
        self.save_as_action = QAction(MainWindow)
        self.save_as_action.setObjectName(u"save_as_action")
        self.save_as_action.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/copy.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_as_action.setIcon(icon2)
        self.close_action = QAction(MainWindow)
        self.close_action.setObjectName(u"close_action")
        self.close_action.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/times.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_action.setIcon(icon3)
        self.about_action = QAction(MainWindow)
        self.about_action.setObjectName(u"about_action")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/info-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.about_action.setIcon(icon4)
        self.save_action = QAction(MainWindow)
        self.save_action.setObjectName(u"save_action")
        self.save_action.setEnabled(False)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_action.setIcon(icon5)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.colorize_button = QPushButton(self.centralwidget)
        self.colorize_button.setObjectName(u"colorize_button")
        self.colorize_button.setEnabled(False)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/palette.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.colorize_button.setIcon(icon6)

        self.gridLayout.addWidget(self.colorize_button, 1, 0, 1, 2)

        self.source_scroll_area = QScrollArea(self.centralwidget)
        self.source_scroll_area.setObjectName(u"source_scroll_area")
        self.source_scroll_area.setWidgetResizable(True)
        self.source_scroll_area_widget_contents = QWidget()
        self.source_scroll_area_widget_contents.setObjectName(u"source_scroll_area_widget_contents")
        self.source_scroll_area_widget_contents.setGeometry(QRect(0, 0, 389, 516))
        self.verticalLayout = QVBoxLayout(self.source_scroll_area_widget_contents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.source_label = QLabel(self.source_scroll_area_widget_contents)
        self.source_label.setObjectName(u"source_label")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_label.sizePolicy().hasHeightForWidth())
        self.source_label.setSizePolicy(sizePolicy)
        self.source_label.setScaledContents(True)

        self.verticalLayout.addWidget(self.source_label)

        self.source_scroll_area.setWidget(self.source_scroll_area_widget_contents)

        self.gridLayout.addWidget(self.source_scroll_area, 0, 0, 1, 1)

        self.result_scroll_area = QScrollArea(self.centralwidget)
        self.result_scroll_area.setObjectName(u"result_scroll_area")
        self.result_scroll_area.setWidgetResizable(True)
        self.result_scroll_area_widget_contents = QWidget()
        self.result_scroll_area_widget_contents.setObjectName(u"result_scroll_area_widget_contents")
        self.result_scroll_area_widget_contents.setGeometry(QRect(0, 0, 389, 516))
        self.verticalLayout_2 = QVBoxLayout(self.result_scroll_area_widget_contents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.result_label = QLabel(self.result_scroll_area_widget_contents)
        self.result_label.setObjectName(u"result_label")
        sizePolicy.setHeightForWidth(self.result_label.sizePolicy().hasHeightForWidth())
        self.result_label.setSizePolicy(sizePolicy)
        self.result_label.setScaledContents(False)

        self.verticalLayout_2.addWidget(self.result_label)

        self.result_scroll_area.setWidget(self.result_scroll_area_widget_contents)

        self.gridLayout.addWidget(self.result_scroll_area, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.file_menu = QMenu(self.menubar)
        self.file_menu.setObjectName(u"file_menu")
        self.help_menu = QMenu(self.menubar)
        self.help_menu.setObjectName(u"help_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.help_menu.menuAction())
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.save_as_action)
        self.file_menu.addAction(self.close_action)
        self.help_menu.addAction(self.about_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043a\u0440\u0430\u0448\u0438\u0432\u0430\u0442\u0435\u043b\u044c \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0439", None))
        self.open_action.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c...", None))
#if QT_CONFIG(shortcut)
        self.open_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.save_as_action.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a...", None))
#if QT_CONFIG(shortcut)
        self.save_as_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.close_action.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.close_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.about_action.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435...", None))
#if QT_CONFIG(shortcut)
        self.about_action.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.save_action.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.save_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.colorize_button.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043a\u0440\u0430\u0441\u0438\u0442\u044c", None))
        self.source_label.setText("")
        self.result_label.setText("")
        self.file_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.help_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

