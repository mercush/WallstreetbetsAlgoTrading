import db_man
import pathlib
path = str(pathlib.Path(__file__).parent.absolute())
g = open(path + '/run_key.txt', 'w')
g.write('Running')
g.close()


f = open(path + '/run_key.txt', 'r')
while f.read() == 'Running':
    f.close()
    f = open(path + '/run_key.txt', 'r')