#Charles Ajjan
#CMP131
#Week06
#Lab01
#Mobile Phone Bill
#Date started 09/30/2026
print("Please Select A Service Plan:")
print("A) Package A: $39.99/mo, 450 mins included, $0.45/extra min")
print("B) Package B: $59.99/mo, 900 mins included, $0.40/extra min")
print("C) Package C: $69.99/mo, Unlimited mins included")
pacs = input("\nPlease Select Package A, B or C: ").strip().upper()
nom = int(input("Please enter number of Minutes Planned to used each month: "))
monthly_charge = 0.0
included_minutes = 0
extra_minute_rate = 0.0
unlimited = False
if pacs == 'A':
    print("\n[ PACKAGE A | Monthly charge: $39.99 | Included minutes: 450 | Additional minutes: $0.45 per minute ]")
    monthly_charge = 39.99
    included_minutes = 450
    extra_minute_rate = 0.45
elif pacs == 'B':
    print("\n[ PACKAGE B | Monthly charge: $59.99 | Included minutes: 900 | Additional minutes: $0.40 per minute ]")
    monthly_charge = 59.99
    included_minutes = 900
    extra_minute_rate = 0.40
elif pacs == 'C':
    print("\n[ PACKAGE C | Monthly charge: $69.99 | Included minutes: Unlimited | No additional-minute charge ]")
    monthly_charge = 69.99
    unlimited = True
else:
    print("\nInvalid package selected.")
if pacs in ['A', 'B', 'C']:
    if unlimited or nom <= included_minutes:
        total_bill = monthly_charge
    else:
        extra_minutes = nom - included_minutes
        total_bill = monthly_charge + (extra_minutes * extra_minute_rate)
    
    print(f"Your calculated total monthly bill is: ${total_bill:.2f}")
    