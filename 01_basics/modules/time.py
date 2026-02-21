# The "time" module provides funcations to work with time-related tasks
# key uses:
      # measures execution time of code(benchmarking)
      # pause program exection(sleep)
      # get current time in seeconds since epoch(jan 1,1970)
      # convert between UTC and local time
      # format time into human-readable strings.
      # build clocks, timers, and alarms.

# import time
# time.time()  current time in seconds since epoch
# time.sleep(seconds) pause execution
# time.localtime() local time as struct_time
# time.gmtiime() UTC time as struct_time
# time.ctime() human-readable current time
# time.strftime("%Y-%m-%d $H:%M:%S",time.localtime())
# time.strptime("2026-02-21 09:30:00","%Y-%m-%d $H:%M:%S")
# both belows for high-precision times for benchmarking
# time.pref_counter()
# time.process_time()

# Challenge-Wise practice Questions

# Ch 1 (stopwatch)
   # start a timer when user presses Enter.
   # stop when user presses Enter again.
   # print elapsed time.
# import time
# input("Press Enter to start the stopwatch....")
# start_time=time.time() # record start time
# input("Press Enter to stop the stopwatch....")
# end_time=time.time()
# elapses=end_time-start_time
# print(f"Elpased time: {elapses:.2f} seconds") 

# # Ch 2 (countdown timer)
# #     Input: number of seconds 
# #     print countdown second by second
# #     End with "Time's up!"
# import time
# sec=int(input("Enter countdown time in  seconds: "))
# print("Countdown starts now!")
# # for i in range(sec,0,-1):
# #     print(i)
# #     time.sleep(1)
# while sec>0:
#     print(sec)
#     time.sleep(1)
#     sec-=1
# print("Time's up!")

# # Challenge 3 (Execution time measurement)
#   # Write a function that sums numbers from 1 to 1,000,000
#   # measure how long it takes using time.pref.counter()
# import time as tm
# def sum_nums(n):
#     total_sum=0
#     for i in range(1,n+1):
#         total_sum+=i
#     return total_sum
# start=tm.perf_counter()
# result=sum_nums(1000000)
# end=tm.perf_counter()
# print("Sum: ",result)
# print(f"Execition time: {end-start:.6f} seconds")

# # Ch 4 (Digital clock)
#    # Continuously print current time in HH:MM:SS
#    # Update every second.
# import time as tm
# print("Digital Clock(press Ctrl+C to stop)") # ctrl+c is universal way to stop a python program(sends a KeyboardInterrupt)
# while True:
#     current_time=tm.strftime("%H:%M:%S",tm.localtime())
#     print(current_time,end="\r") # overwrite the same line
#     tm.sleep(1)








