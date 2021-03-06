import xlsxwriter
import os


def generate_report_excel(output, filename):
    if os.path.exists(filename):
        os.remove(filename)
    workbook = xlsxwriter.Workbook(filename)
    bold = workbook.add_format({'bold': 1})
    for server in range(len(output)):
        for key, value in output[server]['result'].items():
            worksheet = workbook.add_worksheet(key)
            worksheet.set_column('A:A', 40)
            worksheet.set_column('B:B', 15)
            worksheet.write('A1', 'Components', bold)
            worksheet.write('B1', 'Status', bold)
            row = 1
            col = 0
            for k, v in value.items():
                worksheet.write_string(row, col, k)
                if v == 0:
                    status = 'OK'
                else:
                    status = 'Error'
                worksheet.write_string(row, col + 1, k)
                worksheet.write_string(row, col + 1, status)
                row += 1
    workbook.close()
