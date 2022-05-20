'''
Created By:
Created On:
Last Modified By:
Last Modified On:
Course:
Assignment:
Purpose:
'''

# Imports used for hashing functions, file functions, sys calls,
# converting between ascii and hex, and packing binaries.
import hashlib, sys, os, binascii, struct

# A steganography class that embeds the contents of a text file into a PNG
# and extracts it back to a text file.
class Steganography:

	# Creates instance of the Steganography object
	# self - This instance of Steganography
	# task - The task to perform: either embed or extract
	# messageFile - The text file to be embedded; ignored if task == extract
	# inputFile - PNG that the task is to run on
	def __init__(self, task, messageFile, inputFile):
		self.banner()
		self.command = task
		self.image = inputFile
		self.message = messageFile

	# Either embeds a message in a PNG or extracts a message from a PNG
	# self - This instance of Steganography
	def steg(self):
		print("Not yet implemented")
		return

	# Prints out the STEG banner (generated by http://patorjk.com/software/taag/).
	def banner(self):
		print(" .----------------.  .----------------.  .----------------.  .----------------.")
		print("| .--------------. || .--------------. || .--------------. || .--------------. |")
		print("| |    _______   | || |  _________   | || |  _________   | || |    ______    | |")
		print("| |   /  ___  |  | || | |  _   _  |  | || | |_   ___  |  | || |  .' ___  |   | |")
		print("| |  |  (__ \_|  | || | |_/ | | \_|  | || |   | |_  \_|  | || | / .'   \_|   | |")
		print("| |   '.___`-.   | || |     | |      | || |   |  _|  _   | || | | |    ____  | |")
		print("| |  |`\____) |  | || |    _| |_     | || |  _| |___/ |  | || | \ `.___]  _| | |")
		print("| |  |_______.'  | || |   |_____|    | || | |_________|  | || |  `._____.'   | |")
		print("| |              | || |              | || |              | || |              | |")
		print("| '--------------' || '--------------' || '--------------' || '--------------' |")
		print(" '----------------'  '----------------'  '----------------'  '----------------' ")
