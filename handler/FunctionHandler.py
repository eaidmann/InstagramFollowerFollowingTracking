from handler.FileHandler import FileHandler
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMessageBox

import time
import os
import subprocess

class FunctionHandler :
    def retrieveHTMLData(self, data_type, html_file_path_input) :
        try :
            current_date = datetime.now().strftime("%Y_%m_%d")
            current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

            html_file_path = html_file_path_input.text()
            output_file_path = f"Output\\{current_date}"

            if not os.path.exists(output_file_path):
                os.makedirs(output_file_path)
                print(f"Folder '{output_file_path}' created.")
            else:
                print(f"Folder '{output_file_path}' already exists.")
                QMessageBox.warning(self, "Folder creation", f"Folder '{output_file_path}' already exists.")
            extracted_data = FileHandler.extract_data_from_html(self, html_file_path)

            output_file_path_generated = f"{output_file_path}\\output_{data_type}_{current_time}.csv"

            if extracted_data :
                FileHandler.write_to_csv(self, extracted_data, output_file_path_generated)
                html_file_path_input.setText(output_file_path_generated)
                print(f"Data extracted and written to '{output_file_path_generated}'")
            else:
                print("No data found in the HTML file.")
        except Exception as e :
            QMessageBox.critical(self, "Retrieve HTML Data.", f"Error : {str(e)}")

    
    def compareDataFile(self, original_file_path_input, updated_file_path_input, open_output_button, output_file_input_field) :
        try : 
            original_csv_path = original_file_path_input.text()
            updated_csv_path = updated_file_path_input.text()
            FileHandler.compareCSVFile(self, original_csv_path, updated_csv_path, open_output_button, output_file_input_field)
        except Exception as e :
            QMessageBox.critical(self, "Compare Data File.", f"Error : {str(e)}")


    def openCSVFile(self, output_file_input_field) :
        csv_file_path = output_file_input_field.text()
        try:
            # Check if the file exists
            if os.path.exists(csv_file_path):
                # For Windows, this will open the CSV file in the default application (e.g., Excel or WPS)
                subprocess.run(["start", csv_file_path], shell=True)
            else:
                print(f"File does not exist. {csv_file_path}")
                QMessageBox.warning(self, "Opening a file.", f"File '{csv_file_path}' does not exists.")
        except Exception as e:
            print(f"Error opening file: {str(e)}")
            QMessageBox.critical(self, "Opening a file.", f"Error opening file: {str(e)}")


    def exitApplication() :
        QApplication.quit()