seconds = int(input('введите кол сeкунд '))
d = int(seconds/86400)
h = int((seconds%86400)/3600)
m = int(((seconds%86400)%3600)/60)
s=seconds%60
print(d,':',h,':',m,':',s)
