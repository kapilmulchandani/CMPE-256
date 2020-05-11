from PIL import Image
import numpy as np

def read_image(fname):
    im = Image.open(fname)
    width, height = im.size
    mode   = im.mode
    pixels = list(im.getdata())
    im.close()

    r_pxs  = list(map(lambda x:x[0], pixels))
    g_pxs  = list(map(lambda x:x[1], pixels))
    b_pxs  = list(map(lambda x:x[2], pixels))
    r_pxs  = [r_pxs[i * width:(i + 1) * width] for i in range(height)]
    g_pxs  = [g_pxs[i * width:(i + 1) * width] for i in range(height)]
    b_pxs  = [b_pxs[i * width:(i + 1) * width] for i in range(height)]

    return mode, (width, height), (r_pxs, g_pxs, b_pxs)

def do_svd_compress(matrix, depth = 1):
    matrix_    = np.asarray(matrix, dtype = float)
    U, Sd, Vt  = np.linalg.svd(matrix_, full_matrices = True)
    S          = np.zeros(matrix_.shape, dtype = float)
    S[:depth, :depth] = np.diag(Sd[:depth])
    return np.dot(U, np.dot(S, Vt)), len(Sd)

def svd_compress(mode, size, rgb, depth, fname):
    r, rs_num = do_svd_compress(rgb[0], depth)
    g, gs_num = do_svd_compress(rgb[1], depth)
    b, bs_num = do_svd_compress(rgb[2], depth)

    int_it = lambda f:int(round(f, 0))

    pixels = list(map(lambda x, y, z: (int_it(x), int_it(y), int_it(z)),
                                            r.flat, g.flat, b.flat))

    res = Image.new(mode, size)
    res.putdata(pixels)
    res.save(fname)
    res.close()
    return rs_num, gs_num, bs_num

sample_image = read_image('cat.jpg')
print(sample_image)
i = 10
while i < 101:
    print(i)
    compression = svd_compress(sample_image[0],sample_image[1], sample_image[2], i, "created_"+str(i)+".jpg")
    print('compression : ', compression)
    i = i+10