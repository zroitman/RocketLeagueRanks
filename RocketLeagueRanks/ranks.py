from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import keyboard
import os
import re
import sys
import requests
import json

# 76561198871336776

class Ui_rocketleagueranks(object):
    def setupUi(self, rocketleagueranks):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        rocketleagueranks.setObjectName("rocketleagueranks")
        rocketleagueranks.resize(700, 498)
        self.centralwidget = QtWidgets.QWidget(rocketleagueranks)
        self.centralwidget.setObjectName("centralwidget")
        self.playerName = QtWidgets.QLineEdit(self.centralwidget)
        self.playerName.setGeometry(QtCore.QRect(155, 20, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.playerName.setFont(font)
        self.playerName.setToolTip("")
        self.playerName.setStatusTip("")
        self.playerName.setInputMask("")
        self.playerName.setText("")
        self.playerName.setMaxLength(20)
        self.playerName.setAlignment(QtCore.Qt.AlignCenter)
        self.playerName.setObjectName("playerName")
        self.playerName.returnPressed.connect(self.search_player)
        self.labelDivision = QtWidgets.QLabel(self.centralwidget)
        self.labelDivision.setGeometry(QtCore.QRect(20, 137, 261, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelDivision.setFont(font)
        self.labelDivision.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDivision.setObjectName("labelDivision")
        self.labelDivisionRank = QtWidgets.QLabel(self.centralwidget)
        self.labelDivisionRank.setGeometry(QtCore.QRect(20, 190, 261, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelDivisionRank.setFont(font)
        self.labelDivisionRank.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDivisionRank.setObjectName("labelDivisionRank")
        self.favorites = QtWidgets.QComboBox(self.centralwidget)
        self.favorites.setGeometry(QtCore.QRect(155, 71, 130, 20))
        self.favorites.setEditable(False)
        self.favorites.setCurrentText("")
        self.favorites.setObjectName("favorites")
        self.favorites.addItem('Favorites')
        with open(os.path.join(self.base_dir, 'resources', 'favorites.json'), 'r') as fav:
            favorites_l = json.load(fav)
        self.favorites.addItems(favorites_l)
        self.favorites.activated.connect(self.fill_in_favorite)
        self.labelRank = QtWidgets.QLabel(self.centralwidget)
        self.labelRank.setGeometry(QtCore.QRect(416, 137, 261, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelRank.setFont(font)
        self.labelRank.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelRank.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelRank.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRank.setObjectName("labelRank")
        self.labelRankRank = QtWidgets.QLabel(self.centralwidget)
        self.labelRankRank.setGeometry(QtCore.QRect(416, 190, 261, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelRankRank.setFont(font)
        self.labelRankRank.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRankRank.setObjectName("labelRankRank")
        self.imageDivision = QtWidgets.QLabel(self.centralwidget)
        self.imageDivision.setGeometry(QtCore.QRect(20, 250, 251, 191))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(140)
        font.setItalic(False)
        self.imageDivision.setFont(font)
        self.imageDivision.setAlignment(QtCore.Qt.AlignCenter)
        self.imageDivision.setObjectName("imageDivision")
        self.imageRank = QtWidgets.QLabel(self.centralwidget)
        self.imageRank.setGeometry(QtCore.QRect(416, 230, 256, 256))
        self.imageRank.setText("")
        self.imageRank.setPixmap(QtGui.QPixmap(os.path.join(self.base_dir, 'resources', 'imgs', 'unranked.png')))
        self.imageRank.setScaledContents(True)
        self.imageRank.setObjectName("imageRank")
        self.labelError = QtWidgets.QLabel(self.centralwidget)
        self.labelError.setEnabled(True)
        self.labelError.setGeometry(QtCore.QRect(220, 110, 231, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 7, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 105, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 52, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 7, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 7, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 7, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 105, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 52, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 7, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 7, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 7, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 105, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 52, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 7, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 7, 7))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.labelError.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelError.setFont(font)
        self.labelError.setStyleSheet("color: rgb(255, 7, 7);")
        self.labelError.setObjectName("labelError")
        self.labelError.setAlignment(QtCore.Qt.AlignCenter)
        self.labelError.hide()
        self.comboPlatform = QtWidgets.QComboBox(self.centralwidget)
        self.comboPlatform.setGeometry(QtCore.QRect(431, 70, 105, 22))
        self.comboPlatform.setObjectName("comboPlatform")
        self.comboPlatform.addItems(['Choose Platform', 'Steam', 'Xbox', 'PS'])
        self.comboMode = QtWidgets.QComboBox(self.centralwidget)
        self.comboMode.setGeometry(QtCore.QRect(324, 70, 90, 22))
        self.comboMode.setObjectName("comboMode")
        self.comboMode.addItems(['Choose Mode', '3s', '2s', '1s'])
        self.labelCurrentRank = QtWidgets.QLabel(self.centralwidget)
        self.labelCurrentRank.setGeometry(QtCore.QRect(270, 140, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelCurrentRank.setFont(font)
        self.labelCurrentRank.setObjectName("labelCurrentRank")
        self.currentRank = QtWidgets.QLabel(self.centralwidget)
        self.currentRank.setGeometry(QtCore.QRect(250, 190, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.currentRank.setFont(font)
        self.currentRank.setAlignment(QtCore.Qt.AlignCenter)
        self.currentRank.setObjectName("currentRank")
        rocketleagueranks.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(rocketleagueranks)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        self.menuAdd_Favorites = QtWidgets.QMenu(self.menubar)
        self.menuAdd_Favorites.setObjectName("menuAdd_Favorites")
        rocketleagueranks.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(rocketleagueranks)
        self.statusbar.setObjectName("statusbar")
        rocketleagueranks.setStatusBar(self.statusbar)
        self.actionAdd = QtWidgets.QAction(rocketleagueranks)
        self.actionAdd.setObjectName("actionAdd")
        self.actionRemove = QtWidgets.QAction(rocketleagueranks)
        self.actionRemove.setObjectName("actionRemove")
        self.menuAdd_Favorites.addAction(self.actionAdd)
        self.menuAdd_Favorites.addAction(self.actionRemove)
        self.actionAdd.triggered.connect(self.add_favorite)
        self.actionRemove.triggered.connect(self.remove_favorite)
        self.menubar.addAction(self.menuAdd_Favorites.menuAction())

        self.retranslateUi(rocketleagueranks)
        QtCore.QMetaObject.connectSlotsByName(rocketleagueranks)

    def retranslateUi(self, rocketleagueranks):
        _translate = QtCore.QCoreApplication.translate
        rocketleagueranks.setWindowTitle(_translate("rocketleagueranks", "Rocket League Ranks"))
        self.playerName.setPlaceholderText(_translate("rocketleagueranks", "Player Name"))
        self.labelDivision.setText(_translate("rocketleagueranks", "Next Divison"))
        self.labelDivisionRank.setText(_translate("rocketleagueranks", "Unranked"))
        self.favorites.setAccessibleName(_translate("rocketleagueranks", "0"))
        self.labelRank.setText(_translate("rocketleagueranks", "Next Rank"))
        self.labelRankRank.setText(_translate("rocketleagueranks", "Unranked"))
        self.imageDivision.setText(_translate("rocketleagueranks", "0"))
        self.labelError.setText(_translate("rocketleagueranks", "Error"))
        self.labelCurrentRank.setText(_translate("rocketleagueranks", "Current MMR"))
        self.currentRank.setText(_translate("rocketleagueranks", "0"))
        self.menuAdd_Favorites.setTitle(_translate("rocketleagueranks", "Favorites"))
        self.actionAdd.setText(_translate("rocketleagueranks", "Add"))
        self.actionRemove.setText(_translate("rocketleagueranks", "Remove"))

    def search_player(self):
        """
        Finds the mmr of a player through the selected mode,
        compares the mmr to the mmr rankings and changes the
        text/images of the appropriate rank/division features.
        """
        self.labelError.hide()
        platform = self.comboPlatform.currentText()
        mode = self.comboMode.currentText()
        if mode == 'Choose Mode':
            self.labelError.setText('Please select your mode')
            self.labelError.show()
            return False
        if platform == 'Choose Platform':
            self.labelError.setText('Please select your platform')
            self.labelError.show()
            return False
        ranks = {'1s': 10, '2s': 11, '3s': 13}
        rankings = get_mmr_rankings(ranks[mode])

        user = self.playerName.text()
        url = f'https://rocketleague.tracker.network/profile/mmr/steam/{user}'
        overview_page = requests.get(url)
        soup = BeautifulSoup(overview_page.text, 'lxml')
        try:
            player_id = re.search(r'\d+', soup.find('i', class_='ion-record').parent['href'])[0]
        except Exception:
            self.labelError.setText(f'Player {user} not found')
            self.labelError.show()
            return False

        live_url = 'https://rocketleague.tracker.network/live/data'
        data = json.dumps({'playerIds': [player_id]})
        live_data = requests.post(live_url, data=data).json()
        for stat in live_data['players'][0]['Stats']:
            if mode[0] in stat['Value']['Label']:
                mmr = stat['Value']['ValueInt']
                break
        last_rank = 'Grand Champion'
        last_division = 'XX'
        exit_loop = False
        for rank, divisions in rankings.items():
            for division_name, division_mmr in divisions.items():
                if type(division_mmr) == int:
                    if mmr >= division_mmr:
                        if last_division == 'Division I':
                            next_division_mmr = rankings[last_rank][last_division]
                        else:
                            next_division_mmr = rankings[rank][last_division]
                        next_rank = last_rank
                        next_division = last_division
                        exit_loop = True
                        break
                    else:
                        if division_name[-2:] == ' I':
                            last_rank = rank
                        last_division = division_name
            if exit_loop:
                break

        self.imageRank.setPixmap(QtGui.QPixmap(os.path.join(self.base_dir, 'resources', 'imgs', f'{next_rank}.png')))
        next_rank_mmr = rankings[next_rank]['Division I']
        self.labelRankRank.setText(str(next_rank_mmr))
        self.imageDivision.setText(next_division[-2:])
        self.labelDivisionRank.setText(str(next_division_mmr))
        self.currentRank.setText(str(mmr))

    def fill_in_favorite(self):
        """
        When a user selects a favorite player through the Combo Box,
        that player name will be entered in the playerName line edit
        and the function search_player will be called.
        """
        user = self.favorites.currentText()
        if user == 'Favorites':
            return None
        self.playerName.setText(user)

    def add_favorite(self):
        """
        Adds a user to the favorites json file
        """
        favorite_user = self.playerName.text()
        with open(os.path.join(self.base_dir, 'resources', 'favorites.json'), 'r') as fav:
            favorites = json.load(fav)
        favorites.append(favorite_user)
        with open(os.path.join(self.base_dir, 'resources', 'favorites.json'), 'w') as fav:
            json.dump(favorites, fav)
        self.favorites.addItem(favorite_user)

    def remove_favorite(self):
        """
        Removes a user to the favorites json file
        """
        self.labelError.hide()
        favorite_user = self.favorites.currentText()
        with open(os.path.join(self.base_dir, 'resources', 'favorites.json'), 'r') as fav:
            favorites = json.load(fav)
        if favorite_user != 'Favorites':
            favorites.remove(favorite_user)
            with open(os.path.join(self.base_dir, 'resources', 'favorites.json'), 'w') as fav:
                json.dump(favorites, fav)
            self.favorites.removeItem(self.favorites.currentIndex())
        else:
            self.labelError.setText('You cannot remove the title')
            self.labelError.show()


def get_mmr_rankings(mode):
    """
    :param mode: Number value of rocket league mode selected by user
    :return: Dictionary containing the mmr values of every division of every RL rank
    """
    mmr_rankings = {}
    url = f'https://rocketleague.tracker.network/distribution/{mode}'
    rank_page = requests.get(url)
    soup = BeautifulSoup(rank_page.text, 'lxml')
    ranks = soup.find_all('div', class_='col-md-4')
    for rank in ranks:
        rank_name = rank.h3.text.strip()
        if rank_name == 'Unranked':
            continue
        divisions = [name.text.strip() for name in rank.find_all('div', class_='division-label')]
        division_mmr = [int(mmr.div.text.strip()) for mmr in rank.find_all('div', class_='division')]
        mmr_rankings[rank_name] = {name: mmr for name, mmr in zip(divisions, division_mmr)}
    mmr_rankings['Grand Champion']['XX'] = 'COMPLETE'
    return mmr_rankings


def main():
    """
    Starts the QT app and allows for exit
    """
    while True:
        keyboard.wait('ctrl+h')
        app = QtWidgets.QApplication.instance()
        if app is None:
            app = QtWidgets.QApplication(sys.argv)
        rocketleagueranks = QtWidgets.QMainWindow()
        ui = Ui_rocketleagueranks()
        ui.setupUi(rocketleagueranks)
        rocketleagueranks.show()
        app.exec_()


if __name__ == "__main__":
    main()
