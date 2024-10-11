

ItemsInCart = 0

if ItemsInCart != 2:
    #raise Exception("Products Cart count not matching")
    pass

assert(ItemsInCart == 0)

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except:
    print("Somehow I reached this block cause there is failure in try block")


#If you want Python show us its exception instead only my code try catch
try:
    with open('test.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning up resources")




