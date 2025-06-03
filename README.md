# EWD Project

# 📁 Dataset: Cat Breeds – Dirty Version

Ten zbiór danych zawiera informacje o kotach różnych ras, ich cechach fizycznych, preferencjach oraz warunkach życia. Dane zawierają również lokalizację właściciela kota.

## 📊 Podstawowe informacje

- **Liczba rekordów:** 1103  
- **Liczba kolumn:** 17  
- **Format:** CSV (pola rozdzielone średnikiem `;`)

## 🧾 Opis kolumn

| Kolumna                    | Typ       | Opis                                                                 |
|---------------------------|-----------|----------------------------------------------------------------------|
| `Breed`                   | `string`  | Rasa kota                                                           |
| `Age_in_years`            | `float`   | Wiek kota w latach                                                  |
| `Age_in_months`           | `float`   | Wiek kota w miesiącach                                              |
| `Gender`                  | `string`  | Płeć kota (`male`, `female`)                                        |
| `Neutered_or_spayed`      | `boolean` | Czy kot jest wykastrowany/sterylizowany (`True`, `False`)          |
| `Body_length`             | `float`   | Długość ciała kota (w cm)                                           |
| `Weight`                  | `float`   | Waga kota (w kg)                                                    |
| `Fur_colour_dominant`     | `string`  | Dominujący kolor futra                                              |
| `Fur_pattern`             | `string`  | Wzór futra (np. `solid`, `tabby`)                                   |
| `Eye_colour`              | `string`  | Kolor oczu                                                          |
| `Allowed_outdoor`         | `string`  | Czy kot może wychodzić na zewnątrz (`TRUE`, `FALSE`, komentarze)    |
| `Preferred_food`          | `string`  | Preferowany typ jedzenia (`dry`, `wet`)                             |
| `Owner_play_time_minutes` | `float`   | Dzienny czas zabawy z właścicielem (w minutach)                     |
| `Sleep_time_hours`        | `float`   | Czas snu w ciągu doby (w godzinach)                                 |
| `Country`                 | `string`  | Kraj właściciela kota                                               |
| `Latitude`                | `float`   | Szerokość geograficzna                                              |
| `Longitude`               | `float`   | Długość geograficzna     
## Installing requirements

```bash
pip install -r requirements.txt
```

## Run aplication
```bash
streamlit run app.py
```
