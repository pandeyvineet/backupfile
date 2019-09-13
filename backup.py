import os
import sys
import subprocess
import time

def create_file(a_file_name):
  subprocess.call(['touch',a_file_name])
   return open(a_file_name, 'w+')
 
def write_exclusions(ex_list, a_file):
  for entry in ex_list:
     a_file.write(entry+'\n')
     start_dir= '/home/'
     dest_dir = '/media/'
     file_name = 'rsyncexclude.txt'

exclude_file = create_file(file_name)
directories = [
                'Downloads/',
                   'ImageFiles/',
                'VirtualBox VMs/',
                  '.config/google-chrome/',
                 '.cache/google-chrome/',
                  ]
  
   write_exclusions(directories, exclude_file)
   exclude_file.close()
  
  argstwo= ["rsync",
          "-avhXA",
          "--exclude-from="+file_name,
          "--delete",
          start_dir,
          dest_dir,
          ]
  
 subprocess.call(argstwo)
  
 subprocess.call(['rm', file_name])