import tkinter
import datetime
import tkinter.font

today = datetime.date.today()
target_day = datetime.date(2023,1,9)
d_day = today-target_day
# print('D+day : {0}일'.format(d_day.days))
day_count = tkinter.Tk()

day_count.title('MS&JH D-day')
day_count.geometry('480x320+1000+450')
day_count.resizable(False,False)
day_count.configure(bg='white')

title_font=font = tkinter.font.Font(family = '굴림체',size=16,weight='bold')
font = tkinter.font.Font(family = '굴림',size=36,weight='bold')

label = tkinter.Label(day_count, text = 'MS&JH D-day',width=14,height=2,bg='pink',font=title_font)
label2 = tkinter.Label(day_count,text = '사귄날 : 2023년 1월 10일',font=tkinter.font.Font(size=12),bg='white')
label3 = tkinter.Label(day_count, text = '오늘 날짜 : {0}년 {1}월 {2}일'.format(today.year,today.month,today.day),font=tkinter.font.Font(size=12),bg='white')
label4 = tkinter.Label(day_count,text = 'D+day : {0}일'.format(d_day.days),bg='pink',font=font)

label.pack()
label2.pack()
label3.pack()
label4.pack(expand=True,fill='both')

day_count.mainloop()