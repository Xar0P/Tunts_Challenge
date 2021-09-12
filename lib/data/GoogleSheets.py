from googleapiclient.discovery import build
from google.oauth2 import service_account
from pprint import pprint

class GoogleSheet:

    def __init__(self, spreadsheet_id: str = '1kdJdxgnWIuuVdDffhEq9vUWassPJgU5qrknZXmV1Xww') -> None:
        
        service_account_file = 'keys.json' 
        scopes = ['https://www.googleapis.com/auth/spreadsheets']
        
        self.credentials = service_account.Credentials.from_service_account_file(service_account_file, scopes=scopes)
        self.spreadsheet_id = spreadsheet_id

        service = build('sheets', 'v4', credentials=self.credentials)
        self.sheet = service.spreadsheets()

        print('Spreadsheet opened')

    def read(self, context: str = 'engenharia_de_software', range_: str = '!A1:H27') -> list:
        """ Read the spreadsheet """

        result = self.sheet.values().get(spreadsheetId=self.spreadsheet_id,
                                    range=f'{context}{range_}').execute()
        values = result.get('values')

        print('Spreadsheet data has been read')
        
        return values

    def write(self, context: str = 'engenharia_de_software',coord: str = '!A1', content: list = [['Hello!']]) -> None:
        """ Write in spreadsheet """

        self.sheet.values().update(spreadsheetId=self.spreadsheet_id, 
                                    range=f"{context}{coord}", 
                                    valueInputOption="RAW", 
                                    body={"values":content}).execute()

        print('Data entered in the spreadsheet')

if __name__ == "__main__":
    plan = GoogleSheet()
    pprint(plan.read(), width=120)
    plan.write(coord="!H27",content=[["..."]])