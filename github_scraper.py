from bs4 import BeautifulSoup
from urllib.request import urlopen

URL = "https://github.com/trending"

def main():
    """
    Output:
        1: r4j0x00/exploits
        2: microsoft/Swin-Transformer
        3: Light-City/CPlusPlusThings
        4: opensearch-project/OpenSearch
        5: tailwindlabs/headlessui
        6: d2l-ai/d2l-zh
        7: bradtraversy/vanillawebprojects
        8: tauri-apps/tauri
        9: opensearch-project/OpenSearch-Dashboards
        10: DidierRLopes/GamestonkTerminal
        11: PaddlePaddle/PaddleOCR
        12: pamoroso/free-python-books
        13: thedevdojo/wave
        14: easychen/one-person-businesses-methodology
        15: Chia-Network/chia-blockchain
        16: nordicgiant2/awesome-landing-page
        17: mikepound/enigma
        18: academind/react-complete-guide-code
        19: lindelof/awesome-web-effect
        20: semi-technologies/weaviate
        21: qiurunze123/miaosha
        22: Serial-Studio/Serial-Studio
        23: huggingface/transformers
        24: nlohmann/json
        25: foxlet/macOS-Simple-KVM
    """
    get_content()   

def get_content():
        content = urlopen(URL).read()
        soup = BeautifulSoup(content, "html.parser")
        articles = soup.find_all('article')
        print_content(articles)

def print_content(articles):
    for idx, article in enumerate(articles):
        title = article.h1.a['href'][1:]
        print(str(idx+1) + ": " + title)

main()



    