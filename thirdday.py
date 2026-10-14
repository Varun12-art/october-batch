Rama_height=1.3
Raja_height=1.7
if Rama_height>Raja_height:
    print("Rama is taller")
else:
    print("Raja is taller")
    
    
total=float(input("Enter total purchase amount:"))
if total>1000:
    discount=total*0.10
    final_discount=total-discount
    print("Discount applied:",discount)
    print("Final amount to pay:",final_discount)
else:
    print("No discount applied")
    print("Total amount:",total)