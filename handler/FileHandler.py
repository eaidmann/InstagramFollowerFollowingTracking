from PySide6.QtWidgets import QFileDialog, QMessageBox
from datetime import datetime

import re
import csv
import pandas as pd
import os

class FileHandler :
    def locateFileToTextField(self, input_text_field, retrieve_button=None) :
        try : 
            file_path, _ = QFileDialog.getOpenFileName(self, "Select a File")
            if file_path:
                input_text_field.setText(file_path)
                if retrieve_button == None :
                    pass
                else :
                    retrieve_button.setEnabled(True)
        except Exception as e :
            QMessageBox.critical(self, "Locate File.", f"Error : {str(e)}")


    def extract_data_from_html(self, file_path) :
        try :
            with open(file_path, 'r', encoding='utf-8') as file:
                html_data = file.read()

            # Regular expression to extract link, username, and date
            pattern = r'<a target="_blank" href="(https://www\.instagram\.com/\S+)">(\S+)</a></div>\s*<div>([\w\s,]+ \d{1,2}, \d{4} \d{1,2}:\d{2} (?:am|pm))</div>'

            # Find all matches in the HTML data
            matches = re.findall(pattern, html_data)

            return matches
        except Exception as e :
            QMessageBox.critical(self, "Extract HTML Data File.", f"Error : {str(e)}")
    

    # Function to write extracted data to CSV
    def write_to_csv(self, data, output_file):
        try :
            with open(output_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Link", "Username", "Date Joined"])  # Write header
                writer.writerows(data)  # Write the extracted data
        except Exception as e :
            QMessageBox.critical(self, "Write to CSV.", f"Error : {str(e)}")


    # Compare two csv files
    def compareCSVFile(self, original_csv_file, updated_csv_file, open_output_button, output_file_input_field) :
        try :
            # Read both CSV files into DataFrames
            csv_file_1 = pd.read_csv(original_csv_file)
            csv_file_2 = pd.read_csv(updated_csv_file)

            # Add "Status" column to both CSVs
            csv_file_1['Status'] = 'Unfollowed'
            csv_file_2['Status'] = 'New'

            # Concatenate both dataframes
            merged_df = pd.concat([csv_file_1, csv_file_2])

            # Remove duplicates based on Name, Age, and DateJoined, but keep the status (Missing or New)
            # This will effectively remove duplicates while preserving the 'Status' column
            final_df = merged_df.drop_duplicates(subset=['Link', 'Username', 'Date Joined'], keep=False)

            """ # Merge the two DataFrames to find the rows that are in file1 but not in file2
            merged = pd.merge(csv_file_1, csv_file_2, how='left', on=["Link", "Username", "Date Joined"], indicator=True)

            # Filter out the rows that only exist in file1 (missing in file2)
            missing_rows = merged[merged['_merge'] == 'left_only'].drop('_merge', axis=1) """

            current_date = datetime.now().strftime("%Y_%m_%d")
            missing_output_path = f"Output\\Missing\\{current_date}"

            if not os.path.exists(missing_output_path):
                os.makedirs(missing_output_path)
                print(f"Folder '{missing_output_path}' created.")
            else:
                print(f"Folder '{missing_output_path}' already exists.")
                QMessageBox.warning(self, "Folder creation", f"Folder '{missing_output_path}' already exists.")

            # Write the missing rows to a new CSV file
            #missing_rows.to_csv(f"{missing_output_path}\\missing_data_{current_date}.csv", index=False)
        

            # Now, write this result to a new CSV
            final_df.to_csv(f"{missing_output_path}\\missing_data_{current_date}.csv", index=False)

            print(f"Missing data has been written to '{missing_output_path}\\missing_data_{current_date}.csv'.")
            open_output_button.setEnabled(True)
            output_file_input_field.setText(f"{missing_output_path}\\missing_data_{current_date}.csv")
        except Exception as e :
            QMessageBox.critical(self, "Compare Data File.", f"Error : {str(e)}")


