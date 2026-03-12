"""Stock Price Analyzer - Minimal Implementation"""

def next_greater_price(prices):
    """Find next greater price for each element using monotonic stack"""
    result = [-1] * len(prices)
    stack = []
    for i in range(len(prices)):
        while stack and prices[i] > prices[stack[-1]]:
            idx = stack.pop()
            result[idx] = prices[i]
        stack.append(i)
    return result

def max_profit(prices):
    """Calculate maximum profit from one buy-sell transaction"""
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

def moving_average(prices, window):
    """Calculate moving averages using sliding window"""
    if len(prices) < window:
        return []
    result = []
    window_sum = sum(prices[:window])
    result.append(window_sum / window)
    for i in range(window, len(prices)):
        window_sum += prices[i] - prices[i - window]
        result.append(window_sum / window)
    return result

class StreamProcessor:
    """Process stock prices in real-time stream"""
    def __init__(self, window_size=3):
        self.prices = []
        self.window_size = window_size
    
    def add_price(self, price):
        """Add new price and return current analysis"""
        self.prices.append(price)
        analysis = {
            'current_price': price,
            'total_prices': len(self.prices),
            'max_profit': max_profit(self.prices),
            'moving_avg': moving_average(self.prices, self.window_size)[-1] if len(self.prices) >= self.window_size else None
        }
        return analysis

def main():
    print("=" * 60)
    print("STOCK PRICE ANALYZER")
    print("=" * 60)
    
    # Sample stock prices
    prices = [100, 80, 120, 130, 70, 60, 100, 125]
    print(f"\nStock Prices: {prices}")
    
    # 1. Next Greater Price
    print("\n1. NEXT GREATER PRICE")
    print("-" * 60)
    ngp = next_greater_price(prices)
    for i, (price, next_price) in enumerate(zip(prices, ngp)):
        print(f"Price {price} → Next Greater: {next_price if next_price != -1 else 'None'}")
    
    # 2. Maximum Profit
    print("\n2. MAXIMUM PROFIT ANALYSIS")
    print("-" * 60)
    profit = max_profit(prices)
    print(f"Maximum Profit: ${profit}")
    
    # 3. Moving Averages
    print("\n3. MOVING AVERAGES (Window=3)")
    print("-" * 60)
    ma = moving_average(prices, 3)
    for i, avg in enumerate(ma):
        print(f"Period {i+1}: ${avg:.2f}")
    
    # 4. Stream Processing
    print("\n4. REAL-TIME STREAM PROCESSING")
    print("-" * 60)
    stream = StreamProcessor(window_size=3)
    stream_prices = [100, 105, 110, 108, 115]
    print(f"Streaming prices: {stream_prices}\n")
    
    for price in stream_prices:
        result = stream.add_price(price)
        print(f"Price: ${result['current_price']} | Max Profit: ${result['max_profit']} | MA: {f'${result["moving_avg"]:.2f}' if result['moving_avg'] else 'N/A'}")
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main()
