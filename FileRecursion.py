
import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    returnList = list()

    fileList = os.listdir(path)

    for file in fileList:
        fullpath = path + '/' + file
        if (os.path.isfile(fullpath)):
            if (fullpath.endswith(suffix)):
                returnList.append(fullpath)
        else:
            returnList.extend(find_files(suffix, fullpath))

    return returnList

print(find_files('.c', '.'))