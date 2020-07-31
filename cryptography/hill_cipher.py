# The Hill Cipher
import numpy as np

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
    pass



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
