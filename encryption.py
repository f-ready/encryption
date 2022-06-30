# %% ######################################################################
###                                                                     ###
###                          Table of Contents                          ###
###                                                                     ###
###     0.          Dependent Libraries                                 ###
###     1.          Class Initialization                                ###
###     2.          Compression                                         ###
###     3.          Encryption                                          ###
###     4.          Process Flow                                        ###
###     z.          Miscellaneous                                       ###
###                                                                     ###
###########################################################################
###                                                                     ###
###     1.  Compress file(s) into zip archive.                          ###
###     2.  Encrypt file.                                               ###
###     3.  Compress file with gzip algorithm.                          ###
###                                                                     ###
###########################################################################
###                                                                     ###
###     1.  Expand file with gzip algorithm.                            ###
###     2.  Decrypt file.                                               ###
###     3.  Extract file(s) from zip archive.                           ###
###                                                                     ###
###########################################################################



# %% ######################################################################
###     0.          Dependent Libraries                                 ###
###########################################################################

import gzip, os, shutil, sys, zipfile



# %% ######################################################################
###     1.          Class Initialization                                ###
###########################################################################

class encrypt:
    ###
    wrk_dir = ""
    file_list = []
    file_zip = "__files_zip__"
    file_zip_encrypt = "__files_zip_encrypt__"
    file_zip_encrypt_gz = ""
    ###
    def __init__(self, wrk_dir, file_list = [], file_zip_encrypt_gz = ""):
        self.wrk_dir = wrk_dir
        assert ((file_list != []) ^ (file_zip_encrypt_gz != "")), \
            "Either encryption or decryption needs to be specified."
        if (file_list != []):
            self.file_list = file_list
            self.file_zip_encrypt_gz = "file_encrypted"
        else:
            self.file_list = []
            self.file_zip_encrypt_gz = file_zip_encrypt_gz
###
###
###
# %% ######################################################################
###     2.          Compression                                         ###
###########################################################################
###
    def zip_compress(self):
        with zipfile.ZipFile(os.path.join(
            self.wrk_dir, self.file_zip), "w",
            compression = zipfile.ZIP_DEFLATED) as f_zip:
            for f in self.file_list:
                f_zip.write(os.path.join(self.wrk_dir, f), f)
        return
###
    def zip_extract(self):
        with zipfile.ZipFile(os.path.join(
            self.wrk_dir, self.file_zip), "r") as f_zip:
            f_zip.extractall(os.path.join(
                self.wrk_dir, "files_decrypted"))
        return
###
    def gzip_compress(self):
        with open(os.path.join(
            self.wrk_dir, self.file_zip_encrypt), "rb") as f_old:
            with gzip.open(os.path.join(
                self.wrk_dir, self.file_zip_encrypt_gz), "wb") as f_new:
                f_new.writelines(f_old)
        return
###
    def gzip_extract(self):
        with gzip.open(os.path.join(
            self.wrk_dir, self.file_zip_encrypt_gz), "rb") as f_old:
            with open(os.path.join(
                self.wrk_dir, self.file_zip_encrypt), "wb") as f_new:
                shutil.copyfileobj(f_old, f_new)
        return
###
###
###
# %% ######################################################################
###     3.          Encryption                                          ###
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
                shutil.copyfileobj(f_old, f_new)
        return
###
###
###
# %% ######################################################################
###     4.          Process Flow                                        ###
###########################################################################
###
    def encrypt(self):
        self.zip_compress()
        self.encrypt_decrypt("encrypt")
        self.gzip_compress()
        os.remove(os.path.join(self.wrk_dir, self.file_zip))
        os.remove(os.path.join(self.wrk_dir, self.file_zip_encrypt))
        return
###
    def decrypt(self):
        self.gzip_extract()
        self.encrypt_decrypt("decrypt")
        self.zip_extract()
        os.remove(os.path.join(self.wrk_dir, self.file_zip_encrypt))
        os.remove(os.path.join(self.wrk_dir, self.file_zip))
        return



# %% ######################################################################
###     z.          Miscellaneous                                       ###
###########################################################################

# crypt_task = encrypt(
#     wrk_dir = r"C:\Users\xufre\Desktop" \
#                 r"\work\git\encryption" \
#                 r"\test_encryption",
#     file_list = [
#         r"secret_file_1.txt",
#         r"secret_file_2.txt"])
#
# crypt_task.encrypt()
#
#
#
# crypt_task = encrypt(
#     wrk_dir = r"C:\Users\xufre\Desktop" \
#                 r"\work\git\encryption" \
#                 r"\test_encryption",
#     file_zip_encrypt_gz = "file_encrypted")
#
# crypt_task.decrypt()
