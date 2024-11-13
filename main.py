from wad_data import WADData

class DoomeEngine:
    def __init__(self, wad_path='Doom.wad'):
        self.wad_path = wad_path
        self.on_init()

    def on_init(self):
        self.wad_data = WADData(self, map_name='E1M1')

if __name__ == '__main__':
    doom = DoomeEngine()