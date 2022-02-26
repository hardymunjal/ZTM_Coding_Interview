from time import time

small_arr = ["nemo"]

medium_arr = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']

large_arr = ["Random"]*1000000
large_arr.append("nemo")

def findNemo_simple(arr):
  for i in range(0, len(arr)):
    if arr[i] == "nemo":
      print("FOUND NEMO!")


def findNemo_time_analysis(arr):
  start = time()

  for i in range(0, len(arr)):
    if arr[i] == "nemo":
      print("FOUND NEMO!")
  
  end = time() - start
  print(f'Total time taken to run the program: {"{:.2f}".format(end)} seconds')

def findNemo_optimized(arr):
  pass

# Main
if __name__ == "__main__":
  # findNemo_simple(medium_arr) # O(n) --> linear time
  # findNemo_time_analysis(large_arr) # O(n) --> linear time
  findNemo_optimized(large_arr)