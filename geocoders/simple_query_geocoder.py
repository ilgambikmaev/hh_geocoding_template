from geocoders.geocoder import Geocoder
from api import API


# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:
        """
            TODO:
            - Делать запросы к API для каждой area
            - Для каждого ответа формировать полный адрес
        """
        node = API.get_area(area_id)
        address = node.name
        while True:
            if node.parent_id is None:
                break
            node = API.get_area(node.parent_id)
            address = node.name + ", " + address

        return address
