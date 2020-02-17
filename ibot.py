"""
    instabot example
    Workflow:
    1) likes your timeline feed
    2) likes user's feed
    Notes:
    1) You should pass user_id, not username
"""

import os
import sys

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402

bot = Bot()
bot.login(username="USER", password="pass")

bot.like_user("stbcbeer")