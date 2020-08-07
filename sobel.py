from PIL import Image


def sobel(list_of_pixels, size):
    """
    Performs the Sobel function on a list of pixels.
    :param size: A tuple with the size of the image.
    :param list_of_pixels: A list of pixel intensities. Must be values from 0-255.
    :return: A new list of pixels with only the edges inside.
    """
    width, height = size

    gradient_x = [0 for _ in list_of_pixels]
    gradient_y = [0 for _ in list_of_pixels]

    for y in range(height):
        print(y)
        for x in range(width):
            # find values of surrounding pixels

            if x == 0:
                up_left    = 0
                up         = list_of_pixels[(y - 1) * height + x - 0]
                up_right   = list_of_pixels[(y - 1) * height + x + 1]
                left       = 0
                right      = list_of_pixels[(y - 0) * height + x + 1]
                down_left  = 0
                down       = list_of_pixels[(y + 1) * height + x - 0]
                down_right = list_of_pixels[(y + 1) * height + x + 1]
            elif x == width:
                up_left    = list_of_pixels[(y - 1) * height + x - 1]
                up         = list_of_pixels[(y - 1) * height + x - 0]
                up_right   = 0
                left       = list_of_pixels[(y - 0) * height + x - 1]
                right      = 0
                down_left  = list_of_pixels[(y + 1) * height + x - 1]
                down       = list_of_pixels[(y + 1) * height + x - 0]
                down_right = 0
            elif y == 0:
                up_left    = 0
                up         = 0
                up_right   = 0
                left       = list_of_pixels[(y - 0) * height + x - 1]
                right      = list_of_pixels[(y - 0) * height + x + 1]
                down_left  = list_of_pixels[(y + 1) * height + x - 1]
                down       = list_of_pixels[(y + 1) * height + x - 0]
                down_right = list_of_pixels[(y + 1) * height + x + 1]
            elif y == height:
                up_left    = list_of_pixels[(y - 1) * height + x - 1]
                up         = list_of_pixels[(y - 1) * height + x - 0]
                up_right   = list_of_pixels[(y - 1) * height + x + 1]
                left       = list_of_pixels[(y - 0) * height + x - 1]
                right      = list_of_pixels[(y - 0) * height + x + 1]
                down_left  = 0
                down       = 0
                down_right = 0
            else:
                up_left    = list_of_pixels[(y - 1) * height + x - 1]
                up         = list_of_pixels[(y - 1) * height + x - 0]
                up_right   = list_of_pixels[(y - 1) * height + x + 1]
                left       = list_of_pixels[(y - 0) * height + x - 1]
                right      = list_of_pixels[(y - 0) * height + x + 1]
                down_left  = list_of_pixels[(y + 1) * height + x - 1]
                down       = list_of_pixels[(y + 1) * height + x - 0]
                down_right = list_of_pixels[(y + 1) * height + x + 1]

            gradient_x[y * height + x] = (-1 * up_left   + 0 * up   + 1 * up_right +
                                          -2 * left      + 0        + 2 * right +
                                          -1 * down_left + 0 * down + 1 * down_right)
            gradient_y[y * height + x] = (-1 * up_left   + -2 * up  + -1 * up_right +
                                           0 * left      + 0        + 0 * right +
                                           1 * down_left + 2 * down + 1 * down_right)

    gradient = [(x**2 + y**2)**0.5 for x,y in zip(gradient_x, gradient_y)]
    grad_max = max(gradient)
    gradient = [x/grad_max*255 for x in gradient] # normalize

    return gradient


im = Image.open('line.png')

# perform sobel on grayscale image
im_gray_pixels = list(im.getdata())
im_gray_pixels = [(x[0] ** 2 + x[1] ** 2 + x[2] ** 2) ** 0.5 for x in im_gray_pixels]  # pythagorean theorem

orig_pic_gray = Image.new('L', im.size)
orig_pic_gray.putdata(im_gray_pixels)
orig_pic_gray.show()

edges = sobel(im_gray_pixels, im.size)
edge_pic = Image.new('L', im.size)
edge_pic.putdata(edges)
edge_pic.show()