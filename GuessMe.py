import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time
import GuessMe_lib
import GuessMeGui

lvl_chances = {"1": "10", "2": "100"}
lvl = None
rand_no = None
attempts_left = None


class MW(QMainWindow, GuessMeGui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MW, self).__init__(parent)
        self.setupUi(self)

        self.Help.setText("The GuessMe game is a game full of fun. "
                          "\nThe main objective of the game is to correctly "
                          "\n identify the random number that the computer has guessed."
                          "\n There are two levels."
                            "\n  (i)  Random No range 1-10"
                                "\n    Guess Available 5"
                            "\n  (ii) Random No range 1-100"
                                "\n    Guess Available 10"
                          "\nYou have to guess the correct number before "
                          "\nyou run out of attempts.")

        # Menu Bar Connection
        self.connect(self.actionStart, SIGNAL("triggered()"), self.start_game)
        self.connect(self.actionMain_Menu, SIGNAL("triggered()"), self.main_menu)
        self.connect(self.actionHelp, SIGNAL("triggered()"), self.help)
        self.connect(self.actionExit, SIGNAL("triggered()"), self.exit)
        # Main Frame Connection
        self.connect(self.pushButton_Start, SIGNAL("clicked()"), self.start_game)
        self.connect(self.pushButton_Help, SIGNAL("clicked()"), self.help)
        self.connect(self.pushButton_Exit, SIGNAL("clicked()"), self.exit)
        # Help Frame Connection
        self.connect(self.pushButton_Help_back, SIGNAL("clicked()"), self.helpback)
        # Game Frame Connection
        self.connect(self.lineEdit_EnterValue, SIGNAL("returnPressed()"), self.game)
        # End Frame Connection
        self.connect(self.pushButton_MainMenu, SIGNAL("clicked()"), self.main_menu)
        self.connect(self.pushButton_Start_2, SIGNAL("clicked()"), self.start_game)
        self.connect(self.pushButton_Exit_2, SIGNAL("clicked()"), self.exit)

    def game(self):

        global attempts_left
        global rand_no
        global lvl

        entered_value = self.lineEdit_EnterValue.text()
        self.lineEdit_EnterValue.clear()
        attempts_left = int(attempts_left) - 1
        self.label_Attempt.setText("Attempts Left: " + str(attempts_left))
        # print lvl_chances[str(lvl)]
        check_result = GuessMe_lib.check(rand_no, int(entered_value))
        if check_result[0] == True:
            lvl += 1
            """
            lvl = lvl + 1
            self.stackedWidget.setCurrentIndex(2)
            self.Win_Lost.setText("You Won")
            """
            self.Number_CorrectWrong.setText("\t CORRECT.... ")
            if lvl <= 2:
                x = 0
                while x < 100:
                    x += 0.001
                    self.progressBar_2.setValue(x)
                self.progressBar_2.setValue(0)
                time.sleep(1)

                rand_no, attempts_left = GuessMe_lib.set_game(lvl, lvl_chances[str(lvl)])
                self.stackedWidget.setCurrentIndex(1)
                self.label_Attempt.setText("Attempts Left: " + str(attempts_left))
                self.label_Level.setText("Level: " + str(lvl))
                self.label_Range.setText("Range: " + str(lvl_chances[str(lvl)]))
                self.Number_CorrectWrong.setText("  ")

            else:
                self.stackedWidget.setCurrentIndex(2)
                self.Win_Lost.setText("You Won")
        elif check_result[0] == False:
            if check_result[1] == "less":
                self.Number_CorrectWrong.setText("Too small, the Number is larger ")
            elif check_result[1] == "greater":
                self.Number_CorrectWrong.setText("Too large, the Number is smaller ")

        if attempts_left == 0:
            self.stackedWidget.setCurrentIndex(2)
            self.Win_Lost.setText("You Lost")

    def start_game(self):
        global lvl
        global rand_no
        global attempts_left
        lvl = 1

        x = 0
        while x < 100:
            x += 0.001
            self.progressBar.setValue(x)
        self.progressBar.setValue(0)

        rand_no, attempts_left = GuessMe_lib.set_game(lvl, lvl_chances[str(lvl)])
        self.stackedWidget.setCurrentIndex(1)
        self.label_Attempt.setText("Attempts Left: " + str(attempts_left))
        self.label_Level.setText("Level: " + str(lvl))
        self.label_Range.setText("Range: " + str(lvl_chances[str(lvl)]))
        self.Number_CorrectWrong.setText(" ")

    def main_menu(self):
        self.stackedWidget.setCurrentIndex(0)

    def help(self):
        self.stackedWidget.setCurrentIndex(3)

    def helpback(self):
        self.stackedWidget.setCurrentIndex(0)

    def exit(self):
        # print "Exit"
        x = 0
        while x < 100:
            x += 0.001
            self.progressBar.setValue(x)
        app.exit()


app = QApplication(sys.argv)
form = MW()
form.show()
app.exec_()
