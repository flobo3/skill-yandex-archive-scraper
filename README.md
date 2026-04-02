# yandex-archive-scraper

A skill for searching and extracting data from **Yandex.Archive** (Яндекс.Архив) — a free online service by Yandex that provides digitized historical documents from Russian archives, libraries, and museums.

## What is Yandex.Archive?

Yandex.Archive (https://yandex.ru/archive) is a searchable database of millions of digitized pages from Russian historical sources. It includes:

- **Metric books** (метрические книги) — birth, marriage, and death records from church registries (18th–20th centuries).
- **Revision tales** (ревизские сказки) — population census records from the Imperial era.
- **Confessional statements** (исповедные ведомости) — parishioner lists maintained by the Orthodox Church.
- **Old newspapers** (периодика) — digitized issues of pre-revolutionary and Soviet-era newspapers.
- **Address calendars & directories** (справочники) — official reference books listing residents, officials, and organizations by city and governorate.

This is an invaluable resource for genealogy, historical research, and local history studies.

## Features

- Converts natural language queries into optimized Yandex.Archive search URLs.
- Uses `Scrapling` (StealthyFetcher) to bypass Yandex bot protection and Cloudflare Turnstile.
- Extracts search results (document titles, text snippets, and direct links).
- Supports pagination to collect multiple pages of results.
- Can search across all three Yandex.Archive indexes:
  - `archive` (Архивы) — Metric books, revision tales, confessional statements.
  - `mass_media` (Периодика) — Old newspapers (e.g., "Senate Gazette", "Provincial Gazette").
  - `directories` (Справочники) — Address calendars, lists of residents, memorable books.

## Installation

1. Install the required dependencies:
```bash
pip install scrapling playwright curl_cffi patchright msgspec browserforge
playwright install chromium
```

2. Add the skill to your agent.

## Usage

Run the script directly from the command line:
```bash
python search.py "Александр Пушкин" archive 2
```

Or use it as an agent tool:
```json
{
  "name": "yandex_archive_search",
  "arguments": {
    "query": "Александр Пушкин Москва",
    "index": "archive",
    "max_pages": 2
  }
}
```

---

# yandex-archive-scraper (Русский)

Скилл для поиска и извлечения данных из сервиса **Яндекс.Архив** с использованием фреймворка `Scrapling` для обхода защиты от ботов и Cloudflare Turnstile.

## Что такое Яндекс.Архив

Яндекс.Архив (https://yandex.ru/archive) — бесплатный сервис Яндекса с миллионами оцифрованных страниц исторических документов из российских архивов, библиотек и музеев. Включает:

- **Метрические книги** — записи о рождении, браке и смерти из церковных реестров (XVIII–XX века).
- **Ревизские сказки** — переписи населения имперского периода.
- **Исповедные ведомости** — списки прихожан православных церквей.
- **Периодика** — оцифрованные номера дореволюционных и советских газет.
- **Справочники** — адрес-календари, памятные книжки, списки жителей и должностных лиц по городам и губерниям.

Незаменимый ресурс для генеалогических исследований, исторических изысканий и краеведения.

## Возможности

- Преобразует запросы на естественном языке в оптимизированные поисковые URL для сервиса Яндекс.Архив.
- Использует `Scrapling` (StealthyFetcher) для обхода защиты Яндекса.
- Извлекает результаты поиска (названия документов, текстовые фрагменты/сниппеты и прямые ссылки).
- Поддерживает пагинацию для сбора нескольких страниц результатов.
- Поиск по всем трём разделам сервиса:
  - `archive` (Архивы) — Метрические книги, ревизские сказки, исповедные ведомости.
  - `mass_media` (Периодика) — Старые газеты (например, «Сенатские ведомости», «Губернские ведомости»).
  - `directories` (Справочники) — Адрес-календари, списки жителей, памятные книжки.

## Установка

1. Установите необходимые зависимости:
```bash
pip install scrapling playwright curl_cffi patchright msgspec browserforge
playwright install chromium
```

2. Добавьте скилл в вашего агента.

## Использование

Запуск скрипта напрямую из командной строки:
```bash
python search.py "Александр Пушкин" archive 2
```

Или использование в качестве инструмента агента:
```json
{
  "name": "yandex_archive_search",
  "arguments": {
    "query": "Александр Пушкин Москва",
    "index": "archive",
    "max_pages": 2
  }
}
```
