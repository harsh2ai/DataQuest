def message(text, plain, encryp):
	dictionary = dict(zip(plain, encryp))
	newmessage = ''
	for char in text:
		try:
			newmessage += dictionary[char]
		except:
			newmessage += ' '
	print (text + '\nhas been encrypted to:')
	print (newmessage)

message('Many languages do not use articles (a, an, and the), or if they do exist, the way they are used may be different than in English. Multilingual writers often find article usage to be one of the most difficult concepts to learn. Although there are some rules about article usage to help, there are also quite a few exceptions. Therefore, learning to use articles accurately takes a long time. To master article usage, it is necessary to do a great deal of reading, notice how articles are used in published texts, and take notes that can apply back to your own writing.', 'a', encryp="encrypt" )
