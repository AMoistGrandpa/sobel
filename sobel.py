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
            # I know having this many if statements isn't good but I didn't see a way to optimize it
            if x == 0 or y == 0:
                up_left = 0
            else: up_left = list_of_pixels[(y - 1) * width + x - 1]

            if x == 0:
                left = 0
            else: left = list_of_pixels[(y - 0) * width + x - 1]

            if x == 0 or y == height - 1:
                down_left = 0
            else: down_left = list_of_pixels[(y + 1) * width + x - 1]

            if y == 0:
                up = 0
            else: up = list_of_pixels[(y - 1) * width + x - 0]

            if y == height - 1:
                down = 0
            else: down = list_of_pixels[(y + 1) * width + x - 0]

            if x == width - 1 or y == 0:
                up_right = 0
            else: up_right = list_of_pixels[(y - 1) * width + x + 1]

            if x == width - 1:
                right = 0
            else: right = list_of_pixels[(y - 0) * width + x + 1]

            if x == width - 1 or y == height -1:
                down_right = 0
            else: down_right = list_of_pixels[(y + 1) * width + x + 1]


            gradient_x[y * width + x] = (-1 * up_left   + 0 * up   + 1 * up_right +
                                          -2 * left      + 0        + 2 * right +
                                          -1 * down_left + 0 * down + 1 * down_right)
            gradient_y[y * width + x] = (-1 * up_left   + -2 * up  + -1 * up_right +
                                           0 * left      + 0        + 0 * right +
                                           1 * down_left + 2 * down + 1 * down_right)

    gradient = [(x**2 + y**2)**0.5 for x,y in zip(gradient_x, gradient_y)]
    grad_max = max(gradient)
    gradient = [int(x/grad_max*255 + 0.5) for x in gradient] # normalize and round

    return gradient




if __name__ == '__main__':

    im = Image.open('smash.jpg')
    im.show()

    # perform sobel on grayscale image
    im_gray_pixels = list(im.getdata())
    im_gray_pixels = [int(((x[0] ** 2 + x[1] ** 2 + x[2] ** 2) ** 0.5)/(3**0.5)) for x in im_gray_pixels]  # pythagorean theorem

    edges = sobel(im_gray_pixels, im.size)
    edge_pic = Image.new('L', im.size)
    edge_pic.putdata(edges)
    edge_pic.show()

    # perform sobel using colour data
    r,g,b = im.split()
    r = list(r.getdata())
    g = list(g.getdata())
    b = list(b.getdata())

    r_edges = sobel(r, im.size)
    g_edges = sobel(g, im.size)
    b_edges = sobel(b, im.size)

    colour_edges = list(zip(r_edges, g_edges, b_edges))
    edge_pic_colour = Image.new('RGB', im.size)
    edge_pic_colour.putdata(colour_edges)
    edge_pic_colour.show()
