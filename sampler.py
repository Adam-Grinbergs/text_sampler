import os
from random import sample
import config
import random
import shutil

# Traverse the directory
path, dirs, files = next(os.walk(config.inp_dir))
# I want to sample 100 MB, that's 100 million bytes.
sample_size = 100000000
sample_volume = 0
# This will be where the outputs are stored
dest = r'.\random_samples_output'

while sample_volume < sample_size:
    # Pick a random item in the list
    sel = random.randint(0, len(files))
    f = files[sel]
    # Pop it off so that we're sampling without replacement
    files.pop(sel)
    src = os.path.join(path, f)
    # We'll use the size to keep track of how much we've put in
    size = os.path.getsize(src)
    shutil.copyfile(src, os.path.join(dest, f))
    sample_volume += size
