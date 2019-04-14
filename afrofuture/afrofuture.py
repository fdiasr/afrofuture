import cmd
import json
import os
import time

import simpleaudio as sa
from PIL import Image
import requests


class AfrofutureShell(cmd.Cmd):
    intro = '''\033[1;32;40m



 █████╗ ███████╗██████╗  ██████╗ ███████╗██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔════╝██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝
███████║█████╗  ██████╔╝██║   ██║█████╗  ██║   ██║   ██║   ██║   ██║██████╔╝█████╗  
██╔══██║██╔══╝  ██╔══██╗██║   ██║██╔══╝  ██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝  
██║  ██║██║     ██║  ██║╚██████╔╝██║     ╚██████╔╝   ██║   ╚██████╔╝██║  ██║███████╗
╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝      ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                                                                    

Welcome to the Afrofuture cyberspace. SPACE IT THE PLACE !  =.=


'''

    prompt = '\033[1;32;40m [AF] > '
    file = None
    data = []
    img_path = "{parent_path}/imgs".format(parent_path=os.path.dirname(__file__))
    sound_path = "{parent_path}/sounds".format(parent_path=os.path.dirname(__file__))
    data_path = "{parent_path}/data".format(parent_path=os.path.dirname(__file__))

    def preloop(self):
        """
        Initialize CLI
        """
        # self.clear()
        self.connect()
        self.play_sound("space_is_the_place.wav")

    def clear(self):
        """
        Clear screen
        """
        os.system('cls') # windows
        os.system('clear') # unix

    def connect(self):
        """
        Initialize a conection with Wakanda Network
        """
        print("\n \n \033[1;32;40m > > > Connecting with Wakanda", end="", flush=True)

        for i in range(5):
            print(".", end="", flush=True)
            time.sleep(.5)

        try:
            data_url = "https://raw.githubusercontent.com/fdiasdev/afrofuture/master/afrofuture/data/en.json"
            self.data = requests.get(data_url).json()['data']
            # file_path = "{path}/{file}".format(path=self.data_path, file='en.json')
            # self.data = json.load(open(file_path))['data']
        except Exception as e:
            print('\033[1;32;40m Error to stablish connection...')
            print('\033[1;32;40m {}'.format(e))
            exit(999)


        print("\n\n\n")

    def load(self, command, field):
        for item in self.data:
            if item['topic'] == command:
                return item[field]
        raise NameError

    def default(self, definition):
        """
        Get definition from data JSON file.
        """
        try:
            self.text(definition)
            self.play(definition)
            self.picture(definition)

        except NameError:
            print("\n > > > ERROR: Invalid command ! \n")

    def text(self, definition):
        """
        Output text definition
        """
        print("\n{definition}\n\n".format(definition="\n\n".join(self.load(definition, 'text'))))

    def play(self, definition):
        """
        Get audio call player method, when audio_file attribute is defined and audio exists
        """
        audio_file = self.load(definition, 'audio_file')
        if audio_file and os.path.isfile(audio_file):
            self.play_sound(audio_file)

    def play_sound(self, sound_file):
        """
        Use SimpleAudio player to play audio file
        """
        audio_path = "{sound_path}/{sound_file}".format(sound_path=self.sound_path, sound_file=sound_file)
        wave_obj = sa.WaveObject.from_wave_file(audio_path)
        wave_obj.play()

    def picture(self, definition):
        """
        Get image and display it, when picture attribute is defined and image exists
        """
        img_file = self.load(definition, 'picture')
        img_path = "{img_path}/{img_file}".format(img_path=self.img_path, img_file=img_file)
        if img_file and os.path.isfile(img_path):
            img = Image.open(img_path)
            # time.sleep(7)
            img.show()

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
