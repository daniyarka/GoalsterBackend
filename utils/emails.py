from utils import deeplinks, encoding

import constants


def generate_activation_email(email, language, version):
    if language == 'ru-ru':
        start = constants.ACTIVATION_EMAIL_BODY_START_RU
        end = constants.ACTIVATION_EMAIL_BODY_END_RU
    else:
        start = constants.ACTIVATION_EMAIL_BODY_START_EN
        end = constants.ACTIVATION_EMAIL_BODY_END_EN
    if version == 1:
        link = deeplinks.construct_link(constants.DEEPLINK_AUTH, email=encoding.encode(email))
    elif version == 2:
        link = deeplinks.construct_link_v2(constants.DEEPLINK_AUTH, email=encoding.encode(email))
    elif version == 3:
        link = deeplinks.construct_link_v3(constants.DEEPLINK_AUTH, email=encoding.encode(email))
    return f"""{start}

{link}

{end}"""


def generate_premium_email(language):
    if language == 'ru-ru':
        body = constants.PREMIUM_EMAIL_BODY_RU
    else:
        body = constants.PREMIUM_EMAIL_BODY_EN
    return f"""{body}
"""


def generate_observation_confirmation_email(email, language, version):
    if language == 'ru-ru':
        start = constants.OBSERVATION_EMAIL_BODY_START_RU
        end = constants.OBSERVATION_EMAIL_BODY_END_RU
    else:
        start = constants.OBSERVATION_EMAIL_BODY_START_EN
        end = constants.OBSERVATION_EMAIL_BODY_END_EN
    if version == 1:
        link = deeplinks.construct_link(constants.DEEPLINK_PREMIUM, email=encoding.encode(email))
    elif version == 2:
        link = deeplinks.construct_link_v2(constants.DEEPLINK_PREMIUM, email=encoding.encode(email))
    elif version == 3:
        link = deeplinks.construct_link_v3(constants.DEEPLINK_PREMIUM, email=encoding.encode(email))
    return f"""{start}
    
{link}
    
{end}"""
