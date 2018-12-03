import segmentation

img = segmentation.CharSeg("test_sample/", "test_sample/saved/", "0_0.png", output_size = (58, 58))
print(img.image_gray.shape)
img.run()