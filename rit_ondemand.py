import pyautogui
import time

order_image_rit_website = 'images/order_orange.png'
closed_order_button = 'images/closed_pickup.png'
shopping_cart = 'images/shopping_cart.png'




# use var names for images for each restruants 
# if pickup image is grayed out - return that the restuant is closed and pick a new one

def rit_web_order_button():
    time.sleep(2)
    try:
        x, y = pyautogui.locateCenterOnScreen(order_image_rit_website)
        print(f'I found it...{x} by {y}')
    except TypeError:
        print('did not work, sorry anni')
        return 

    pyautogui.click(x, y)
    print('just clicked!')

def click_shopping_cart():
    try:
        x, y = pyautogui.locateCenterOnScreen(shopping_cart)
        print(f'I found it...{x} by {y}')
    except TypeError:
        print('did not work, sorry anni')
        return
    
    pyautogui.click(x, y)
    print('just clicked!')

    


def main():
    rit_web_order_button()
    time.sleep(12)
    # click_shopping_cart()


    


main()




# recognizes the wireshark icon on the website and clicks out of the window automatically - or
# 