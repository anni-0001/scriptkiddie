
import pyautogui
# import matplotlib
import webcolors
import time



def grabber():
    time.sleep(2)

    x, y = pyautogui.position()

    r, g, b = pyautogui.pixel(x, y)


    print('RGB= ','(',r,',', g, ',', b, ')', sep = '')


    hex_code = webcolors.rgb_to_hex((r,g,b))

    return hex_code


def main():

    print(grabber())



main()