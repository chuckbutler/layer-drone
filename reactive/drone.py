



from charms.docker.compose import Compose

from charms.reactive import hook
from charms.reactive import set_state
from charms.reactive import when
from charms.reactive import when_not

from charmhelpers.core import hookenv
from charmhelpers.core.hookenv import config
from charmhelpers.core.hookenv import status_set
from charmhelpers.core.templating import render


@when('docker.available')
def start_drone():
    cfg = config()
    if not cfg.get('github_secret') or not cfg.get('github_client'):
        status_set('blocked', 'Requires DVCS credentials - see charm config')
        return
    render('docker-compose.yml', 'files/drone/docker-compose.yml', {})
    render('drone.env', 'files/drone/drone.env', cfg)
    compose = Compose('files/drone')
    compose.up()
    hookenv.open_port(80)
    status_set('active', 'Drone running.')
