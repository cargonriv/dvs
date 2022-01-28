class coordinate_point:
    def __init__(self, time, x_point, y_point, polarity):
        self.time = time
        self.x_point = x_point
        self.y_point = y_point
        self.polarity = polarity
    def __repr__(self):
        return repr((self.time, self.x_point, self.y_point, self.polarity))