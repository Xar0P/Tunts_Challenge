# https://docs.google.com/spreadsheets/d/1kdJdxgnWIuuVdDffhEq9vUWassPJgU5qrknZXmV1Xww/edit?usp=sharing
# https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit?usp=sharing

import warnings
from lib.data.GoogleSheets import GoogleSheet
from lib.data.Analysis import Analyze

warnings.filterwarnings('ignore')

sheet = GoogleSheet(spreadsheet_id='1kdJdxgnWIuuVdDffhEq9vUWassPJgU5qrknZXmV1Xww')
sheet_complete = sheet.read(context='engenharia_de_software', range_='!A1:H27')
total_students = Analyze.get_total_students(Analyze, sheet_complete)
total_students = [int(total) for total in total_students.split(' ') if total.isdigit()]

sheet_data = sheet.read(context='engenharia_de_software', range_='!A3:H27')
a = Analyze(sheet_data)
content = a.situation(total_students[0])
sheet.write(context='engenharia_de_software', coord="!G4", content=[[f'{el}'] for el in content])
content = a.naf()
sheet.write(context='engenharia_de_software', coord="!H4", content=[[f'{el}'] for el in content])