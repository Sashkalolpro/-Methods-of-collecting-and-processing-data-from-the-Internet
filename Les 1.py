import requests

main_link='https://api.github.com/users/'
username = input("Введите имя пользователя на GitHub: ")
response=requests.get(f'{main_link}{username}/repos')
data = response.json()
for i in range(0,len(data)):
  print("Project Number:",i+1)
  print("Project Name:",data[i]['name'])
  print("Project URL:",data[i]['svn_url'],"\n")
  #