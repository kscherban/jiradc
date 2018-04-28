import re
from os import environ
import sys


def get_parameters(env_variables):
  parameters = {}
  for env_var in env_variables:
    ev_key = env_var.lower().replace('_', '.')
    ev_value = environ.get(env_var, '')
    parameters[ev_key] = ev_value
  return parameters
