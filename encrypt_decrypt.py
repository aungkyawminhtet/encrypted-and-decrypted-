import random


class Encryption:
    def __init__(self):
        self.random_key = random.randint(1, 65536)

        # print("#####---Start Encryption---#####")

    def start_encryption(self, keys, values):
        encrypted = ""
        encrypted_data = ""

        total_key: int = 0
        for i in keys:
            total_key += ord(i)
        # print(total_key)

        for j in values:
            encrypt = ord(j) ^ total_key

            double_encrypted = encrypt ^ self.random_key

            encrypted += hex(double_encrypted) + ':Xz:'
        encrypted_data += hex(total_key) + ':Xz:' + encrypted + hex(self.random_key)

        print("Encrypted data is :", encrypted_data)
        return encrypted_data


class Decryption:
    def __init__(self):
        pass
        # print("####---Start Decryption---####")

    def start_decryption(self, encrypted_data):
        decrypted_data = ""

        data_split = encrypted_data.split(':Xz:')
        t_key = data_split[:1]
        r_key = data_split[-1:]
        total_key = int(t_key[0], 16)
        random_key = int(r_key[0], 16)

        key_list: list = data_split[1:-1]
        # print("key list is:", key_list)

        for i in range(len(key_list)):
            decrypted = int(key_list[i], 16) ^ random_key

            double_decrypt = decrypted ^ total_key
            decrypted_data += chr(double_decrypt)

        print("Decrypted data is :", decrypted_data)
        return decrypted_data


if __name__ == '__main__':
    User_key = input("Enter your user key :")
    while True:
        User_value = input("Enter your user value :")
        encryption = Encryption()
        en_data = encryption.start_encryption(User_key, User_value)
        decryption = Decryption()
        decryption.start_decryption(en_data)
