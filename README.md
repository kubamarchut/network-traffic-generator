# 🌐 Network Traffic Generator 🚦

To repozytorium przechowuje materiały zgromadzone przy pracy na projektem "Generatora ruchu sieciowego", który powstał w ramach przedmiotu Podstawy Cyberbezpieczeństwa. Ten skrypt został stworzony do symulowania ruchu sieciowego, umożliwiając generację ruchu w różnych scenariuszach i konfiguracjach. Pozwala on na tworzenie ruchu mającego na celu dezorientacię atakującego (technika Honeypot), który już dostał się do danej sieci komputerowej np. poprzez atak Wi-Fi spoofing.

## Przewodnik użytkownika 🚀

Skrypt Generatora Ruchu Sieciowego pozwala na symulację ruchu sieciowego poprzez użycie różnych parametrów za pomocą wiersza poleceń. Wykorzystuje moduł `argparse` w języku Python do analizy argumentów podanych w wierszu poleceń i uruchamia odpowiednią symulację ruchu.

### Instalacja ⚙️

1. Pobierz skrypt np. klonując to repozytorium:

```bash
git clone https://github.com/kubamarchut/network-traffic-generator.git
```

2. Przejdź do katalogu zawierającego skrypt:

```bash
cd network-traffic-generator
```

3. Upewnij się, że masz zainstalowane wszystkie wymagane biblioteki Pythona. Użyj pliku `requirements.txt` do instalacji potrzebnych zależności:

```bash
pip install -r requirements.txt
```

Ten krok zapewni, że wszystkie wymagane biblioteki są zainstalowane na Twoim systemie. Po zakończeniu instalacji możesz rozpocząć korzystanie z Generatora Ruchu Sieciowego.

### Rozpoczęcie pracy 🎉

Aby uruchomić Generator Ruchu Sieciowego, otwórz terminal lub wiersz poleceń i upewnij się że znajdujesz się w katalogu zawierającym skrypt, w razie potrzeby przejdź do niego.

```bash
cd network-traffic-generator
```

### Argumenty wiersza poleceń 🛠️

Skrypt obsługuje następujące argumenty wiersza poleceń:

- `--ip`: **(Wymagane)** Określa adres IP docelowy, do którego zostanie wysłany wygenerowany ruch.

- `--threads`: Ustawia liczbę wątków dla jednoczesnej generacji ruchu. Domyślna wartość to `1`.

- `--timespan`: Ustawia czas trwania (w sekundach) dla każdego wątku generującego ruch. Domyślna wartość to `1` sekunda.

- `--test`: Włącza test osiągalności docelowego miejsca przed rozpoczęciem generacji ruchu.

### Przykłady 📝

Oto kilka przykładów użycia Generatora Ruchu Sieciowego:

1. **Podstawowe użycie:**
   ```bash
   python network_gen.py --ip 192.168.0.105
   ```
   To spowoduje wygenerowanie ruchu na adres IP `192.168.0.105` przy użyciu domyślnych ustawień (1 wątek przez 1 sekundę).

2. **Dostosowanie liczby wątków i czasu trwania:**
   ```bash
   python network_gen.py --ip 192.168.0.105 --threads 5 --timespan 3
   ```
   To spowoduje wygenerowanie ruchu z `5` wątkami przez `3` sekundy każdy na adres IP `192.168.0.105`.

3. **Testowanie osiągalności celu:**
   ```bash
   python network_gen.py --ip 192.168.0.105 --test
   ```
   To spowoduje wykonanie testu osiągalności na adresie IP `192.168.0.105` przed rozpoczęciem generowania ruchu.

### Uwaga ⚠️

- Upewnij się, że masz odpowiednie uprawnienia do wysyłania ruchu sieciowego pod wskazany adres IP docelowy.
- Dostosuj argumenty według swojego środowiska testowego i preferowanych ustawień generacji ruchu.

## 🖐️ Autorzy

- Jakub Marchut [@kubamarchut](https://www.github.com/kubamarchut)
- Jakub Kadłubowski [@kubakadlubowski](https://www.github.com/kadlub)

## 📃 Dokumentacja

[Dokumentacja - overleaf]()