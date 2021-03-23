#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "bab29103-1fe0-4da3-9614-d214443706c2")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "C.X85iUOE7~h-CHXfl03a~0nk._gERt3cn")
