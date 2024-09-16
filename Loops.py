
def main():
    num=get_number()
    mew(num)
    
    
    
def get_number():
    while True:
        n= int(input("what is  n ? "))
        if n>0:
            return n


def mew(n):
    for _ in range(n):
        print("mew")
    

main()
    
