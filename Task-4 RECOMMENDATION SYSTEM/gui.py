import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QTextEdit, QLabel, QMessageBox
from PyQt5.QtGui import QFont

from movie_recommendation import recommend_movies

class MovieRecommender(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 550)
        self.setWindowTitle('Movie Recommendation System')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.title = QLabel('Enter your Favourite Movie')
        self.title.setFont(QFont("Arial", 16))
        self.layout.addWidget(self.title)

        self.movieInput = QLineEdit(self)
        self.movieInput.setFont(QFont("Arial", 14))
        self.layout.addWidget(self.movieInput)

        self.btn = QPushButton('Recommend', self)
        self.btn.setFont(QFont("Arial", 14))
        self.btn.clicked.connect(self.recommendMovies)
        self.layout.addWidget(self.btn)
        
        self.movieInput.returnPressed.connect(self.btn.click)

        self.textDisplay = QTextEdit(self)
        self.textDisplay.setFont(QFont("Arial", 14))
        self.textDisplay.setReadOnly(True)
        self.layout.addWidget(self.textDisplay)

    def recommendMovies(self):
        movie_name = self.movieInput.text()
        
        # Check if the input is empty
        if not movie_name.strip():
            QMessageBox.information(self, 'Input Error', "Please enter a movie name")
            return

        recommended_movies = recommend_movies(movie_name)
        self.textDisplay.setText("\n".join(recommended_movies[:20]))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MovieRecommender()
    ex.show()
    sys.exit(app.exec_())
