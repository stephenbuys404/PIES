def str_to_binary(string):
    print('creating array')
    binary_list = []
    print('running')
    for char in string:
        binary_list.append(bin(ord(char))[2:].zfill(8))
    return str().join(binary_list)

def BinaryToDecimal(binary):
    print('setting values')
    decimal, i, n = 0, 0, 0
    print('running')
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return (decimal)

test_str = 'goodMorning'
bin=str_to_binary(test_str)
str_data=str()
for i in range(0, len(bin), 8):
    temp_data = int(bin[i:i + 8])
    decimal_data = BinaryToDecimal(temp_data)
    str_data = str_data + chr(decimal_data)
print(str_data)