seg = 355
h = seg // 3600
seg = seg -h*3600
m = seg //60
seg = seg -m*60
s = seg
print(f"seg = {seg}")