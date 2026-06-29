import threading
import requests




class Dowmload:
    def download(self,url,callback_word_cout):
        print(f'line:{threading.get_ident()}start_dowmload:{url}')
        response = requests.get(url)
        response.encoding = 'urf-8'
        callback_word_cout(url,response.text)

    def start_download(self, url,callback_word_cout):

        thread = threading.Thread(target=self.download,args=(url,callback_word_cout))
        thread.start()


def word_count(url,result):

    print(f"{url}:{len(result)}->{result[ :5]}")

def main():
    download=Dowmload()
    download.start_download('http://0.0.0.0:8000/novel1.xt',word_count)
    download.start_download('http://0.0.0.0:8000/novel2.xt',word_count)
    download.start_download('http://0.0.0.0:8000/novel3.xt',word_count)
