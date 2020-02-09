# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + {"slideshow": {"slide_type": "slide"}, "id": "OWTWS9tmFApF", "colab_type": "text", "cell_type": "markdown"}
# # Jupyter Notebook 使用技巧彙整
#
# > 轉換為投影片格式
#
# > `jupyter nbconvert my-nb-slide.ipynb --to slides --post serve`
#
# [Pyradise](https://www.facebook.com/pyradise.geek/)，郭耀仁
#
# [Jupyter Notebook 使用技巧彙整：轉換為投影片格式](https://medium.com/pyradise/jupyter-notebook-tricks-slideshows-a057a39c0a23)
#
# Edit by Yu Long Tsai
#

# + {"slideshow": {"slide_type": "slide"}, "id": "L0BKNkE6FApH", "colab_type": "text", "cell_type": "markdown"}
# ## 水平投影片

# + {"id": "u7bX-APCFApI", "colab_type": "code", "colab": {}, "outputId": "f941c83b-a641-4e67-e762-52b8f81f1713"}
# 會直接顯示在1.1中，以Slide進行區隔
print("Horizontal slide")

# + {"slideshow": {"slide_type": "subslide"}, "id": "mpqdj5NNFApQ", "colab_type": "text", "cell_type": "markdown"}
# ## 垂直投影片
# * 從下面出現，透過**下方向鍵**來控制

# + {"id": "lNpfzisnFApR", "colab_type": "code", "colab": {}, "outputId": "f57faf3c-d620-41f0-a7f0-4899ef105448"}
# 會跟著1.2一起出現
print("Vertical slide")

# + {"slideshow": {"slide_type": "slide"}, "id": "wq6pp_gBFApV", "colab_type": "text", "cell_type": "markdown"}
# ## 另一張水平投影片

# + {"id": "NeADejJtFApW", "colab_type": "code", "colab": {}, "outputId": "42289e99-ef8c-44cc-d462-12ee0a8f395a"}
print("Another horizontal slide")

# + {"slideshow": {"slide_type": "subslide"}, "id": "kYZCGdM9FApb", "colab_type": "text", "cell_type": "markdown"}
# ## 另一張垂直投影片
# * 另一張圖影片

# + {"id": "oyQlgs98FApd", "colab_type": "code", "colab": {}, "outputId": "eb51e3ab-0455-498c-c4c2-9b86c00d8771"}
print("Another vertical slide")

# + {"slideshow": {"slide_type": "fragment"}, "id": "VNOlbh0oFApi", "colab_type": "text", "cell_type": "markdown"}
# ## Fragment 投影片
# * 依序顯示多個儲存格

# + {"slideshow": {"slide_type": "fragment"}, "id": "ebTUYWxEFApk", "colab_type": "code", "colab": {}, "outputId": "efb16958-6638-404d-8c2e-abb9b3ba7c0b"}
print("A fragment slide")

# + {"slideshow": {"slide_type": "fragment"}, "id": "UBQ-JVpYFApp", "colab_type": "text", "cell_type": "markdown"}
# ## 另一張 Fragment 投影片

# + {"slideshow": {"slide_type": "fragment"}, "id": "M5OVFL8uFApq", "colab_type": "code", "colab": {}, "outputId": "f13143d6-4321-4e1f-e74e-f93564062d86"}
print("Another fragment slide")

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # 使用須知
# * `.py`檔案雖然和`jupytext`相容，但是無法被`jupyter nbconvert`轉譯
#   * 解法為light script，用`ipynb`進行簡報，用`.py`編輯
# * 無法即時更新，需要重啟jupyter server

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## 轉成pdf
# * 原本
# `http://127.0.0.1:8000/my-nb-slide.slides.html#/`
# * 加上print-pdf
# `http://127.0.0.1:8000/my-nb-slide.slides.html?print-pdf`

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Live coding
# * `pip install rise` or `conda install rise`
#
# * 上方工具列，圖表按鈕
# * 可以Live coding
# * 但是會顯示章節

# + {"slideshow": {"slide_type": "skip"}, "id": "Tv-bty7lFApu", "colab_type": "text", "cell_type": "markdown"}
# ## Skip

# + {"slideshow": {"slide_type": "skip"}, "id": "QtDhfBHJFApw", "colab_type": "code", "colab": {}, "outputId": "55c21732-e1b3-40ae-cf02-de7f8d061c1c"}
print("Skip slide")

# + {"slideshow": {"slide_type": "notes"}, "id": "hhEYn6BcFAp0", "colab_type": "text", "cell_type": "markdown"}
# ## Notes
# * 備忘錄

# + {"slideshow": {"slide_type": "notes"}, "id": "ynklVTNiFAp1", "colab_type": "code", "colab": {}, "outputId": "d15e5884-a9c0-443e-af59-414bcc129df7"}
print("Notes slide")
