from app import PreprocessingFactory,TextPreprocessingFactory,ImagePreprocessingFactory
def client_code(factory: PreprocessingFactory,data):
    cleaner=factory.create_cleaner()
    normalizer=factory.create_normalizer()
    extractor=factory.create_feature_extractor()

    print(cleaner.clean(data))
    print(normalizer.normalize(data))
    print(extractor.extract(data))

def run_pipeline(factory: PreprocessingFactory,data):
    cleaner=factory.create_cleaner()
    normalizer=factory.create_normalizer()
    extractor=factory.create_feature_extractor()

    # Sequential execution
    cleaned=cleaner.clean(data)
    normalized=normalizer.normalize(cleaned)
    features=extractor.extract(normalized)

    print("[Pipleline Result]: ",features)


# Test with Text Data
print(f"'-'*7 Text Preprocessing'-'*7")
client_code(TextPreprocessingFactory(),"This is a sample stopword text")


# Test with Image Data
print(f"'-'*7 Image Preprocessing'-'*7")
client_code(ImagePreprocessingFactory(),"sample_image.png")

# Text Factory with uppercase normalization
text_factory=TextPreprocessingFactory(mode="uppercase")
client_code(text_factory,"This is a sample stopword text")

# Image Factory with pixel scaling to 0-511
image_factory=ImagePreprocessingFactory(scale_range=(0,511))
client_code(image_factory,"demo_image.jpeg")

print(f"'-'*7 Text Pipleling'-'*7")
run_pipeline(TextPreprocessingFactory(mode="uppercase"),"This is a sample stopword text")

print(f"'-'*7 Image Pipleling'-'*7")
run_pipeline(ImagePreprocessingFactory(scale_range=(0,1023)),"demo_image.png")

