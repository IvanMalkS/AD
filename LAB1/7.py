import sys

def solve():
  try:
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    if n == 0:
      print(0)
      return

    shavings = n * b
    
    if shavings < a:
      print(n)
      return

    net_cost = a - b

    new_details = (shavings - a) // net_cost + 1
    
    total_details = n + new_details
    
    print(total_details)

  except (ValueError, IndexError):
    pass

if __name__ == "__main__":
  solve()
