import requests, constants


def send_notification(user, type):
    parameters = { 
        'notification': {
            'title': get_texts(type, user.language)[0],
            'body': get_texts(type, user.language)[1],
            'sound': 'default',
            'badge': 1
        },
        'data': {
            'type': type
        },
        'to': user.fcm_token
    }
    headers = {
        'Authorization': f'key={constants.FIREBASE_SERVER_KEY}'
    }
    requests.request(method='POST', url=constants.FCM_SEND_URL, json=parameters, headers=headers)


def get_texts(type, language):
    if type == constants.NOTIFICATION_3DAYS:
        if language == constants.LANGUAGE_RUSSIAN:
            return constants.THREE_DAYS_TITLE_RU, constants.THREE_DAYS_BODY_RU
        else:
            return constants.THREE_DAYS_TITLE_EN, constants.THREE_DAYS_BODY_EN
    if type == constants.NOTIFICATION_BEFORE_END:
        if language == constants.LANGUAGE_RUSSIAN:
            return constants.BEFORE_END_TITLE_RU, constants.BEFORE_END_BODY_RU
        else:
            return constants.BEFORE_END_TITLE_EN, constants.BEFORE_END_BODY_EN
    if type == constants.NOTIFICATION_END:
        if language == constants.LANGUAGE_RUSSIAN:
            return constants.END_TITLE_RU, constants.END_BODY_RU
        else:
            return constants.END_TITLE_EN, constants.END_BODY_EN
