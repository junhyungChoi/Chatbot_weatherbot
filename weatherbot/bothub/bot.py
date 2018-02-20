# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

from bothub_client.bot import BaseBot
from bothub_client.messages import Message

from .weather import get_weather


class Bot(BaseBot):

    def handle_message(self, event, context):
        location = event.get('location')
        appid = '6a5beaeff30e04d92c42f59d7c17eba5'

        if location:
            lat = location['latitude']
            lon = location['longitude']
            weather = get_weather(lat, lon, appid)
            self.send_message(weather)

        msg = Message(event).set_text('날씨 확인을 위해 현재 위치를 전송해주세요.') \
                            .add_location_request('Send Location')
        self.send_message(msg)
		
		# msg = Message(event).set_text('날씨 확인을 위해 현재 위치를 전송해주세요.')
        # self.send_message('날씨 확인을 위해 현재 위치를 전송해주세요.')
		# self.send_message(msg)
