from bs4 import BeautifulSoup
import sys
from loggin_abstract.log_status import logger
class B4SApartmentExtractor:
    """
    Abstracts BeatifulSoup's way to find html objects,
    with the only objective to find the objects for the GetApartmentsInfo class.
    """

    def __init__(self,rent_info: str) -> None:
        self.rent_info=rent_info

    def find_apartment_rent_price(self) -> int:
        """
        Return Apartment's rent price, through the HTML's element.
        """
        logger("Getting Apartment prices information.",status="DEBUG")
        price_element = self.rent_info.find('div', class_='simple-card__listing-prices simple-card__prices')
        price = price_element.select_one('strong').next.strip()
        return price
    
    def find_apartment_address(self) -> str:
        """
        Return Apartment's address, through the HTML's element.
        """
        logger("Getting Apartment address information.",status="DEBUG")
        address_element = self.rent_info.find('h2',class_="simple-card__address color-dark text-regular")
        address=address_element.next.strip()
        return address

    def find_apartment_codominium(self) -> int:
        """
        Return Apartment's condominium price, through the HTML's element.
        """
        logger("Getting Apartment condominium information.",status="DEBUG")
        condominium_element = self.rent_info.find('li', class_='card-price__item condominium text-regular')
        condominium=condominium_element.find('span',class_="card-price__value").get_text(strip=True) if condominium_element else 0
        return condominium

    def find_apartment_floor_size(self) -> str:
        """
        Return Apartment's Floor Size, through the HTML's element.
        """
        logger("Getting Apartment floor_size information.",status="DEBUG")
        floor_size_element = self.rent_info.find('span',itemprop="floorSize")
        floor_size=floor_size_element.next.strip()
        return floor_size

    def find_apartment_iptu(self) -> int:
        """
        Return Apartment's IPTU, through the HTML's element.
        """
        logger("Getting Apartment iptu information.",status="DEBUG")
        iptu_element = self.rent_info.find('li', class_="card-price__item iptu text-regular")
        iptu=iptu_element.find('span',class_="card-price__value").get_text(strip=True) if iptu_element else 0
        return iptu
    
    def find_apartment_number_of_rooms(self) -> int:
        """
        Return Apartment's Number of Rooms, through the HTML's element.
        """
        logger("Getting Apartment number_of_rooms information.",status="DEBUG")
        number_of_rooms_element=self.rent_info.find('span',itemprop="numberOfRooms")
        number_of_rooms=number_of_rooms_element.next.strip() if number_of_rooms_element else 0  
        return number_of_rooms
    
    def find_apartment_number_of_bathrooms(self) -> int:
        """
        Return Apartment's Number of Bathrooms, through the HTML's element.
        """
        logger("Getting Apartment number_of_bathrooms information.",status="DEBUG")
        number_of_bathrooms_element=self.rent_info.find('span',itemprop="numberOfBathroomsTotal")
        number_of_bathrooms=number_of_bathrooms_element.next.strip() if number_of_bathrooms_element else 0
        return number_of_bathrooms
    
    def find_apartment_parking_spots(self) -> int:
        """
        Return Apartment's Number of Parking Spots, through the HTML's element.
        """
        logger("Getting Apartment parking information.",status="DEBUG")
        parking_element = self.rent_info.find('li', class_="feature__item text-small js-parking-spaces")
        parking=parking_element.find_all('span')[1].get_text(strip=True) if parking_element else 0        
        return parking
    
    def find_apartment_description(self) -> str:
        """
        Return Apartment's Renting Description, through the HTML's element.
        """
        logger("Getting Apartment description information.",status="DEBUG")
        description_element=self.rent_info.find('span', class_="simple-card__text text-regular")
        description=description_element.next.strip() if description_element else str()
        return description

