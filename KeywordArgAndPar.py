def about(name, age, likes):
	sentence = "Meet {}! He's {} years old and he likes {}".format(name, age, likes)
	return sentence

about(age=23, name = "John", likes = "Potato")

##Default value. Just add it in arguments. Default value have to go last ALWAYS.
##U can't just add it in chaotic way.

#arguments -> what you see in def (age, name, likes)
#parameters -> what you pass when call def (John, 23, Potato)
def aboutWdefVal(name, age, likes="himself"):
	sentence = "Meet {}! He's {} years old and he likes {}".format(name, age, likes)
	return sentence


    
