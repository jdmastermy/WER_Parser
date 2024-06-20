# Windows Error Reporting (WER) Parser
A simple script to parse all WER crash reports and save to CSV

## How to Use
Instructions to Use the Script:

- Save the script as wer_parser.py.
- Open a terminal or command prompt.
- Navigate to the directory where the script is saved.
- Run the script using the following command:

   `python wer_parser.py path_to_your_wer_files_directory output.csv`

Replace path_to_your_wer_files_directory with the path to the directory containing your WER files (the script will process files in subdirectories as well), and output.csv with the desired path for the output CSV file.

# Help Output
To see the help message and usage instructions, you can run:

`python wer_parser.py --help`

# WER Path
Here are the paths that we should take a look at to find these artifacts.
```
C:\ProgramData\Microsoft\Windows\WER\ReportArchive
C:\ProgramData\Microsoft\Windows\WER\ReportQueue
C:\Users\XXX\AppData\Local\Microsoft\Windows\WER\ReportArchive
C:\Users\XXX\AppData\Local\Microsoft\Windows\WER\ReportQueue
```
