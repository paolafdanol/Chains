str = 'X-DSPAM-Confidence:0.8475'
index = str.find(":") #variable donde se guarda el lugar donde estan los puntos
print(float(str[index + 1:]))

