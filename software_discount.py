#Charles Ajjan
#CMP131
#Week06
#Lab01
#Software Discount
#Date started 09/30/2026
units_sold=float(input('Enter Amount of Units Sold:'))
Origional_cost=("Origional Cost : f{99.00}")
Quantity0= (99.00*units_sold)
Quantity1=(99.00*units_sold-99.00*units_sold*.2)
Quantity2=(99.00*units_sold-99.00*units_sold*.3)
Qunatity3=(99.00*units_sold-99.00*units_sold*.4)
Quantity4=(99.00*units_sold-99.00*units_sold*.5)
if units_sold >=1 and units_sold <=9:  
    print("Discount: NONE","Total:", {Quantity0})
elif units_sold >=10 and units_sold <= 19:
    print("Discount: 20%", "Total:", (f{Quantity1}.2f))
elif units_sold >=20 and units_sold <=49:
    print("Discount: 30%","Total:", (f{Quantity2}.2f))
elif units_sold >= 50 and units_sold <=99:
    print("Discount: 40%","Total:", f{Qunatity3}.2f)
else:
    print("Discount: 50%","Total:", f{Quantity4}.2f)
print("Origional Cost: f{99.00}",)
print("Number of Untits Sold:", units_sold)



