import numpy as np

def matrix_vector_product(mat1, mat2):
    """
    Multiply a matrix by a column vector (or a matrix with one column).

    mat1 shape -> (m, n)
    mat2 shape -> (n, q)

    Returns:
        result shape -> (m, q)
    """
    m, n = mat1.shape
    p, q = mat2.shape

    # Number of columns in mat1 must match number of rows in mat2
    assert n == p, "Matrix product not possible"

    # Create an output matrix filled with zeros
    result = np.zeros((m, q), dtype=mat1.dtype)

    # Compute each element of the result
    for i in range(m):
        for j in range(q):
            # Row of mat1 multiplied by column of mat2
            result[i, j] = np.sum(mat1[i, :] * mat2[:, j])

    return result

def matrix_matrix_product(mat1, mat2):
    """
    Multiply two matrices using the matrix_vector_product function.

    mat1 shape -> (m, n)
    mat2 shape -> (n, q)

    Returns:
        result shape -> (m, q)
    """
    m, n = mat1.shape
    p, q = mat2.shape

    # Matrix multiplication condition
    assert n == p, "Matrix product not possible"

    # Create output matrix
    result = np.zeros((m, q), dtype=mat1.dtype)

    # Take one column of mat2 at a time and multiply with mat1
    for j in range(q):
        col = mat2[:, j].reshape(p, 1)   # Convert column into 2D shape (p, 1)
        result[:, j] = matrix_vector_product(mat1, col).flatten()

    return result


# A is a 2x5 matrix
A = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 1]
])

# B must have 5 rows, because A has 5 columns
# So B is a 5x2 matrix here
B = np.array([
    [6, 4],
    [3, 2],
    [4, 2],
    [3, 5],
    [6, 3]
])

print("Given matrix product:")
print(matrix_matrix_product(A, B))

print("\nChecking the answer with built-in NumPy matrix multiplication:")
print(A @ B)
