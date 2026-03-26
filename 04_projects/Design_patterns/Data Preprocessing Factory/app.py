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
        result= f"Text cleaned: {data.lower().replace('stopword','')}"
        print("[LOG]: TextCleaner applied stopword removal")
        return result
class TextNormalizer(Normalizer):
    def normalize(self, data):
        result=f"Text normalized: {data.lower()}"
        print("[LOG]: TextNormalizer applied text normalized")
        return result
class TextFeatureExtractor(FeatureExtractor):
    def extract(self, data):
        result=f"Text features extracted: word_count={len(data.split())}"
        print("[LOG]: TextFeatueExtractor applied text feature extracted")
        return result

# Concrete Products for Image
class ImageCleaner(Cleaner):
    def clean(self,data):
        result=f"Image cleaned: remove noise from {data}"
        print("[LOG]: ImageClearner removed noise")
        return result
class ImageNormalizer(Normalizer):
    def normalize(self, data):
        result= f"Image normalized: scaled pixels of {data}"
        print("[LOG]: ImageNormalizer scaled pixels")
        return result
class ImageFeatureExtractor(FeatureExtractor):
    def extract(self, data):
        result= f"Image features extracted: histogram of {data}"
        print("[LOG]: ImageFeatureExtractor extracted additional features")
        return result

# Abstract Factories
class PreprocessingFactory:
    def create_cleaner(self):
        raise NotImplementedError
    def create_normalizer(self):
        raise NotImplementedError
    def create_feature_extractor(self):
        raise NotImplementedError

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
client_code(TextPreprocessingFactory(),"This is a sample stopword text")


# Test with Image Data
print(f"{'-'*7} Image Preprocessing {'-'*7}")
client_code(ImagePreprocessingFactory(),"sample_image.png")