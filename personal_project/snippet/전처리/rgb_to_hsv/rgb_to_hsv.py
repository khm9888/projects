################################### HSV 적용 (start) ########################

def rgb_to_hsv(img):

    import matplotlib.pyplot as plt

    from skimage import data
    from skimage.color import rgb2hsv

    # We first load the RGB image and extract the Hue and Value channels
    # print()
    rgb_img = img #이미지 읽어오되, np.array 형태로

    print(rgb_img.shape)#np.array 형태로 (height, width, channel 출력)
    hsv_img = rgb2hsv(rgb_img)
    hue_img = hsv_img[:, :, 0]
    sat_img = hsv_img[:, :, 1]
    value_img = hsv_img[:, :, 2]



    plt.imshow(hsv_img)
    plt.savefig("0_hsv_img.png")
    # plt.imshow(rgb_img)
    # plt.savefig("0_rgb_img.png")
    # plt.imshow(hue_img)
    # plt.savefig("1_hue_img.png")
    # plt.imshow(sat_img)
    # plt.savefig("2_sat_img.png")
    # plt.imshow(value_img)
    # plt.savefig("3_value_img.png")

    # We then set a threshold on the Hue channel to separate the cup from the background:

    hue_threshold = 0.04
    binary_img = hue_img > hue_threshold

    fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(8, 3))

    # #histogram

    # ax0.hist(hue_img.ravel(), 512)
    # ax0.set_title("Histogram of the Hue channel with threshold")
    # ax0.axvline(x=hue_threshold, color='r', linestyle='dashed', linewidth=2)
    # ax0.set_xbound(0, 0.12)
    # ax1.imshow(binary_img)
    # ax1.set_title("Hue-thresholded image")
    # ax1.axis('off')

    # fig.tight_layout()
    
    return hsv_img

hsv_img = rgb_to_hsv(img)


################################### HSV 적용 (end) ########################