#Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = "medium"
extra_shot =  True

if extra_shot:
    coffee = order_size + " Coffee with extra shot of espresso"
else:
    coffee = order_size + " coffee"
    
print("Order:", coffee)