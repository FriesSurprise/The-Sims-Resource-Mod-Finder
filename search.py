import requests
from bs4 import BeautifulSoup
import time
import handle_file
start_time = time.time()
search_type = "clothing"
look_for = handle_file.search_for(search_type)
origin_page = "https://www.thesimsresource.com/downloads/browse/category/sims4-" + search_type + "/page/"
for x in range(handle_file.range_base(search_type), 3442):
    find = look_for + "<button"
    find_in = str(BeautifulSoup(requests.get(origin_page + str(x)).content, 'html5lib')
                  .find_all('div', class_='browse-info'))
    if find in find_in:
        print("Page number: " + str(x))
        handle_file.overwrite(x, search_type)
        break
print("Run time: " + str(round(((time.time() - start_time) / 60), 2)) + " minutes")
