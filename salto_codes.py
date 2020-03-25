import csv

def toRCO(salto):
  #remove last 6 zeroes
  salto = salto[:-6]

  #toHex = hex(notSalto)
  #split
  salto = [salto[0:2], salto[2:4], salto[4:6], salto[6:8]]
  
  #reverse groups
  salto.reverse()
  
  block1 = ''.join(salto[:2])
  block2 = ''.join(salto[2:])
  
  # RCO = ''.join(salto)
  RCO = str(int(block1, 16)) + str(int(block2, 16))
  if len(RCO) == 10:
    RCO = RCO[1:]

  return RCO

 
f = open('a.csv')
reader = csv.reader(f)
for row in reader:
   # line = row[0].split(';')
   salto = row[0]
   if len(salto) == 14:
     rco = toRCO(salto)
     if len(rco) < 9:
       zeros = 9 - len(rco)
       rco = '0'*zeros + rco
     print(rco)
   else:
     print
    
  
f.close()

# print(toRCO('645CC6D3000000'))