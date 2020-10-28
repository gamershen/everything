# import the following libraries 
# will convert the image to text string 
import pytesseract       
  
# adds image processing capabilities 
from PIL import Image     
        
  
#translates into the mentioned language 
from googletrans import Translator       
  
 # opening an image from the source path 
img = Image.open('C:\\Users\\User\\Desktop\\python screenshots\\shapestone_price_4.png')   
  
# describes image format in the output 
print(img)                           
# path where the tesseract module is installed 
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'   
# converts the image to result and saves it into result variable 
result = pytesseract.image_to_string(img)    
# write text in a text file and save it to source path    
with open('abc.txt',mode ='w') as file:      
      
                 file.write(result) 
                 print(result) 
                   
p = Translator()                       
# translates the text into german language 
k = p.translate(result,dest='german')       
print(k) 
