

#Задана строка S, состоящая из малых латинских букв. Требуется узнать длину наибольшей подстроки, в которой все буквы одинаковы.

#Например:
#
#"" -> 0
#"a" -> 1
#"abbc" -> 2
#"adddaabaa" -> 3



def p(x):
	new =' '
	chek = x[0]
	count=0
	for i in x:		
		if i == chek:
			count+=1

		else:
			new = chek + str(count)
			i = chek
			count =1  
	print

	return new
print('hello world')





print(p('sssaaafffffrrr'))

