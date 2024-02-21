from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


#
# Window for dynamic plotting train & val losses
#

class PlotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Обучение нейросети")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.losses = []
        self.val_losses = []

        # Создаем график
        self.plot()

    def plot(self):
        self.figure.clear()

        # Строим график
        ax = self.figure.add_subplot()
        ax.plot(self.losses, color='blue', label='Training Loss')
        ax.plot(self.val_losses, color='red', label='Validation Loss')
        ax.set_xlabel('Epoch')
        ax.set_ylabel('Loss')
        ax.set_title('График обучения')
        ax.legend()

        # Обновляем холст
        self.canvas.draw()

    def update_plot(self, loss, val_loss):
        self.losses.append(loss)
        self.val_losses.append(val_loss)
        self.plot()
