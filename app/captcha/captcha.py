import uuid
from copy import copy
from datetime import datetime, timedelta

from fast_captcha import img_captcha


class GetCaptcha:
    uuid_list = {}

    def get_img(self):
        img, text = img_captcha(code_num=4, lines_num=8, draw_points=False)
        get_uuid = str(uuid.uuid4())
        current_time = datetime.now()
        print(current_time)
        self.uuid_list[get_uuid] = {'text': text, 'current_time': current_time}
        print(self.uuid_list)
        return img, get_uuid

    def is_captcha_valid(self, text, uuid):
        result = copy(self.uuid_list)
        for key, val in result.items():
            get_text = val['text']
            get_current_time = val['current_time']
            if datetime.now() < (get_current_time + timedelta(minutes=1)):
                if key == uuid:
                    if get_text == text:
                        return True
                    return False
            self.uuid_list.pop(key)



















