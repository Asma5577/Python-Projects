#import art
#print(art.logo)

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bid_dictionary = {}

name = input("What is your name?: ")
bid = int(input("What's your bid?: $"))
decision = input("Do you have more people?: yes or no? ").lower()
bid_dictionary[name] = bid

while decision=="yes":
    print("\n" * 50)
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    decision = input("Do you have more people?: yes or no? ").lower()
    bid_dictionary[name] = bid

print(bid_dictionary)

temp_value =0
for ele in bid_dictionary:
    if temp_value >= bid_dictionary[ele]:
        temp_value = temp_value
    else:
        temp_value = bid_dictionary[ele]

for value in bid_dictionary:
    if temp_value == bid_dictionary[value]:
        print(value)

print(temp_value)