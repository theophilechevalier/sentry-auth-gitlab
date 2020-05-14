#!/usr/bin/env python

from setuptools import setup

setup(
    entry_points={
        'sentry.apps': [
            'auth_gitlab = sentry_auth_gitlab.apps.Config',
         ],
    }
)
