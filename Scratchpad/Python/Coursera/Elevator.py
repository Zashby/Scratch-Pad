class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.top = top
        self.bottom = bottom
        if current in range(self.bottom, self.top):
            self.current = current
        else:
            raise Exception

    def up(self):
        """Makes the elevator go up one floor."""
        if self.current + 1 <= self.top:
            self.current += 1
        else:
            return "At top floor."

    def down(self):
        """Makes the elevator go down one floor."""
        if self.current - 1 >= self.bottom:
            self.current -= 1
        else:
            return "At bottom floor."

    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if floor in range(self.bottom, self.top+1):
            self.current = floor
        else:
            return "That is not a floor choice"

    def __str__(self):
        return "Elevator is on floor number {}".format(self.current)


# Test case
elevator = Elevator(-1, 10, 0)

elevator.up()
print(elevator.current)  # should output 1

elevator.down()
print(elevator.current)  # should output 0

elevator.go_to(10)
print(elevator.current)  # should output 10

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current)  # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current)  # should be 1

elevator.go_to(5)
print(elevator)
