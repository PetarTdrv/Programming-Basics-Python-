city = input()
sales_volume = float(input())
commisions = 0
error_data = False

if city == 'Sofia':
   if 0 < sales_volume <= 500: 
       commisions = sales_volume * 0.05
   elif 500 < sales_volume <= 1000:
       commisions = sales_volume * 0.07
   elif  1000 < sales_volume <= 10000:
       commisions = sales_volume * 0.08
   elif sales_volume >10000:
       commisions = sales_volume * 0.12 
   else:
       error_data = True
elif city == 'Varna':
   if 0 < sales_volume <= 500: 
       commisions = sales_volume * 0.045
   elif 500 < sales_volume <= 1000:
       commisions = sales_volume * 0.075
   elif  1000 < sales_volume <= 10000:
       commisions = sales_volume * 0.10
   elif sales_volume >10000:
       commisions = sales_volume * 0.13
   else:
       error_data = True     
elif city == 'Plovdiv':
   if 0 < sales_volume <= 500: 
       commisions = sales_volume * 0.055
   elif 500 < sales_volume <= 1000:
       commisions = sales_volume * 0.08
   elif  1000 < sales_volume <= 10000:
       commisions = sales_volume * 0.12
   elif sales_volume >10000:
       commisions = sales_volume * 0.145
   else:
       error_data = True 
else:
    error_data = True

if not error_data:
    print(f"{commisions:.2f}")
else:
    print('error')