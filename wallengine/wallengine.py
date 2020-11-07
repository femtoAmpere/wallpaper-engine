import os
import send2trash

from wallengine import files

import logging

logger = logging.getLogger("wallengine")


class WallEngine:
    def __init__(self, wall_cache_dir, wall_cache_size, wall_cache_tags):
        if not os.path.isdir(wall_cache_dir):
            os.mkdir(wall_cache_dir)
        self.wall_cache_dir = wall_cache_dir
        self.wall_cache_size = wall_cache_size
        self.wall_cache_tags = wall_cache_tags

    def rotate_walls(self):
        old_files = files.get_files_in_dir(self.wall_cache_dir)
        logger.info("Old files: " + str(old_files))
        new_files = files.download_wallpapers(tags=self.wall_cache_tags,
                                              download_dir=self.wall_cache_dir,
                                              amount=self.wall_cache_size)
        logger.info("New files: " + str(new_files))
        for file in old_files:
            send2trash.send2trash(file)
