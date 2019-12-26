cryptedMsg= "69,70mZk.m76]69,83mZk.m]ZZ]ZZZZZZZZ]ZZ],70mZk.m88]Z,69mZZZk.m]ZZZZZ]Z],70mZk.m70]ZZ,70mZZk.m]96]ZZ]]76]76,70mZk.m],70mZk.m69]m69,70mZk.m76],88mZZZk.m]ZZZZZZZZZZZZZ]93]98]ZZZZZZZZZZZZ]98]ZZZZZZZZZ]ZZZZZZ]ZZZ,69mZZZk.m]69,69mZZZk.m]01]Z,69mZZZk.m]ZZZZZ]70]76,70mZk.m69]70,69mZZZZk.m]08],70mZk.m70],69mZZZk.mZ]76,70mZk.m76]70]08],70mZk.m70]]Z,69mZZZk.mZZ]Z,70mZk.m],83mZk.m]Z,69mZZZk.mZ]mZZZZZZZZZZ]ZZ,ZZZZm70k.m]69,76mZZZk.m],ZZm70k.m76]70,69mZZZZk.m69]ZZZZ,69mZZZk.m]ZZZZZZZZZ]ZZZZZ]85],70mZk.m88]Z,69mZZZk.mZ]Z]ZZZZZZZ]]08]69,69mZZZk.m]76,69mZZZZk.m76],83mZk.m]ZZZZZZZZZZZ]Z,69mZZZk.mZZ]69,70mZZk.m69]Z,76mZk.m]Z,69mZZk.m],76mZZZk.mZZ]ZZZ]85,69mZZZk.m]01]70,69mZZZZk.m69]ZZZZ,69mZZZk.m]76,70mZk.m69]Z,88mZk.mZ]Z]69]69,69mZZZZZk.m69]Z,69mZZZk.m]ZZZZZZ],70mZk.m70]ZZ,69mZZZk.m]ZZZZZZZZZ]ZZZZ]]05],70mZk.m70],69mZZZk.mZ]ZZZZZZZZZZZZZ]08]ZZZZZZZZZZZZ]ZZZ]ZZZ,69mZZZk.mZZ]69,69mZZZk.m],69mZZZk.mZ]76,70mZk.m70]]93],69mZZZZZZk.m],69mZZZk.m69]76,70mZk.m69]88],69mZZZZZk.mZ]01]ZZ,70mZZk.m]08]69,69mZZZk.m]76,69mZZZZk.m76],83mZk.m]ZZZZZZZZZZZ]Z,69mZZZk.mZZ]69,69mZZZk.m]Z,88mZk.mZ]Z]69]69,69mZZZZZk.m69]69,70mZZk.m76]96]69,69mZZZk.m]70,69mZZZZk.mZ]96]69,69mZZZZZk.m69]70,69mZZZZk.m69]ZZZZ,69mZZZk.m]ZZZZZZZZZ]ZZZZZ]85],70mZk.m88]ZZZZZZZZ]Z,70mZk.m]ZZZZZZZZZZZZ]76]98]76,70mZk.m69]ZZZZZ,69mZZZk.m]98]ZZZZZZZ]88],70mZk.m70]Z,69mZZZk.m]ZZZZZZZZZZZZ]ZZZZ]ZZ,69mZZZk.mZZ],70mZZZZk.m]01]Z,69mZZZk.mZ]Z]ZZZZZZZ],ZZm70k.m76]70,88mZZk.m]04],70mZk.m85]Z]88]Z,ZZm70k.mZ]69,76mZZZk.m76],76mZk.mZZZ]ZZ,69mZZZk.m]88]69,69mZZZk.m]70,69mZZZZk.m69]85]70]ZZZ],70mZk.m88]70,69mZZZZk.m69]ZZZ,69mZZZk.mZ]ZZZZZ]Z]70]ZZZZZZZZZ],69mZZZZZk.mZZZ]mZZZZZZZZZZ],69mZZZZZZZk.m69]69,76mZk.m76]70,69mZZZZk.m]Z]69,85mZk.mZZZ]69,70mZZk.m76]96]ZZZZZZZZ],70mZk.m70],76mZZZZZZZk.m]08]ZZZZZZZZZZZZZ]Z]85],70mZk.m88]70,69mZZZZk.m]ZZZ,69mZZZk.m]ZZZZZZZZ]ZZZ]69],69mZZZZZk.mZZZ]mZZZZZZZZZZ],69mZZZZZZZk.m69]69,76mZk.m76]85,69mZZZZk.mZ]ZZZZ],69mZZZk.mZZ]76,70mZk.m76]05],70mZk.m70]70,69mZZZZk.m69]05]83]69,70mZk.m69]70]ZZZ,69mZZZk.mZZ]ZZZZZZZZZZZZ]98]ZZZZZZZZZ]ZZZZZZ]ZZZ,69mZZZk.m]76,70mZk.m69]ZZ,69mZZZk.m]88]ZZZZZZZZ],70mZk.m70]70,69mZZZZk.m69]ZZZ,69mZZZk.mZ]ZZZZZ]Z]70]ZZZZZZZZZ],70mZk.m88],69mZZZk.mZ]ZZZZZZZZZZZZZ]08]ZZZZZ]70]76,70mZk.m69]70,69mZZZZk.m]ZZZ,69mZZZk.m],69mZZZk.m69]"

#UTILS:

def rot47(s):
    x = []
    for i in range(0,len(s)):
        j = ord(s[i])
        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(s[i])
    return ''.join(x)


def numbersToDashes(msg, numList, bsList):
	if(len(numList)!=len(bsList)): 
		print("numList len="+str(len(numList))+"; bsList len="+str(len(bsList)))
		return "error"
	for k in range(0, len(numList)):
		msg=msg.replace(numList[k],bsList[k])
	return msg
# /UTILS


# Il messaggio è criptato in ROT47 (estensione del ROT13 usato in Mr. Robot)
# torno ai corretti caratteri ASCII, a parte per i numeri che non sono codificati in ROT47

rot47DecryptedMsg=""
rot47DecryptedMsg_noNums = rot47(cryptedMsg)
for k in range(0,len(cryptedMsg)):
	if(cryptedMsg[k]<= '9' and cryptedMsg[k]>='0'):
		rot47DecryptedMsg+=cryptedMsg[k]
	else:
		rot47DecryptedMsg+=rot47DecryptedMsg_noNums[k]

print("Codice con numeri al posto dei backslash:\n"+rot47DecryptedMsg)

# noto che i caratteri del messaggio così decriptato sono quelli del linguaggio Brainfuck. 
# devo trovare ancora quanti backslash corrispondono ad ogni cifra: un po' di try-and-catch sul convertitore textToBrainfuck

# trovo la corrispondenza e sostituisco
numbers=["01", "04", "05", "08", "69", "70", "76", "83", "85", "88", "93", "96", "98"]
dashes=["------------", "-------------", "----------", "-----------", "-", "---", "--", "------", "----", "-----", "---------","-------", "--------"]

bfCode=numbersToDashes(rot47DecryptedMsg,numbers,dashes);


# Salvo il codice in brainfuck in un file
fopn=open("brainfuckCode.txt", "w")
fopn.write(bfCode)
fopn.close()

# runnare il codice brainfuck ad esempio su https://copy.sh/brainfuck/ per ottenere il messaggio
