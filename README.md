# BigdataInl-mning1

Petrit Kukaj

Översikt

Programmet består av flera Python-skript som samverkar med en Redis-databas för att lagra, hämta, lägga till och ta bort citat. Redis är en in-memory databas som används för att snabbt hämta och manipulera data.

Skript och Funktioner
init-db.py
Syfte: Initierar Redis-databasen med en uppsättning fördefinierade citat.
Användning: Körs en gång för att förbereda databasen med startdata.
Funktioner:
Ansluter till Redis.
Lägger till ett urval av citat i databasen.
get_quote.py
Syfte: Hämtar och visar ett slumpmässigt citat från databasen.
Användning: Körs varje gång en användare vill se ett slumpmässigt citat.
Funktioner:
Ansluter till Redis.
Väljer och visar ett slumpmässigt citat.
add_quote.py
Syfte: Låter användaren lägga till ett nytt citat i databasen.
Användning: Körs när en användare vill lägga till ett eget citat.
Funktioner:
Ansluter till Redis.
Tar emot ett citat och dess författare från användaren.
Lägger till citatet i databasen.
delete_specific_quote.py
Syfte: Tar bort ett specifikt citat baserat på innehåll och författare.
Användning: Körs när ett specifikt citat behöver tas bort från databasen.
Funktioner:
Ansluter till Redis.
Söker igenom alla citat för att hitta och ta bort det specifika citatet.

Användarinstruktioner
Initiera Databasen: Starta med att köra init-db.py för att lägga till startdata i databasen.
Visa Ett Slumpmässigt Citat: Kör get_quote.py varje gång du vill se ett nytt slumpmässigt citat.
Lägg Till Ett Citat: Använd add_quote.py för att mata in och lagra ett nytt citat i databasen.
Ta Bort Ett Specifikt Citat: Om du behöver ta bort ett specifikt citat, använd delete_specific_quote.py och följ instruktionerna.
