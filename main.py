import user_views

def end_persistent_update():
    import pathlib
    path = str(pathlib.Path(__file__).parent.absolute())
    g = open(path + '/run_key.txt', 'w')
    g.write('')
    g.close()
if __name__ == '__main__':
    user_views.run()
    end_persistent_update()
