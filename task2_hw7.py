def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        row = ""
        for j in range(1, num_columns + 1):
            row += str(operation(i, j)) + " "
        print(row)

print_operation_table(lambda x, y: x * y)