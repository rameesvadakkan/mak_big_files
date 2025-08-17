try:
 print("Enter numbers :")
 mylist = [int(input()) for i in range(6)]
 square_list = [i**2 for i in mylist]
 even_list = [i for i in mylist if i % 2 == 0]
 prime_list = [n for n in mylist if n > 1 and all(n % d != 0 for d in range(2, int(n**0.5) + 1))]
 print(f"Original list {mylist}")
 print(f"Square: {square_list}")
 print(f"Even List: {even_list}")
 print(f"Prime list: {prime_list}")
except Exception as e :
    print(str(e))

