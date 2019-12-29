from charms.reactive import when
from charmhelpers.core.hookenv import status_set


@when('snap.installed.slurmctld',
      'snap.installed.munge')
def set_available():
    status_set("active", "")
