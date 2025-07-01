def compute_grade(score1=0, score2=0, score3=0):
    w1 = score1*0.3
    w2 = score2*0.3
    w3 = score3*0.4
    avg = w1+w2+w3

    if avg >= 90:
        grade = 'A'
    elif 85 <= avg < 90:
        grade = 'A-'
    elif 80 <= avg < 85:
        grade = 'B+'
    elif 70 <= avg < 80:
        grade = 'B'
    elif 60 <= avg < 70:
        grade = 'C'
    elif 50 <= avg < 60:
        grade = 'D'
    else:   grade = 'F'

    return avg, grade

with open('Grade.txt', mode='r') as file, open('gradebook.txt', mode='w') as outfile:
    for count,line in enumerate(file, start=1):
        line = line.strip('\n')
        data = line.split(',')

        fname = data[0]
        lname = data[1]
        sid = data[2]
        test1 = int(data[3])
        test2 = int(data[4])
        final = int(data[5])

        average, grade = compute_grade(test1, test2, final)

        print(f"{count}. ID: {sid} \tLast Name: {lname} \tGrade: {grade}")
        outfile.write(f'{count}. ID: {sid} \tLast Name: {lname} \tGrade: {grade}\n')
