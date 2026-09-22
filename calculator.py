
def add(a,b):
    return a+b

def subs(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    return a/b 


def main():
        try:
             a= float(input("Enter the first value : "))
             op=input("Enter the operator{+  -  * / } :")
             b=float(input("Enter the second value : "))

        except ValueError:
             print("Wrong Entry")
             return
        except ZeroDivisionError:
             print("You cant divide by 0. ")
             return
        if op=="+":
            result=add(a,b)
        elif op=="-":
            result=subs(a,b)
        elif op=="*":
             result=multi(a,b)
        elif op =="/":
             result=div(a,b)
            
        else:
             print("unknown operator")
             return 
        


        print (round(result),2 )
             

        
        

                
      

    



if __name__=="__main__":
    main()

