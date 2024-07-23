# Windows Error Reporting (WER) Parser
A simple script to parse all WER crash reports and save to CSV. During Incident Response or Digital Forensics examinations, sometimes we need to check WER reports where the malware or suspicious programs maybe crashed during the execution. These WER reports would be helpful to identify the cause of the crash and maybe we can get the timestamp of the execution, MD5 hashes and many more.

## How to Use
Instructions to Use the Script:

- Save the script as wer_parser.py.
- Open a terminal or command prompt.
- Navigate to the directory where the script is saved.
- Run the script using the following command:

   `python wer_parser.py <inputfolder> output.csv`

Replace <inputfolder> with the path to the directory containing your WER files (the script will process files in subdirectories as well), and output.csv with the desired path for the output CSV file. The most easy way is just to point to your C:\ root folder.

# Help Output
To see the help message and usage instructions, you can run:

`python wer_parser.py --help`

# WER Paths
Here are the paths that we should take a look at to find these artifacts.
```
C:\ProgramData\Microsoft\Windows\WER\ReportArchive
C:\ProgramData\Microsoft\Windows\WER\ReportQueue
C:\Users\XXX\AppData\Local\Microsoft\Windows\WER\ReportArchive
C:\Users\XXX\AppData\Local\Microsoft\Windows\WER\ReportQueue
```

# Example of Commands
Here are the paths that we should take a look at to find these artifacts.
```
python3 wer_parser.py C:\ D:\WER\WER_Reports.csv
```
