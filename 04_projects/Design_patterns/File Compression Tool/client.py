from app import FileCompressor,ZipCompression,RarCompression,GzipCompression

compressor=FileCompressor(ZipCompression())
compressor.compress_file("re_dit.txt")

compressor.set_strategy(RarCompression())
compressor.compress_file("tning.txt")

compressor.set_strategy(GzipCompression())
compressor.compress_file("vromt.txt")

