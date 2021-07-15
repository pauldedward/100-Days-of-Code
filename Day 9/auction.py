
import os
clear = lambda: os.system('cls')
isPersonThere = True
AuctionArray = []

while isPersonThere:
    clear()
    bidder = input("Who is the bidder? ")
    bidAmount = int(input("Please enter the amount you want to bid: "))
    AuctionArray.append({'bidder':bidder,'bidAmount':bidAmount})
    
    if input("Isthere another person?(y/n) ").lower() == "y":
        isPersonThere = True
    else:
        isPersonThere = False

bestAmount = 0
for bidderObj in AuctionArray:
    if bidderObj["bidAmount"] > bestAmount:
        bestAmount = bidderObj["bidAmount"]
        bestBidder = bidderObj["bidder"]

clear()
if bestAmount:
    print("The highest bid was made by {} for {} rupees".format(bestBidder,bestAmount))
else:
    print("somethings wrong")
