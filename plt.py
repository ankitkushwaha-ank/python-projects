import matplotlib.pyplot as plt

# Data from the image
datasets = {
    'I': {
        'x': [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
        'y': [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
    },
    'II': {
        'x': [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
        'y': [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
    },
    'III': {
        'x': [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
        'y': [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
    },
    'IV': {
        'x': [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 19],
        'y': [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 5.56, 7.91, 6.89, 12.50]
    }
}

# Create a 2x2 subplot for each dataset
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot each dataset
for i, (key, data) in enumerate(datasets.items()):
    ax = axs[i // 2, i % 2]  # Access subplot
    ax.scatter(data['x'], data['y'])
    ax.set_title(f'Dataset {key}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

# Adjust layout and show plot
plt.tight_layout()
plt.show()