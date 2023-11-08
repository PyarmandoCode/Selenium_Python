import  openpyxl

class ExcelReader:
    def __init__(self,excel_file):
        self.excel_file=excel_file
    def read_excel_to_list(self,sheet_name):
        data_list=list()
        try:
            worbook=openpyxl.load_workbook(self.excel_file)
            sheet=worbook[sheet_name]
            for row in sheet.iter_rows(values_only=True):
                data_list.append(row)
            return data_list
        except FileNotFoundError:
            print(f"El Archivo {self.excel_file} No se encontro")
            return None
        except Exception as e:
            print(f"Ocurrio un error al leer el archivo de excel {e}")
            return None

if __name__=="__main__":
    excel_file="data_excel_pruductos_81123.xlsx"
    reader=ExcelReader(excel_file)

    sheet_name="datos"
    data=reader.read_excel_to_list(sheet_name)

    if data:
        for row in data:
            print(row)