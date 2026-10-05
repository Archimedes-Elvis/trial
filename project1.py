import numpy as np

scores = np.array([55, 70, 80, 45, 90, 65, 78])

print(f"Average score: {np.mean(scores):.1f}")
print(f"Highest score: {np.max(scores)}")
print(f"Lowest score: {np.min(scores)}")
print(f"Students who passed greater than 50: {np.sum(scores > 50)}")
print(f"Square root of each: {np.sqrt(scores)}")
print(f"Standard deviation: {np.std(scores):.3f}")
print(f"Variance: {np.var(scores):.2f}")

print(scores + 5)