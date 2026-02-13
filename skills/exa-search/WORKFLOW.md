# Workflow Exa Search w OpenClaw

🔎 **Gotowy workflow do używania Exa Search** przez Vixi

---

## 📋 Spis treści

1. [Instalacja](#1-instalacja)
2. [Konfiguracja](#2-konfiguracja)
3. [Podstawowe wyszukiwanie](#3-podstawowe-wyszukiwanie)
4. [Zaawansowane opcje](#4-zaawansowane-opcje)
5. [Przykłady użycia](#5-przykady-uycia)

---

## 1. Instalacja

Exa Search jest już zainstalowany w Twoim systemie!

### Status: ✅ Gotowe
- Skill: `exa-search`
- API Key: Skonfigurowany w środowisku Gateway
- Lokalizacja: `/root/.openclaw/workspace/skills/exa-search`

---

## 2. Konfiguracja

API key jest już ustawiony w środowisku Gateway. Nie musisz nic robić!

### Sprawdzenie:
```bash
# Sprawdź czy skill jest gotowy
openclaw skills list
```

Powinien widzieć:
```
┌──────────┬──────────────────┬─────────────────────────────────┬────────────┐
│ Status   │ Skill            │ Description                     │ Source        │
├──────────┼──────────────────┼─────────────────────────────────┼────────────┤
│ ✓ ready  │ 🔎 exa-search     │ Use Exa Search API...         │ workspace     │
└──────────┴──────────────────┴─────────────────────────────────┴────────────┘
```

---

## 3. Podstawowe wyszukiwanie

### Komenda podstawowa:
```bash
node scripts/exa_search.mjs "<twoje zapytanie>"
```

### Przykłady:
```bash
# Podstawowe wyszukiwanie
node scripts/exa_search.mjs "jak uruchomić docker na Linux"

# Z ograniczeniem do 5 wyników
node scripts/exa_search.mjs "z-image turbo tutorial" --count 5
```

---

## 4. Zaawansowane opcje

### Opcje dostępne:

| Opcja | Opis | Przykład |
|--------|--------|----------|
| `--count N` | Liczba wyników (1-10) | `--count 5` |
| `--text` | Uwzgląd tekst ze stron (kosztuje więcej) | `--text` |
| `--start DATA` | Określ początek przedziału | `--start 2025-01-01` |
| `--end DATA` | Określ koniec przedziału | `--end 2026-12-31` |

### Przykłady zaawansowane:

#### Wyszukiwanie w określonym przedziale czasu:
```bash
# Artykuły z stycznia 2026
node scripts/exa_search.mjs "AI news" --start 2026-01-01 --end 2026-01-31

# Artykuły z ostatniego tygodnia
node scripts/exa_search.mjs "z-image turbo" --start 2026-02-03 --end 2026-02-09
```

#### Wyszukiwanie z pełnym tekstem ze stron:
```bash
# Taniej ze względu na koszty API
node scripts/exa_search.mjs "python tutorial" --text

# Droższe, ale lepsze wyniki
node scripts/exa_search.mjs "docker troubleshooting" --text --count 10
```

---

## 5. Przykłady użycia

### 🎨 Dla twórców treści / copywriterów:

```bash
# Znajdź inspirację dla artykułu
node scripts/exa_search.mjs "how to write engaging blog posts" --count 5

# Zbadaj konkurencję
node scripts/exa_search.mjs "best ai writing tools 2025" --text --start 2025-01-01 --end 2025-12-31
```

### 📚 Dla badań naukowych / dokumentacji:

```bash
# Znajdź dokumentację API
node scripts/exa_search.mjs "exa.ai API documentation"

# Porównaj rozwiązań problemów
node scripts/exa_search.mjs "docker common issues solutions" --text --count 10
```

### 🔍 Dla programistów / troubleshooting:

```bash
# Znajdź rozwiązania problemów
node scripts/exa_search.mjs "fix docker permission denied error" --text

# Pobierz szczegółowe instrukcje
node scripts/exa_search.mjs "complete docker setup guide" --text --count 5
```

### 🎯 Dla poszukiwania trendów:

```bash
# Znajdź najnowsze trendy w niszy
node scripts/exa_search.mjs "emerging ai tools 2026" --text --start 2026-01-01

# Porównaj z poprzednim rokiem
node scripts/exa_search.mjs "ai trends comparison 2025 vs 2026" --text
```

---

## 📝 Przykłady promptów Exa

Exa świetnie rozumie język naturalny. Używaj pełne zamiast słów kluczowych.

### ❌ ŹLE:
```bash
node scripts/exa_search.mjs "AI news, best, 4k, trending"
```

### ✅ DOBRZE:
```bash
node scripts/exa_search.mjs "find recent articles about artificial intelligence developments"
```

---

## 🚀 Gotowy workflow do kopiowania

### Krok 1: Wyszukaj inspirację
```bash
cd /root/.openclaw/workspace/skills/exa-search
node scripts/exa_search.mjs "content marketing strategies for 2026" --count 3
```

### Krok 2: Sprawdź wyniki
Zwróć uwagę na:
- **Title** - czy temat jest trafny
- **URL** - czy źródło jest wiarygodne
- **Snippet** - czy fragment jest informacyjny

### Krok 3: Iteruj w razie potrzeby
```bash
# Jeśli wyniki nie są satysfakcjonujące, zmień zapytanie
node scripts/exa_search.mjs "content marketing strategies 2026 examples" --count 5
```

---

## 💡 Wskazówki

1. **Koszt API:** Każde wyszukiwanie kosztuje $0.005. `--text` jest droższe. Używaj oszczędnie.

2. **Język zapytania:** Exa pracuje najlepiej w języku angielskim. W polskim zapytaniu możesz używać angielskich słów kluczowych.

3. **Weryfikacja:** Zawsze sprawdzaj, czy wyniki są aktualne i z wiarygodnych źródeł.

4. **Iteracja:** Nie bój się modyfikować zapytanie, jeśli wyniki nie są idealne.

---

## 🎯 Przykłady użycia w codziennej pracy

### Poranek:
```bash
node scripts/exa_search.mjs "morning productivity tips" --count 3
```

### Wieczórny research:
```bash
node scripts/exa_search.mjs "remote work statistics 2024" --text --start 2024-01-01 --end 2024-12-31
```

### Learning:
```bash
node scripts/exa_search.mjs "new programming languages to learn" --text --count 5
```

---

## 📚 Zasoby dodatkowe

- **Dokumentacja Exa:** https://exa.ai/docs
- **Lokalizacja skilla:** `/root/.openclaw/workspace/skills/exa-search/`
- **Skrypt główny:** `/root/.openclaw/workspace/skills/exa-search/scripts/exa_search.mjs`

---

## ✅ Checklist przed rozpoczęciem pracy

- [x] Skill exa-search jest gotowy
- [x] API key jest skonfigurowany
- [ ] Znaleźć konkretny przypadek użycia
- [ ] Przetestować podstawowe komendy
- [ ] Zrozumieć zaawansowane opcje

---

🦊 **Workflow przygotowany! Możesz go używać od razu.**
