

class LegacyImageLibrary:
    def load_file(self, filename):
        print(f"Image loaded from file: {filename}")

    def display_image(self):
        print("Image displayed.")



class ModernImageLibrary:
    def load(self, file_path):
        print(f"Image loaded from path: {file_path}")

    def render(self):
        print("Image rendered.")


class ModernImageAdapter(LegacyImageLibrary):
    def __init__(self):
        self.modern_image_library = ModernImageLibrary()

    def load_file(self, filename):
        self.modern_image_library.load(filename)
    
    def display_image(self):
        self.modern_image_library.render()


def main():
    legacy_image_library = ModernImageAdapter()
    # modern_image_adapter = ModernImageAdapter()

    legacy_image_library.load_file("image.png")
    legacy_image_library.display_image()

    # modern_image_adapter.load_file("image.png")
    # modern_image_adapter.display_image()

print("Output:")
main()


