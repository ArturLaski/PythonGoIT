def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def number_of_groups(n, k):
    if n < k:
        return 0  # Invalid input, can't choose more winners than total subscribers
    else:
        combinations = factorial(n) / (factorial(n - k) * factorial(k))
        return int(combinations)

# test:
total_subscribers = 50
winners_count = 7

result = number_of_groups(total_subscribers, winners_count)
print(f"There are {result} different lists of winners.")