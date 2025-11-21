artista = "";
fav_artisti = [];

while artista != "q":
    artista = input("Dammi il nome dell'artista(premi 'q' per chiudere): ");
    print(f"artista inserito è: {artista}");
    #fav_artisti = ["Jimi Hendrix", "Dua Lipa", "Eminem", "Arctic Monkeys"];
    fav_artisti.append(artista);
    print(len(fav_artisti));

i = 0;

while i < len(fav_artisti):
     print(fav_artisti[i]);
     i += 1;
