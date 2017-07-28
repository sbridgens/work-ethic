strK = "knowledge"
strHW = "hardwork"
strATT = "attitude"
ansAlpha = ""
ansNum = ""
kStr = ""
hwStr = ""
attStr = ""
ansK = 0
ansHW = 0
ansATT = 0
values = {chr(i): i + 1 for i in range(ord("a"), ord("a") + 26)}
for alpha in sorted(values):
    if not alpha == 'z':
        ansAlpha += alpha + ", "
    else:
        ansAlpha += alpha
for nums in sorted(values):
    if not nums == 'z':
        ansNum += ''.join(str(values[nums] - 97) + ", ")
    else:
        ansNum += ''.join(str(values[nums] - 97))
for k in strK:
    if k == strK[:-1]:
        kStr += ''.join(str(values[k] - 97))
    else:
        kStr += ''.join(str(values[k] - 97) + "+")
    ansK = values[k] - 97 + ansK
kStr = kStr[:-1]
for hw in strHW:
    if hw == strHW[-1]:
        hwStr += ''.join(str(values[hw] - 97))
    else:
        hwStr += ''.join(str(values[hw] - 97) + "+")
    ansHW = values[hw] - 97 + ansHW
for att in strATT:
    if att == strATT[-1]:
        attStr += ''.join(str(values[att] - 97))
    else:
        attStr += ''.join(str(values[att] - 97) + "+")
    ansATT = values[att] - 97 + ansATT
print "IF:\n" + ansAlpha
print
print "EQUALS:\n" + ansNum
print
print "THEN:\nK+N+O+W+L+E+D+G+E\n" + kStr + " = " + str(ansK) + "%"
print
print "AND:\nH+A+R+D+W+O+R+K\n" + hwStr + " = " + str(ansHW) + "%"
print
print "BUT:\nA+T+T+I+T+U+D+E\n" + attStr + " = " + str(ansATT) + "%"
print
    
