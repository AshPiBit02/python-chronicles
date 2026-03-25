from app import PreprocessingFactory,TextPreprocessingFactory,ImagePreprocessingFactory
def client_code(factory: PreprocessingFactory,data):
    cleaner=factory.create_cleaner()
    normalizer=factory.create_normalizer()
    extractor=factory.create_feature_extractor()

    print(cleaner.clean(data))
    print(normalizer.normalize(data))
    print(extractor.extract(data))

# Test with Text Data
print(f"'-'*7 Text Preprocessing'-'*7")
client_code(TextPreprocessingFactory,"This is a sample stopword text")


# Test with Image Data
print(f"'-'*7 Image Preprocessing'-'*7")
client_code(ImagePreprocessingFactory,"sample_image.png")