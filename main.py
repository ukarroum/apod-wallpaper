import requests
import re


def download_apod():
    """ Download  Astronomy Picture of the Day """
    apod_html = requests.get("https://apod.nasa.gov/apod/").text

    img_src = re.search('<IMG SRC="(.*)"\n', apod_html).group(1)

    img_data = requests.get(f"https://apod.nasa.gov/apod/{img_src}").content

    with open("apod.jpg", "wb") as f:
        f.write(img_data)


if __name__ == "__main__":
    download_apod()
