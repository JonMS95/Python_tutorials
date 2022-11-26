# First of all, check if PIP is installed in your machine. Just type pip --version.
# If it's already installed, the version will be displayed.
# If that's not the case, go ahead and install it by using the "sudo apt install python-pip" command.
# Upgrading it may be required as well. To do so, use the "sudo pip install --upgrade pip" command.
# If any version of Python3 is already installed, it's strongly recommended to use "sudo apt install python3-pip"
# instead of any of the commands mentioned above.

# Once the Linux PIP package is installed and upgraded, it can be used to download python open-source modules
# from a large library. To find them, just click on the following link:
# https://pypi.org/

# In this case, a simple string encryption-decryption library is going to be installed:
# https://pypi.org/project/scryp/.
# Type "pip3 install scryp" in the linux console to install it.

# In order to use it, it should be imported first. Just do it as if it was an ordinary module.

# An error may occur at this point, as the libraries may be stored within a not-well-known path.
# In this case, libraries seem to be kept in the /home/userName/.local/lib/python3.6/site-packages path.
# Use export "PYTHONPATH=$PYTHONPATH:/home/jon/.local/lib/python3.6/site-packages" command to fix it.

from scryp import encrypt, decrypt

from password import PASSWORD, RANDOM_STRING

encrypted_string = encrypt(RANDOM_STRING, PASSWORD)
print("Encrypted string: " + encrypted_string)

decrypted_string = decrypt(encrypted_string, PASSWORD)
print("Decrypted string: " + decrypted_string)