class mark:
        def user_data(self):
                self.opt = int(input("theory mark"))
                self.oop = int(input("theory mark"))
                self.wp = int(input("theory mark"))
                
        def final_result(self):
                self.total = self.opt+self.oop+self.wp
                return self.total
        
student_1 = Mark()
student_1.user_data()
print(student_1.final_result())
        
                
