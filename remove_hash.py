def remove_url_anchor(url):
    if "#" in url:
        find = url.index("#")
        return url[:find]
    return url
