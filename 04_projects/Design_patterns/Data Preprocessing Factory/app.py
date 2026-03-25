# Abstract Products
class Cleaner:
    def clean(self,data):
        raise NotImplementedError
class Normalizer:
    def normalize(self,data):
        raise NotImplementedError
class FeatureExtractor:
    def extract(self,data):
        raise NotImplementedError

# Concrete Products for Text
class TextCleaner(Cleaner):
    def clean(self,data):
        return f"Text cleaned: {data.lower().replace('stopword','')}"
class TextNormalizer(Normalizer):
    def normalize(self, data):
        return f"Text normalized: {data.lower()}"
class TextFeatureExtractor(FeatureExtractor):
    def extract(self, data):
        return f"Text features extracted: word_count={len(data.split())}"

# Concrete Products for Image
class ImageCleaner(Cleaner):
    def clean(self,data):
        return f"Image cleaned: remove noise from {data}"
class ImageNormalizer(Normalizer):
    def normalize(self, data):
        return f"Image normalized: scaled pixels of {data}"
class ImageFeatureExtractor(FeatureExtractor):
    def extract(self, data):
        return f"Image features extracted: histogram of {data}"

# Abstract Factories
class PreprocessingFactory:
    def create_cleaner(self):
        return NotImplementedError
    def create_normalizer(self):
        return NotImplementedError
    def create_feature_extractor(self):
        return NotImplementedError

# Concrete Factories
class TextPreprocessingFactory(PreprocessingFactory):
    def create_cleaner(self):
        return TextCleaner()
    def create_normalizer(self):
        return TextNormalizer()
    def create_feature_extractor(self):
        return TextFeatureExtractor()
    
class ImagePreprocessingFactory(PreprocessingFactory):
    def create_cleaner(self):
        return ImageCleaner()
    def create_normalizer(self):
        return ImageNormalizer()
    def create_feature_extractor(self):
        return ImageFeatureExtractor()
    
def client_code(factory: PreprocessingFactory,data):
    cleaner=factory.create_cleaner()
    normalizer=factory.create_normalizer()
    extractor=factory.create_feature_extractor()

    print(cleaner.clean(data))
    print(normalizer.normalize(data))
    print(extractor.extract(data))

# Test with Text Data
print(f"{'-'*7} Text Preprocessing {'-'*7}")
client_code(TextPreprocessingFactory,"This is a sample stopword text")


# Test with Image Data
print(f"{'-'*7} Image Preprocessing {'-'*7}")
# client_code(ImagePreprocessingFactory,"sample_image.png")