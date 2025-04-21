import arcade

# Constants for screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Simple Arcade Game"

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2

    def on_draw(self):
        """Render the screen."""
        arcade.start_render()
        arcade.draw_rectangle_filled(self.x, self.y, 50, 50, arcade.color.RED)

    def on_key_press(self, key, modifiers):
        """Handle user input for movement."""
        if key == arcade.key.UP:
            self.y += 10
        elif key == arcade.key.DOWN:
            self.y -= 10
        elif key == arcade.key.LEFT:
            self.x -= 10
        elif key == arcade.key.RIGHT:
            self.x += 10

if __name__ == "__main__":
    game = MyGame()
    arcade.run()
