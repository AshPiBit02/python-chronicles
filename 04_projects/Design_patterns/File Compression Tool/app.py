# Strategy Interface
class CompressionStrategy:
    def compress(self,file):
        pass

# Concrete Strategies
class ZipCompression(CompressionStrategy):
    def compress(self,file):
        print(f"Compressing {file} using ZIP algorithm.")

class RarCompression(CompressionStrategy):
    def compress(self, file):
        print(f"Compressing {file} using RAR algorithm.")

class GzipCompression(CompressionStrategy):
    def compress(self, file):
        print(f"Compressing {file} using GZIP algorithm.")

class FileCompressor:
    def __init__(self,strategy: CompressionStrategy):
        self.strategy=strategy
    def set_strategy(self,strategy:CompressionStrategy):
        self.strategy=strategy
    def compress_file(self,file):
        self.strategy.compress(file)

