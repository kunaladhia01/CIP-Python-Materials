# The Hill Cipher
import numpy as np
from itertools import combinations

# Generate a random 3x3 key matrix K
def random_key():
    ret = np.random.randint(101, size=(3, 3))
    if np.linalg.det(ret):
        return ret
    return random_key()

# Adds filler characters to the plaintext to make its length a multiple of 3
def add_filler_text(text):
    if len(text) % 3:
        return text + " " * (3 - len(text) % 3)
    return text

# Create the matrix P
def string_to_matrix(text):
    return np.array([ord(x) for x in text]).reshape(3, len(text) // 3)

# Given P and K, generate E = K*P
def generate_ciphertext(key, plaintext_matrix):
    return np.matmul(key, plaintext_matrix)

# Given E and K, generate P = K^-1*E
def decrypt_plaintext(key, ciphertext_matrix):
    return np.round(np.matmul(np.linalg.inv(key), ciphertext_matrix))

# Given P, recover the original string
def matrix_to_string(plaintext_matrix):
    ret = ""
    for i in plaintext_matrix:
        for j in i:
            ret += chr(int(j))
    return ret

# Given P and E, you should be able to return K.
def break_scheme(plaintext_matrix, ciphertext_matrix):
    # Take the transpose so it's easier to take different rows of each matrix
    plain_transpose = np.transpose(plaintext_matrix)
    cipher_transpose = np.transpose(ciphertext_matrix)
    # If the two matrices are 2x3, for example, there's no way we can find K.
    if len(plain_transpose) < 3:
        return "Not Possible"
    # Here, I loop through all possible combinations of taking 3 different columns,
    # or rows of the transpose matrices, until one plaintext combination is invertible.
    # If none are invertible, we exit the loop and return "Not Possible"
    for row_choice in combinations([i for i in range(len(plain_transpose))], 3):
        # For example, if we're trying the first, second, and fourth columns of the plaintext_matrix,
        # or the first, second and fourth ROWS of the TRANSPOSE, trial_matrix will reflect this.
        trial_matrix = np.array([plain_transpose[i] for i in row_choice])
        # A useful property of linear algebra is that if a matrix is invertible, so is its transpose.
        # Remember that if the determinant of a matrix is nonzero, the matrix is invertible.
        if np.linalg.det(trial_matrix):
            # Construct the new ciphertext matrix with the same columns (rows of transpose) as the plaintext.
            ciphertext_same_rows = np.array([cipher_transpose[i] for i in row_choice])
            # These matrices are the TRANSPOSES of the intended matrices, so we take the transpose of each
            # again to get the original matrices with the selected columns.
            cut_plaintext = np.transpose(trial_matrix)
            cut_ciphertext = np.transpose(ciphertext_same_rows)
            # Remember that because KP = E, K = E(P^-1) for square matrices E and invertible P, which we have now!
            return np.round(np.matmul(cut_ciphertext, np.linalg.inv(cut_plaintext)))
    # We failed to find a combination of three columns that was invertible.
    return "Not Possible"


# Sample run of the Hill Cipher

# Encryption
string = "Lorem ipsum dolor sit amet, consectetur adipiscing elita" # Latin!!
print("Original String: " + string)
K = random_key()
P = string_to_matrix(add_filler_text(string))
E = generate_ciphertext(K, P)
print("Ciphertext: ")
print(E)

# Decryption
P_1 = decrypt_plaintext(K, E)
recovered_string = matrix_to_string(P_1)
print("Recovered String: " + recovered_string)

# Breaking the Hill Cipher! We have E and P, and want to get the key K.
print(K)
print(break_scheme(P, E)) # Should be the same as K
