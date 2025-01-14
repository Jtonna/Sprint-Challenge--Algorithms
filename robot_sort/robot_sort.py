class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """Plan to Sort the robot's list.
        Since the initial steps are the robot being able to move right and left we should use a while loop we also have to
        Take in to account the original index position of 0 and get the object in its hand to start sorting things from the l array to the r array

        While <robot can move right>
            <do these>
            if <thing> is bigger:
                do thing
            
        
        Once the robot cant move right anymore he should be theoretically at the end of the array.
        We need a way to see if 
        """
        # Fill this out
        self.swap_item()

        # function that moves left, swaps, moves right, swaps because im lazy and want to save reading space
        def move_n_swap():
                self.move_left()
                self.swap_item()
                self.move_right()
                self.swap_item()


        while self.can_move_right():
            self.move_right()

            #  If the robot compares the item and its 1 do things
            if self.compare_item() == 1:
                # We need to turn the light on, swap item, move left, swap the item, move right & swap the item (calls move_n_swap function)
                self.set_light_on()
                self.swap_item()
                move_n_swap()
            else:
                #  If the item isnt = 1 we need to move left, swap, move right & swap (calls move_n_swap function)
                move_n_swap()
        
        #  If we cant move right we have to do this
        else:
            self.swap_item()

            #   If the light is on we need to move left & then turn off the light
            if self.light_is_on():
                #  Move left ONLY if we can move left, things break if we dont check first
                while self.can_move_left():
                    self.move_left()
                # Now we can turn off the light and continue
                self.set_light_off()
                #  Recursion
                self.sort()

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
