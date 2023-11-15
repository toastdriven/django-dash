import hashlib
import urllib


BASE_GRAVATAR_URL = "http://www.gravatar.com/avatar.php?"


def gravatar_id(email):
    return hashlib.md5(email.lower()).hexdigest()


def gravatar_url(email, size=40, default=""):
    gravatar_url = BASE_GRAVATAR_URL + urllib.urlencode(
        {
            "gravatar_id": gravatar_id(email),
            "default": default,
            "size": str(size),
        }
    )
    return gravatar_url
