import cmd, sys, json, time, os
import simpleaudio as sa


class AfrofuturismShell(cmd.Cmd):
    intro = '''\033[1;32;40m
    ___    ____           ____      __             _  
   /   |  / __/________  / __/_  __/ /___  _______(_)________ ___ 
  / /| | / /_/ ___/ __ \/ /_/ / / / __/ / / / ___/ / ___/ __ `__ 
 / ___ |/ __/ /  / /_/ / __/ /_/ / /_/ /_/ / /  / (__  ) / / / / /
/_/  |_/_/ /_/   \____/_/  \__,_/\__/\__,_/_/  /_/____/_/ /_/ /_/ 


Welcome to the Afrofuture cyberspace. SPACE IT THE PLACE !  =.=



'''

    prompt = '\033[1;32;40m [AF] > '
    file = None
    data = []
    sound_path = "{parent_path}/sounds".format(parent_path=os.path.dirname(__file__))
    data_path = "{parent_path}/data".format(parent_path=os.path.dirname(__file__))

    def preloop(self):
        # self.clear()
        self.connect()
        self.play_sound("sample.wav")

    def clear(self):
        os.system('cls') # windows
        os.system('clear') # unix

    def connect(self):
        print("\n \n \033[1;32;40m > > > Connecting with Wakanda", end="", flush=True)

        for i in range(5):
            print(".", end="", flush=True)
            time.sleep(.5)

        try:
            file_path = "{path}/{file}".format(path=self.data_path, file='en.json')
            self.data = json.load(open(file_path))['data']
        except:
            print('\033[1;32;40m Error to stablish connection...')

        print("\n\n\n")

    def play_sound(self, file):
        audio_path = "{sound_path}/{file}".format(sound_path=self.sound_path, file=file)
        wave_obj = sa.WaveObject.from_wave_file(audio_path)
        wave_obj.play()

    def load(self, command, field):
        for item in self.data:
            if item['topic'] == command:
                return item[field]
        raise Error

    def default(self, definition):
        """
        Get definition from data JSON file.
        """

        # try:"

        # if it has sound play it
        audio_file = self.load(definition, 'audio_file')

        if audio_file:
            self.play_sound(audio_file)

        print("\n{definition}\n".format(definition="\n\n".join(self.load(definition, 'text'))))

        # except:
        #    print("\n > > > ERROR: Invalid command ! Press help to see the command list \n")


    #def do_collect_and_results(self, arg):
    #    'It collects some info from user to search into the internet and show at the end of the presentation

    def emptyline(self):
        """
        Make empty line return nothing
        """
        return

    def do_exit(self, arg):
        """
        Finish Wakanda connection
        """
        print("\n\n > > > Ending Wakanda connection \n\n")
        time.sleep(2)
        return True
