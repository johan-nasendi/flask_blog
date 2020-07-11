import os
import secrets
from blog import app
from PIL import Image



def simpan_gambar(self):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(self.filename)
    nama_gambar = random_hex + f_ext
    path_gambar = os.path.join(app.root_path, 'blog/static/img', nama_gambar)

    output_size = (600, 600)
    i = Image.open(self)
    i.thumbnail(output_size)
    i.save(path_gambar)

    return nama_gambar
