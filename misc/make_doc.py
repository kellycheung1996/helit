#! /usr/bin/env python

# Copyright 2016 Tom SF Haines

# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

import tps

from utils import doc_gen



# Setup...
doc = doc_gen.DocGen('misc', 'Miscellaneous Algorithms', 'Miscellaneous algorithms that ar not big enough to warrent their own module.')
doc.addFile('readme.txt', 'Overview')



# Classes...
doc.addClass(tps.TPS)