from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QTimer
from tw.statusGetter import TWCheck
from tw.icon import get_icon


class TWTrayApp(QApplication):
    def __init__(self, argv, checker: TWCheck, delay_sec: int):
        super().__init__(argv)
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setToolTip("TW tasks")
        self.checker = checker
        self.last_status = None
        self.update_tray_icon()
        
        menu = QMenu()
        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self.quit)
        menu.addAction(quit_action)
        self.tray_icon.setContextMenu(menu)

        timer = QTimer(self)
        timer.timeout.connect(self.update_tray_icon)
        timer.start(delay_sec * 1000)

        self.tray_icon.show()

    def update_tray_icon(self):
        status = self.checker.get_status()
        if status != self.last_status:
            self.tray_icon.setIcon(get_icon(status))
            self.tray_icon.setToolTip(f"TW tasks: {status.tasks_count}")
            self.last_status = status
