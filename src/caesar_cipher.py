from string import ascii_lowercase
from string import ascii_uppercase

#  Variation on Caesar Cipher
#  https://www.codewars.com/kata/5508249a98b3234f420000fb
def moving_shift(str, shift):
    output_str = str
    for i in range(len(output_str)):
        letter = str[i]
        if ascii_lowercase.find(letter) >= 0:
            index = ascii_lowercase.find(letter)
            output_str = output_str[:i] + ascii_lowercase[(index + shift) % len(ascii_lowercase)] + output_str[i + 1:]
        if ascii_uppercase.find(letter) >= 0:
            index = ascii_uppercase.find(letter)
            output_str = output_str[:i] + ascii_uppercase[(index + shift) % len(ascii_uppercase)] + output_str[i + 1:]

        shift += 1
    return divide(output_str, str)

def divide(output_str, str):
    result = []
    for i in range(5):
        length_part = 0
        if len(str) % 5 == 0:
            length_part = len(str) / 5
        else:
            length_part = int(len(str) / 5) + 1
        result.append(output_str[length_part * i:length_part * (i + 1)])
    return result
    
def demoving_shift(str, shift):
    output_str = "".join(str)
    str = "".join(str)

    for i in range(len(output_str)):
        letter = str[i]
        if ascii_lowercase.find(letter) >= 0:
            index = ascii_lowercase.find(letter)
            output_str = output_str[:i] + ascii_lowercase[(index - shift) % len(ascii_lowercase)] + output_str[i + 1:]
        if ascii_uppercase.find(letter) >= 0:
            index = ascii_uppercase.find(letter)
            output_str = output_str[:i] + ascii_uppercase[(index - shift) % len(ascii_uppercase)] + output_str[i + 1:]

        shift += 1
    return output_str
