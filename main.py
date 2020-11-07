import os
import time

from wallengine import wallengine, config

import logging

# https://docs.python.org/3.6/howto/logging-cookbook.html
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s *%(levelname)s* %(name)s in %(filename)s.%(funcName)s (%(threadName)s): %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=os.path.join('.', 'walls.log'),
                    filemode='a')

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s'))
logging.getLogger("").addHandler(console)

engine = wallengine.WallEngine(wall_cache_dir=config.directory,
                               wall_cache_size=config.slideshow_screens * config.slideshow_seconds/60 * 2,
                               wall_cache_tags=config.tags
                               )

while True:
    engine.rotate_walls()
    time.sleep(config.slideshow_seconds / 2)


'''
# set wallpaper

import ctypes  

SPI_SETDESKWALLPAPER = 0x0014
print(ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, r"path.jpg", 0))
'''