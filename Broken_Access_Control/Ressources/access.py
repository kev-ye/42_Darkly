import requests

def linesParsing(index):
  linesArray = index.text.split('\n');
  lines = filter(lambda line: '<a' in line and '../' not in line, linesArray)
  return lines

def getName(line):
  line[line.find('href="') + 6 : line.find('">') if line.find('README') != 0 else line.find('/"')]

def getContent(url):
  newReq = requests.get(url)
  return newReq.text

def recursive(index):
  for x in index:
    path = getName(x)
    print(path)
    if str(path) == 'README':
      result = getContent(url + path)
      readmeArray.append(result)
      print('result: ' + result)
      return
    else:
      newIndex = list(linesParsing(requests.get(url + str(path))))
      recursive(newIndex)

url = 'http://192.168.56.101/.hidden/'

req = requests.get(url)
index = list(linesParsing(req))
readmeArray = []

recursive(index)