class Time:
    def __init__(self,h,m,s):
        self.s=s
        self.m=m
        self.h=h
    def show(self):
        print(self.h,":",self.m,":",self.s)

    def zaman_sanieh(self):
        result=(self.h*3600)+(self.m*60)+(self.s)
        return result
    
    def sanieh_zaman(self,f):
        self.h = f// 3600
        f=f-(self.h*3600)
        self.m=f//60
        f=f-(self.m*60)
        self.s=f

time=Time(2,24,30)

f=4600
t=Time(None,None,None)
t.sanieh_zaman(f)
t.show()
result=time.zaman_sanieh()
print(result)

    


# result_stoz=time.sanieh_zaman()
# result_stoz.show()
