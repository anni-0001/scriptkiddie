import pyautogui
import time


auto = pyautogui

print(pyautogui.size())


def basic_mouse_movement(amount, x, y):
    try:
        for i in range(amount):
            pyautogui.moveRel(x, y, duration = .5)
            print(pyautogui.position(), '\n')

    except KeyboardInterrupt:
        print('\ndDone.')


# prints mouse coordinates of user activity, not program moving mouse
def print_mouse_coords():
    print('hit control-c to quit')
    
    try:
        while True:
            x,y = pyautogui.position()
            positionStr = 'X: ', str(x) , '  ', 'Y: ', str(y)
            print(positionStr)
            print('\b' * len(positionStr), end='', flush= True)
            
    except KeyboardInterrupt:
        print('\ndone')
    
# dragging mouse -- not working
def click_mouse():

    time.sleep(5)
    auto.click()


    
    # pyautogui.move(x, y, duration = .5)
    # pyautogui.click(10,5)
    

# makes an alert box, makes a password log-in alert box, takes screenshots 
def display_message():
    # pyautogui.alert('This is an alert')
    # pyautogui.confirm(text = 'Hi butthole', title='', buttons=['yes', 'no'])

    # auto.password(text = '', default = 'abcdefg', mask = '*')

    # img1 = auto.screenshot()
    # img2 = auto.screenshot('img123.jpg')

    auto.sleep(5)

# not working yet
# should locate an image on screen based off the image provided in strawberry var
def locate_on_screen():
    # print_mouse_coords()
    time.sleep(5)
    strawberry = auto.locateOnScreen('simple_strawberry.png', confidence= .2)
    print(strawberry)
    return strawberry
    
    # if strawberry == None:
    #     print('not found')
    # else:
    #     # print(strawberry)
    #     print(strawberry)
    #     # print('hi') 
    #     # auto.click(x,y)

    
def pixel_matching():
    img = auto.pixel(100, 200)
    print(img)



def main():
    # basic_mouse_movement(10, 10, 40)
    # print_mouse_coords()


    # click_mouse()



    # print(display_message())



    locate_on_screen() # returns the same val everytime- not working

    # pixel_matching()



main()
