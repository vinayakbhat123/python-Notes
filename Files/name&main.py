#__name__ == __main__  dunder
# __name__ and __main__ are special built-in variables used to control how a file behaves when it is run vs imported.

# What is __name__?

# __name__ stores the name of the current module.
# If a file is run directly → __name__ == "__main__"
# If a file is imported → __name__ == "filename"

# ⭐ Interview One-Line Answer
# __name__ == "__main__" ensures that code runs only when the file is executed directly, not when imported as a module.
print(__name__)

def add(a,b):
  return a+b

def mul(x,y):
  return x*y

def main():
  print(add(3,5))
  print(mul(5,4))

if __name__ == "__main__":
  main()
  