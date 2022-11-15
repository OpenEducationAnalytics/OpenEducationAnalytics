import re

#with open('example_metadata.csv', 'r') as f: 
with open('test2.csv', 'r', encoding='utf-8') as f: 
  metadata_str = f.read()

#import urllib.request
#url = "https://raw.githubusercontent.com/microsoft/OpenEduAnalytics/gene/v0.7dev/modules/module_catalog/Student_and_School_Data_Systems/example_metadata.csv"
#response = urllib.request.urlopen(url)
#metadata_str = response.read().decode('utf-8')    

metadata = {}
current_entity = ''
captured_header = False
attribute_header = None
for line in metadata_str.splitlines():
  line = line.strip()
  # skip empty lines, lines that start with # (because these are comments), and lines with only commas (which is what happens if someone uses excel and leaves a row blank) 
  if len(line) == 0 or line.startswith('#') or re.match(r'^,+$', line): continue
  ar = line.split(',')
  
  # check for the start of a new entity
  if ar[0] != '':
    print('got entity')
    current_entity = ar[0]
    metadata[current_entity] = []
    attribute_header = None
  # an attribute row must have an attribute name in the second column
  elif len(ar[1]) > 0:
    ar = ar[1:] # remove the first element because it will be blank
    if not attribute_header:
      attribute_header = ar
    else:
      metadata[current_entity].append(ar)
  else:
    print('invalid row')

print(metadata)


#  l = [i for i in ar if (i is not None and len(i) > 0)]
#  print(l)
  #print(len(ar.tolist()))
  #print(ar[0])