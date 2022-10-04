import pyjokes

print("Welcome to the Joke Generator")
num = int(input("Enter the number of jokes to be genrated: "))

for i in range(num):
    print(f"{i+1}. {pyjokes.get_joke( )}")
