import requests
#import subprocess
from perceval.backends.core.git import Git

#username = input("Enter the github username:")
request = requests.get('https://api.github.com/users/amfoss/repos')
json = request.json()


for i in range(0,len(json)):
      url=json[i]['svn_url']
      repo_dir = '/tmp/perceval.git'
      repo = Git(uri=url, gitpath=repo_dir)
#      print("Repository Number:",i+1) => For getting repo number if needed.
      print("Repository Name:",json[i]['name'])
#      print("Repository URL:",url,)   => For getting repo url if needed.Added this to make it #easier to go into the repo as and when needed.
      for commit in repo.fetch():
          print(commit['data'])  
      print("\n"*5) #I used this for seperating the repositories as it is clumsy.
  
