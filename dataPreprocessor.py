import csv
import xlsxwriter


def makeExcelFile(status, multipleOf):
    with open('state_wise_daily.csv') as csv_file:
        csv_reader = list(csv.reader(csv_file, delimiter=','))
        workbook = xlsxwriter.Workbook(status)
        worksheet = workbook.add_worksheet()

        for i in range(len(csv_reader[0])):
            worksheet.write(0, i, csv_reader[0][i])

        rowCount = 1

        for i in range(multipleOf,len(csv_reader),3):
            for j in range(len(csv_reader[0])):
                worksheet.write(rowCount, j, csv_reader[i][j])
            rowCount += 1
        workbook.close()



CONFIRMED = "confirmed.xlsx"
RECOVERED = "recovered.xlsx"
DECEASED = "deceased.xlsx"

makeExcelFile(CONFIRMED, 1)
makeExcelFile(RECOVERED, 2)
makeExcelFile(DECEASED, 3)
