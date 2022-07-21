# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Char_encode(object):
    def setupUi(self, Char_encode):
        if not Char_encode.objectName():
            Char_encode.setObjectName(u"Char_encode")
        Char_encode.resize(800, 600)
        self.lb_title = QLabel(Char_encode)
        self.lb_title.setObjectName(u"lb_title")
        self.lb_title.setGeometry(QRect(250, 10, 231, 41))
        font = QFont()
        font.setPointSize(25)
        self.lb_title.setFont(font)
        self.layoutWidget = QWidget(Char_encode)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 60, 551, 51))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_path = QLabel(self.layoutWidget)
        self.lb_path.setObjectName(u"lb_path")
        font1 = QFont()
        font1.setPointSize(15)
        self.lb_path.setFont(font1)

        self.horizontalLayout.addWidget(self.lb_path)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pbtn_choose = QPushButton(self.layoutWidget)
        self.pbtn_choose.setObjectName(u"pbtn_choose")
        self.pbtn_choose.setFont(font1)
        self.pbtn_choose.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.pbtn_choose)

        self.lb_encode = QLabel(Char_encode)
        self.lb_encode.setObjectName(u"lb_encode")
        self.lb_encode.setGeometry(QRect(20, 120, 91, 31))
        self.lb_encode.setFont(font1)
        self.cb_encode = QComboBox(Char_encode)
        self.cb_encode.addItem("")
        self.cb_encode.addItem("")
        self.cb_encode.addItem("")
        self.cb_encode.addItem("")
        self.cb_encode.addItem("")
        self.cb_encode.setObjectName(u"cb_encode")
        self.cb_encode.setGeometry(QRect(110, 120, 461, 31))
        self.cb_encode.setFont(font1)
        self.lb_text = QLabel(Char_encode)
        self.lb_text.setObjectName(u"lb_text")
        self.lb_text.setGeometry(QRect(20, 170, 91, 31))
        self.lb_text.setFont(font1)
        self.te_text = QTextEdit(Char_encode)
        self.te_text.setObjectName(u"te_text")
        self.te_text.setGeometry(QRect(110, 170, 461, 181))
        font2 = QFont()
        font2.setPointSize(12)
        self.te_text.setFont(font2)
        self.label = QLabel(Char_encode)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 360, 91, 31))
        self.label.setFont(font1)
        self.te_encode = QTextEdit(Char_encode)
        self.te_encode.setObjectName(u"te_encode")
        self.te_encode.setGeometry(QRect(110, 360, 461, 171))
        self.te_encode.setFont(font2)
        self.te_encode.setReadOnly(True)
        self.line = QFrame(Char_encode)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(580, 30, 20, 561))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.te_tip = QTextEdit(Char_encode)
        self.te_tip.setObjectName(u"te_tip")
        self.te_tip.setGeometry(QRect(600, 30, 191, 561))
        self.te_tip.setReadOnly(True)
        self.pbtn_check = QPushButton(Char_encode)
        self.pbtn_check.setObjectName(u"pbtn_check")
        self.pbtn_check.setGeometry(QRect(490, 540, 81, 31))
        self.pbtn_check.setFont(font2)

        self.retranslateUi(Char_encode)

        QMetaObject.connectSlotsByName(Char_encode)
    # setupUi

    def retranslateUi(self, Char_encode):
        Char_encode.setWindowTitle(QCoreApplication.translate("Char_encode", u"\u5b57\u7b26\u5185\u7801\u67e5\u770b\u5668", None))
        self.lb_title.setText(QCoreApplication.translate("Char_encode", u"\u5b57\u7b26\u5185\u7801\u67e5\u770b\u5668", None))
        self.lb_path.setText(QCoreApplication.translate("Char_encode", u"\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.pbtn_choose.setText(QCoreApplication.translate("Char_encode", u"\u9009\u62e9\u6587\u4ef6", None))
        self.lb_encode.setText(QCoreApplication.translate("Char_encode", u"\u7f16\u7801\u683c\u5f0f\uff1a", None))
        self.cb_encode.setItemText(0, QCoreApplication.translate("Char_encode", u"Unicode(UTF-16-LE)", None))
        self.cb_encode.setItemText(1, QCoreApplication.translate("Char_encode", u"Unicode big endian(UTF-16-BE)", None))
        self.cb_encode.setItemText(2, QCoreApplication.translate("Char_encode", u"UTF-8", None))
        self.cb_encode.setItemText(3, QCoreApplication.translate("Char_encode", u"UTF-8 with BOM(UTF-8-sig)", None))
        self.cb_encode.setItemText(4, QCoreApplication.translate("Char_encode", u"ANSI(GBK)", None))

        self.lb_text.setText(QCoreApplication.translate("Char_encode", u"\u6587\u672c\uff1a", None))
        self.label.setText(QCoreApplication.translate("Char_encode", u"\u5b57\u7b26\u5185\u7801\uff1a", None))
        self.te_tip.setHtml(QCoreApplication.translate("Char_encode", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#5500ff;\">\u4f7f\u7528\u8bf4\u660e\uff1a</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#0000ff;\">\u672c\u5e94\u7528\u652f\u6301\u8f93\u5165\u6587\u672c\u6216\u6253\u5f00\u5df2\u7ecf\u7f16\u8f91\u597d\u7684\u6587\u672c\uff0c\u4f46\u4e24\u8005\u4e0d\u53ef\u540c\u65f6\u4f7f\u7528\u3002\u5728\u6709\u6587\u672c\u88ab\u6253\u5f00\u65f6\uff0c\u4f18\u5148\u8f93"
                        "\u51fa\u6587\u672c\u7684\u5b57\u7b26\u5185\u7801</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">\u4e00\u3001\u5173\u4e8e\u6253\u5f00\u6587\u672c\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">      1.\u70b9\u51fb&quot;\u9009\u62e9\u6587\u4ef6&quot;\u6309\u94ae</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">      2.\u9009\u62e9\u8be5\u6587\u672c\u6587\u6863\u7684\u7f16\u7801\u65b9\u5f0f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">      3.\u70b9\u51fb&quot;\u67e5\u770b"
                        "&quot;\u6309\u94ae\u67e5\u770b\u5b57\u7b26\u5185\u7801\u548c\u6587\u672c</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">\u4e8c\u3001\u5173\u4e8e\u8f93\u5165\u6587\u672c\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">      1.\u5728\u6587\u672c\u5bf9\u5e94\u7684\u6846\u4e2d\u8f93\u5165\u6587\u672c</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">      2.\u9009\u62e9\u4f60\u60f3\u67e5\u770b\u7684\u7f16\u7801\u65b9\u5f0f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">     "
                        " 3.\u70b9\u51fb&quot;\u67e5\u770b&quot;\u6309\u94ae\u67e5\u770b\u5b57\u7b26\u5185\u7801</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">\u4e09\u3001\u4f5c\u8005\uff1a\u8427\u57a3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">       B\u7ad9\u53f7\uff1aSUS\u4e36\u57ce\u57a3 \u6b22\u8fce\u6765\u8bbf~</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">\u56db\u3001\u5173\u4e8eBUG\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#000000;\">       \u53ef\u628alogs\u6587\u4ef6\u5939\u4e0b\u7684"
                        "log\u6587\u4ef6\u53d1\u5f80\u90ae\u7bb12330153227@qq.com\u5e76\u7559\u4e0b\u8054\u7cfb\u65b9\u5f0f\uff0c\u4f5c\u8005\u4f1a\u5c3d\u5feb\u8054\u7cfb\u60a8</span></p></body></html>", None))
        self.pbtn_check.setText(QCoreApplication.translate("Char_encode", u"\u67e5\u770b", None))
    # retranslateUi

