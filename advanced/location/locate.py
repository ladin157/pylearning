#!/usr/bin/env python
import geocoder

g = geocoder.ip('111.65.248.132')

print(g.city)