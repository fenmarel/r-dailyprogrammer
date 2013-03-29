import time

def lose_money(coin):
    start = time.time()
    coins = [coin]
    zeros = 0

    for c in coins:
        if c == 0:
            zeros += 1
        else:
            coins += [c//2, c//3, c//4]
    print "finished in %.5f secs" % float(time.time() - start)
    return zeros


