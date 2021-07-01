import sys
from des import *
from sort import *
from save import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._PATH_TO_FILE_1 = None
        self._PATH_TO_FILE_2 = None

        # Указание пути для первого файла
        self.ui.pushButton.clicked.connect(self.set_first_path)
        # Указание пути для второго файла
        self.ui.pushButton_2.clicked.connect(self.set_second_path)

        # Начало процесса слияния
        self.ui.pushButton_3.clicked.connect(self.start_process)

    # Выбор пути первого файла
    def set_first_path(self):
        self._PATH_TO_FILE_1 = QFileDialog.getOpenFileName(self, 'Выберете файл', '', '*.xlsx')
        self.ui.lineEdit.setText(f'{self._PATH_TO_FILE_1[0]}')

    # Выбор пути второго файла
    def set_second_path(self):
        self._PATH_TO_FILE_2= QFileDialog.getOpenFileName(self, 'Выберете файл', '', '*.xlsx')
        self.ui.lineEdit_2.setText(f'{self._PATH_TO_FILE_2[0]}')

    # Функция слияния и сохранения
    def start_process(self):
        # Проверка ссылок на файлы
        if (self._PATH_TO_FILE_1 and self._PATH_TO_FILE_2) == None:
            self.notifications(404)
            return
        # Выбор пути сохранения
        file_path = QFileDialog.getSaveFileName(self, 'Сохранить результат как', '', '*xlsx')

        self.ui.pushButton_3.setEnabled(False)
        self.ui.label_3.setText('Идет процесс слияния...')

        # Передаем файлы на слияние
        result = sort(self._PATH_TO_FILE_1, self._PATH_TO_FILE_2)

        self.ui.pushButton_3.setEnabled(True)

        if result[0] != 200:
            self.notifications(result[0])
            self.ui.label_3.setText('Попробуйте еще раз')
            return

        status_code = save_table(result[1], file_path)
        self.notifications(status_code)

        self.ui.pushButton_3.setEnabled(True)
        self.ui.label_3.setText('Готово')

    # Функция оповещения
    def notifications(self, status_code):
        if status_code == 200:
            QMessageBox.information(self, 'Оповещение', 'Файл преобразован и успешно сохранен!')
        elif status_code == 404:
            QMessageBox.warning(self, 'Внимание', 'Выберете оба файла, прежде начала'
                                                  ' операции слияния.')
        elif status_code == 503:
            QMessageBox.critical(self, 'Ошибка', 'При сохранении файла произошла ошибка')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())