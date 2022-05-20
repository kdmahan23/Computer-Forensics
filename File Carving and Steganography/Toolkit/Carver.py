'''
Created By:
Created On:
Last Modified By: Kayla Mahan
Last Modified On: 
Course: Forensics F20
Assignment: Lab 2
Purpose: Create a python class that can scan a binary file and attempt to retrieve files
'''

# Imports used for hashing functions, file functions,
# sys calls, and converting between ascii and hex.
import hashlib, os, sys, binascii

# A file carver that accepts a binary and writes all discovered files to
# the specified output directory
class FileCarver:

	# Creates instance of the FileCarver object
	# self - This instance of FileCarver
	# inputFile - Binary to be parsed
	# output - Destination directory for carved files to be written to
	def __init__(self, inputFile, output):
		self.banner()
		self.iFile = inputFile
		self.oDest = output

	# Carves the binary that the object was instantiated with
	# self - This instance of FileCarver
	def carve(self):

		# Header and footer signatures
		# pdfSig = "\x25\x50\x44\x46"
		# pdfSig_2 "\x25\x25\x45\x4F\x46"
		# pngSig = "\x89\x50\x4E\x47"
		# pngSig_2 = "\x0D\x0A\x1A\x0A"
		# wavSig = "\x52\x49\x46\x46"
		
		with open(sys.argv[3], "rb") as self.iFile:
			self.iFile.seek(0,2)
			fileSize = self.iFile.tell()

			pdfCount = 0
			pngCount = 0
			wavCount = 0

			for i in range(fileSize):
				self.iFile.seek(i)
				four_bytes = self.iFile.read(4)
				self.iFile.seek(i)
				eight_bytes = self.iFile.read(8)
				if eight_bytes == b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a":
					print("Found PNG")
					pngCount += 1
					
					png_size_bytes = self.iFile.read(4)
					png_size = int.from_bytes(png_size_bytes, byteorder='little',signed=False)

					self.iFile.seek(i)
					png_data = self.iFile.read(png_size + 8)
					with open("png" + str(pngCount) + ".png", "wb") as self.oDest:
						self.oDest.write(png_data)
						print("PNG carved")
					i = png_size + 8
				elif four_bytes == b"\x25\x50\x44\x46":
					j = i + 4
					for j in range(fileSize):
						self.iFile.seek(j)
						five_bytes = self.iFile.read(5)
						if five_bytes == b"\x25\x25\x45\x4F\x46":
							pdf_size = (j+4) - i
							if j > i:
								print("Found PDF")
								pdfCount += 1
								self.iFile.seek(i)
								pdf_data = self.iFile.read(pdf_size)
								with open("pdf" + str(pdfCount) + ".pdf", "wb") as self.oDest:
									self.oDest.write(pdf_data)
									print("PDF carved")
								i = pdf_size
				elif four_bytes == b"\x52\x49\x46\x46":
					print("Found WAV")
					wavCount += 1
					
					wav_size_bytes = self.iFile.read(4)
					wav_size = int.from_bytes(wav_size_bytes, byteorder='little',signed=False)

					self.iFile.seek(i)
					wav_data = self.iFile.read(wav_size + 8)
					with open("wav" + str(wavCount) + ".wav", "wb") as self.oDest:
						self.oDest.write(wav_data)
						print("WAV carved")
					i = wav_size + 4
				
			print("Number of PDFs found: " + str(pdfCount))
			print("Number of PNGs found: " + str(pngCount))
			print("Number of WAVs found: " + str(wavCount))


	# Prints out the file carver's banner (generated by http://patorjk.com/software/taag/).
	def banner(self):
		print("   (                                ")
		print("   )\      )  (     )      (   (    ")
		print(" (((_)  ( /(  )(   /((    ))\  )(   ")
		print(" )\___  )(_))(()\ (_))\  /((_)(()\  ")
		print("((/ __|((_)_  ((_)_)((_)(_))   ((_) ")
		print(" | (__ / _` || '_|\ V / / -_) | '_| ")
		print("  \___|\__,_||_|   \_/  \___| |_|   ")
