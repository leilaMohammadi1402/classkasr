class Kasr:
    def __init__(self,s,m) :
        self.s=s
        self.m=m

    def show(self):
        print(self.s,"/",self.m)

    def zarb(self,f):
        result=Kasr(None,None)
        result.s=self.s*f.s
        result.m=self.m*f.m
        print("zarb:")
        return result

    def jam(self,f):
        result=Kasr(None,None)
        result.s=(self.s*f.m)+(f.s*self.m)
        result.m=self.m*f.m
        print('jam:')
        return result

    def tahsim(self,f):
        result=Kasr(None,None)
        result.s=self.s*f.m
        result.m=self.m*f.s
        print('taghsim:')
        return result

    def menha(self,f):
        result=Kasr(None,None)
        result.s=(self.s*f.m)-(f.s*self.m)
        result.m=self.m*f.m
        print("menha:")
        return result


    
f1=Kasr(3,5)
f2=Kasr(4,8)
f1.show()
f2.show()

result_z=f1.zarb(f2)
result_z.show()

result_j=f1.jam(f2)
result_j.show()

result_t=f1.tahsim(f2)
result_t.show()

result_m=f1.menha(f2)
result_m.show()
