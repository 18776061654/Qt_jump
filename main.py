import sys
import speed.Speed as Speed
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Signal

class MainWindow(QUiLoader):
    closed = Signal()


    def __init__(self):
        super().__init__()

        ui_file = QFile("./resources/main.ui")  
        ui_file.open(QFile.ReadOnly)
        self.ui = self.load(ui_file)

        self.ui.RealTimeBtn.clicked.connect(self.realtime_clicked)
        self.ui.SelectVideoBtn.clicked.connect(self.selectvideo_clicked)
        self.ui.SettingBtn.clicked.connect(self.setting_clicked)



    def realtime_clicked(self):
        print("实时检测按钮")

    def selectvideo_clicked(self):
        print("选择视频按钮")
        
        # 加载选择视频窗口UI
        self.select_window =SelectVideoWindow()
        
        self.select_window.show()

    def setting_clicked(self):
        print("设置按钮")

class SelectVideoWindow(QUiLoader):
  def __init__(self):
    super().__init__()
    ui_file = QFile('./resources/SelectVideoWindow.ui')
    ui_file.open(QFile.ReadOnly) 
    self.ui = self.load(ui_file)

  def show(self):
    self.ui.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow() 
    main_window.ui.show()

    sys.exit(app.exec())