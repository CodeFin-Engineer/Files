import sys
file = open('GuestAdvocates.txt','r')
ft_string = file.read()
grid = ft_string.split('\n')
grid.remove(grid[len(grid)-1])
scroll = {}
for user in grid:
    name = user[0:user.find(':')]
    phone = user[user.find(':')+1:user.find('?')]
    date = user[user.find('?')+1:len(user)]
    scroll[name] = (phone,date)
target = sys.argv[1].split(',')
for worker in target:
    phonenumber,date = scroll.get(worker)
    print(worker,'|','Phone Number: ',phonenumber,'|','Date joined: ',date,end='\n')
