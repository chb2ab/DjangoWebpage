__author__ = 'chb2ab'

from Crypto.PublicKey import RSA
from Crypto.Cipher import ARC4

def decrypt_file(lines, key, name):
	""" decrypt a .enc file to a DEC_ file using the given key """
	dec = ARC4.new(key)
	fw = open("downloads/"+name, 'wb');
	for line in lines:
		enc_text = line.encode('latin-1');
		text = dec.decrypt(enc_text);
		fw.write(text);
	print("#######################")
	print("Decryption Sucessful: File saved to downloads/" + name)
	print("#######################")
	print()
	return True;

if __name__ == "__main__":
	inp = str( input("Enter a key: ") )
	key = inp.encode();
	filename = str( input("Enter filename: ") )
	decrypt_file( filename, key );
