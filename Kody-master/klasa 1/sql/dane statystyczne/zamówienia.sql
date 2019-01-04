DROP TABLE IF EXISTS zamowienia1;
CREATE TABLE zamowienia1
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NumerZam INTEGER,
    AdresKlienta TEXT,
    DataZamowienia DATE,
    SzczegolyZamowienia TEXT
);

DROP TABLE IF EXISTS zamowienia2;
CREATE TABLE zamowienia2
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NumerZam INTEGER,
    IDKlienta INTEGER,
    DataZamowienia DATE TIME,
    WartZamNetto DECIMAL,
    Vat INTEGER
);

DROP TABLE IF EXISTS zamowienia3;
CREATE TABLE zamowienia3
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    IDKlienta INTEGER,
    NazwaKlienta TEXT,
    Adres TEXT,
    KodPOcztowy TEXT,
    Miasto TEXT,
    Wojewodztwo TEXT
);


