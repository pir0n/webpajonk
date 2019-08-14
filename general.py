import os


def creat_new_dir(directory):
    if not os.path.exists(directory):
        print('Creating new project' + directory)
        os.makedirs(directory)

#creat_new_dir('psycho')

# create queue and crwaled files (if not created_)

def creat_new_fil(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

#creat new file:

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

#creat_new_fil('psycho','https://psychonautwiki.org/wiki/Main_Page/')

# Add data ontoo an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# delete the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass #do nothing

# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

#iterate through a set, each item wil be a new line in the file

def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file,link)
