import sys
import inspect
from pathlib import Path

# Static variables
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

### Helper Methods ###
# Returns the current line number of the program.
def lineno():
    return inspect.currentframe().f_back.f_lineno

######

### Process system arguments ###

# argv[1] Cipher rotation number. Can be negative to rotate backwards or positive to rotate forwards.
rot_key = int(sys.argv[1])

# argv[2] Can be ommited for default behavior. Flags. "-f" means the encrypted message is stored in a file.
if (len(sys.argv) > 2 and sys.argv[2] == "-f"):
    global isFile
    isFile = True
else:
    isFile = False

# print(f'Line {lineno()}: isFile is "{isFile}".') # Hint

# argv[-1] The last argument is always the encrypted message, either as a path to a file or as a string.
if (isFile):
    global encrypted_msg
    encrypted_msg = Path(sys.argv[-1]).read_text()
else:
    encrypted_msg = sys.argv[-1]

# print(f'Line {lineno()}: encrypted_msg is "{encrypted_msg}".') # Hint

######

### Decrypt Caesar Cipher with rotation key ###

decrypted_msg = ""

for c in encrypted_msg:
    if (c.lower() in alphabet):
        pos = alphabet.index(c.lower())
        new_pos = pos + int(rot_key)
        if (new_pos >= len(alphabet)):
            new_pos = new_pos - len(alphabet)
        # print(f'Line {lineno()}: The new character position is {new_pos}.') # Hint
        if c.isupper():
            new_c = alphabet[new_pos].upper()
        else:
            new_c = alphabet[new_pos]

        """ Hint
        print(f'Line {lineno()}: Beginning to decrypt message with a rotation of {rot_key}...')
        print(f'Line {lineno()}: Encrypted character is {c} with an alphabet position of {pos}')
        print(f'Line {lineno()}: Decrypted character is {new_c} with an alphabet position of {new_pos}')
        """
    else:
        new_c = c
    decrypted_msg = decrypted_msg + new_c

# print(f'Line {lineno()}: Here is your decrypted message!\n') # Hint

print(decrypted_msg)

# print(f"\nCaesar Cipher decryption of {sys.argv[-1]} completed with a rotational key of {rot_key}.") #Hint

######





