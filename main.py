import pyautogui as pg
import time, cv2
import numpy as np


def confirm():
    while True:
            template = cv2.imread('confirm.png', cv2.IMREAD_GRAYSCALE)
            screenshot = np.array(pg.screenshot())
            gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if max_val >= 0.8:
                x, y = max_loc
                w, h = template.shape[::-1]
                x += w // 2
                y += h // 2
                print("Confirm Button Found")
                pg.moveTo(x,y)
                time.sleep(0.5)
                pg.click(x, y)
                time.sleep(1)
                pg.moveTo(1090, 500)
                break # exit the loop
            else:
                print("Confirm Button Not Found")
                time.sleep(0.01)


def nested_loop_Youtube_subs():
    pg.click(557,47)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pg.typewrite("https://www.like4like.org/user/earn-youtube-subscribe.php")
    pg.press('enter')
    time.sleep(5)

    start_time = time.time() 
    while True:
        yt_earn_button = cv2.imread('yt_earn_button.png', cv2.IMREAD_GRAYSCALE)
        yt_subs_no_more = cv2.imread('yt_subs_no_more.png', cv2.IMREAD_GRAYSCALE)
        screenshot = np.array(pg.screenshot())
        gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        yt_earn_button_result = cv2.matchTemplate(gray_screenshot, yt_earn_button, cv2.TM_CCOEFF_NORMED)
        yt_subs_no_more_result = cv2.matchTemplate(gray_screenshot, yt_subs_no_more, cv2.TM_CCOEFF_NORMED)
        yteb_min_val, yteb_max_val, yteb_min_loc, yteb_max_loc = cv2.minMaxLoc(yt_earn_button_result)
        ytsnm_min_val, ytsnm_max_val, ytsnm_min_loc, ytsnm_max_loc = cv2.minMaxLoc(yt_subs_no_more_result)
        if yteb_max_val >= 0.8:
            x, y = yteb_max_loc
            w, h = yt_earn_button.shape[::-1]
            x += w // 2
            y += h // 2
            print("Youtube Earn Button Found")
            time.sleep(0.5)
            pg.click(x, y)
            time.sleep(0.5)
            pg.moveTo(1200, 800)
            start_time = time.time() 
            while True:
                yt_subs_button = cv2.imread('yt_subs_button.png', cv2.IMREAD_GRAYSCALE)
                yt_unsubs_button = cv2.imread('yt_unsubs_button.png', cv2.IMREAD_GRAYSCALE)
                screenshot = np.array(pg.screenshot())
                gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
                yt_subs_button_result = cv2.matchTemplate(gray_screenshot, yt_subs_button, cv2.TM_CCOEFF_NORMED)
                yt_unsubs_button_result = cv2.matchTemplate(gray_screenshot, yt_unsubs_button, cv2.TM_CCOEFF_NORMED)
                ytsubsb_min_val, ytsubsb_max_val, ytsubsb_min_loc, ytsubsb_max_loc = cv2.minMaxLoc(yt_subs_button_result)
                ytunsubsb_min_val, ytunsubsb_max_val, ytunsubsb_min_loc, ytunsubsb_max_loc = cv2.minMaxLoc(yt_unsubs_button_result)
                if ytsubsb_max_val >= 0.8:
                    x, y = ytsubsb_max_loc
                    w, h = yt_subs_button.shape[::-1]
                    x += w // 2
                    y += h // 2
                    print("Youtube Subs Button Found")
                    time.sleep(0.5)
                    pg.click(x, y)
                    time.sleep(2)
                    pg.hotkey("ctrl", "w")
                    break
                elif ytunsubsb_max_val >= 0.8:
                    x, y = ytunsubsb_max_loc
                    w, h = yt_unsubs_button.shape[::-1]
                    x += w // 2
                    y += h // 2
                    print("Youtube UnSubs Button Found")
                    time.sleep(0.5)
                    pg.click(x, y)
                    time.sleep(2)
                    pg.hotkey("ctrl", "w")
                    break
                else:
                    print("Youtube Subs Or Unsubs Button Not Found")
                    time.sleep(0.1)
                    elapsed_time = time.time() - start_time
                    print(elapsed_time)
                    if elapsed_time >= 30:
                        print("Elapsed time exceeded 30 seconds, exiting the loop")
                        break # exit the loop
            confirm()   



            
        elif ytsnm_max_val >= 0.8:
            x, y = ytsnm_max_loc
            w, h = yt_subs_no_more.shape[::-1]
            x += w // 2
            y += h // 2
            print("Youtube earns No More Pleas Wait 20 minutes")
            time.sleep(1200)
            break
        else:
            print("Youtube Earn or Youtube earns No More Button Not Found")
            time.sleep(0.1)
            elapsed_time = time.time() - start_time
            print(elapsed_time)
            if elapsed_time >= 30:
                print("Elapsed time exceeded 30 seconds, exiting the loop")
                break # exit the loop
    

        
            
    

    


pg.click(557,47)
nested_loop_Youtube_subs()
            
            