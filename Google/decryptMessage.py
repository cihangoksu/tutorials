#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

MESSAGE = '''
GE4bFA1NAhwYVFUUGB8EGw0AGglLT0wQGkJUXQIOHQRJDl1PTBYGWl1dDgwMRkIOQAoNFRpcTEtE SVJBSUcJDBkWEUdaVAZOREFJTwQHAhYDS1VdDR1PQVQOQBoFHxpNU10HTkRBSVwGDQkaAV0fGFlJ TxIPSAJIR1NSSFdXRElSQUlZDgFKVAg=
'''
KEY = 'cihan.goksu.88'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))