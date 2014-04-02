#----------Algorithm

#set divisor=2
#set dividend = given number
#do:
#	check dividend%divisor == 0
#		yes : quotient = dividend/divisor; dividend = quotient; continue
#		no : divisor++; continue
#	if dividend==divisor : break;
#print divisor (or dividend - as dividend = divisor at the end of the loop)

dsor = 3
ddend = 600851475143

print dsor

#for i in range(3):
while True:
#	print dsor
#	print ddend
#	if dsor == 1:
#		break
	if dsor >= ddend:
		break
	elif ddend%dsor==0:
		ddend = ddend/dsor
		continue
	else:
		dsor+=1


print 'Largest Prime Factor = ', ddend
