from translate import Translator
translator = Translator(to_lang ="ja")


my_file = open('C:\\Users\\User\\Desktop\\תכנות\\python\\test.txt','r')

translation = translator.translate("hello, sushi is tasty")
print(translation)
