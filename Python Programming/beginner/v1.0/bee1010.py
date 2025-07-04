string_one = input().split()
value_amount_one = int(string_one[1])
value_price_one = float(string_one[2])
price_final_one = value_amount_one * value_price_one

string_two = input().split()
value_amount_two = int(string_two[1])
value_price_two = float(string_two[2])
price_final_two = value_amount_two * value_price_two
price_final = price_final_one + price_final_two
print("The value final is: %.2f" % price_final)
