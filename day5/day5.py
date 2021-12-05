class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def is_diagonal(self):
        return self.x == self.y

    def __str__(self):
        return f'{self.x}, {self.y}'

class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def is_diagonal(self):
        return not(self.a.x == self.b.x or self.a.y == self.b.y)

    def sort_points(self, dimension='x'):
        if dimension == 'x':
            return min(self.a.x, self.b.x), max(self.a.x, self.b.x)
        if dimension == 'y':
            return min(self.a.y, self.b.y), max(self.a.y, self.b.y)

    def get_diagonal_range(self):
        direction_x = -1 if self.a.x > self.b.x else 1
        direction_y = -1 if self.a.y > self.b.y else 1
        points_in_range = []
        i, j = self.a.x, self.a.y
        while True:
            if i == self.b.x and j == self.b.y:
                points_in_range.append(Point(i, j))
                break
            points_in_range.append(Point(i, j))
            i += direction_x
            j += direction_y
        return points_in_range

    def get_line_range(self):
        dimension = 'y' if self.a.x == self.b.x else 'x'
        start, end = self.sort_points(dimension)
        if dimension == 'y':
            return [Point(self.a.x, i) for i in range(start, end + 1)]
        return [Point(i, self.a.y) for i in range(start, end + 1)]

    def get_points_in_range(self):
        if not self.is_diagonal():
            return self.get_line_range()
        return self.get_diagonal_range()

    def __str__(self):
        return f'{self.a}, {self.b}'

clouds = []
points = []

with open('day5.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    point1, point2 = line.split(' -> ')
    point1 = Point(*point1.strip().split(','))
    point2 = Point(*point2.strip().split(','))
    cloud = Line(point1, point2)
    clouds.append(cloud)
    points.append(point1)
    points.append(point2)

def select_simple_clouds(clouds):
    simple_clouds = []
    for cloud in clouds:
        if not cloud.is_diagonal():
            simple_clouds.append(cloud)
    return simple_clouds

simple_clouds = select_simple_clouds(clouds)
max_x = max([point.x for point in points])
max_y = max([point.y for point in points])

area_1 = [[0 for i in range(max_x+1)] for j in range(max_y+1)]

for cloud in simple_clouds:
    points_in_range = cloud.get_points_in_range()
    for point in points_in_range:
        area_1[point.x][point.y] += 1

overlaps_1 = 0

for x in range(max_x + 1):
    for y in range(max_y + 1):
        if area_1[x][y] > 1:
            overlaps_1 += 1

print(f'Task 1: {overlaps_1}')

area_2 = [[0 for i in range(max_x+1)] for j in range(max_y+1)]

for cloud in clouds:
    points_in_range = cloud.get_points_in_range()
    for point in points_in_range:
        area_2[point.x][point.y] += 1

overlaps_2 = 0

for x in range(max_x + 1):
    for y in range(max_y + 1):
        if area_2[x][y] > 1:
            overlaps_2 += 1

print(f'Task 2: {overlaps_2}')

