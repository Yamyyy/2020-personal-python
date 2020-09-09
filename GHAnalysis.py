import argparse


class Run:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.data = None
        self.argInit()

    def argInit(self):
        self.parser.add_argument('-u','--user')
        self.parser.add_argument('-e','--event')

    def
if __name__ == "__main__":
    a = Run()