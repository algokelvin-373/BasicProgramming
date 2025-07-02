def find_higher_bidder(bidder_dictionary):
    winner = ""
    higher_bidder = 0
    for name_bidder in bidder_dictionary:
        if bidder_dictionary[name_bidder] > 0:
            higher_bidder = bidder_dictionary[name_bidder]
            winner = name_bidder
    print(f"Winner: {winner} - ${higher_bidder}")

bids = {}
continue_bidding = True
while continue_bidding:
    name = input('Your Name: ')
    price = int(input('Your Bids: $'))
    bids[name] = price
    should_be_continue = input("Are there any order bidders? Type 'yes' or 'no' \n").lower()
    if should_be_continue == 'no':
        continue_bidding = False
find_higher_bidder(bids)