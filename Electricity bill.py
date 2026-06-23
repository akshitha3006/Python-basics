unit_consumed = 63
if unit_consumed<50:
    print("The electricity bill is:",unit_consumed*2.60*25)
elif unit_consumed<100:
    print("The electricity bill is:",unit_consumed*3.25*35)
elif unit_consumed<200:
    print("The electricity bill is:",unit_consumed*5.25*45)
else:
    print("The electricity bill is:",unit_consumed*8.45*75)    
