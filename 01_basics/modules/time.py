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

