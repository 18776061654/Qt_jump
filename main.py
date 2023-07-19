import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Signal

class MainWindow(QUiLoader):
    closed = Signal()


    def __init__(self, ui_file):
        super().__init__()
        self.ui = self.load(ui_file)

        self.ui.RealTimeBtn.clicked.connect(self.realtime_clicked)
        self.ui.SelectVideoBtn.clicked.connect(self.selectvideo_clicked)
        self.ui.SettingBtn.clicked.connect(self.setting_clicked)


    def closeEvent(self, event):
        print("Main window closed!")
        self.closed.emit()
        event.accept()

    def realtime_clicked(self):
        print("实时检测按钮clicked")

    def selectvideo_clicked(self):
        print("选择视频按钮clicked")
        
        # 加载选择视频窗口UI
        self.select_window = QUiLoader().load('./resources/SelectVideoWindow.ui') 
        # 连接closed信号
        
        self.closed.connect(self.select_window.close) 
    
        # 显示窗口 
        self.select_window.show()

    def setting_clicked(self):
        print("设置按钮clicked")

        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file = QFile("./resources/main.ui")
    ui_file.open(QFile.ReadOnly)

    main_window = MainWindow(ui_file) 
    main_window.ui.show()

    sys.exit(app.exec())