# The "time" module provides funcations to work with time-related tasks
# key uses:
#       measures execution time of code(benchmarking)
#       pause program exection(sleep)
#       get current time in seeconds since epoch(jan 1,1970)
#       convert between UTC and local time
#       format time into human-readable strings.
#       build clocks, timers, and alarms.

# import time
# time.time()  current time in seconds since epoch
# time.sleep(seconds) pause execution
# time.localtime() local time as struct_time
# time.gmtiime() UTC time as struct_time
# time.ctime() human-readable current time
# time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
# time.strptime("2026-02-21 09:30:00","%Y-%m-%d $H:%M:%S")
# both belows for high-precision times for benchmarking
# time.pref_counter()
# time.process_time()

# Challenge-Wise practice Questions

# Ch 1 (stopwatch)
   # start a timer when user presses Enter.
   # stop when user presses Enter again.
   # print elapsed time.
import time as tm
input("Press Enter to start the stopwatch....")
start_time=tm.time() # record start time
input("Press Enter to stop the stopwatch....")
end_time=tm.time()
elapses=end_time-start_time
print(f"Elpased time: {elapses:.2f} seconds") 

# Ch 2 (countdown timer)
#     Input: number of seconds 
#     print countdown second by second
sec=int(input("Enter countdown time in  seconds: "))
print("Countdown starts now!")
# for i in range(sec,0,-1):
#     print(i)
#     time.sleep(1)
while sec>0:
    print(sec)
    tm.sleep(1)
    sec-=1
print("Time's up!")

# Challenge 3 (Execution time measurement)
  # Write a function that sums numbers from 1 to 1,000,000
  # measure how long it takes using time.pref.counter()

def sum_nums(n):
    total_sum=0
    for i in range(1,n+1):
        total_sum+=i
    return total_sum
start=tm.perf_counter()
result=sum_nums(1000000)
end=tm.perf_counter()
print("Sum: ",result)
print(f"Execition time: {end-start:.6f} seconds")

# Ch 4 (Digital clock)
   # Continuously print current time in HH:MM:SS
   # Update every second.

# print("Digital Clock(press Ctrl+C to stop)") # ctrl+c is universal way to stop a python program(sends a KeyboardInterrupt)
# while True:
#     current_time=tm.strftime("%H:%M:%S",tm.localtime())
#     print(current_time,end="\r") # overwrite the same line
#     tm.sleep(1)

# Ch 5 (Loading Simulation)
   # print "Loading.","Loading..","Loading..." with 1- second delay.
   # repeat 3 times.

print("Loading Simulations:")
for i in range(3):
    for dots in range(1,4):
        text="Loading"+"."*dots
        print(text.ljust(12),end='\r',flush=True) #text.ljust(12)-ensures that string is always padded to at least 12 characters, so shorter version overwrite longer ones
                                                  #flush=True - forces immediate printing(important for smooth animation)
        tm.sleep(1)
print("Done!")

# Ch 6 (Local vs UTC)

# print local time 
local_time=tm.strftime("%Y-%m-%d %H:%M:%S",tm.localtime())
# print UTC time
utc_time=tm.strftime("%Y-%m-%d %H:%M:%S",tm.gmtime())
print(f"Local time : {local_time} ")
print(f"UTC time : {utc_time} ")

# Ch 7 (Alarm Clock)
# input:time
# Continuously check current time.
# When it matches, print "Alarm rigining."
import time
alarm_time=input("Enter alarm time(HH:MM): ")
print(f"Alarm set for {alarm_time}....")
while True:
    current_time=time.strftime("%H:%M",time.localtime())
    if(current_time==alarm_time):
        print("Alarm ringing...")
        break
    time.sleep(30) # sleep to avoid constant time checking (optional)

# Ch 8 (Benchmark Comparison)
# Compare execution time of:
     # Loop appending numbers to a list.
     # Loop appending numbers to a tuple(new tuple each time).
# Use time.perf_counter().
# for list

list_st_time=tm.perf_counter()
list1=[ x for x in range(10000)]
list_en_time=tm.perf_counter()
tuple_st_time=tm.perf_counter()
tuple1=(x for x in range(10000))
tuple_en_time=tm.perf_counter()
print(f"The execution time for list is {list_en_time-list_st_time:.6f}")
print(f"The execution time for list is {tuple_en_time-tuple_st_time:.6f}")




