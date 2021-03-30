import pyautogui
from PIL import Image , ImageGrab
import time
#from numpy import asarray


def hit(key):
    pyautogui.keyDown(key)

#def draw():
def iscollide(data):
# birds
    for i in range(225,380):
            for j in range(539,559):
               if data[i,j]<100 :
                 hit('down')
                 return True
# dino
    for i in range(250,450):
         for j in range(582,700):
             if (data[i,j]<100):
                 hit('up')
                 return True
    return False

    # birds
    for i in range(225,380):
         for j in range(539,559):
               if data[i,j]<255 :
                   hit('down')
                   return True
# dino
    for i in range(250,450):
         for j in range(582,700):
             if (data[i,j]<255):
                 hit('up')
                 return True
    return False




if __name__ == "__main__" :
    print("Dino Game is about to start in 3 sec....")
    time.sleep(3)
    #hit('up')
    while True:
         image=ImageGrab.grab().convert('L')
         data=image.load()
         iscollide(data)
        

         #print(asarray(image))
'''    
# Draw rectangle for cactus
         for i in range(250,450):
             for j in range(582,700):
                data[i,j]=0

        # Draw rectangle for birds     
         for i in range(225,380):
             for j in range(539,559):
                 data[i,j]=150

         image.show()
         break
'''
        




        