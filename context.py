class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('Starting context...')
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        print('Finishing context...')
        self.open_file.close()

if __name__ == '__main__':
    file = File('test.txt', 'w')
    print('File created')

    with file as f:
        print('Context...')
        f.write('hello!')
