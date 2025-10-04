try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui 

IMAGE_DIR = 'C:/Users/ICT68/Documents/maya/2025/scripts/styletool/image'

class StyleToolDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setWindowTitle('Style Tool')
		self.resize(300,300)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet(
			'''
				QDialog {
					background-color: #D14dF4;
				}
			'''
		)
	
		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f'{IMAGE_DIR}/whiteman.png')
		scaledPixmap = self.imagePixmap.scaled(
			QtCore.QSize(64,64),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)

		self.imageLabel.setPixmap(scaledPixmap)
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

		self.mainLayout.addWidget(self.imageLabel)

		self.nameLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)
		self.namelabel = QtWidgets.QLabel('Name')
		self.nameLineEdit = QtWidgets.QLineEdit()
		self.nameLineEdit.setStyleSheet(
			'''
				QLineEdit {
					background-color: qlineargradient(x1:0, y1:0, y2:1, stop:0 blue, stop:1 navy);
					color: White;
					border-radius: 8px;
					font-family: Arial;
					font-weight: bold;
				}

			'''
		)

		self.nameLayout.addWidget(self.namelabel)
		self.nameLayout.addWidget(self.nameLineEdit)

		self.buttonlayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonlayout)
		self.selectButton = QtWidgets.QPushButton('Select')
		self.selectButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #E500F5;
					border-radius: 10px;
					font-size: 16;
					font-family: Papyrus;
					font-weight: bold;
					padding: 4px;
				}
				QPushButton:hover {
					background-color: qlineargradient(x1:0, x2:1, y2:1, stop:0 red, stop:1 blue);
				}
				QPushButton:pressed {
					background-color: black;
				}

			'''
		)
		self.cancelButton = QtWidgets.QPushButton('Cancel')
		self.buttonlayout.addWidget(self.selectButton)
		self.buttonlayout.addWidget(self.cancelButton)

		self.mainLayout.addStretch()

def run():
	global ui
	try:
		ui.close()
	except:
		pass
	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = StyleToolDialog(parent=ptr)
	ui.show()