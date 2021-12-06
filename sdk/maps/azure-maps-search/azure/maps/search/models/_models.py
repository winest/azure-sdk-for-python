import msrest.serialization
from typing import List, Optional

class LatLon(object):

    def __init__(
        self,
        lat: float=None,
        lon: float=None
    ):
        self._lat = lat
        self._lon = lon

    def __transform__(self, **kwargs): # type: (...) -> List[float]
        return [self._lat, self._lon]

    @property
    def lat(self) -> float:
        return self._lat

    @lat.setter
    def lat(self, value: float) -> None:
        if type(value) is not float:
            raise TypeError('lat.setter(): got {} but expected type is float'
                            .format(type(value).__name__))
        else:
            self._lat = value

    @property
    def lon(self) -> float:
        return self._lon

    @lon.setter
    def lon(self, value) -> None:
        if type(value) is not float:
            raise TypeError('lon.setter(): got {} but expected type is float'
                            .format(type(value).__name__))
        else:
            self._lon = value

class BoundingBox(object):

    def __init__(
        self,
        top_left: str=None,
        bottom_right: str=None
    ):
        self.top_left = top_left
        self.bottom_right = bottom_right


class StructuredAddress(object):
    def __init__(
        self,
        *,
        country_code: str,
        cross_street: Optional[str] = None,
        street_number: Optional[str] = None,
        street_name: Optional[str] = None,
        municipality: Optional[str] = None,
        municipality_subdivision: Optional[str] = None,
        country_tertiary_subdivision: Optional[str] = None,
        country_secondary_subdivision: Optional[str] = None,
        country_subdivision: Optional[str] = None,
        postal_code: Optional[str] = None,
        **kwargs
    ):
        self.country_code = country_code
        self.cross_street = cross_street
        self.street_number = street_number
        self.street_name = street_name
        self.municipality = municipality
        self.municipality_subdivision = municipality_subdivision
        self.country_tertiary_subdivision = country_tertiary_subdivision
        self.country_secondary_subdivision = country_secondary_subdivision
        self.country_subdivision = country_subdivision
        self.postal_code = postal_code


# class Polygon(msrest.serialization.Model):
#     """This object is returned from a successful Search Polygon call.

#     Variables are only populated by the server, and will be ignored when sending a request.

#     :ivar polygons: Results array.
#     :vartype polygons: list[~azure.maps.search.models.Polygon]
#     """

#     _validation = {
#         'provider_id': {'readonly': True},
#         'polygons': {'readonly': True},
#     }

#     _attribute_map = {
#         'provider_id': {'key': 'providerID', 'type': 'str'},
#         'geometry_data': {'key': 'geometryData', 'type': 'GeoJsonObject'},
#     }


#     def __init__(
#         self,
#         **kwargs
#     ):
#         super(Polygon, self).__init__(**kwargs)
#         self.provider_id = None
#         self.geometry_data = kwargs.get('geometry_data', None)


# class Polygon(msrest.serialization.Model):
#     """Polygon.

#     Variables are only populated by the server, and will be ignored when sending a request.

#     :ivar provider_id: ID of the returned entity.
#     :vartype provider_id: str
#     :param geometry_data: Geometry data in GeoJSON format. Please refer to `RFC 7946
#      <https://tools.ietf.org/html/rfc7946>`_ for details. Present only if "error" is not present.
#     :type geometry_data: ~azure.maps.search.models.GeoJsonObject
#     """

#     _validation = {
#         'provider_id': {'readonly': True},
#     }

#     _attribute_map = {
#         'provider_id': {'key': 'providerID', 'type': 'str'},
#         'geometry_data': {'key': 'geometryData', 'type': 'GeoJsonObject'},
#     }

#     def __init__(
#         self,
#         **kwargs
#     ):
#         super(Polygon, self).__init__(**kwargs)
#         self.provider_id = None
#         self.geometry_data = kwargs.get('geometry_data', None)
