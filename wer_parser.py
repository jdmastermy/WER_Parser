# WER Parser by DFIR Jedi
# Version 0.1
# 26/06/2024
# python wer_parser.py path_to_your_wer_files_directory output.csv

import csv
import os
import argparse
from datetime import datetime

def parse_wer_file(file_path):
    data = {}
    try:
        with open(file_path, 'rb') as file:
            content = file.read().replace(b'\x00', b'').decode('utf-8', errors='ignore')
            for line in content.splitlines():
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    data[key] = value
    except UnicodeError as e:
        print(f"Unicode error reading file {file_path}: {e}")
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    print(f"Parsed data from {file_path}: {data}")  # Debugging statement
    return data

def convert_timestamp(timestamp):
    try:
        # Convert the hexadecimal timestamp to an integer
        timestamp_int = int(timestamp, 16)
        # Convert the integer to a datetime object
        dt_object = datetime.utcfromtimestamp(timestamp_int)
        # Format the datetime object to a readable string
        return dt_object.strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        print(f"Error converting timestamp {timestamp}: {e}")
        return timestamp

def extract_information(data, file_path):
    application_timestamp = data.get('Sig[2].Value', '')
    if application_timestamp:
        application_timestamp = convert_timestamp(application_timestamp)
    
    application_name = data.get('Sig[0].Value', '')
    application_version = data.get('Sig[1].Value', '')

    # Check if the application name is actually the version and fix it
    if application_version and any(char.isdigit() for char in application_name):
        application_name = data.get('AppName', '')
    
    if not application_version:
        application_version = data.get('AppVersion', '')

    information = {
        'Report Path': file_path,
        'Application Name': application_name,
        'Application Version': application_version,
        'Application Timestamp': application_timestamp,
        'Fault Module Name': data.get('Sig[3].Value', ''),
        'Fault Module Version': data.get('Sig[4].Value', ''),
        'Fault Module Timestamp': data.get('Sig[5].Value', ''),
        'Exception Code': data.get('Sig[6].Value', ''),
        'Exception Offset': data.get('Sig[7].Value', ''),
        'OS Version': data.get('DynamicSig[1].Value', ''),
        'Locale ID': data.get('DynamicSig[2].Value', ''),
        'App Path': data.get('AppPath', ''),
        'App Name': data.get('AppName', ''),
        'Event Type': data.get('EventType', ''),
        'Event Time': data.get('EventTime', ''),
        'Report Identifier': data.get('ReportIdentifier', ''),
        'Upload Time': data.get('UploadTime', ''),
        'Metadata Hash': data.get('MetadataHash', '')
    }
    print(f"Extracted information: {information}")  # Debugging statement
    return information

def write_to_csv(information_list, output_file):
    if not information_list:
        print("No WER files found to write to CSV.")
        return
    
    keys = information_list[0].keys()
    with open(output_file, 'w', newline='') as output:
        dict_writer = csv.DictWriter(output, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(information_list)

def main(input_dir, output_file):
    information_list = []
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.wer'):
                file_path = os.path.join(root, file)
                print(f"Parsing file: {file_path}")  # Debugging statement
                data = parse_wer_file(file_path)
                if data:
                    information = extract_information(data, file_path)
                    if any(information.values()):  # Check if there is any non-empty value
                        information_list.append(information)
                    else:
                        print(f"No valid information extracted from file: {file_path}")  # Debugging statement
                else:
                    print(f"No data found in file: {file_path}")  # Debugging statement

    print(f"Total WER files processed: {len(information_list)}")  # Debugging statement
    write_to_csv(information_list, output_file)
    print(f"CSV file created at: {output_file}")  # Debugging statement

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Parse WER files and output the extracted information to a CSV file.",
        epilog="Example usage: python wer_parser.py path_to_your_wer_files_directory output.csv"
    )
    parser.add_argument('input_dir', type=str, help="Directory containing WER files")
    parser.add_argument('output_file', type=str, help="Output CSV file")

    args = parser.parse_args()

    main(args.input_dir, args.output_file)
