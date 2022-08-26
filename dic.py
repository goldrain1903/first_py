mos_qty={
	"2022년6월" : [7, 3, 6, 9],
                 "2022년7월" : [12, 5, 9, 15],
                 "2022년8월" : [23, 15, 12, 5]
}

for month in mos_qty:
	total = sum(mos_qty[month])
	print(month + "판매량 : " + str(total))

print('*' * 10)
