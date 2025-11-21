listaAnime = [];
while True:
    print("");
    print("");
    operation = int(input("Dimmi quale operazione vuoi fare(1. Create, 2. Delete, 3. Modifica, 4. Mostra lista, 5. personaggio con nome più lungo, 6. numero personaggi, 7. media lunghezza nomi personaggi, 8. percentuale personaggi con la 'o' nel nome, 0. uscire): "));
    
    
    if operation == 0:  #Ferma programma
        print("ciao ciao");
        exit();
        
    if operation == 1:  #operazione di CREATE
        print(listaAnime);
        nome = input("Dammi il nome del personaggio: ");
        listaAnime.append(nome);
        print(f"il personaggio {nome} è stato creato e aggiunto");
        
    if operation == 2:  #operazione di DELETE
        print(listaAnime);
        nome = input("Dimmi il nome del personaggio da eliminare: ");
        if nome in listaAnime:
            listaAnime.remove(nome);
            print(f"Il personaggio {nome} è stato eliminato");
            
        else:
            
            print(f"personaggio {nome} non è nella lista");
        

    if operation == 3:  #operazione di UPDATE
        print(listaAnime);
        nome = input("Dimmi il nome del personaggio da modificare: ");
        nomeAfter = input("Dammi il nome che sostituirà quello vecchio: ");
        del listaAnime[nome];
        listaAnime.append(nomeAfter);
        print(f"il personaggio {nome} è stato sostituito con {nomeAfter}.");
        
    if operation == 4:  #Mostra la LISTA
        print(listaAnime);



        

    if operation == 5:  #Calcolo nome più lungo
        
        if len(listaAnime)>0:
            
            count = 0;
            maybeMax = "";
            
            while count < len(listaAnime):
                
                if len(listaAnime[count]) > len(maybeMax):  
                    maybeMax = listaAnime[count];
                
                count += 1;
            print(f"Il personaggio con il nome più lungo è: {maybeMax}");
            
        else:
            print("Lista vuota, quindi non esiste");

    if operation == 6:  #operazione per stampare il numero dei personaggi
        print("Il numero dei personaggi è:", len(listaAnime));



        

    if operation == 7:  #operazione per calcolare la media della lunghezza dei nomi

        if len(listaAnime)>0:
            summ = 0;
            count = 0;
            maybeMax = "";

            while count < len(listaAnime):
                summ += len(listaAnime[count]);
                count += 1;

            avg = summ / count;
            print(f"La media della lunghezza dei nomi dei personaggi è: {avg}");

        else:
            print("Lista vuota, quindi 0");



    if operation == 8:  #percentuale nomi con dentro 'o'
        count = 0;
        countO = 0;
        while count < len(listaAnime):
            if "o" in listaAnime[count]:
                countO += 1;
            count += 1;
        
        percent = (countO * 100)/len(listaAnime);
                                      
        print(f"la percentuale dei nomi con la lettera 'o' è {percent}%");

        












        
        
        
        
