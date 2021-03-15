#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
#Convert the extracted value to a floating point number and print it out.


str = 'X-DSPAM-Confidence: 0.8475'
num = str.find(":")
numEnd = len(str)
number = str[num+1:numEnd]
cleanNumber = number.lstrip()
final = float(cleanNumber)
print(final)
