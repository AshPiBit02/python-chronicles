# format specifiers = {:flags} format a value based on what flags are inserted
# .(number)f=round to that many decimal places(fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = centre justify
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comman separator
num1=19955.2342
num2=-9845.12302
print(f" num is {num1:.2f}")
print(f" num is {num2:.2f}")
print(f" num is {num1:20}")
print(f" num is {num2:20}")
print(f" num is {num1:<}")
print(f" num is {num2:<}")
print(f" num is {num1:>}")
print(f" num is {num2:>}")
print(f" num is {num1:^}")
print(f" num is {num2:^}")
print(f" num is {num1:+,}")
print(f" num is {num2:+}")