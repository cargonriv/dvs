class coordinate_point:
    def __init__(self, timestep, x_point, y_point, polarity):
        self.timestep = timestep
        self.x_point = x_point
        self.y_point = y_point
        self.polarity = polarity
    def __repr__(self):
        return repr((self.time, self.x_point, self.y_point, self.polarity))

def poker_polarity_separator(data):
    data_points = data
    points_0_polarity = []
    points_1_polarity = []
    for coordinate_points in data_points:
        polarity = coordinate_points[3]
        if polarity == 1:
            points_0_polarity.append(coordinate_points)
        else:
            points_1_polarity.append(coordinate_points)
    return points_0_polarity, points_1_polarity