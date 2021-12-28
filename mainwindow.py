# This Python file uses the following encoding: utf-8
from cv2 import cvtColor, imread, resize, split, COLOR_BGR2LAB, COLOR_LAB2RGB
from cv2.dnn import blobFromImage, readNetFromCaffe
from numpy import clip, concatenate, full, load, newaxis
from os.path import dirname, isfile, join
from sys import exit
from threading import local, Thread

from PySide6.QtCore import QIODevice, QSaveFile, Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import \
    QApplication, QFileDialog, QMainWindow, \
    QMessageBox, QProgressBar
from mainwindow_ui import Ui_MainWindow

from utils import resource_to_bytes_io, numpy_array_to_qt_image

from __feature__ import snake_case, true_property


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.open_action.triggered.connect(self.open_image)
        self.ui.save_action.triggered.connect(self.save_image)
        self.ui.save_as_action.triggered.connect(self.save_image_as)
        self.ui.close_action.triggered.connect(self.close_image)
        self.ui.about_action.triggered.connect(self.about)

        self.ui.colorize_button.clicked.connect(self.colorize)
        self.ui.result_scroll_area.visible = False

        self.ui.progressbar = QProgressBar(self)
        self.ui.progressbar.visible = False
        self.ui.progressbar.minimum = 0
        self.ui.progressbar.maximum = 0
        self.ui.statusbar.add_permanent_widget(self.ui.progressbar)

    @Slot()
    def open_image(self, checked):
        source_path, _ = QFileDialog.get_open_file_name(
            self, 'Открыть изображение', dirname(__file__),
            'Изображения (*.png *.jpg *.jpeg *.bmp)')
        self.source_image_path = source_path
        if not source_path:
            return
        self.ui.sourceLabel.pixmap = QPixmap(source_path)
        self.ui.open_action.enabled = False
        self.ui.close_action.enabled = True
        self.ui.colorize_button.enabled = True
        self.ui.statusbar.show_message(
            'Исходное изображение успешно открыто', 2000)

    @Slot()
    def close_image(self, checked):
        self.source_image = None
        self.source_image_path = None
        self.result = None
        self.ui.open_action.enabled = True
        self.ui.save_action.enabled = False
        self.ui.save_as_action.enabled = False
        self.ui.close_action.enabled = False
        self.ui.source_label.clear()
        self.ui.result_scroll_area.visible = False
        self.ui.result_label.clear()
        self.ui.colorize_button.enabled = False

    def save_inner(self, saved_result_file):
        self.ui.statusbar.show_message('Идёт сохранение изображения...')
        self.ui.progressbar.visible = True
        saved_result = QSaveFile(saved_result_file)
        if saved_result.open(QIODevice.WriteOnly):
            self.ui.resultLabel.pixmap.save(saved_result)
            saved_result.commit()
            self.closeImage()
            msg = 'Изображение успешно сохранено'
        else:
            msg = 'Ошибка при сохранении изображения'
        self.ui.statusbar.clear_message()
        self.ui.progressbar.visible = False
        self.ui.statusbar.show_message(msg, 2000)

    @Slot()
    def save_image(self, checked):
        self.save_inner(self.source_image_path)

    def save_image_as(self, checked):
        saved_result_file, _ = QFileDialog.get_save_file_name(
            self, 'Сохранить изображение', self.source_image_path,
            'Изображения (*.png *.jpg *.jpeg *.bmp)')
        if not saved_result_file:
            return
        self.save_inner(saved_result_file)

    def colorize_implementation(self):
        thread_data = local()
        thread_data.success = True
        try:
            thread_data.image = imread(self.source_image_path)
            thread_data.scaled = thread_data.image.astype('float32') / 255.0
            thread_data.lab = cvtColor(thread_data.scaled, COLOR_BGR2LAB)

            thread_data.resized = resize(thread_data.lab, (224, 224))
            thread_data.L = split(thread_data.resized)[0]
            thread_data.L -= 50

            net.setInput(blobFromImage(thread_data.L))
            thread_data.ab = net.forward()[0, :, :, :].transpose((1, 2, 0))

            thread_data.ab = resize(thread_data.ab, (
                thread_data.image.shape[1], thread_data.image.shape[0]))

            thread_data.L = split(thread_data.lab)[0]
            thread_data.colorized = concatenate(
                (thread_data.L[:, :, newaxis], thread_data.ab), axis=2)

            thread_data.colorized = cvtColor(
                thread_data.colorized, COLOR_LAB2RGB)
            thread_data.colorized = clip(thread_data.colorized, 0, 1)

            thread_data.colorized = \
                (255 * thread_data.colorized).astype('uint8')

            img = numpy_array_to_qt_image(thread_data.colorized)
            self.ui.result_label.pixmap = QPixmap.from_image(img)
            self.ui.result_scroll_area.visible = True
            self.ui.save_action.enabled = True
            self.ui.save_as_action.enabled = True
        except (Exception, RuntimeError) as e:
            thread_data.success = False
            QMessageBox.critical(
                self, 'Ошибка при окраске изображения',
                f'Произошла непредвиденная ошибка: {e}')

        self.ui.statusbar.clear_message()
        self.ui.progressbar.visible = False

        self.ui.file_menu.enabled = True
        self.ui.statusbar.show_message(
            'Изображение успешно окрашено'
            if thread_data.success
            else 'При окраске изображения произошла ошибка',
            2000)

    @Slot()
    def colorize(self):
        self.ui.colorize_button.enabled = False
        self.ui.file_menu.enabled = False
        self.ui.statusbar.show_message('Идёт окраска изображения...')
        self.ui.progressbar.visible = True
        self.background_thread = Thread(None, self.colorize_implementation)
        self.background_thread.start()

    @Slot()
    def about(self):
        QMessageBox.about(
            self,
            'Раскрашиватель фотографий',
            'Версия 1.0, 28.12.2021')


if __name__ == '__main__':
    prototxt = join(
        dirname(__file__), 'model', 'colorization_deploy_v2.prototxt')
    model = join(
        dirname(__file__), 'model', 'colorization_release_v2.caffemodel')
    if not isfile(prototxt) or not isfile(model):
        QMessageBox.critical(
            None, 'Отсутствуют файлы модели',
            'Не хватает некоторых файлов')
        exit()

    net = readNetFromCaffe(prototxt, model)

    points = resource_to_bytes_io(':/model/model/pts_in_hull.npy')
    pts = load(points)
    points.close()

    class8 = net.getLayerId('class8_ab')
    conv8 = net.getLayerId('conv8_313_rh')
    pts = pts.transpose().reshape(2, 313, 1, 1)
    net.getLayer(class8).blobs = [pts.astype('float32')]
    net.getLayer(conv8).blobs = [full([1, 313], 2.606, dtype='float32')]

    app = QApplication(['Раскрашиватель фотографий'])
    widget = MainWindow()
    widget.show()
    exit(app.exec())
