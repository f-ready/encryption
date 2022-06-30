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
###     2.  Encrypt file
###                                                                     ###
###########################################################################
###                                                                     ###
###     2.  Decrypt file
###                                                                     ###
###########################################################################



# %% ######################################################################
###     0.          Dependent Libraries                                 ###
###########################################################################

import os, sys
import encryption



# %% ######################################################################
###     1.          Class Initialization                                ###
###########################################################################

class encrypt_with_modular(encryption.encrypt):
###
###
###
# %% ######################################################################
###     3.0.        Encryption - Helper Functions                       ###
###########################################################################
###
    def __():
        return
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
                continue
        return



# %% ######################################################################
###     z.          Miscellaneous                                       ###
###########################################################################

# crypt_task = encrypt_with_modular(
#     wrk_dir = r"C:\Users\xufre\Desktop" \
#                 r"\work\git\encryption" \
#                 r"\test_modular",
#     file_list = [
#         r"secret_file_1.txt",
#         r"secret_file_2.txt"])
#
# crypt_task.encrypt()
#
#
# crypt_task = encrypt_with_modular(
#     wrk_dir = r"C:\Users\xufre\Desktop" \
#                 r"\work\git\encryption" \
#                 r"\test_modular",
#     file_zip_encrypt_gz = "file_encrypted")
#
# crypt_task.decrypt()
