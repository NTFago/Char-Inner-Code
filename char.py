import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from ui_form import Ui_Char_encode
import logging, datetime

def start_log():    # 日志
    import os
    now_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    if os.path.exists(".\\logs"):
        logging.basicConfig(level=logging.INFO, filename=".\\logs\\{}.log".format(now_time), 
                            format='%(asctime)s: %(levelname)s: %(message)s')
    else:
        os.mkdir(".\\logs")
    logging.info("Program started successfully.")

class Char_Encode(QMainWindow, Ui_Char_encode):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 文件路径
        self.file = None

        # 编码
        self.encoding_type = {
            "Unicode(UTF-16-LE)": "UTF-16-LE",
            "Unicode big endian(UTF-16-BE)": "UTF-16-BE",
            "UTF-8": "UTF-8",
            "UTF-8 with BOM(UTF-8-sig)": "UTF-8-SIG",
            "ANSI(GBK)": "GBK"
        }

        # 绑定信号与槽函数
        self.pbtn_choose.clicked.connect(self.choose_file)
        self.pbtn_check.clicked.connect(self.check)

        # 显示窗口
        self.show()
        logging.info("Ui has been showed.")
    # 选择文件
    def choose_file(self):
        file_path = QFileDialog.getOpenFileName(caption="选择文件", filter="*.txt")
        if file_path[0]:
            self.file = file_path[0]
            self.lb_path.setText("文件路径:"+self.file)
            logging.info("File path:{}.".format(file_path[0]))
        else:
            QMessageBox.warning(self, "注意", "请重新选择文本文档")

    def check(self):
        try:
        # 有文件
            if self.file:
                self.encoding = self.encoding_type[self.cb_encode.currentText()]
                logging.info("Encoding has been chosen as {}".format(self.encoding))
                # 读文件
                with open(self.file, "r", encoding=self.encoding) as f:
                    contents = f.readlines()
                # 处理文本
                txts = []
                for i in contents:
                    s = i.strip()
                    txts.append(s)
                txt = "\n".join(txts)
                logging.info("The contents of the file are '{}'".format(txt))
                self.get_inner_code(txt)
                self.file = None
                self.lb_path.setText("文件路径:")

            elif self.te_text.toPlainText():
                txts = self.te_text.toPlainText()
                logging.info("The user entered '{}'".format(txts))
                self.encoding = self.encoding_type[self.cb_encode.currentText()]
                logging.info("Encoding has been chosen as {}".format(self.encoding))
                self.get_inner_code(txts)
        except Exception as e:
            QMessageBox.warning(self, "注意", "出现了一点小意外，请重试。")
            logging.error(e)

    # 获取内码
    def get_inner_code(self, txt):
        self.te_text.setText(txt)
        inner_code = txt.encode(encoding=self.encoding)
        inner_code = str(inner_code).replace("b", "").replace("\'", "").split("\\x")
        if "" in inner_code:
            inner_code.remove("")
        inner_code = "\t".join(inner_code)
        self.te_encode.setText(inner_code)
        logging.info("Inner code has been displayed.")
        logging.info("Inner code is {}".format(inner_code))


if __name__ == "__main__":
    try:
        start_log()
        app = QApplication(sys.argv)
        window = Char_Encode()
        sys.exit(app.exec_())
    except Exception as e:
        logging.error("Unexpected error: {}".format(e))