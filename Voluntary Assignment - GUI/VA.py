"""
Presented to: Mikael Johansson
Date: 12 October 2022
"""
import tkinter, random
import numpy as np
from numpy import linalg as LA

# Global constant
WINDOW_SIZE = 600
SIZE_MINIMUM, SIZE_MAXIMUM = 5, 30
VELOCITY_MINIMUM, VELOCITY_MAXIMUM = -10, 10

# Global Variables
number_of_balls = 10
ball_list = []
simulation_speed = 20


class Ball:
    def __init__(self, size, position, velocity, color, canvas: tkinter.Canvas) -> None:
        """Initialize a ball object and drawing on canvas"""
        self.mass = self.radius = size
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.color = color
        self.canvas = canvas
        self.drawing = self.create_drawing()
        self.active = False

    def create_drawing(self):
        """Create drawing of ball onto canvas"""
        x, y = self.position[0], self.position[1]
        r = self.radius
        return self.canvas.create_oval(
            [x - r, y - r, x + r, y + r], outline="black", fill=self.color
        )

    def wall_collision(self):
        """Checks for and handles wall collision"""
        coordinates = self.canvas.coords(self.drawing)
        if (coordinates[0] <= 0 and self.velocity[0] < 0) or (
            coordinates[2] >= WINDOW_SIZE and self.velocity[0] > 0
        ):
            self.velocity[0] *= -1
        if (coordinates[1] <= 0 and self.velocity[1] < 0) or (
            coordinates[3] >= WINDOW_SIZE and self.velocity[1] > 0
        ):
            self.velocity[1] *= -1

    def check_ball_collision(self, ball):
        """Check for ball collision"""
        if self is ball:  # Don't check with self
            return False

        r1, r2 = self.radius, ball.radius
        pos1, pos2 = self.position, ball.position
        delta_pos = pos2 - pos1
        distance = LA.norm(delta_pos)
        if distance <= r1 + r2:
            return True
        else:
            return False

    def merge_balls(self, ball):
        """Deletes the smaller drawing and enlarges the bigger one"""
        self.canvas.delete(ball.drawing)
        self.canvas.delete(self.drawing)

        if self.radius >= ball.radius:
            if self.radius < WINDOW_SIZE:
                self.radius += ball.radius
            self.drawing = self.create_drawing()
            ball.active = False
            ball_list.remove(ball)
            del ball
        else:
            if ball.radius < WINDOW_SIZE:
                ball.radius += self.radius
            ball.drawing = ball.create_drawing()
            self.active = False
            ball_list.remove(self)
            del self

    def ball_collision(self, ball_list):
        """Compute ball collision"""
        i = 0
        for ball in ball_list[i:]:
            if self.check_ball_collision(ball):
                self.merge_balls(ball)
            i += 1

    def move(self):
        """Moves the ball"""
        if self.active and self.canvas.coords(self.drawing) != []:
            self.wall_collision()
            self.ball_collision(ball_list)
            velocity_x, velocity_y = self.velocity[0], self.velocity[1]
            self.canvas.move(self.drawing, velocity_x, velocity_y)
            self.position += self.velocity  # Update the position of the ball
            self.canvas.after(simulation_speed, self.move)


def start():
    """
    Command for start button:
        Starts the simulation
    """
    if ball_list != []:
        for ball in ball_list:
            if not ball.active:
                ball.active = True
                ball.move()


def stop():
    """
    Command for stop button:
        Stops the simulation
    """
    if ball_list != []:
        for ball in ball_list:
            if ball.active:
                ball.active = False


def ball_list_radius_sum(ball_list):
    res = 0
    for ball in ball_list:
        res += ball.radius
    return res


def create_ball_list():
    global ball_list
    global number_of_balls
    if ball_list == [] or ball_list is None:
        _create_ball_list(number_of_balls, canvas)


def _create_ball_list(n, canvas):
    """
    Appends n balls with random position, velocity and color to the global variable 'ball_list'
    """
    colors = [
        "LightYellow",
        "Plum",
        "Tomato",
        "MediumSpringGreen",
        "LightCyan",
        "SandyBrown",
        "PaleGreen",
        "CornflowerBlue",
        "SpringGreen",
        "PowderBlue",
        "Violet",
        "Sienna",
    ]
    for _ in range(n):
        # size_range = 0
        # while ball_list_radius_sum(ball_list) + size_range > WINDOW_SIZE:
        size_range = random.randint(SIZE_MINIMUM, SIZE_MAXIMUM)
        b = Ball(
            size=size_range,
            position=[
                random.randint(size_range, WINDOW_SIZE - size_range) for _ in range(2)
            ],
            velocity=[
                random.randint(VELOCITY_MINIMUM, VELOCITY_MAXIMUM) for _ in range(2)
            ],
            color=random.sample(colors, k=1),
            canvas=canvas,
        )
        ball_list.append(b)


def retrieve_number_input():
    """Retrieves the new number of balls from a text box and clears the text box afterwards"""
    global number_of_balls
    user_input = number_text_box.get("1.0", "end-1c")
    if user_input.isdigit():
        number_of_balls = int(user_input)
        number_text_box.delete("1.0", tkinter.END)


def retrieve_sim_speed_input():
    """Retrieves the new simulation speed from a text box and clears the text box afterwards"""
    global simulation_speed
    user_input = simulation_speed_text_box.get("1.0", "end-1c")
    if user_input.isdigit():
        simulation_speed = int(user_input)
        simulation_speed_text_box.delete("1.0", tkinter.END)


def clear_ball_list():
    """
    Deletes the drawings of all balls from the canvas and
    clears the global variable 'ball_list' of its balls.
    """
    global ball_list
    # map(canvas.delete, ball_list)
    ball_list.clear()
    canvas.delete("all")


def update_number_text(label):
    """Updates the text for number of balls in the canvas"""
    global number_of_balls
    label["text"] = f"Number of balls: {number_of_balls}"


def update_speed_text(label):
    """Updates the text for simulation speed in the canvas"""
    global simulation_speed
    label["text"] = f"Simulation speed: {simulation_speed} ms"


def new_simulation():
    """Starts a new simulation"""
    retrieve_number_input()
    retrieve_sim_speed_input()
    update_number_text(number_of_balls_text)
    update_speed_text(simulation_speed_text)
    clear_ball_list()
    create_ball_list()


if __name__ == "__main__":
    window = tkinter.Tk()
    canvas = tkinter.Canvas(
        window, width=WINDOW_SIZE, height=WINDOW_SIZE, bg="Seashell"
    )
    canvas.pack(side=tkinter.LEFT)

    create_ball_list()

    # Create text labels:
    simulation_speed_text = tkinter.Label(
        window, text=f"Simulation speed: {simulation_speed} ms"
    )

    number_of_balls_text = tkinter.Label(
        window, text=f"Number of balls: {len(ball_list)}"
    )

    input_sim_speed_text = tkinter.Label(
        window, text="Input new simulation speed below:"
    )

    input_number_of_balls_text = tkinter.Label(
        window, text="Input new number of balls below:"
    )
    # Create buttons
    start_button = tkinter.Button(window, text="Start", command=start)
    stop_button = tkinter.Button(window, text="Pause", command=stop)
    new_simulation_button = tkinter.Button(
        window, text="Create new simulation", command=new_simulation
    )

    # Create text boxes for input
    number_text_box = tkinter.Text(window, height=2, width=10)
    simulation_speed_text_box = tkinter.Text(window, height=2, width=10)

    # Pack labels
    simulation_speed_text.pack(padx=20, pady=10)
    number_of_balls_text.pack(padx=20, pady=10)

    # Pack buttons & text boxes
    start_button.pack(padx=20, pady=10)
    stop_button.pack(padx=20, pady=10)
    input_number_of_balls_text.pack(padx=20, pady=10)
    number_text_box.pack(padx=20, pady=10)
    input_sim_speed_text.pack(padx=20, pady=10)
    simulation_speed_text_box.pack(padx=20, pady=10)
    new_simulation_button.pack(padx=20, pady=10)

    canvas.mainloop()
