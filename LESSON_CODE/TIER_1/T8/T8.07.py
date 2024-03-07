from collections import Counter

def get_count_visits_from_ip(ips):
    return dict(Counter(ips))

def get_frequent_visit_from_ip(ips):
    ip_count = Counter(ips)
    most_common_ip, count = ip_count.most_common(1)[0]
    return (most_common_ip, count)

# Example usage:
IP = [
    "85.157.172.253",
    "85.157.172.253",
    "66.50.38.43",
    "66.50.38.43",
    "66.50.38.43",
    "66.50.38.43",
    "192.168.1.1",
]

# Test get_count_visits_from_ip
count_visits = get_count_visits_from_ip(IP)
print("Count Visits from IP:", count_visits)

# Test get_frequent_visit_from_ip
frequent_visit = get_frequent_visit_from_ip(IP)
print("Most Frequent Visit from IP:", frequent_visit)