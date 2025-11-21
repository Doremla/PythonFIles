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
bbbg    grades.append(grade);

i = 0;

while i < count:
     print(f"voto: {grades[i]}");
     i += 1;

i2 = 0;
summ = 0;

while i2 < count:
     summ += grades[i2];
     print(grades[i2]);
     i2 += 1;
     
print(f"la somma è: {summ}");

print("la media è: ", summ/count);
