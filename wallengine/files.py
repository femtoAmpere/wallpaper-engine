import urllib.parse
import requests

import random
import os

import logging

logger = logging.getLogger("files")


def download_wallpapers(tags, download_dir, amount):
    submissions = get_submissions(tags, amount)
    return download_submissions(submissions, download_dir)


def get_files_in_dir(fdir):
    files = []
    for file in os.listdir(os.path.join(fdir)):
        files.append(os.path.join(".", fdir, file))
    return files


def _list_to_string(list_to_str, separator):
    """
    Convert a list to a string with separator.
    :param list_to_str: List to be converted to string.
    :param separator: String seperator between list items
    :return: String from converted list
    """
    str_return = ''
    for item in list_to_str:
        str_return = str_return + urllib.parse.quote(str(item)) + separator
    return str_return.rsplit(separator, 1)[0]


def _download_file(url, filename):
    """
    Download a file via stream.
    :param url: url to download
    :param filename: filename to download to
    :return: filename to download to
    """
    logger.info("Downloading " + str(url) + " -> " + str(filename))
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                if chunk:
                    f.write(chunk)
    return filename


def get_submissions(tags, amount=16, pool_size=320):
    """
    Get submissions from e621.net: https://e621.net/help/api
    :param tags: list of tags for e621
    :param amount: size of samples
    :param pool_size: submission pool size to take the samples from
    :return: list of randomly picked submissions
    """
    api_url = 'https://e621.net/posts.json?tags=' + _list_to_string(tags, '+') + '&limit=' + str(pool_size)
    logger.debug('Getting e621 api call json for ' + api_url)
    r = requests.get(api_url, headers={'User-Agent': 'wallpaper engine by femtoAmpere'})

    i = 0
    submissions = []
    while len(submissions) < amount:
        submission = random.choice(r.json()["posts"])
        if submission["file"]["url"] and submission["id"] not in submissions:
            logger.debug("Adding submission " + str(submission["id"]))
            submissions.append(submission)
        if i > amount*1.5:
            logger.warning("Could not get full submissions. i = " + str(i) + ", submissions: " + str(submissions))
            break
        else:
            i += 1

    return submissions


def download_submissions(submissions, target_dir):
    """
    Download a submission from e621.net
    :param submissions: list of submissions (https://e621.net/help/api)
    :param target_dir: directory to download submissions to
    :return: list of filenames of downloaded submissions
    """
    downloaded = []
    for submission in submissions:
        fname = os.path.join(".", target_dir, str(submission['id']) + '.' + submission['file']['ext'])
        try:
            downloaded.append(_download_file(submission['file']['url'], fname))
        except Exception as e:
            logger.error('Could not download post ' + str(submission['id']) + '. Exception: ' + str(e))
    return downloaded



