# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from dtmf_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from dtmf_client.model.endpoint import Endpoint
from dtmf_client.model.tunnel import Tunnel
