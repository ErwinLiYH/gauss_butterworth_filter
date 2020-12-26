<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Filter image base on Fourier transfer

The filter application written by Erwin for course Numerical Computation(1001).
2020-12

## help

```
$ python3 filter.py -h
usage: filter.py [-h] [-i input file] [-o output file] [-hol high or low]
                 [-D D] [-n N]
                 filter

a simple image processer base on fourier transfer

positional arguments:
  filter            the filter you want to use, candidate:[butterworth,gauss]

optional arguments:
  -h, --help        show this help message and exit
  -i input file     the path of input file
  -o output file    the path of output file
  -hol high or low  high pass filter or low pass filter
  -D D              D0 parameter
  -n N              n parameter

```

## Thheory

1. Butterworth filter:

    low pass filter: $H(u,v)=\frac{1}{1+[D(u,v)/D_0]^{2n}}$

    high pass filter: $H(u,v)=\frac{1}{1+[D_0/D(u,v)]^{2n}}$

2. Gauss filter:

    low pass filter: ![](./gauss_low.svg)

    high pass filter: ![](./gauss_high.svg)

## Example

```shell
python3 filter.py gauss -i example.jpg -o example_out.jpg -D 40 -hol high
```

There will have a window pop out, which display the process of filter:
![](./example_pop_out.png)

After there will have a image named “example_out.jpg” in the folder, which is the result we want:
<img src="./example_out.jpg" style="zoom: 20%;" />

