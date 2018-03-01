from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import SpatialDatasetServiceSetting


class Mapapp(TethysAppBase):
    """
    Tethys app class for Map App.
    """

    name = 'Map App'
    index = 'mapapp:home'
    icon = 'mapapp/images/my-icon.gif'
    package = 'mapapp'
    root_url = 'mapapp'
    color = '#141E30'
    description = 'This is my first Tethys App that shows maps from a geoserver.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='mapapp',
                controller='mapapp.controllers.home'
            ),
            UrlMap(
                name='proposal',
                url='mapapp/proposal',
                controller='mapapp.controllers.proposal'
            ),
            UrlMap(
                name='mockup',
                url='mapapp/mockup',
                controller='mapapp.controllers.mockup'
            ),
            UrlMap(
                name='mapview',
                url='mapapp/mapview',
                controller='mapapp.controllers.mapview'
            ),
            UrlMap(
                name='dataservices',
                url='mapapp/dataservices',
                controller='mapapp.controllers.dataservices'
            ),
            UrlMap(
                name='about',
                url='mapapp/about',
                controller='mapapp.controllers.about'
            ),
        )

        return url_maps
