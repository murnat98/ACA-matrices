if __name__ == '__main__':
    A_matrix = read_matrix_from_file('A.txt')
    B_matrix = read_matrix_from_file('B.txt')
    C_matrix = multiply_matrices(A_matrix, B_matrix)
    write_matrix_to_file(C_matrix, 'result.txt')
