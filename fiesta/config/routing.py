"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from routes import Mapper

def make_map(config):
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False
    map.explicit = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE

    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')
    map.connect('mapping1', '/celebrations/auth', controller='celebrations', action='auth' )
    map.connect('mapping2', '/celebrations/index', controller='celebrations', action='index' )
    map.connect('mapping3', '/userauth/auth', controller='userauth', action='auth' )
    map.connect('mapping4', '/userauth/authnext', controller='userauth', action='authnext' )
    map.connect('mapping5', '/retailer/store', controller='retailer', action='store' )
    map.connect('mapping6', '/plugins/celebrations', controller='plugins', action='celebrations' )
    map.connect('mapping7', '/plugins/paisan', controller='plugins', action='paisan' )
    map.connect('mapping8', '/plugins/saltation', controller='plugins', action='saltation' )
    map.connect('mapping9', '/plugins/setpluginurl', controller='plugins', action='setpluginurl' )
    map.connect('mapping9', '/plugins/geturl', controller='plugins', action='geturl' )

    return map
