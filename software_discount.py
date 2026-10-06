#Charles Ajjan
#CMP131
#Week06
#Lab01
#Software Discount
#Date started 09/30/2026
units_sold=float(input('Enter Amount of Units Sold:'))
Origional_cost=("Origional Cost : $99.00")
flat=(99.00+units_sold)
Quantity0= (99.00*units_sold)
Quantity1=(99.00*units_sold-99.00*units_sold*.2)
Quantity2=(99.00*units_sold-99.00*units_sold*.3)
Qunatity3=(99.00*units_sold-99.00*units_sold*.4)
Quantity4=(99.00*units_sold-99.00*units_sold*.5)
ppu=(Quantity1 or Quantity2 or Qunatity3 or Quantity4 or flat or Quantity0 /units_sold)
print("Number of Units Sold:", units_sold)
print("Origional Cost: $99.00",)
print((f"\nPrice Per Unit: ${ppu:.2f}"))
print(((f"\nNone Discounted price: ${flat:.2f}")))

if units_sold >=1 and units_sold <=9:  
    print(f"\nDiscount NONE: ${Quantity0:.2f}")
elif units_sold >=10 and units_sold <= 19:
    print(f"\nDiscount 20%: ${Quantity1:.2f}")
elif units_sold >=20 and units_sold <=49:
    print(f"\nDiscount 30%: ${Quantity2:.2f}")
elif units_sold >= 50 and units_sold <=99:
    print(f"\nDiscount 40%: ${Qunatity3:.2f}")
else:
    print(f"\nDiscount 50%: ${Quantity4:.2f}")



