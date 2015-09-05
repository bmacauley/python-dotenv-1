# Copyright 2015 Konstantinos Pachnis.  All rights reserved.
# Use of this source code is governed by the BSD 3-Clause License that can be
# found in the LICENSE file.

import os
import json

def load(file='.env'):
    """
    Load application settings from a json file and export them as environment
    variables.
    """
    with open(file, 'r') as f:
        settings = json.loads(f.read())
        for k, v in settings.items():
            os.environ.setdefault(k, str(v))
