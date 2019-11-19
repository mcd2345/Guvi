starting_distance=int(input("The starting distance is:"))
ending_distance=int(input("The destination distance is:"))
peakhour=int(input("Press 2 for peaktime o for Normal time:"))
total_distance=(ending_distance-starting_distance)

if(total_distance>5):
	basic_fare=((total_distance-5)*8)+100
else:
	print("The ride fare is 100rs")
if(peakhour==2):
	total_fare=basic_fare+(basic_fare*0.25)
else:
	print("The Basic fare is=",basic_fare)