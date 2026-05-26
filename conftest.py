from clients.remoteok_client import RemoteokClient
from clients.weworkremotely_client import WeworkremotelyClient
from clients.glassdoor_client import GlassdoorClient
from clients.wellfound_client import WellfoundClient
import pytest

@pytest.fixture
def remoteok_client():
    return RemoteokClient()

@pytest.fixture
def weworkremotely_client():
    return WeworkremotelyClient()

@pytest.fixture
def glassdoor_client():
    return GlassdoorClient()

@pytest.fixture
def wellfound_client():
    return WellfoundClient()