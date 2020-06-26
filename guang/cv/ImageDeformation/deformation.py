import numpy, imageio, elasticdeform
import numpy as np
import matplotlib.pyplot as plt
import guang.cv.imageDeformation.gryds as gryds


original_image = imageio.imread('pikaqiu.jpg')
image = original_image.copy()[:,:,0]

interpolator = gryds.Interpolator(image) # 生成一个图像的插值对象

# -------------------------------------平移----------------------------------------
# 执行一个变换，让图像相左移动 10%，即让 *所有的列* 全部减去 *图像宽度* 的10% :
a_translation = gryds.TranslationTransformation([0., 0.1]) # [行，列]
translated_image = interpolator.transform(a_translation) # 对这个插值对象应用一个变换
fig0 = plt.figure()
plt.imshow(translated_image)
fig0.show()

# -------------------------------------任意扭曲----------------------------------------
sp_shape = (50,50)
x = np.linspace(0, np.pi, sp_shape[0])
bspline = gryds.BSplineTransformation(np.meshgrid(np.zeros(5), np.sin(x)/5-0.2)) # 行偏移为0， 列偏移为sin函数性质
translated_image = interpolator.transform(bspline) # 对这个插值对象应用一个变换
fig1 = plt.figure()
plt.imshow(translated_image)
fig1.show()

# -------------------------------------仿射----------------------------------------
affine_transformation = gryds.AffineTransformation(
    ndim=2,
    angles=[np.pi/10.], # the rotation angle
    scaling=[1.5, 1.5], # the anisotropic scaling
    # shear_matrix=[[1, 0.5], [0, 1]], # shearing matrix
    translation=[0., 0.], # translation
    center=[0.5, 0.5] # center of rotation
)

# ----------------------------------组合-----------------------------------------
composed = gryds.ComposedTransformation(bspline, affine_transformation)
twice_transformed_image = interpolator.transform(composed)
fig3 = plt.figure()
plt.imshow(twice_transformed_image)
fig3.show()

