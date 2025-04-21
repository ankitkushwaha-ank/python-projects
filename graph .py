# import matplotlib.pyplot as plt
# x = ['ankit','saurav','adarsh','unkwon','aayushi']
# y = [200,250,300,500,600]
# plt.plot(x,y, marker='o', label='marks')
#
# plt.xlabel('student')
# plt.ylabel('marks')
# plt.title ('marks graph')
# plt.legend()
# plt.scatter(x,y)
# plt.bar(x,y)
# plt.show ()
from cProfile import label

# import matplotlib.pyplot as graph
#
#
# x= ['rahul','shahshi','raza','naman']
# y = [274,748,264,633]
#
# graph.plot(x,y, marker = 'o', label= "college marks")
#
# graph.xlabel('students')
# graph.ylabel('marks')
#
# graph.title('result')
# graph.legend()
# graph.bar(x,y)
# graph.show()

# Encapsulation
# public,protected, and private attributes


class public:
    def __init__(self):
        self.name = 'shah'
        # 'SHAH'  # public variable

    def display_name(self):
        print(self.name)  # public method


obj1 = public()
# Accessible
obj1.display_name()
