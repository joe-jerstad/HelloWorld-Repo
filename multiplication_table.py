#multiplication table
#takes in rows and columns and prints out a multiplication table of the two

def multiplication_table(rows, columns):
    for i in range(1, rows + 1):
        row = ''
        for x in range(1, columns + 1):
            mul_num = x * i
            if mul_num < 10:
                row += (f'{mul_num}   ')
            elif mul_num >= 10 and mul_num < 100:
                row += (f'{mul_num}  ')
            elif mul_num >= 100:
                row += (f'{mul_num} ')

        print(f'{row}')
        
def main():
    row =  int(input('Enter the number for the rows: '))
    column =  int(input('Enter the number for the columns: '))
    multiplication_table(row, column)

main()
