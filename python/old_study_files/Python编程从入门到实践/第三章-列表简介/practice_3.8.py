travel_destination = ['beijing','mohe','xiaweiyi','niuyue','dongjing']
print(travel_destination)
print(sorted(travel_destination))#sorted()临时修改顺序（按字母顺序）

print(travel_destination)
print(sorted(travel_destination,reverse=True))#,reverse=True 反转

print(travel_destination)
travel_destination.reverse()#永久反转
print(travel_destination)

travel_destination.reverse()
print(travel_destination)

travel_destination.sort()#.sort()永久按字母顺序排列
print(travel_destination)

travel_destination.sort(reverse=True)
print(travel_destination)