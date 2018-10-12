import cmd, sys

class AfrofuturismShell(cmd.Cmd):
    intro = 'Welcome to the Afrofuturism world. Type black to get knowledge.\n'
    prompt = '(afro) '
    file = None

    def do_whatis(self, arg):
        print('A cultural aesthetic, philosophy of science, and philosophy of history that explores the developing intersection of African/African Diaspora culture with technology')

    def do_originators(self, arg):
        print('The originators from Afrofuturism')

    def do_term(self, arg):
        print('The term was defined in 1994...')

    def do_nuschool(self, arg):
        print('People that are raising the movement again...')

    def do_black_panter(self, arg):
        print('Let\'s talk about the movie and the story of black panter...')

    def do_books(self, arg):
        print('Books that define the term afro futurism')

    def do_movies(self, arg):
        print('Movies that define the term afro futurism')

    def do_arts(self, arg):
        print('Arts that define the term afro futurism')

    def do_music(self, arg):
        print('Music that define the term afro futurism')

    def do_technology(self, arg):
        print('Lets talk about IT')

    def do_black_on_IT(self, arg):
        print('Lets talk about black people on IT')

    def do_future(self, arg):
        print('Future and black people and technoloy')

    def do_reset(self, arg):
        reset()
 
    def do_bye(self, arg):
        'Stop recording, close the turtle window, and exit:  BYE'
        print('Thank you for using Turtle')
        self.close()
        bye()
        return True

if __name__ == '__main__':
    AfrofuturismShell().cmdloop()
