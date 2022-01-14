import matplotlib.pyplot as plt

plt.imshow(img)
plt.title('Image name:{}  Bone age: {} years  Gender: {}'.format(filename, boneage/12, gender))
plt.axis('off')
plt.savefig('/home/con/data/boneage/p/'+ filename)
plt.show()