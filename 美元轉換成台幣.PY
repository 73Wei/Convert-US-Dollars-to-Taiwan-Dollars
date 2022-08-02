print('==================================')
"""
=====第一題：匯率轉換=====
美金：   Entry
台幣：
Button
Exchange Rate：29.89
提示：
str1=”12.5”              
x=float(str1)*10              # 字串轉浮點數
y=str(x)                      # 浮點數轉字串
"""

print("=====第一題：匯率轉換=====")

"""
def exchangeRateUSDToTWD():                                 # 此種寫法 會無法把輸入的數字和 視窗輸入框的數字做連結                                                     
    n=float(input("美金:"))                                  # 思考邏輯-幾個對話框 幾個label 幾個要轉換的程序  串聯一起
    n1=str(n*29.94)

    return n1

#print("美金轉台幣為:",exchangeRateUSDToTWD())

def exchangeRateTWDToUSD():

    x=float(input("台幣:"))
    x1=str(x*0.033)

    return x1

#print("台幣轉美金為:",exchangeRateTWDToUSD())

"""

import tkinter as tk                                          # 在Python 3.x 匯入該tkinter 函式庫
from PIL import ImageTk, Image                                # 匯入 圖片 函示庫

#建立視窗
win = tk.Tk()                                                 # 步驟2：建立GUI 應用程式的主視窗
win.wm_title("0714HW-01-exchangeRate")                        # 視窗 上的標題
win.resizable(width=False, height=False)                      # 是否可以調整
win.minsize(width=480, height=480)                            # 最小的視窗
win.maxsize(width=480, height=480)                            # 最大的視窗


# 建立背景 圖片來源：https://www.ypppt.com/p/d.php?aid=410
x=Image.open("background-01.jpg")                              # 讀取圖片
img = ImageTk.PhotoImage(x)                                    # 轉換成PhotoImage
label1 =tk.Label(win, image = img)                             # 建立Label物件 顯示圖片
label1.pack()


def exchangeRateUSDToTWD():
   global usdStr
   global twdStr
   global exrate
   getEntry = entry1String.get()                                 # 取得entry1 上的文字  用getEntry 變數包起來
   usdStr.set("USD："+str(float(getEntry)))                      # 設定 usdStr 上文字   (轉換浮點數到字串)
   exchangeStr.set("Exchange Rate："+str(exrate))                # 設定 exchangeStr 上文字
   twdStr.set("TWD："+str(float(getEntry) * exrate))             # 設定 twdStr 上文字


# 1. 輸入框Entry
entry1String = tk.StringVar()
entry1=tk.Entry(win,textvariable = entry1String,font=("微軟正黑體", 15),fg="black",bd=4)  #bd是 輸入框的邊 預設值是 2
entry1.place(x=120, y=50)
entry1String.set("輸入美金")

# 2.顯示從美金金額
# Label usdStr usd
usdStr = tk.StringVar()                                                                  #  建立StringVar 變數
usdLabel =tk.Label(win,text="用戶輸入的資料", textvariable=usdStr,font=("微軟正黑體", 15))    #  建立Label物件, 綁定這個變數
usdLabel.place(x=30, y=150)
usdStr.set("USD：0.0")

# 3.顯示台幣金額
twdStr = tk.StringVar()                                                                      # 建立StringVar 變數
twdLabel = tk.Label(win,text="twdLabel", textvariable=twdStr,font=("微軟正黑體", 15))          # 建立Label物件, 綁定這個變數
twdLabel.place(x=30, y=200)                                                                  # 指定位置
twdStr.set("TWD：0.0")

# 4.USD 轉換 label-美金轉台幣匯率的文字
exrate = 29.94
exchangeStr = tk.StringVar()                                                                        # 建立StringVar 變數
exchangeLabel = tk.Label(win,text="exchangeLabel", textvariable=exchangeStr,font=("微軟正黑體", 10))  # 建立Label物件, 綁定這個變數
exchangeLabel.place(x=30, y=300)                                                                    # 指定位置
exchangeStr.set("Exchange Rate："+str(exrate))

# 5.按鈕Button
convertButton = tk.Button(win,text="按我\n進行\n轉換",command=exchangeRateUSDToTWD,font=("微軟正黑體", 15))# 建立Button物件 按下後會出叫 函式
convertButton.place(x=350, y=150)

win.mainloop()                                                                                       # 最後步驟：程式做無限循環



