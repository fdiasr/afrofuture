import cmd, sys, json, time

class AfrofuturismShell(cmd.Cmd):
    intro = ''' 
    ___    ____           ____      __             _  
   /   |  / __/________  / __/_  __/ /___  _______(_)________ ___ 
  / /| | / /_/ ___/ __ \/ /_/ / / / __/ / / / ___/ / ___/ __ `__ 
 / ___ |/ __/ /  / /_/ / __/ /_/ / /_/ /_/ / /  / (__  ) / / / / /
/_/  |_/_/ /_/   \____/_/  \__,_/\__/\__,_/_/  /_/____/_/ /_/ /_/ 


Welcome to the Afrofuturism world. Type black to get knowledge.  =.=
'''
    prompt = '|== afrofuturism ==| '
    file = None

    def preloop(self):
        print('== Connecting with Wakanda ... ==\n\n')
        
        try:
            self.data = json.load(open('data/pt-br.json'))['data']
        except:
            print('Error')
        
        #print(type(self.data['data'][0]))
        #print(self.data)
       
        time.sleep(3)

    def load(self, command, field):
        for item in self.data:
            if item['topic'] == command:
                return item[field]
        raise Error

    def do_whatis(self, arg):
        'The definition of the Afrofuturism'
        print(self.load('whatis', 'text'))

    def do_term(self, arg):
        'Explain how the term was defined'
        print(self.load_cmd('term'))

    def do_originators(self, arg):
        'Give information about the 3 pillars originators from the culture'
        print(self.load_cmd('originators'))

    def do_pionners(self, arg):
        'Show up about the pionners of afrofuturism, event before the concept be defined'
        print(self.load_cmd('pionners'))

    def do_black_panter(self, arg):
        'Talk about the representation of the movie Black Panther showing up Afrofuturism to the pop culture'
        print(self.load_cmd('black-panther'))

    def do_books(self, arg):
        'Show some books related with the culture'
        print(self.load_cmd('books'))

    def do_movies(self, arg):
        'Present some movies related with the culture'
        print(self.load_cmd('movies'))

    def do_arts(self, arg):
        'Show some visual artists that use Afrofuturism as main subject'
        print(self.load_cmd('arts'))

    def do_fashion(self, arg):
        'Expose how the culture influences and be parte of fashion world'
        print(self.load_cmd('fashion'))

    def do_music(self, arg):
        'Musicians....'
        print(self.load_cmd('music'))

    def do_technology(self, arg):
        print(self.load_cmd('technology'))
    
    def do_blackwoman_on_IT(self, arg):
        print(self.load_cmd('blackwoman-on-it'))

    def do_brasil(self, arg):
        print(self.load_cmd('brasil'))

    def do_nuschool(self, arg):
        print(self.load_cmd('nuschool'))

    def do_the_book(self, arg):
        print(self.load_cmd('the-book'))
    
    def do_future(self, arg):
        print(self.load_cmd('future'))

    def do_presentation(self, arg):
        print('Loop presentation')

    def do_reset(self, arg):
        reset()

    def do_collect_and_results(self, arg):
        'It collects some info from user to search into the internet and show at the end of the presentation'

    def do_exit(self, arg):
        'Finish Wakanda connection'
        print('== Ending Wakanda connection ==')
        time.sleep(3)
        #self.close()
        #bye()
        return True

if __name__ == '__main__':
    AfrofuturismShell().cmdloop()
