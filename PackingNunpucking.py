numbers = [1,2,3,4,5]
print(numbers)


def add(x,y):
    return x+y
##how to use a lot of parameters? Just add *before argument
def add(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return(total)    


add(1,2,3,4,5,6,7,8,9)

def about(name,age,likes):
    sentence = "Meet {}! He is {} years old and he likes {}".format(name, age, likes)
    return sentence

dictionary = {"name":"Andriy", "age":28, "likes":"Katerine"}
about(**dictionary)

##*args
##**keys


def foo(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key, value))
        
