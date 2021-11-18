import pyautogui
import time

# paths
wireshark_logo = 'images/wireshark_logo.png'


def spot_wireshark_logo(filepath):
    # time.sleep()
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen(wireshark_logo)
            print(f'I found it...{x} by {y}')
            return x, y
            
        except TypeError:
            print('did not work, sorry anni')
            return None

def close_wireshark_page(x, y):
    pyautogui.moveTo(x,y)
    # pyautogui.hotkey('alt', 'shift', 'q')

    pyautogui.confirm(text = 'SUCKER', title ='BUTTHOLE', buttons= ['stupid', 'nice'])
    # make a hard math problem in the password function they have to solve to exit
    
    
    
    # SCHEDULE QUITTING SCRIPT IN THE CRONTABS FOR EVERY SECOND
    # PUT ALL DIFF IMAGES OF SOFTWARE THAT REDTEAM DOESNT WANT OPEN AND CLOSE IT
            
            
    

    



def main():
    x, y = spot_wireshark_logo(wireshark_logo)

    close_wireshark_page(x,y)

main()



# instead of exing out miminize