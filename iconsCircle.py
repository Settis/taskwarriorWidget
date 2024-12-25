import sys
from tw.app import TWTrayApp
from tw.circleStatusGetter import StatusGetter

app = TWTrayApp(sys.argv, StatusGetter(), 1)
sys.exit(app.exec())

