"""
Connor Cox
U3 Lab 1
While Substitution
"""

def while_substitute(num):
  storage = []
  while num >= 1:
    print(f"Recursing; num = {num}")
    storage.append(num)
    num -= 1
    if num == 0:
      index = 0
      print("\nBASE CASE REACHED\n")
      while index < 5:
        index += 1
        number = storage[-index]
        print(f"Returning; num = {number}")

  

def main():
  while_substitute(5)

if __name__ == "__main__":
  main()