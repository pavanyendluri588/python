def fun():
   inp=str(input("Enter the palindrome:"))
   inp1=inp[::-1]
   if inp==inp1:
        print("palindrome")
   else:
        print("not palindrome")
fun()