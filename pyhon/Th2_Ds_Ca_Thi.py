with open('CATHI.in', 'r') as f:
    n = int(f.readline())
    exams = []
    for i in range(n):
        date = f.readline().strip()
        time = f.readline().strip()
        room = f.readline().strip()
        exams.append({
            'id': f'C{i+1:03d}',
            'date': date,
            'time': time,
            'room': room
        })


exams.sort(key=lambda x: (x['date'], x['time'], x['id']))

for exam in exams:
    print(f"{exam['id']} {exam['date']} {exam['time']} {exam['room']}")