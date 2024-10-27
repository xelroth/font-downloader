from colorama import(
    Fore as ColoramaFore,
    init as ColoramaInit,
    Style as ColoramaStyle
)
import requests
import os

class FontDownloader:
    def __init__(self):
        os.system("cls" if os.name == "nt" else "clear")
        ColoramaInit()
        self.weights1 = [
		"Hairline",
		"Line",
		"Book",
		"News",
		"Demi",
		"Regular",
		"Normal",
		"Text",
		"Medium",
		"Heavy",
		"Mass",
		"Fat",
		"Poster"
	]
        self.weights2 = [
		"Thin",
		"Light",
		"Lite",
		"Thick",
		"Bold",
		"Dark",
		"Black"
	]
        self.weights3 = [
		"Light",
		"Bold"
	]
        self.formats = [
		"eot",
		"otf",
		"svg",
		"ttf",
		"woff",
		"woff2"
	]
        self.links = []
        self.count = 0
        self.font_name = ""
        self.pattern_url = ""

    def __DISPLAYTITLE__(self):
        print(ColoramaFore.CYAN + "Font Downloader")
        print(ColoramaFore.MAGENTA + "            https://github.com/xelroth        " + "\n")

    def __GETINSPECTIONSPEED__(self):
        print(ColoramaFore.GREEN + "Enter inspection speed (1 for Fastest, 2 for Slower):", end=" ")
        return input()

    def __CREATETEMPWEIGHTS__(self):
        self.weights2_temp = [f"{weight}{suffix}" for weight in self.weights2 for suffix in ["", "Extra", "Ultra", "Very"]]
        self.weights3_temp = [f"{weight}{suffix}" for weight in self.weights3 for suffix in ["", "Semi", "Demi"]]

    def __GETFONTDETAILS__(self):
        self.font_name = input(ColoramaFore.YELLOW + "Enter the font name: " + ColoramaStyle.RESET_ALL)
        self.pattern_url = input(ColoramaFore.YELLOW + "Enter the font file Direct or Pattern URL: " + ColoramaStyle.RESET_ALL)

    def __GENERATELINKS__(self):
        for weight in self.weights1 + self.weights2_temp + self.weights3_temp:
            for fmt in self.formats:
                url = self.pattern_url.replace("{WEIGHT}", weight).replace("{FORMAT}", fmt)
                self.links.append(url)

    def __DOWNLOADFONT__(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0",
            "referer": "https://github.com/hamid0740/Font-Downloader"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(os.path.join(self.font_name, os.path.basename(url)), "wb") as f:
                f.write(response.content)
            self.count += 1
            print(ColoramaFore.GREEN + f"[✓] Downloaded: {os.path.basename(url)}")
        else:
            print(ColoramaFore.RED + f"[X] Error downloading: {url} (Status code: {response.status_code})")

    def __STARTDOWNLOAD__(self):
        if not os.path.exists(self.font_name):
            os.makedirs(self.font_name)
        for link in self.links:
            self.__DOWNLOADFONT__(link)

    def RUN(self):
        self.__DISPLAYTITLE__()
        speed = self.__GETINSPECTIONSPEED__()
        self.__CREATETEMPWEIGHTS__()
        self.__GETFONTDETAILS__()
        self.__GENERATELINKS__()
        self.__STARTDOWNLOAD__()
        print(ColoramaFore.CYAN + f"[!] Total files downloaded: {self.count}")

if __name__ == "__main__":
    downloader = FontDownloader()
    downloader.RUN()
