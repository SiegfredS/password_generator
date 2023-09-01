from password_generator import PasswordGenerator
from screen import Screen

pass_gen = PasswordGenerator(5, 5, 5)

my_screen = Screen(gen_password_func=pass_gen.generate_pass)

my_screen.run()
