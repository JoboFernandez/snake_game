class Snake:

    def __init__(self):
        self.body = [(0, 0), (1, 0), (2, 0), (3, 0)]
        self.direction = (1, 0)
        self.previous_tail = None
        self.alive = True

    @property
    def head(self):
        return self.body[-1]

    @property
    def neck(self):
        return self.body[-2]

    @property
    def backward_direction(self):
        x_delta = self.head[0] - self.neck[0]
        y_delta = self.head[1] - self.neck[1]
        return -x_delta, -y_delta

    def change_direction(self, new_direction):
        if new_direction != self.backward_direction:
            self.direction = new_direction

    def update(self, world):
        if not self.alive:
            return

        new_head = (self.head[0] + self.direction[0], self.head[1] + self.direction[1])
        if new_head in self.body:
            self.alive = False
        elif new_head[0] < 0 or new_head[0] >= world.width or new_head[1] < 0 or new_head[1] >= world.height:
            self.alive = False
        else:
            self.body.append(new_head)
            self.previous_tail = self.body.pop(0)

    def grow(self):
        self.body.insert(0, self.previous_tail)