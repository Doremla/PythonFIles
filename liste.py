Ngrades = int(input("Dimmi il  numero dei voti: "));
while Ngrades <= 0:
    Ngrades = int(input("Valore negativo non valido, riprova: "));
print(f"Il numero dei voti inserito è: {Ngrades}"); 
grades = [];
count = 0;

while count < Ngrades:
    count += 1;
    grade = int(input("Dammi il voto: "));
    print(f"Il voto inserito è: {grade}");
    grades.append(grade);

i = 0;

while i < count:
     print(f"voto: {grades[i]}");
     i += 1;
