# %% ######################################################################
###                                                                     ###
###                          Table of Contents                          ###
###                                                                     ###
###     0.          Dependent Libraries                                 ###
###     1.          Class Initialization                                ###
###     3.0.        Encryption - Helper Functions                       ###
###     3.1.        Encryption                                          ###
###     z.          Miscellaneous                                       ###
###                                                                     ###
###########################################################################
###                                                                     ###
###     2.  Encrypt file with involution of binary bit flips.           ###
###         Each character is 1 byte = 2 hexadecimals = 8 bits.         ###
###         Flip half the bits of each byte.                            ###
###             8 choose 4 = 70                                         ###
###             4 choose 2 =  6                                         ###
###             2 choose 1 =  2                                         ###
###                                                                     ###
###########################################################################
###                                                                     ###
###     2.  Decrypt file with involution of binary bit flips.           ###
###                                                                     ###
###########################################################################



# %% ######################################################################
###     0.          Dependent Libraries                                 ###
###########################################################################

import os, struct, sys
import encryption



# %% ######################################################################
###     1.          Class Initialization                                ###
###########################################################################

class encrypt_with_involution(encryption.encrypt):
###
###
###
# %% ######################################################################
###     3.0.        Encryption - Helper Functions                       ###
###########################################################################
###
    def num_to_binary(self, iter_old, size = "b"):
        sizes = {
            "b" : 8, ### 8 bits in a byte
            "x" : 2, ### 2 hexadecimals in a byte
            }
        iter_new = ()
        for i in iter_old:
            iter_new += (format(i, size).zfill(sizes[size]),)
        return(iter_new)
###
    def encrypt_involute(self, bin_str, keep_bits_idx = []):
        bin_str_list = [None] * 8
        for i in range(8):
            if (i in keep_bits_idx):
                bin_str_list[i] = bin_str[i]
            else:
                bin_str_list[i] = str(1 ^ int(bin_str[i]))
        bin_str_encrypt = "".join(bin_str_list)
        return(bin_str_encrypt)
###
    def __keep_idx_helper__(self, *args):
        idx = []
        for arg in args:
            idx += [arg * 2, arg * 2 + 1]
        return(idx)
###
###
###
# %% ######################################################################
###     3.1.        Encryption                                          ###
###########################################################################
###
    def encrypt_decrypt(self, encrypt_or_decrypt):
        assert encrypt_or_decrypt in ["encrypt", "decrypt"], \
            "Set encrypt_or_decrypt."
        if (encrypt_or_decrypt == "encrypt"):
            file_old = self.file_zip
            file_new = self.file_zip_encrypt
        else:
            file_old = self.file_zip_encrypt
            file_new = self.file_zip
        with open(os.path.join(
            self.wrk_dir, file_old), "rb") as f_old:
            with open(os.path.join(
                self.wrk_dir, file_new), "wb") as f_new:
                while (True):
                    f_bytes = f_old.read(6)
                    if (not f_bytes):
                        break
                    f_bytes_num = struct.unpack(
                        "B" * len(f_bytes), f_bytes)
                    f_bytes_bin = self.num_to_binary(f_bytes_num, "b")
                    for i, lst in [
                            (0, self.__keep_idx_helper__(0, 1)),
                            (1, self.__keep_idx_helper__(0, 2)),
                            (2, self.__keep_idx_helper__(0, 3)),
                            (3, self.__keep_idx_helper__(1, 2)),
                            (4, self.__keep_idx_helper__(1, 3)),
                            (5, self.__keep_idx_helper__(2, 3)),]:
                        try:
                            f_bytes_encrypt = \
                                self.encrypt_involute(f_bytes_bin[i], lst)
                            f_bytes_encrypt_char = struct.pack(
                                "B", int(f_bytes_encrypt, 2))
                            f_new.write(f_bytes_encrypt_char)
                        except: continue
        return



# %% ######################################################################
###     z.          Miscellaneous                                       ###
###########################################################################

# crypt_task = encrypt_with_involution(
#     wrk_dir = r"C:\Users\xufre\Desktop" \
#                 r"\work\git\encryption" \
#                 r"\test_involution",
#     file_list = [
#         r"secret_file_1.txt",
#         r"secret_file_2.txt"])
#
# crypt_task.encrypt()
#
#
# crypt_task = encrypt_with_involution(
#     wrk_dir = r"C:\Users\xufre\Desktop" \
#                 r"\work\git\encryption" \
#                 r"\test_involution",
#     file_zip_encrypt_gz = "file_encrypted")
#
# crypt_task.decrypt()
