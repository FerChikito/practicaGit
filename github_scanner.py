import os
import subprocess
import time
import webbrowser
#import requests
import winreg

git_dir = r"C:\Users\cfern\OneDrive\Desktop\practica git"

repos = [name for name in os.listdir(git_dir)
         if os.path.isdir(os.path.join(git_dir, name)) and
         os.path.exists(os.path.join(git_dir, name, ".git"))]

select_repo = None
if repos:
    print("found the following GitHub repository")
    for idx, repo in enumerate(repos, 1):
        print(f"{idx}. {repo}")