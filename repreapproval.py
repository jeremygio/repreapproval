
import sys
__author__ = 'paul.rangel'
# dudeface
sys.path.insert(0, './libs/reportlab.zip')
sys.path.insert(1, './src')

import API

import webapp2

app = webapp2.WSGIApplication(
    [
        ('/api/v[0-9]/humans/add', API.HumansAdd),
        ('/api/v[0-9]/humans/edit', API.HumansEdit),
        ('/api/v[0-9]/humans/delete', API.HumansDelete),
        ('/api/v[0-9]/humans/list', API.HumansList),
        ('/api/v[0-9]/request/add', API.RequestAdd),
        ('/api/v[0-9]/letters/edit', API.LettersEdit),
        ('/api/v[0-9]/letters/print', API.LettersPrint),
        ('/api/v[0-9]/request/list', API.RequestList)
    ],
    debug=True)

