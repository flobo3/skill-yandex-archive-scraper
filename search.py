import sys
import json
import urllib.parse
import time
from scrapling.fetchers import StealthyFetcher

# Fix encoding for Windows CMD
sys.stdout.reconfigure(encoding='utf-8')

def search_yandex_archive(query: str, index: str = "archive", max_pages: int = 1):
    """
    Search Yandex.Archive and extract results.
    index can be 'archive' (Архивы), 'mass_media' (Периодика), or 'directories' (Справочники).
    """
    # Map friendly names to Yandex index names
    index_map = {
        "archive": "archive",
        "архивы": "archive",
        "periodicals": "mass_media",
        "периодика": "mass_media",
        "mass_media": "mass_media",
        "directories": "directories",
        "справочники": "directories"
    }
    
    actual_index = index_map.get(index.lower(), "archive")
    print(f"🔍 Ищем '{query}' в разделе '{actual_index}' (макс. страниц: {max_pages})...")
    
    encoded_query = urllib.parse.quote(query)
    base_url = f"https://yandex.ru/archive/search?text={encoded_query}&rankMode=by_relevance&index={actual_index}"
    
    all_results = []
    
    for page_num in range(max_pages):
        # Yandex pagination uses 'pageNum' parameter (1-indexed)
        url = base_url
        if page_num > 0:
            url += f"&pageNum={page_num + 1}"
            
        print(f"📄 Загружаю страницу {page_num + 1}: {url}")
        
        try:
            # Use StealthyFetcher to bypass Yandex bot protection
            page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
            
            # Find all links that look like archive documents
            links = page.css('a')
            page_results = []
            
            for link in links:
                href = link.attrib.get('href', '')
                text = link.css('::text').get()
                
                # Check if it's a document link
                if ('/archive/catalog/' in href or '/archive/periodicals/' in href or '/archive/directories/' in href) and text:
                    # Try to extract the snippet from the URL if it's there
                    snippet = ""
                    parsed_url = urllib.parse.urlparse(href)
                    query_params = urllib.parse.parse_qs(parsed_url.query)
                    if 'snippet' in query_params:
                        snippet = query_params['snippet'][0]
                    
                    # Clean up text and snippet
                    text = text.strip()
                    snippet = snippet.replace('\x07', '').replace('[', '').replace(']', '').strip()
                    
                    # Avoid duplicates (sometimes Yandex has multiple links to the same doc)
                    if not any(r['url'] == href for r in page_results):
                        page_results.append({
                            "title": text,
                            "url": f"https://yandex.ru{href}" if href.startswith('/') else href,
                            "snippet": snippet
                        })
            
            if not page_results:
                print("⚠️ На этой странице не найдено результатов. Возможно, мы достигли конца или сработала защита.")
                break
                
            all_results.extend(page_results)
            print(f"✅ Найдено {len(page_results)} документов на странице {page_num + 1}.")
            
            # Be polite to the server
            if page_num < max_pages - 1:
                time.sleep(2)
                
        except Exception as e:
            print(f"❌ Ошибка при загрузке страницы {page_num + 1}: {e}")
            break
            
    return all_results

if __name__ == "__main__":
    # Simple CLI for testing
    query = sys.argv[1] if len(sys.argv) > 1 else "Александр Пушкин"
    index = sys.argv[2] if len(sys.argv) > 2 else "archive"
    pages = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    
    results = search_yandex_archive(query, index, pages)
    
    print("\n" + "="*50)
    print(f"ИТОГО НАЙДЕНО: {len(results)} документов")
    print("="*50)
    
    for i, res in enumerate(results[:20]):
        print(f"\n[{i+1}] {res['title']}")
        if res['snippet']:
            print(f"    Фрагмент: {res['snippet']}")
        print(f"    Ссылка: {res['url']}")
        
    if len(results) > 20:
        print(f"\n... и еще {len(results) - 20} результатов.")