# This Python file uses the following encoding: utf-8

from io import BytesIO
from numpy import ndarray, uint8
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtGui import QImage, qRgb

from __feature__ import snake_case, true_property


def resource_to_bytes_io(resource: str):
    qfile = QFile(resource)
    qfile.open(QIODevice.ReadOnly)
    bytes_stream = BytesIO(bytes(qfile.read_all().data()))
    qfile.close()
    return bytes_stream


def numpy_array_to_qt_image(im: ndarray):
    gray_color_table = [qRgb(i, i, i) for i in range(256)]
    if im is None:
        return QImage()
    if im.dtype == uint8:
        if len(im.shape) == 2:
            qim = QImage(
                im.data,
                im.shape[1], im.shape[0], im.strides[0],
                QImage.Format_Indexed8)
            qim.setColorTable(gray_color_table)
            return qim
        elif len(im.shape) == 3:
            if im.shape[2] == 3:
                qim = QImage(
                    im.data,
                    im.shape[1], im.shape[0], im.strides[0],
                    QImage.Format_RGB888)
                return qim
            elif im.shape[2] == 4:
                qim = QImage(
                    im.data,
                    im.shape[1], im.shape[0], im.strides[0],
                    QImage.Format_ARGB32)
                return qim
