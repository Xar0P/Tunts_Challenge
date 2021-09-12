import pandas as pd
import math

class Analyze:
    def __init__(self, sheet) -> None:
        self.sheet_dict = self._transform_to_dict(sheet)
        self.df = pd.DataFrame(self.sheet_dict)

    def situation(self, total_students) -> list:
        """ Returns the analysis result for the Situação header """

        absence_limit = total_students * (25/100)
        self.means = self.df.loc[:,['P1','P2','P3']].mean(axis=1)

        for index,mean in enumerate(self.means):
            if float(self.df['Faltas'][index]) > absence_limit:
                self.df['Situação'][index] = 'Reprovado por Falta'
            elif mean < 50:
                self.df['Situação'][index] = 'Reprovado por Nota'
            elif mean < 70:
                self.df['Situação'][index] = 'Exame Final'
            elif mean >= 70:
                self.df['Situação'][index] = 'Aprovado'

        content = list(self.df['Situação'])

        print('Analysis of situation has been complete')

        return content

    def naf(self) -> list:
        """ Returns the analysis result for the NAF header """
        
        for index,el in enumerate(self.df['Situação']):
            if el == 'Exame Final':
                self.df['Nota para Aprovação Final'][index] = f'{math.ceil((self.means[index] + 70) / 2)}'
            else:
                self.df['Nota para Aprovação Final'][index] = 0

        content = list(self.df['Nota para Aprovação Final'])

        print('Analysis of NAF has been complete')

        return content

    @staticmethod
    def _transform_to_dict(sheet) -> dict:
        """ Transform the spreadsheet in a dict """
        
        sheet_dict = {}

        for i,elem in enumerate(sheet[0]):
            for j in range(1, len(sheet)):
                if not elem in sheet_dict.keys():
                    try:
                        sheet_dict[elem] = [int(sheet[j][i]) if elem == "P1" or elem == "P2" or elem == "P3" else sheet[j][i]]
                    except IndexError:
                        sheet_dict[elem] = ['']
                elif elem in sheet_dict.keys():
                    try:
                        sheet_dict[elem].append(int(sheet[j][i]) if elem == "P1" or elem == "P2" or elem == "P3" else sheet[j][i])
                    except IndexError:
                        sheet_dict[elem].append([''])

        return sheet_dict

    @staticmethod
    def get_total_students(self, sheet) -> str:
        """ Get the element that contains the total number of students """

        sheet_dict = self._transform_to_dict(sheet)
        df = pd.DataFrame(sheet_dict)

        return df.loc[0][0]