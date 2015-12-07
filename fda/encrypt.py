__author__ = 'chb2ab'

from Crypto.PublicKey import RSA
from Crypto.Cipher import ARC4
import json

def encrypt_file(file_name, inp):
	""" encrypt a given file to a .enc file using the given key """
	key = inp.encode();
	
	splitted = file_name.split('/')
	docname = splitted[len(splitted)-1]
	
	enc = ARC4.new(key)
	try:
		fr = open(file_name, 'rb');
		fw = open("encoded/" + docname + ".enc", 'w');
	except FileNotFoundError:
		return False;
	lines = [];
	for line in fr:
		text = enc.encrypt(line);
		lines.append( text.decode('latin-1') );
	json.dump(lines, fw);
	print("#######################")
	print("Encryption Sucessful: File saved to encoded/" + docname + ".enc")
	print("#######################")
	print()
	return True;

if __name__ == "__main__":
	inp = str( input("Enter a key: ") )
	key = inp.encode();
	filename = str( input("Enter filename: ") )
	encrypt_file( filename, key );
