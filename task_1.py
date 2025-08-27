time = '1h 45m,360s,25m,30m 120s,2h 60s'
itog=0
time_new = time.split(',')
for piece in time_new:
    time_point= piece.split(' ')

    for segment in time_point:
        if 'h' in segment:
            segment = segment.replace('h', '')
            itog += int(segment) * 60

        elif 'm' in segment:
            segment = segment.replace('m', '')
            itog += int(segment)

        elif 's' in segment:
            segment = segment.replace('s', '')
            itog += int(segment) // 60
print(itog)


