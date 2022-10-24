class Cur_Words:
    def __init__(self):
        self.swearing = ['бля', 'блять', 'хуй', 'нахуй']

    def __iter__(self):
        return self

    def __next__(self):
        for i_elem in self.swearing:
            return i_elem
            




