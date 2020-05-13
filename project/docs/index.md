## Linear Algebra

### REVIEW 

一个向量A可以用一个单列矩阵 $\mathbf{a}$ 来表示，它的元素是A的分量:
$$
\mathbf{A} \Longrightarrow \mathbf{a}=\left(\begin{array}{l}
A_{1} \\
A_{2} \\
A_{3}
\end{array}\right) \notag
$$
表示向量A的矩阵的转置是一个单行矩阵，称为行向量:
$$
\mathbf{a}^{T}=\left(A_{1} \quad A_{2} \quad A_{3}\right) \notag
$$

#### 内积(inner  Product)：

#### 点积(dot product)

$\mathbf{A} \cdot \mathbf{B}$ 可由$\mathbf{a}^{T} \mathbf{b}$ 表示，，或者 a 和b 都是实数，所以有$a^†b$。此外，$a^ T b = b^ T a$。
$$
\begin{equation}
\begin{aligned}
\mathbf{A} \cdot \mathbf{B}&=\mathbf{a}^{T} \mathbf{b}=\left(\begin{array}{lll}
A_{1} & A_{2} & A_{3}
\end{array}\right)\left(\begin{array}{l}
B_{1} \\
B_{2} \\
B_{3}
\end{array}\right)\\
&=A_{1} B_{1}+A_{2} B_{2}+A_{3} B_{3}\\
&=\sum_{i}A_i B_i \\
\end{aligned}
\end{equation}
$$

在此，给出一个以后将会用到的例子:

对于
$$
\begin{equation}
A=\left(\begin{array}{l}
1 \\
2 \\
3
\end{array}\right), \quad B=\left(\begin{array}{lll}
4 & 5 & 6
\end{array}\right)
\notag
\end{equation}
$$
给出矩阵内积 $AB $ 以及 $B A$
$$
\begin{equation}
\label{example1}
A B=\left(\begin{array}{rrr}
4 & 5 & 6 \\
8 & 10 & 12 \\
12 & 15 & 18
\end{array}\right), \quad B A=(4 \times 1+5 \times 2+6 \times 3)=(32)\end{equation}
$$




#### 叉积/外积( cross Product)：

$\mathbf{A} \times \mathbf{B}$  定义：
$$
\mathbf{C}=\mathbf{A} \times \mathbf{B}=(A B \sin \theta) \hat{\mathbf{e}}_{c}
$$
满足反交换律：
$$
\mathbf{B} \times \mathbf{A}=-\mathbf{A} \times \mathbf{B}
$$
也满足分配律：
$$
\mathbf{A} \times(\mathbf{B}+\mathbf{C})=\mathbf{A} \times \mathbf{B}+\mathbf{A} \times \mathbf{C}, \quad k(\mathbf{A} \times \mathbf{B})=(k \mathbf{A}) \times \mathbf{B}
$$
引入 Levi-Civita 符号  $\varepsilon_{i j k}$ 
$$
\hat{\mathbf{e}}_{i} \times \hat{\mathbf{e}}_{j}=\sum_{k} \varepsilon_{i j k} \hat{\mathbf{e}}_{k}
$$
上式表示，例如 $\hat{\mathbf{e}}_{x} \times \hat{\mathbf{e}}_{x}=0$ , $\hat{\mathbf{e}}_{x} \times \hat{\mathbf{e}}_{y}=\hat{\mathbf{e}}_{z}$,  但是  $\hat{\mathbf{e}}_{y} \times \hat{\mathbf{e}}_{x}=-\hat{\mathbf{e}}_{z}$

那么我们展开$\mathbf{A} \times \mathbf{B}$ ，得到：
$$
\begin{equation}
\begin{aligned}
\mathbf{C}=& \mathbf{A} \times \mathbf{B}=\left(A_{x} \hat{\mathbf{e}}_{x}+A_{y} \hat{\mathbf{e}}_{y}+A_{z} \hat{\mathbf{e}}_{z}\right) \times\left(B_{x} \hat{\mathbf{e}}_{x}+B_{y} \hat{\mathbf{e}}_{y}+B_{z} \hat{\mathbf{e}}_{z}\right) \\
=&\left(A_{x} B_{y}-A_{y} B_{x}\right)\left(\hat{\mathbf{e}}_{x} \times \hat{\mathbf{e}}_{y}\right)+\left(A_{x} B_{z}-A_{z} B_{x}\right)\left(\hat{\mathbf{e}}_{x} \times \hat{\mathbf{e}}_{z}\right) \\
&+\left(A_{y} B_{z}-A_{z} B_{y}\right)\left(\hat{\mathbf{e}}_{y} \times \hat{\mathbf{e}}_{z}\right) \\
=&\left(A_{x} B_{y}-A_{y} B_{x}\right) \hat{\mathbf{e}}_{z}+\left(A_{x} B_{z}-A_{z} B_{x}\right)\left(-\hat{\mathbf{e}}_{y}\right)+\left(A_{y} B_{z}-A_{z} B_{y}\right) \hat{\mathbf{e}}_{x} \\
\label{cross}
\end{aligned}
\end{equation}
$$
于是$\mathbf{C}$ 的各个分量为：
$$
C_{x}=A_{y} B_{z}-A_{z} B_{y}, \quad C_{y}=A_{z} B_{x}-A_{x} B_{z}, \quad C_{z}=A_{x} B_{y}-A_{y} B_{x} \notag
$$
即：
$$
C_{i}=\sum_{j k} \varepsilon_{i j k} A_{j} B_{k} \label{cross1}
$$
当然，公式$(\ref{cross}) (\ref{cross1})$也可表示为行列式形式：
$$
\mathbf{C}=\left|\begin{array}{lll}
\hat{\mathbf{e}}_{x} & \hat{\mathbf{e}}_{y} & \hat{\mathbf{e}}_{z} \\
A_{x} & A_{y} & A_{z} \\
B_{x} & B_{y} & B_{z}
\end{array}\right| \label{lalal}
$$

### 直积/ 克罗内克积（Direct Product/  Kronecker product）：

将$m×n$矩阵$\mathbf{A}$与$m'× n'$矩阵$\mathbf{B}$结合得到直积矩阵 $\mathrm{C}=\mathrm{A} \otimes \mathrm{B}$ ,其维度为$m m^{\prime} \times n n^{\prime}$ ，具体例子如下：

如果A和B都是2×2矩阵，我们可以这样写，先用符号形式，然后用完全展开的形式
$$
\begin{equation}\mathrm{A} \otimes \mathrm{B}=\left(\begin{array}{ll}
a_{11} \mathrm{B} & a_{12} \mathrm{B} \\
a_{21} \mathrm{B} & a_{22} \mathrm{B}
\end{array}\right)=\left(\begin{array}{llll}
a_{11} b_{11} & a_{11} b_{12} & a_{12} b_{11} & a_{12} b_{12} \\
a_{11} b_{21} & a_{11} b_{22} & a_{12} b_{21} & a_{12} b_{22} \\
a_{21} b_{11} & a_{21} b_{12} & a_{22} b_{11} & a_{22} b_{12} \\
a_{21} b_{21} & a_{21} b_{22} & a_{22} b_{21} & a_{22} b_{22}
\end{array}\right)\end{equation}
$$
另一个例子是两个两元列向量x和y的直接乘积，还是先写符号，然后扩展形式
$$
\begin{equation}\left(\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right) \otimes\left(\begin{array}{l}
y_{1} \\
y_{2}
\end{array}\right)=\left(\begin{array}{l}
x_{1} \mathbf{y} \\
x_{2} \mathbf{y}
\end{array}\right)=\left(\begin{array}{l}
x_{1} y_{1} \\
x_{1} y_{2} \\
x_{2} y_{1} \\
x_{2} y_{2}
\end{array}\right)\end{equation}
$$
第三个例子是来自例子方程$(\ref{example1})$ :

它是特殊情况下的一个实例(列向量乘以行向量)，其中直积和内积重合: $AB =A \otimes B$ 


## 一维积分：

$$
\begin{equation}
\begin{aligned}
I(f) 
&= \int_{x_1}^{x_n}f(x)dx \\
&= \sum_{i=1}^{n} w_{i} f\left(x_{i}\right)+ R(n) \\
&\approx  \sum_{i=1}^{n} w_{i} f\left(x_{i}\right) 
\end{aligned}
\end{equation}
$$



不同的数值积分方法就是上面的$w_i$不同， 最简单的矩形积分法如下：
$$
\begin{equation}
\begin{aligned}
\int_{x_0}^{x_n}f(x)dx  
&\approx \sum_{i=1}^{n} f(x_i) \Delta x = \Delta x \sum_{i=1}^{n} f(x_i)\\
&= \frac{x_n - x_1}{n}\sum_{i=1}^{n} f(x_i)
\end{aligned}
\end{equation}
$$

复合一维积分：
$$
\begin{equation}
\begin{aligned}
\label{eq: integ1d}
I(f) &=\int_{x_1}^{x_n}f(x)g(x)dx
\approx \sum_{i=1}^{n} f(x_i)g(x_i) \Delta x = \Delta x \sum_{i=1}^{n} f(x_i)g(x_i)\\
&= \frac{x_n - x_1}{n} \vec{f(x)} \cdot \vec{g(x)}  
\end{aligned}
\end{equation}
$$





##  二维积分：

对于两个变量的积分的表达式，比如x和y，可以写成两种积分符号：
$$
\begin{equation}
\begin{aligned}
\label{integ2d}
\iint f(x, y) d x d y \text { 或者 } \, \int_{x_{1}}^{x_{2}} d x \int_{y_{1}(x)}^{y_{2}(x)} d y\ f(x, y) 
\end{aligned}
\end{equation}
$$


其中，右边的形式可以更具体地表示积分界限，并给出了一个明确的指示，即y积分应该首先执行，或者使用单个积分符号，如
$$
\int_{S} f(x, y) d A
$$
其中S(如果显式显示)为二维积分区域，$dA$为“area” (在笛卡尔坐标系中，等于$dxdy$)

OK，这不是重点。

对于公式$\ref{integ2d}$ ，将其中的$f(x,y)$变量分离为 $f_1(x)f_2(y)$ ，将得到：
$$
\label{sepa_value}
\int_{x_1}^{x_2} f_1(x)dx \int_{y_1(x)}^{y_2(x)} f_2(y)dy\\
$$

当然， 这可能不是我要的形式， 我希望的是：  
$$
\begin{equation}
\begin{aligned}
&\int_{x_1}^{x_2} dx \int_{y_1(x)}^{y_2(x)}dy \ f_1(x)f_2(y)\\
&\approx  \Delta x \Delta y \sum_{i}^{N}\sum_{j}^{M}\ f_1(x_i)f_2(y_j) \\
&=\frac{x_2 - x_1}{N} \frac{y_2(x) - y_1(x)}{M} \sum \vec{f_1(x)} \otimes \vec{f_2(y)}
\end{aligned}
\end{equation}
$$






计算

一维：

$$
\pi = I(f) =\int_{0}^{1}\frac{4}{1+x^2}dx
$$


二维：
$$
\begin{aligned}
\iint x y \, \mathrm{d} \sigma &=\int_{1}^{2}\left[\int_{1}^{x} x y \mathrm{d} y\right] \mathrm{d} x=\int_{1}^{2}\left[x \cdot \frac{y^{2}}{2}\right]_{1}^{x} \mathrm{d} x \\
&=\int_{1}^{2}\left(\frac{x^{3}}{2}-\frac{x}{2}\right) \mathrm{d} x=\left[\frac{x^{4}}{8}-\frac{x^{2}}{4}\right]_{1}^{2}=\frac{9}{8}
\end{aligned}
$$
