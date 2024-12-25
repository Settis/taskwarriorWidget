#!/usr/bin/env python3

import sys
from tw.app import TWTrayApp
from tw.statusGetter import TWCheck

app = TWTrayApp(sys.argv, TWCheck(), 60)
sys.exit(app.exec())
