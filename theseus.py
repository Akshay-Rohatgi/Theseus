from pathlib import Path
import pandas
import os

print('''

============================================================================
ooooooooooooo oooo                                                         
8'   888   `8 `888                                                          
     888       888 .oo.    .ooooo.   .oooo.o  .ooooo.  oooo  oooo   .oooo.o 
     888       888P"Y88b  d88' `88b d88(  "8 d88' `88b `888  `888  d88(  "8 
     888       888   888  888ooo888 `"Y88b.  888ooo888  888   888  `"Y88b.  
     888       888   888  888    .o o.  )88b 888    .o  888   888  o.  )88b 
    o888o     o888o o888o `Y8bod8P' 8""888P' `Y8bod8P'  `V88V"V8P' 8""888P'
============================================================================

''')

# get user input for settings
handle = open("output/final.conf", "w")

event_name = input("Enter in your event name: ")
event_password = input("Enter in the password you would like to use for encrypting scoring data: ")

admin_name = input("Enter in your preferred admin username: ")
admin_password = input("Enter in your preferred admin password: ")

# Write settings to file
settings = '''
event = "{}"
password = "{}"

[[admin]]
username = "{}"
password = "{}"

'''.format(event_name, event_password, admin_name, admin_password)
handle.write(settings)

image_num = int(input("Enter in the amount of images you would like: "))

i = 0
while i < image_num:
    image_name = input("Image Name: ")
    image_color = input("Image Color (for no preference just put None): ")
    if image_color == 'None':
        image_conf = '''
[[image]]
name = "{}"

'''.format(image_name)
        handle.write(image_conf)
    else:
        image_conf = '''
[[image]]
name = "{}"
color = "{}"

'''.format(image_name, image_color)
        handle.write(image_conf)
    i += 1


# Get data
colnames = ['email', 'Alias', 'IDs']
data = pandas.read_csv('csvs/ids.csv', names=colnames)

# Convert to array
emails = data.email.tolist()
aliases = data.Alias.tolist()
team_ids = data.IDs.tolist() 

for (email, alias, team_id) in zip(emails, aliases, team_ids):
    team_conf = '''
[[team]]
id = "{}"
alias = "{}"
email = "{}"
'''.format(team_id, alias, email)
    handle.write(team_conf)

handle.close()