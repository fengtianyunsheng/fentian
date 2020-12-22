import datetime
import locale
import time

locale.setlocale(locale.LC_CTYPE, 'chinese')
class Date_calculaion:
    dic = {'Sunday':'星期日',
                'Monday':'星期一',
                'Tuesday':'星期二',
                'Wednesday':'星期三',
                'Thursday':'星期四',
                'Friday':'星期五',
                'Saturday':'星期六'}

    def Clac_ZBdate(self,last,step,frequency):
        
        LastDay = datetime.date.today()+datetime.timedelta(days=last)
    
        a = 0
    
        for i in range(frequency):
            
            a += step
            
            ZhiBanDay = LastDay + datetime.timedelta(days=a)

            ZBDWeek = self.dic[str(ZhiBanDay.strftime('%A'))]
            
            ZhiBan = str(ZhiBanDay) + ZBDWeek     
            
            print('您于'+str(ZhiBanDay.strftime('%Y年%m月%d日'))+'值班，'+'这一天是'+ZBDWeek)

    def IS_ZBdate(self,date1,date2,step1):

        date1=datetime.datetime.strptime(date1,"%Y%m%d")

        date2=datetime.datetime.strptime(date2,"%Y%m%d")

        date2_week = self.dic[str(date2.strftime('%A'))]
        
        Date_difference = int((date2 - date1).days)

        remainder = Date_difference % step1

        if remainder == 0:
            print(str(date2.strftime('%Y年%m月%d日'))+'您值班,这一天是'+date2_week)
        else:
            print(str(date2.strftime('%Y年%m月%d日'))+'这一天您不值班')


if __name__ == "__main__":
    function_select = str(input("计算接下来的值班日期请输入1，计算某年某月每日是否值班请输入2："))
    if function_select == '1':
        last = int(input("请输入您上次值班或下次值班距今的日期，用-号表示过去的天数："))
        step = int(input("请输入每次值班间隔几天："))
        fre = int(input('请输入要计算接下来的几个排班：'))
        Day = Date_calculaion()
        Day.Clac_ZBdate(last,step,fre)
    elif function_select == '2':
        Day = Date_calculaion()
        date1 = str(input('请输入您上次值班的日期，格式为20201010：'))
        date2 = str(input('请输入您想要判断是否值班的日期，格式为20201010：'))
        step = int(input("请输入每次值班间隔几天："))
        Day.IS_ZBdate(date1,date2,step)
    else:
        print('不好意思，暂时没有该选项功能，Bye-Bye')
    