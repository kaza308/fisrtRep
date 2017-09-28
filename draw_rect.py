#coding=utf-8

# import sys, math
# from PyQt5 import QtCore, QtGui, QtWidgets

# class MyWidget(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         QtWidgets.QWidget.__init__(self, parent)
#         self.pen = QtGui.QPen(QtGui.QColor(0,0,0))                      # set lineColor
#         self.pen.setWidth(3)                                            # set lineWidth
#         self.brush = QtGui.QBrush(QtGui.QColor(255,255,255,255))        # set fillColor
#         self.polygon = self.createPoly(8,150,0)                         # polygon with n points, radius, angle of the first point
#
#     def createPoly(self, n, r, s):
#         polygon = QtGui.QPolygonF()
#         w = 360/n                                                       # angle per step
#         for i in range(n):                                              # add the points of polygon
#             t = w*i + s
#             x = r*math.cos(math.radians(t))
#             y = r*math.sin(math.radians(t))
#             polygon.append(QtCore.QPointF(self.width()/2 +x, self.height()/2 + y))
#
#         return polygon
#
#     def paintEvent(self, event):
#         painter = QtGui.QPainter(self)
#         painter.setPen(self.pen)
#         painter.setBrush(self.brush)
#         painter.drawPolygon(self.polygon)
#
# app = QtWidgets.QApplication(sys.argv)
#
# widget = MyWidget()
# widget.show()
#
# sys.exit(app.exec_())

import sys, random
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *

draw_box=[0,0,0,0]
class Example(QtGui.QWidget):
    global draw_box
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        super(Example, self).__init__()
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Points')
        self.lastpoint=None
        self.endpoint=None
        # self.pixmap_image=QImage()
        self.label_imageDisplay = QLabel()
        view=QGraphicsScene(self)

        # if self.pixmap_image.load("/home/kaza/who.jpg"):
        #     self.label_imageDisplay.setPixmap(QPixmap.fromImage(self.pixmap_image))
        self.pixmap_image = QtGui.QPixmap("who.jpg")
        self.drawflag=False
        # create painter instance with pixmap
        self.painterInstance = QtGui.QPainter(self.pixmap_image)

        # set rectangle color and thickness
        # self.penRectangle = QtGui.QPen(QtCore.Qt.red)
        # # self.penRedBorder.setWidth(3)
        #
        # # draw rectangle on painter
        # self.painterInstance.setPen(self.penRectangle)
        # self.painterInstance.drawRect(100,100,200,200)
        #
        # # set pixmap onto the label widget
        # self.label_imageDisplay.setPixmap(self.pixmap_image)
        # self.label_imageDisplay.show()

    def paint(self):
        self.penRectangle = QtGui.QPen(QtCore.Qt.red)
        # self.penRedBorder.setWidth(3)

        # draw rectangle on painter
        self.painterInstance.setPen(self.penRectangle)
        self.painterInstance.drawLine(self.lastpoint, self.endpoint)
        # painter.drawLine(self.lastpoint, self.endpoint)
        self.lastpoint = self.endpoint
        self.update()
        # set pixmap onto the label widget
        self.label_imageDisplay.setPixmap(self.pixmap_image)
        self.label_imageDisplay.show()
        self.update()

    def draw(self):
        painter=QPainter()
        pen=QPen()
        pen.setWidth(2)
        pen.setColor(QColor(0,0,255))
        # painter.begin()
        painter.drawLine(self.lastpoint,self.endpoint)
        self.lastpoint=self.endpoint
        self.update()

    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            # draw_box[0]=event.x()
            # draw_box[1]=event.y()
            self.lastpoint=event.pos()
            self.lastpoint=event.pos()
            print "press",draw_box

    def mouseMoveEvent(self, event):
        print "current axis is :",event.x(),event.y()
        # draw_box[2] = event.x()
        # draw_box[3] = event.y()
        self.endpoint = event.pos()
        self.endpoint = event.pos()
        self.paint()



    def mouseReleaseEvent(self, event):
        if event.button()==Qt.LeftButton:

            print "rel",draw_box
            # self.paint()
    #
    # def paintEvent(self, e):
    #     qp = QtGui.QPainter()
    #     qp.begin(self)
    #     self.draw_rect(qp,draw_box)
    #     # qp.setPen(QtCore.Qt.red)
    #     # size = self.size()
    #     # qp.drawPoint(e.x(), e.y())
    #     qp.end()
    #
    # def draw_rect(self,qp,box):
    #     qp.setPen(QtCore.Qt.red)
    #     size = self.size()
    #     qp.drawRect(box[0],box[1],box[2],box[3])
        # for i in range(1000):
        #     x = random.randint(1, size.width() - 1)
        #     y = random.randint(1, size.height() - 1)
        #     qp.drawPoint(x, y)

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QGraphicsView):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # 创建场景
        self.draw_box=[0,0,0,0]
        self.resize(1080,760)
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0,0,1080,760)
        self.graphicItem=None
        # 在场景中添加文字
        # self.scene.addText("Hello, world!")
    def draw(self,box):
        self.pen=QPen()
        self.pen.setColor(QColor(0,255,0))
        rect=QRectF(box[0],box[1],box[2]-box[0],box[3]-box[1])
        self.graphicItem=self.scene.addRect(rect,self.pen)
        # 将场景加载到窗口
        self.setScene(self.scene)
        self.scene.update()
    def remove(self,item):
        self.scene.removeItem(item)

    def mouseMoveEvent(self, event):
        self.remove(self.graphicItem)
        print "current axis is :",event.x(),event.y()
        self.draw_box[2] = event.x()
        self.draw_box[3] = event.y()
        self.draw(self.draw_box)
        self.scene.update()

    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.draw_box[0]=event.x()
            self.draw_box[1]=event.y()

            print "press",self.draw_box

    def mouseReleaseEvent(self, event):
        if event.button()==Qt.LeftButton:

            print "rel",self.draw_box

if __name__ == '__main__':
    import sys
    # 每个PyQt程序必须创建一个application对象，sys.argv 参数是命令行中的一组参数
    # 注意：application在 PyQt5.QtWidgets 模块中
    # 注意：application在 PyQt4.QtGui 模块中
    app = QApplication(sys.argv)
    # 创建桌面窗口
    mainWindow = MainWindow()
    # 显示桌面窗口
    mainWindow.show()
    sys.exit(app.exec_())
    # app = QtGui.QApplication(sys.argv)
    # ex = Example()
    # ex.show()
    # sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
