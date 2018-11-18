import segmentation

img = segmentation.CharSeg("test_sample/", "test_sample/saved/", "ni_hao.jpeg", (150, 150), 3, 0.7)
print(img.image_gray.shape)
img.run()