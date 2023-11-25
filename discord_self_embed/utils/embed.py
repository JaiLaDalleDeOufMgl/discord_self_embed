import urllib.parse

class Embed:
    def __init__(self) -> None:
        self.hide_text = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
        self.base_url = "https://appembed.netlify.app/e?"
        self.params = {}

    def __str__(self) -> str:
        return self.generate_url(hide_url=True)

    def set_title(self, title) -> None:
        self.params["author"] = title

    def set_title_url(self, url) -> None:
        self.params["author_url"] = url

    def set_description(self, description) -> None:
        self.params["description"] = description

    def set_color(self, color) -> None:
        self.params["color"] = color

    def set_author(self, name) -> None:
        self.params["provider"] = name

    def set_author_url(self, url) -> None:
        self.params['provider_url'] = url

    def set_image(self, url) -> None:
        self.params["image"] = url

    def generate_url(self) -> str:
        for key in list(self.params.keys()):
            if self.params[key] == "" or self.params[key] is None:
                del self.params[key]

        url = self.base_url + urllib.parse.urlencode(self.params)

        return self.hide_text + " " + url
