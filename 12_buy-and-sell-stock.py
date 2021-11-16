'''
Ch 7. Array
12. Best time to Buy and Sell stock (leetcode 121)
한 번의 거래로 낼 수 있는 최대 이익을 산출하라. (매수.매도 한 번씩만!)
'''
import time
stock = [7,1,5,3,6,4]  # 시계열 주가 배열
# stock = [7,5,3,6,4,1]

# 1. Brute-force: O(n^2)
start = time.time()
def bruteForce(stock):
    gain = 0
    for i,buy in enumerate(stock[:-1]):
        for j,sell in enumerate(stock[i+1:]):
            gain = max(gain, sell - buy)
    
    return gain

print('\n====== Brute-force =======')
print(bruteForce(stock))
print(f'Runtime: {time.time() - start} sec')


# 2-1. 저점과 현재 값과의 차이 계산: O(n)
# My approach: i번째 값을 저점이라고 가정한 뒤 이후 시점에 대해 최대 이익을 갱신
start = time.time()

def myProfit(stock):
    gain = 0
    for i,n in enumerate(stock[:-1]):
        gain = max(max(stock[i+1:]) - n, gain)
    
    return gain

print('\n====== My approach =======')
print(myProfit(stock))
print(f'Runtime: {time.time() - start} sec')


# 2-2. 저점과 현재 값과의 차이 계산, Textbook: O(n) -> 제일 빠르다.
import sys
start = time.time()

def maxProfit(prices):
    profit = 0
    min_price = sys.maxsize

    # 최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    
    return profit

print('\n====== Textbook =======')
print(maxProfit(stock))
print(f'Runtime: {time.time() - start} sec')