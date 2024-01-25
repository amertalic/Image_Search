import os
import random

import requests
import wikipedia
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    IMAGE_DIR = "storage"
    IMAGE_FILENAME = "image.jpg"

    def set_image(self):
        self.manager.current_screen.ids.img.source = self.get_image()

    def get_image(self):
        image_links = self.get_image_urls()
        imagepath = self.get_imagepath()
        self.save_image(image_links, imagepath)
        return imagepath

    def get_image_urls(self):
        search_keyword = self.manager.current_screen.ids.userquery.text
        return self.search_wikipedia_images(search_keyword)

    def save_image(self, image_links, imagepath):
        if len(image_links) > 1:
            self.download_image(image_links[0], imagepath)

    def search_wikipedia_images(self, search_keyword):
        try:
            page = wikipedia.page(search_keyword)
        except wikipedia.DisambiguationError as e:
            random_search_word = random.choice(e.options)
            page = wikipedia.page(random_search_word)
        return page.images

    def get_imagepath(self):
        os.makedirs(FirstScreen.IMAGE_DIR, exist_ok=True)
        return os.path.join(FirstScreen.IMAGE_DIR, FirstScreen.IMAGE_FILENAME)

    def download_image(self, url, save_path):
        try:
            headers = {'User-Agent': FirstScreen.USER_AGENT}
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                with open(save_path, 'wb') as f:
                    f.write(response.content)

                print("Image downloaded.")
            else:
                print(f"Failed to download image. Status code: {response.status_code}")

        except requests.RequestException as e:
            print(f"An error occurred during the request: {e}")
        except IOError as e:
            print(f"An error occurred while writing the image file: {e}")


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
