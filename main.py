from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLineEdit, QVBoxLayout, QApplication, QPushButton, QHBoxLayout, QLabel)
from PySide6.QtCore import Qt
from handler.FileHandler import FileHandler
from handler.FunctionHandler import FunctionHandler

import sys

class MainGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Instagram Follower and Following Tracker by MannXtrem")

        # Create a central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Define Label
        self.output_file_label = QLabel("Output File : ", self)

        # Define Input Text Field
        self.follower_original_input_field = QLineEdit()
        self.follower_original_input_field.setPlaceholderText("Original Follower Data Path")
        self.follower_original_input_field.setReadOnly(True)
        self.follower_updated_input_field = QLineEdit()
        self.follower_updated_input_field.setPlaceholderText("Updated Follower Data Path")
        self.follower_updated_input_field.setReadOnly(True)
        self.output_file_input_field = QLineEdit()
        self.output_file_input_field.setPlaceholderText("Output CSV File Path")
        self.output_file_input_field.setReadOnly(True)

        # Define Push Button
        self.follower_orginal_import_button = QPushButton("Import")
        self.follower_original_retrieve_button = QPushButton("Retrieve")
        self.follower_original_retrieve_button.setEnabled(False)
        self.follower_updated_import_button = QPushButton("Import")
        self.follower_updated_retrieve_button = QPushButton("Retrieve")
        self.follower_updated_retrieve_button.setEnabled(False)
        self.compare_button = QPushButton("Compare")
        self.open_missing_file_button = QPushButton("Open")
        self.open_missing_file_button.setEnabled(False)
        self.exit_button = QPushButton("Exit")

        # Connect Push Button
        self.follower_orginal_import_button.clicked.connect(lambda : FileHandler.locateFileToTextField(self, self.follower_original_input_field, self.follower_original_retrieve_button))
        self.follower_updated_import_button.clicked.connect(lambda : FileHandler.locateFileToTextField(self, self.follower_updated_input_field, self.follower_updated_retrieve_button))
        self.follower_original_retrieve_button.clicked.connect(lambda : FunctionHandler.retrieveHTMLData(self, "Original", self.follower_original_input_field))
        self.follower_updated_retrieve_button.clicked.connect(lambda : FunctionHandler.retrieveHTMLData(self, "Updated", self.follower_updated_input_field))
        self.compare_button.clicked.connect(lambda : FunctionHandler.compareDataFile(self, self.follower_original_input_field, self.follower_updated_input_field, self.open_missing_file_button, self.output_file_input_field))
        self.open_missing_file_button.clicked.connect(lambda : FunctionHandler.openCSVFile(self, self.output_file_input_field))
        self.exit_button.clicked.connect(lambda : FunctionHandler.exitApplication())


        # Define Layout
        # Vertical Layout
        self.vertical_layout_1 = QVBoxLayout()

        # Horizontal Layout
        self.horizontal_layout_1 = QHBoxLayout()
        self.horizontal_layout_2 = QHBoxLayout()
        self.horizontal_layout_3 = QHBoxLayout()
        self.horizontal_layout_4 = QHBoxLayout()


        # Add Widget to Layout
        # Horizontal Layout 1
        self.horizontal_layout_1.addWidget(self.follower_original_input_field)
        self.horizontal_layout_1.addWidget(self.follower_orginal_import_button)
        self.horizontal_layout_1.addWidget(self.follower_original_retrieve_button)

        # Horizontal Layout 2
        self.horizontal_layout_2.addWidget(self.follower_updated_input_field)
        self.horizontal_layout_2.addWidget(self.follower_updated_import_button)
        self.horizontal_layout_2.addWidget(self.follower_updated_retrieve_button)

        # Horizontal Layout 3
        self.horizontal_layout_3.addWidget(self.output_file_label)
        self.horizontal_layout_3.addWidget(self.output_file_input_field)

        # Horizontal Layout 4
        self.horizontal_layout_4.addWidget(self.compare_button)
        self.horizontal_layout_4.addWidget(self.open_missing_file_button)
        self.horizontal_layout_4.addWidget(self.exit_button)

        # Add Layout
        self.vertical_layout_1.addLayout(self.horizontal_layout_1)
        self.vertical_layout_1.addLayout(self.horizontal_layout_2)
        self.vertical_layout_1.addLayout(self.horizontal_layout_3)
        self.vertical_layout_1.addLayout(self.horizontal_layout_4)


        # Set Layout
        central_widget.setLayout(self.vertical_layout_1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainGUI = MainGUI()
    mainGUI.show()
    app.exec()


