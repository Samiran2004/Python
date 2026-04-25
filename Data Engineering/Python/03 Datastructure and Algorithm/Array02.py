import array as arr

# Create an array

scores = arr.array('i', [85, 90, 78, 92, 88])
print("Original scores: ", scores)

# Add new scores
scores.append(95)
scores.extend([80, 87])
print("After adding: ", scores)

# Insert a score
scores.insert(2, 91)
print("After insert: ", scores)

# Remove a score
scores.remove(78)
print("After remove: ", scores)

# Get array statistics
print(f"Length: {len(scores)}")
print(f"Highest: {max(scores)}")
print(f"Lowest: {min(scores)}")
print(f"Average: {sum(scores) / len(scores)}")

# Sort (Convert to list first)
sorted_scores = sorted(scores)
print("Sorted: ", sorted_scores)

# Loop and process
print("\nScores above 85")
for score in scores:
    if score > 85:
        print(score)