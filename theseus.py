from pathlib import Path
import pandas
import os

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