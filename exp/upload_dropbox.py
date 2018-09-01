#!/usr/bin/python
import os
import sys
import glob
import dropbox

token=""

dbx = dropbox.Dropbox(token)
dbx.users_get_current_account()

fns = glob.glob("${HOME}/cam_images/*.jpg")
print(fns)

for fn in fns:
    if os.path.isfile(fn):
        print(fn)
        f = open(fn,"rb")
        basename = os.path.basename(fn)
        dbx.files_upload(f.read(), "/camera01/%s" % basename)
        f.close()
        os.remove(fn)

