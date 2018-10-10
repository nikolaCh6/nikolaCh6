DROP TABLE IF EXISTS tbOceny;
CREATE TABLE tbOceny
(
    IDucznia INTEGER,
    Ocena INTEGER,
    Data DATE,
    IDprzedmiotu INTEGER,
    FOREIGN KEY (id_przedmiotu) REFERENCES tbUczniowie(id_przedmiotu),
);  

DROP TABLE IF EXISTS tbUczniowie;
CREATE TABLE tbUczniowie
(
    IDucznia INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwisko TEXT (50) NOT NULL,
    imie TEXT (50) NOT NULL,
    ulica TEXT (50) NOT NULL,
    dom INTEGER,
    IDklasy TEXT
);  
  
DROP TABLE IF EXISTS tbPrzedmioty;
CREATE TABLE tbPrzedmioty
(
    IDprzedmiotu INTEGER PRIMARY KEY,
    NazwaPrzedmiotu TEXT (50) NOT NULL,
    Nazwisko_naucz TEXT (50) NOT NULL,
    Imie_naucz TEXT (50) NOT NULL,
    FOREIGN KEY (id_przedmiotu) REFERENCES tbUczniowie(id_przedmiotu),
);    
  





