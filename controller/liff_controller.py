import os
from flask import request, render_template, Response
from flask_restful import Resource

LIFF_A = os.getenv('LIFF_SHARE_A')
LIFF_B = os.getenv('LIFF_SHARE_B')
SHARE_A = f"https://liff.line.me/{LIFF_A}"
SHARE_B = f"https://liff.line.me/{LIFF_B}"

class LiffAController(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self):
        if request.args.get('liff.state'):
            return Response(render_template('liff_redirect.html', liff_id=LIFF_A))
        return Response(render_template('a.html', liff_id=LIFF_A, text='AAAAAAAAA', next=SHARE_B))

class LiffBController(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self):
        if request.args.get('liff.state'):
            return Response(render_template('liff_redirect.html', liff_id=LIFF_B))
        return Response(render_template('b.html', liff_id=LIFF_B, text='BBBBBBBBBB', next=SHARE_A))
