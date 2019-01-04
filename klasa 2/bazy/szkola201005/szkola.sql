DROP TABLE IF EXISTS uczniowie;
CREATE TABLE uczniowie
(
    IDucznia INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwisko TEXT,
    imie TEXT,
    ulica TEXT,
    dom DECIMAL,
    IDklasy INTEGER
);

DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny
(
    IDucznia INTEGER PRIMARY KEY,
    Ocena INTEGER,
    Data DATE,
    IDprzedmiotu INTEGER,
    FOREIGN KEY (IDucznia) REFERENCES uczniowie(IDucznia)
);

DROP TABLE IF EXISTS przedmioty;
CREATE TABLE przedmioty
(
    IDprzedmiotu INTEGER PRIMARY KEY AUTOINCREMENT,
    NazwaPrzedmiotu TEXT,
    Nazwisko_naucz TEXT,
    Imie_naucz TEXT,
    FOREIGN KEY (IDprzedmiotu) REFERENCES oceny(IDprzedmiotu)
);

