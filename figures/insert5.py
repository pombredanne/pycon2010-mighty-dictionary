import insert1, sys

d = {'ftp': 21, 'ssh': 22, 'smtp': 25, 'time': 37, 'www': 80}
surface = insert1.draw_dictionary(d, 512, 330, 10, 30)
surface.write_to_png(sys.argv[1])