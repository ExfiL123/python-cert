input_dict = {'lesson': 2, 'task': 4, 'course': 'python'}
sorted_keys = sorted(input_dict.keys())

pairs = []
for key in sorted_keys:
    pairs.append(f"{key}={input_dict[key]}")

result = '&'.join(pairs)

print(result)
