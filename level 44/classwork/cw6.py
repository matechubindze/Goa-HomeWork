def better_than_average(class_points, your_points):
    other_avg = sum(class_points) / len(class_points)

    if your_points > other_avg: return True
    return False