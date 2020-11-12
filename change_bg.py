import win32gui
import win32con
import win32api
import random
import time
wallpaper_path="D:\\source\\python\\"
k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")
win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")

while True:
   wallpaper=wallpaper_path+str(random.randint(0,9))+".jpg"
   #print(wallpaper)
   time.sleep(60)
   win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,wallpaper, 1+2)

