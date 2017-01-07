# use placebear api to get a picture of a
# bear with user-specified size
#
# Steps:
#  How do I get a bear of size 250 by 250
#  How do I save it?
#  How do I do user input?
#

import requests

#bear = requests.get('http://www.placebear.com/250/250')
placebear_base_url = "http://www.placebear.com/{0}/{1}"

#width = 25
#height = 2500
width = input("How wide do u want it? ")
height = input("How tall do u want it? ")

final_url = placebear_base_url.format(width, height)
print(final_url)
bear = requests.get(final_url)

local_file_name = "bear_{0}_{1}.jpg".format(width, height)
#fo = open("bear_250_250.jpg", "wb")
fo = open(local_file_name, "wb")

# wb write binary file
# fo.write(bear.text)
fo.write(bear.content)

fo.close()