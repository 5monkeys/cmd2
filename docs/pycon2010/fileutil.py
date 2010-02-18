import os
import os.path

for (dirpath, dirnames, filenames) in os.walk('/home/cat/proj/sqlpython/sqlpython'):
    for fname in filenames:
        fullfilename = os.path.join(dirpath, fname)
        stats = os.stat(fullfilename)
        binds['path'] = dirpath
        binds['name'] = fname
        binds['bytes'] = stats.st_size
        cmd("""INSERT INTO cat.files (path, name, bytes)
               VALUES (%(path)s, %(name)s, %(bytes)s)""")
    quit()