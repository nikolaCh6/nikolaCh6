DROP TABLE IF EXISTS pracownicy; 
CREATE TABLE pracownicy
(
    id_pracownika INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT(10),
    nazwisko TEXT(40),
    kod TEXT(10),
    miasto_z TEXT(30),
    ulica TEXT(30),
    data_u DATE,
    miasto_u TEXT (30)
);

DROP TABLE IF EXISTS kontakty;
CREATE TABLE kontakty
(
    id_pracownika INTEGER,
    typ_k INTEGER,
    kontakt TEXT(20),
    uwagi TEXT(50),
    FOREIGN KEY(id_pracownika) REFERENCES pracownicy(id_pracownika)
);

DROP TABLE IF EXISTS stanowiska;
CREATE TABLE stanowiska 
(
    id_stanowiska INTEGER PRIMARY KEY AUTOINCREMENT,
    stanowisko TEXT(25)
);

DROP TABLE IF EXISTS place;
CREATE TABLE place
(
    id_p INTEGER,
    id_s INTEGER,
    placa INTEGER,
    data_z DATE,
    FOREIGN KEY (id_p) REFERENCES kontakty(id_pracownika),
    FOREIGN KEY (id_s) REFERENCES stanowiska(id_stanowiska)
    
);
