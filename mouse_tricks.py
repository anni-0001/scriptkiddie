import pyautogui


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
    
# dragging mouse
def click_mouse(x, y):

    
    pyautogui.move(x, y, duration = .5)
    pyautogui.click(10,5)
    
    
def display_message():
    # pyautogui.alert('This is an alert')
    # pyautogui.confirm(text = 'Hi butthole', title='', buttons=['yes', 'no'])
    # auto.password(text = '', default = 'abcdefg', mask = '*')
    img1 = auto.screenshot()
    img2 = auto.screenshot('img123.jpg')

    




def main():
    # basic_mouse_movement(10, 10, 40)
    # print_mouse_coords()
    # click_mouse(400, 300)
    display_message()


main()
