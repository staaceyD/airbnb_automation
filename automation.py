from functions_utility import set_up, choose_city, choose_check_in_and_out_dates, choose_guests_ammount, click_search, choose_type_of_place, set_max_price

set_up('https://www.airbnb.com/')
choose_city("Lviv")
choose_check_in_and_out_dates("2020-10-03", "2020-11-07")
choose_guests_ammount(2)
click_search()
choose_type_of_place('Entire')
set_max_price("40")


# to loop trough all results need to change offset +20 , scrape data, sort by cheapest, leave 20 the cheapest places in the search
# https://www.airbnb.com/s/Lviv/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2020-10-03&checkout=2020-10-07&adults=2&source=structured_search_input_header&search_type=filter_change&gps_lat=50.4501&gps_lng=30.5234&query=Lviv%2C%20Lviv%20Oblast%2C%20Ukraine&place_id=ChIJV5oQCXzdOkcR4ngjARfFI0I&room_types%5B%5D=Entire%20home%2Fapt&price_max=40
# https://www.airbnb.com/s/Lviv/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2020-10-03&checkout=2020-10-07&adults=2&source=structured_search_input_header&search_type=pagination&gps_lat=50.4501&gps_lng=30.5234&query=Lviv%2C%20Lviv%20Oblast%2C%20Ukraine&place_id=ChIJV5oQCXzdOkcR4ngjARfFI0I&room_types%5B%5D=Entire%20home%2Fapt&price_max=40&federated_search_session_id=cd6b6b94-3f7a-4f38-b8ae-bd24319346d9&section_offset=2&items_offset=20
# https://www.airbnb.com/s/Lviv/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2020-10-03&checkout=2020-10-07&adults=2&source=structured_search_input_header&search_type=pagination&gps_lat=50.4501&gps_lng=30.5234&query=Lviv%2C%20Lviv%20Oblast%2C%20Ukraine&place_id=ChIJV5oQCXzdOkcR4ngjARfFI0I&room_types%5B%5D=Entire%20home%2Fapt&price_max=40&federated_search_session_id=cd6b6b94-3f7a-4f38-b8ae-bd24319346d9&section_offset=2&items_offset=40
