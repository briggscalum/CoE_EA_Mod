import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MyMplCanvas(FigureCanvas):
    """A simple canvas that has a matplotlib figure drawn onto it."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MyMplCanvas, self).__init__(fig)

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the matplotlib canvas
        self.canvas = MyMplCanvas(self, width=5, height=4, dpi=100)
        self.canvas.axes.plot([0, 1, 2, 3], [1, 2, 0, 4])  # Example plot

        # Create a QWidget that will be the central widget and set a layout to it
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        layout = QVBoxLayout()  # Use QVBoxLayout, QHBoxLayout, QGridLayout as needed
        layout.addWidget(self.canvas)

        # If you have other widgets, add them to the layout as well
        # layout.addWidget(other_widget)

        self.centralWidget.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MyMainWindow()
    mainWin.show()
    sys.exit(app.exec_())