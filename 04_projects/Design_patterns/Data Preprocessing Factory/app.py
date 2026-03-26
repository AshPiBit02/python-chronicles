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
    def __init__(self,mode="lowercase"):
        self.mode=mode
    def normalize(self, data):
        if self.mode=="lowercase":
            result=f"Text normalized: {data.lower()}"
        elif self.mode=="uppercase":
            result=f"Text normalized: {data.upper()}"
        else:
            result=f"Text normalized: {data}"
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
    def __init__(self,scale_range=(0,1)):
        self.scale_range=scale_range
    def normalize(self, data):
        result= f"Image normalized: scaled pixels of {data}"
        print(f"[LOG]: Image noramlized to range {self.scale_range} for {data}")
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
    def __init__(self,mode="lowercase"):
        self.mode=mode
    def create_cleaner(self):
        return TextCleaner()
    def create_normalizer(self):
        return TextNormalizer(mode=self.mode)
    def create_feature_extractor(self):
        return TextFeatureExtractor()
    
class ImagePreprocessingFactory(PreprocessingFactory):
    def __init__(self,scale_range=(0,1)):
        self.scale_range=scale_range
    def create_cleaner(self):
        return ImageCleaner()
    def create_normalizer(self):
        return ImageNormalizer(scale_range=self.scale_range)
    def create_feature_extractor(self):
        return ImageFeatureExtractor()
    
def client_code(factory: PreprocessingFactory,data):
    cleaner=factory.create_cleaner()
    normalizer=factory.create_normalizer()
    extractor=factory.create_feature_extractor()

    print(cleaner.clean(data))
    print(normalizer.normalize(data))
    print(extractor.extract(data))
