# #hii this ankit kumar and i am making a pogram that can help people to find a bug in there system
# def application(user_name , age , *hobbies):
#     print("welcome to cybernet security")
#     print(f'Hello {user_name}')
#     print(f'your age is {age}')
#     for hobby in hobbies:
#      print(f'your hobbies is {hobby}')
#     print("thanks for signing in")
#
# application("ankit kushwaha" , 18 , "hacking" , "cricket" , "coding")
#
# hii this ankit kumar and i am making a pogram that can help people to find a bug in there system
def application(user_name, age,*hoobies, **user_info):
    print("welcome to cybernet security")
    print(f'Hello " {user_name} "')
    print(f'you are {age} years old')
    print(f'your hobbies are')
    for hobby in hoobies:
        print(f'   -{hobby}')
    print("user information:")
    for key , value in user_info.items():
        print(f'    {key} - {value}')

    print("thanks for signing in")


application("Ankit kushwaha", 18 , "hacking", "coding", "playing cricket",
            vill = "lakhapur" , mobile_number=8092316838)




