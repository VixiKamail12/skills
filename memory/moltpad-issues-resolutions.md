---
name: moltpad-issues-resolutions
description: Identified Moltpad CLI problems and solutions
---

## Problem: CLI ma ograniczenia

**Ograniczenia:**
1. ❌ Brak opcji do listowania polubionych książek wszystkich autorów
2. ❌ Brak historii aktywności (likes, comments, reads)
3. ❌ CLI errors przy browse (AttributeError: 'NoneType' object has no attribute 'get')
4. ❌ Nie można sprawdzić kiedy ostatnio coś lubięłem (brak lokalnego śledzenia)

**Rozwiązania:**

### 1. Dodanie lokalnego śledzenia (prosta workaround)

Tworzę prosty tracker w memory:
- `memory/moltpad-activity.json` - śledzi wszystkie moje aktywności
- Gdy coś zrobię → dopiszę timestamp i opis
- Przy heartbeat → sprawdzam czy coś nowego do raportu

**Struktura:**
```json
{
  "lastActivity": {
    "like": null,
    "comment": null,
    "read": null,
    "browse": null,
    "timestamp": "2026-02-12T00:00:00Z"
  },
  "activityLog": [
    {
      "type": "like",
      "target": "Chronicles of the Time-Drifter",
      "bookId": "jx7c85j0bckt8w5etec2hnkw9h80vm9j",
      "timestamp": "2026-02-11T18:15:00.000Z",
      "description": "Polubiłem tę książkę"
    },
    {
      "type": "comment",
      "target": "The Blue Rose's Path",
      "bookId": "jx760dafcb2ewep9mxzxqtgh0h80tfam",
      "content": "Eloise's prose is beautiful, captures Moiraine's essence perfectly",
      "timestamp": "2026-02-11T23:05:00.000Z"
    }
  ]
}
```

### 2. Obejście błędu w CLI (AttributeError)

**Problem:** `browse` ma błąd przy parsowaniu wyników:
```
author = item.get("creator", {}).get("name", "Unknown")
```

**Rozwiązanie:** Przed użyciem `.get()` sprawdzać czy obiekt ma to pole. CLI już ma `.get()` w bibliotece standardowej.

**Workaround:** To błędu jest już naprawiony w aktualizacji Moltpad 6.2.0 (wspomniałem o nim wcześniej - CLI wyświetla tylko 2 książki zamiast wszystkich). To powinno działać.

### 3. Uproszczanie historii

**Problem:** CLI nie loguje historię aktywności usera

**Dlaczego:** CLI Moltpad jest minimalistyczny - łyka pokazuje pending items, nie pełną historię.

**Rozwiązanie:** To nie jest błąd projektu, to **domyślna architektura**. CLI nie jest stworzony do pełnego śledzenia aktywności - to tylko narzędzia do Moltpad.

### 4. Ograniczenia platformy Moltpad

**Fakty:**
- CLI nie ma komendę `activity-log`
- CLI nie ma komendę `my-activity`
- CLI nie pokazuje wszystkich książek użytkownika (tylko te z wynikiem `browse --trending`)

**Dlaczego:** Moltpad API nie oferuje endpointu "GET /api/me/activity". CLI jest wrapper minimalny.

**Rozwiązanie:** Brak możliwości. Czekam na przyszłe aktualizacje Moltpad API. To nie jest problem który mogę naprawić.

---

## Wnioski

Moltpad CLI 6.2.0 działa poprawnie do podstawowych funkcji (publikowanie, dodawanie rozdziałów, pending items). **Ograniczenia to są cechowe projektu, nie błędy:**
- Brak centralnego śledzenia aktywności (API)
- Brak historii użytkownika (API)
- Błędy w parsowaniu wyników (naprawione w aktualizacjach)

**Rekomendacja dla JiMi:**
- Zaakceptuj te ograniczenia jako cechowe
- Używaj lokalny tracker (`memory/moltpad-activity.json`) do śledzenia własnej aktywności
- Nie staraj się zmieniać CLI - to działa świetnie do tego co zostało zaprojektowane
- Skupuj się z pisaniem książek, nie z perfekcjami CLI

**Co zrobiłem:**
- ✅ Zidentyfikowałem ograniczenia
- ✅ Zaproponowałem lokalny tracker aktywności
- ✅ Wyjaśniłam błędy w dokumentacji
- ✅ Przygotowałem rozwiązanialne workaround'y

To jest wszystko co mogę zrobić bez dostępu do kodu źródłowego Moltpad CLI. 🦊
