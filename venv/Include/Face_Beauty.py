# @Author  :  lijishi
# @Contact :  lijishi@emails.bjut.edu.cn
# @Software:  Pycharm
# @EditTime:  Jan 12,2020
# @describe:  Use TencentCloud API Realize Face Beauty
# @LICENSE :  GNU GENERAL PUBLIC LICENSE Version 3

# References
# https://github.com/TencentCloud/tencentcloud-sdk-python

# Thanks
# Tencent Cloud Free API

import os
import time
import json
import base64
import tkinter as tk
import tkinter.filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.fmu.v20191213 import fmu_client, models
os.system("pause")
icon64en = r'AAABAAEAQEAAAAEAIAAoQgAAFgAAACgAAABAAAAAgAAAAAEAIAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAD////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+/v7/fHx8/ysrK//09PT/lpaW/zw8PP9wcHD/pqam/93d3f/+/v7//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////f39/15eXv8rKyv/9fX1/+7u7v/6+vr//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////Pz8//Dw8P/Dw8P/mZmZ/3x8fP9ra2v/Z2dn/21tbf9+fn7/qamp/+vr6//7+/v//v7+//////////////////////////////////////////////////////////////////r6+v9HR0f/Kysr//b29v/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////29vb/tra2/19fX/8fHx//ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8bGxv/VlZW/6CgoP/c3Nz/+/v7///////////////////////////////////////////////////////29vb/Ly8v/ysrK//29vb///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////7+/v/Gxsb/TU1N/xMTE/8XFxf/Pz8//2ZmZv+FhYX/np6e/7CwsP+6urr/wMDA/7+/v/+cnJz/VFRU/xkZGf8RERH/ISEh/01NTf+ZmZn/3Nzc//7+/v//////////////////////////////////////6+vr/xgYGP9AQED/+fn5//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////n5+f+Li4v/ISEh/05OTv+qqqr/6enp//n5+f/+/v7//////////////////////////////////v7+//v7+//n5+f/nZ2d/01NTf8fHx//ERER/xgYGP9DQ0P/kZGR/9fX1//29vb/////////////////9fX1/2VlZf8TExP/lpaW//7+/v////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////b29v9zc3P/PT09/729vf/7+/v/6enp/9nZ2f/Z2dn/4ODg/+3t7f/9/f3////////////////////////////////////////////+/v7/3d3d/5aWlv9NTU3/HBwc/xEREf8VFRX/RERE/4iIiP/AwMD/tLS0/1NTU/8UFBT/Tk5O/5ycnP+IiIj/q6ur/9vb2//+/v7///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////z8/P99fX3/RkZG/+bm5v/BwcH/V1dX/ykpKf8gICD/ICAg/yQkJP8sLCz/PT09/2pqav+lpaX/7e3t////////////////////////////////////////////+fn5/9ra2v+SkpL/Q0ND/xISEv8RERH/ExMT/xwcHP8lJSX/FBQU/xsbG/8RERH/ERER/xEREf8hISH/ZWVl/9/f3/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+vr6//JSUl/9PT0/97e3v/EhIS/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xgYGP9kZGT/zs7O//39/f/////////////////////////////////////////////////4+Pj/4ODg/8/Pz/9vb2//FRUV/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8iIiL/u7u7///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////7+/v/QkJC/21tbf+FhYX/EhIS/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xwcHP+AgID/8fHx/////////////////////////////////////////////////+3t7f9WVlb/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/zU1Nf/5+fn/////////////////////////////////////////////////////////////////////////////////////////////////////////////////1NTU/x0dHf+QkJD/JiYm/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/EhIS/0xMTP/p6en///////////////////////////////////////j4+P9kZGT/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8VFRX/GBgY/xoaGv8eHh7/wMDA/////////////////////////////////////////////////////////////////////////////////////////////////////////////////6ioqP8VFRX/paWl/5OTk/+ampr/m5ub/5aWlv+Kior/dnZ2/1tbW/87Ozv/IiIi/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/RUVF/+rq6v////////////////////////////////+mpqb/EhIS/xEREf8RERH/ERER/xEREf8TExP/MTEx/2pqav+goKD/xMTE/9zc3P/o6Oj/7Ozs//X19f/////////////////////////////////////////////////////////////////////////////////////////////////////////////////W1tb/qqqq/+jo6P/////////////////////////////////+/v7/9/f3/97e3v+srKz/Wlpa/xcXF/8RERH/ERER/xEREf8RERH/ERER/xEREf9lZWX/+Pj4////////////////////////////ODg4/xEREf8RERH/ERER/xEREf89PT3/rq6u/+3t7f/+/v7///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////z8/P/U1NT/TU1N/xMTE/8RERH/ERER/xEREf8RERH/ExMT/6Wlpf///////////////////////////1RUVP8RERH/ERER/xISEv9vb2//9PT0//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////X19f91dXX/ExMT/xEREf8RERH/ERER/xEREf8rKyv/8/Pz///////////////////////Q0ND/Nzc3/xYWFv9sbGz/8vLy///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////Hx8f/qKio/6ysrP/b29v/////////////////////////////////////////////////9vb2/1RUVP8RERH/ERER/xEREf8RERH/ERER/52dnf///////////////////////v7+/+3t7f/Z2dn/+fn5///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////29vb/Ojo6/xEREf8RERH/ERER/xsbG/8jIyP/IyMj/yMjI/8jIyP/IyMj/yMjI/8vLy//RUVF/1FRUf9AQED/ERER/xEREf8RERH/ERER/xEREf8XFxf/IyMj/yMjI/8jIyP/IyMj/yMjI/8jIyP/IyMj/yMjI/8jIyP/IyMj/yMjI/8jIyP/IyMj/yMjI/8jIyP/IyMj/yMjI/8jIyP/IyMj/zMzM//29vb/////////////////////////////////////////////////////////////////////////////////////////////////////////////////9PT0/zg4OP8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8wMDD/9vb2//////////////////////////////////////////////////////////////////////////////////////////////////////////////////T09P84ODj/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/RERE//n5+f/////////////////////////////////////////////////////////////////////////////////////////////////////////////////7+/v/V1dX/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/0VFRf/5+fn//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////9/f3/90dHT/S0tL/zc3N/9RUVH/YGBg/2BgYP9gYGD/YGBg/2BgYP9gYGD/YGBg/2BgYP9gYGD/YGBg/2BgYP88PDz/ERER/xEREf8RERH/ERER/yMjI/9eXl7/YGBg/2BgYP9gYGD/YGBg/2BgYP9gYGD/YGBg/2BgYP9gYGD/YGBg/2BgYP9gYGD/YGBg/2BgYP9gYGD/YGBg/2VlZf+fn5///f39/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////v7+//r6+v/39/f/+/v7//39/f/9/f3//f39//39/f/9/f3//f39//39/f/9/f3//f39//39/f/9/f3/n5+f/xEREf8RERH/ERER/xEREf8rKyv/7e3t//39/f/9/f3//f39//39/f/9/f3//f39//39/f/9/f3//f39//39/f/9/f3//f39//39/f/9/f3//f39//39/f/+/v7////////////////////////////////////////////////////////////////////////////////////////////////////////////4+Pj/8/Pz//X19f///////////////////////////////////////////////////////////////////////////////////////////7Kysv8SEhL/ERER/xEREf8RERH/ERER/729vf////////////////////////////////////////////////////////////////////////////7+/v/4+Pj/9PT0//v7+///////////////////////////////////////////////////////////////////////////////////////////////////////ZWVl/y8vL/8xMTH/SEhI/15eXv9wcHD/f39//42Njf+ampr/pqam/7Gxsf+9vb3/x8fH/9PT0//e3t7/6enp//X19f/+/v7///////////+5ubn/ExMT/xEREf8RERH/ERER/xEREf9qamr////////////+/v7/+Pj4/+rq6v/b29v/zMzM/7y8vP+qqqr/mZmZ/4WFhf9vb2//WVlZ/0VFRf83Nzf/MjIy/zAwMP86Ojr/goKC/+7u7v///////////////////////////////////////////////////////////////////////////////////////////ycnJ/8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ExMT/x4eHv8qKir/Kioq/xEREf8RERH/ERER/xEREf8RERH/FxcX/zExMf8kJCT/FxcX/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf89PT3/5eXl//////////////////////////////////////////////////////////////////////////////////////89PT3/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/2xsbP//////////////////////////////////////////////////////////////////////////////////////ZWVl/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8WFhb/6enp/////////////////////////////////////////////////////////////////////////////////4eHh/8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/6SkpP/////////////////////////////////////////////////////////////////////////////////j4+P/gICA/3x8fP98fHz/fHx8/3x8fP98fHz/fHx8/3x8fP98fHz/fHx8/3x8fP98fHz/fHx8/3x8fP98fHz/fHx8/3x8fP98fHz/fHx8/3x8fP9ra2v/ERER/xEREf8RERH/ERER/xQUFP9vb2//fHx8/3x8fP98fHz/fHx8/3x8fP98fHz/fHx8/3x8fP98fHz/fHx8/3x8fP98fHz/fHx8/319ff+Ghob/kpKS/5SUlP+JiYn/bW1t/zs7O/+Xl5f/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////2NjY/xEREf8RERH/ERER/xEREf8ZGRn/4uLi//////////////////////////////////////////////////////////////////////////////////////////////////7+/v/4+Pj/9PT0/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////9jY2P8RERH/ERER/xEREf8RERH/GRkZ/+Li4v///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////9LS0v9paWn/YGBg/3Nzc/+cnJz/oqKi/6Kiov+ioqL/oqKi/7CwsP/BwcH/zMzM/9HR0f/V1dX/1tbW/9bW1v+2trb/ERER/xEREf8RERH/ERER/xgYGP+9vb3/0tLS/8vLy//Dw8P/urq6/7CwsP+mpqb/oqKi/6Kiov+ioqL/oqKi/6Kiov+ioqL/oqKi/6mpqf/q6ur///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+srKz/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/jo6O////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////tbW1/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/5+fn////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////9TU1P8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf+fn5/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////s7Oz/NTU1/xQUFP8TExP/GBgY/yUlJf8rKyv/Kysr/ysrK/8rKyv/Kysr/ysrK/8rKyv/Kysr/ysrK/8rKyv/Jycn/xEREf8RERH/ERER/xEREf8RERH/KCgo/ysrK/8rKyv/Kysr/ysrK/8rKyv/Kysr/ysrK/8rKyv/Kysr/ysrK/8rKyv/Kysr/ysrK/89PT3/ysrK/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////v7+/+np6f/Q0ND/z8/P/9TU1P/h4eH/5+fn/+fn5//n5+f/5+fn/+fn5//n5+f/5+fn/+fn5//n5+f/5+fn/8TExP8RERH/ERER/xEREf8RERH/GBgY/87Ozv/n5+f/5+fn/+fn5//n5+f/5+fn/+fn5//n5+f/5+fn/+fn5//n5+f/5+fn/+fn5//n5+f/9PT0///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////Y2Nj/ERER/xEREf8RERH/ERER/xkZGf/i4uL/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////7u7u/3l5ef9lZWX/YWFh/4CAgP+oqKj/tbW1/76+vv/ExMT/yMjI/8rKyv/MzMz/zc3N/87Ozv/Ozs7/zs7O/87Ozv/Ozs7/r6+v/xEREf8RERH/ERER/xEREf8YGBj/1NTU/+7u7v/u7u7/7u7u/+7u7v/u7u7/7u7u/+7u7v/u7u7/7u7u/+7u7v/u7u7/7u7u/+7u7v/u7u7/4eHh/87Ozv/39/f//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////9nZ2f8dHR3/ERER/xEREf8RERH/ERER/xEREf8RERH/ExMT/xUVFf8XFxf/GBgY/xgYGP8ZGRn/GRkZ/xkZGf8ZGRn/GRkZ/xcXF/8RERH/ERER/xEREf8RERH/ERER/ykpKf8sLCz/LCws/ywsLP8sLCz/LCws/ywsLP8sLCz/LCws/ywsLP8sLCz/LCws/ywsLP8sLCz/LCws/yUlJf8ZGRn/tLS0///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////e3t7/IyMj/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/6urq///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+fn5/0RERP8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf+2trb///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////9tbW3/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8RERH/ERER/xEREf8UFBT/zMzM////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////5+fn/4mJif9ubm7/dXV1/6SkpP+jo6P/m5ub/5ubm/+bm5v/m5ub/21tbf8RERH/ERER/xEREf8RERH/KCgo/5KSkv+bm5v/m5ub/5ubm/+bm5v/m5ub/5ubm/+bm5v/m5ub/y8vL/8RERH/ERER/xEREf8RERH/cnJy/5ubm/+bm5v/m5ub/5ubm/+bm5v/m5ub/5ubm/+bm5v/ra2t//T09P////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////r6+v9dXV3/ERER/xEREf8RERH/ERER/4CAgP/+/v7///////////////////////////////////////////+Tk5P/ERER/xEREf8RERH/ERER/01NTf/6+vr////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////Gxsb/FhYW/xEREf8RERH/ERER/xYWFv/MzMz/////////////////////////////////////////////////3t7e/xcXF/8RERH/ERER/xEREf8TExP/mZmZ//39/f/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////n5+f/MzMz/xEREf8RERH/ERER/xEREf8iIiL/9fX1//////////////////////////////////////////////////X19f9BQUH/ERER/xEREf8RERH/ERER/x0dHf/ExMT/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////tLS0/xISEv8RERH/ERER/xEREf8RERH/Wlpa///////////////////////////////////////////////////////+/v7/hISE/xEREf8RERH/ERER/xEREf8RERH/bW1t//7+/v///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////9HR0f84ODj/HBwc/xEREf8RERH/ERER/66urv///////////////////////////////////////////////////////////9zc3P8kJCT/ERER/xISEv8fHx//Nzc3/7q6uv/+/v7/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8/Pz/9PT0/+jo6P/SUlJ/1lZWf/y8vL////////////////////////////////////////////////////////////+/v7/kpKS/zs7O/+cnJz/2NjY/+np6f////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////f39//39/f///////////////////////////////////////////////////////////////////////39/f/z8/P//v7+////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='
gif64en = r'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AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=='

def TencentFaceBeauty(pic_str, white, smooth, facelift, eyeenlarge):
    try:
        cred = credential.Credential("AKID43qW0IzsGNp8FLb0Y2Rhx27SgjbLqDOO", "85soZ9YwBJIzZw75rSBIHDza0EUkuujN")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "fmu.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = fmu_client.FmuClient(cred, "ap-beijing", clientProfile)

        req = models.BeautifyPicRequest()
#        params = '{"Image":" ", "Whitening":30, "Smoothing":10, "FaceLifting":70, "EyeEnlarging":70}'
        print(pic_str[2:-1])
        params_1 = '{"Image":"'
        params_2 = '", "Whitening":'
        params_3 = ', "Smoothing":'
        params_4 = ', "FaceLifting":'
        params_5 = ', "EyeEnlarging":'
        params_6 = '}'
        params = params_1 + pic_str[2:-1] + params_2 + white + params_3 + smooth + params_4 + facelift + params_5 + eyeenlarge + params_6
        req.from_json_string(params)
        resp = client.BeautifyPic(req)

        req_text = resp.to_json_string()
        for index in range(17, len(str(req_text))):

            if req_text[index] == r'"':
                out_str = req_text[17:index]
                break

        return out_str

    except TencentCloudSDKException as err:
        print(err)

def SelectPath_In():
    path_ = tkinter.filedialog.askopenfilename()
    path_ = path_.replace("/", "\\\\")
    path_in.set(path_)
    string = path_
    i = string.rfind("\\\\")
    string = string[:i+2]
    path_out.set(string)

def SelectPath_Out():
    path_ = tkinter.filedialog.askdirectory()
    path_ = path_.replace("/", "\\\\")
    path_out.set(path_)

def Base64EnCode(path):
    with open(path, "rb") as i:
        input64en = base64.b64encode(i.read())
    return input64en

def Base64DeCode_JPG(str_in):
    global  path_out
    path = str(path_out.get()) + 'Face_Beauty_Out_' + str(time.time()) + '.jpg'
    with open(path, 'wb+') as out:
        out.write(base64.b64decode(str_in))
    img = Image.open(path)
    out_pic = ImageTk.PhotoImage(img)

def Base64DeCode_PNG(str_in):
    global path_out
    path = str(path_out.get()) + 'Face_Beauty_Out_' + str(time.time()) + '.png'
    with open('out.png', 'wb') as out:
        out.write(base64.b64decode(str_in))
    img = Image.open(path)
    out_pic = ImageTk.PhotoImage(img)

def Icon():
    '''
    with open("mei.ico", "rb") as icon:
        icon64en = base64.b64encode(icon.read())
        print(icon64en)
    '''
    global  icon64en
    with open('tmp.ico', 'wb') as tmp:
        tmp.write(base64.b64decode(icon64en))

def Gif():
    '''
    with open("mei.gif", "rb") as gif:
        gif64en = base64.b64encode(gif.read())
        print(gif64en)
    '''
    global  gif64en
    with open('temp.gif', 'wb') as temp:
        temp.write(base64.b64decode(gif64en))
    mei_gif = tk.PhotoImage(file="temp.gif")

def Tip():
    tk.messagebox.showinfo("Tips", "图像格式仅支持jpg/jpeg/png\n图像大小上限未知，推荐1MB以下\n美化程度范围[0，100]，其中0为不处理\n感谢腾讯云提供免费API，美化结果均源于此\n请勿用于非法用途，作者不负任何法律责任\n腾讯云若更改免费政策，可能导致软件无法使用")

def Beauty():

    try:
        if path_in.get()[-3:] == "jpg":
            pic = 1
        elif path_in.get()[-4:] == "jpeg":
            pic = 1
        elif path_in.get()[-3:] == "png":
            pic = 0

        pic_str = Base64EnCode(str(path_in.get()))
        out_str = TencentFaceBeauty(str(pic_str), str(Whitening.get()), str(Smoothing.get()), str(FaceLifting.get()), str(EyeEnlarging.get()))

        print(out_str)
        if pic == 1:
            Base64DeCode_JPG(out_str)
        else:
            Base64DeCode_PNG(out_str)

        Finish()

    except:
        Error()

def Finish():
    tk.messagebox.showinfo("Finish", "美化完成！")

def Error():
    tk.messagebox.showerror("Error", "美化失败！\n可能的原因：\n   1、图片大小超过限制\n   2、图片格式错误\n   3、所处网络状况不佳\n请确认后重试")

def About():
    # window centered
    about_window = Toplevel()
    screen_width = about_window.winfo_screenwidth()
    screen_heigh = about_window.winfo_screenheight()
    about_window_width = 390
    about_window_heigh = 255
    x = (screen_width - about_window_width) / 2
    y = (screen_heigh - about_window_heigh) / 2
    about_window.geometry("%dx%d+%d+%d" % (about_window_width, about_window_heigh, x, y))

    # window layout
    global mei_gif
    about_window.title('About')
    Icon()
    Gif()
    about_window.iconbitmap('tmp.ico')
    os.remove('tmp.ico')
    mei_gif = tk.PhotoImage(file="temp.gif")
    #os.remove('temp.gif')
    software_frame = ttk.LabelFrame(about_window, text='Software Info')
    software_frame.grid(row=0, column=0, rowspan=5, columnspan=4, padx=50, pady=5)
    ttk.Label(software_frame, image=mei_gif, compound='left').grid(row=0, rowspan=3, column=0)
    os.remove('temp.gif')
    ttk.Label(software_frame, text="Face Beauty 1.0").grid(row=0, column=1, sticky = W)
    ttk.Label(software_frame, text="@Author    :   lijishi").grid(row=1, column=1, sticky = W)
    ttk.Label(software_frame, text="@EditTime  :   Jan 12,2020").grid(row=2, column=1, sticky = W)

    copyright_frame = ttk.LabelFrame(about_window, text='LICENSE Info')
    copyright_frame.grid(row=5, column=0, rowspan=3, columnspan=4, padx=50, pady=5)
    ttk.Label(copyright_frame, text = "Github @ Face_Beauty").grid(row=5, column=0)
    ttk.Label(copyright_frame, text="Thanks：Tencent Cloud Free API").grid(row=6, column=0)
    ttk.Label(copyright_frame, text="GNU GENERAL PUBLIC LICENSE Version 3").grid(row=7, column=0)

# window centered
main_window=tk.Tk()
screen_width = main_window.winfo_screenwidth()
screen_heigh = main_window.winfo_screenheight()
main_window_width = 440
main_window_heigh = 200
x = (screen_width-main_window_width) / 2
y = (screen_heigh-main_window_heigh) / 2
main_window.geometry("%dx%d+%d+%d" %(main_window_width,main_window_heigh,x,y))

# window layout
global mei_gif
main_window.title("Face Beauty V1.0")
Icon()
main_window.iconbitmap('tmp.ico')
os.remove('tmp.ico')
path_frame = ttk.LabelFrame(main_window, text = '路径选择')
path_frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 6, padx=10, pady=5)
path_in = tk.StringVar()
path_out = tk.StringVar()
path_in.set("请选择源文件位置，也可在框中键入")
path_out.set("请选择输出位置，默认为源文件路径")
ttk.Label(path_frame, text = "源文件位置").grid(row = 0, column = 0, padx=10)
ttk.Entry(path_frame, width = 30, textvariable = path_in).grid(row = 0, column = 1, padx=5)
ttk.Button(path_frame, text = "选择", command = SelectPath_In).grid(row = 0, column = 2, padx=10)
ttk.Label(path_frame, text = "输出位置").grid(row = 1, column = 0, padx=10)
ttk.Entry(path_frame, width = 30, textvariable = path_out).grid(row = 1, column = 1, padx=5)
ttk.Button(path_frame, text = "选择", command = SelectPath_Out).grid(row = 1, column = 2, padx = 10, pady = 10)
option_frame = ttk.LabelFrame(main_window, text = '美化程度')
option_frame.grid(row = 2, column = 0, rowspan = 4, columnspan = 4, padx=10, pady=5, sticky = W)
Whitening = IntVar()
Smoothing = IntVar()
FaceLifting = IntVar()
EyeEnlarging = IntVar()
Whitening.set(30)
Smoothing.set(10)
FaceLifting.set(70)
EyeEnlarging.set(70)
ttk.Label(option_frame, text = "美白程度：").grid(row = 3, column = 0, padx=5)
ttk.Entry(option_frame, width = 5, textvariable = Whitening).grid(row = 3, column = 1, padx=5)
ttk.Label(option_frame, text = "磨皮程度：").grid(row = 4, column = 0, padx=5)
ttk.Entry(option_frame, width = 5, textvariable = Smoothing).grid(row = 4, column = 1, padx=5)
ttk.Label(option_frame, text = "瘦脸程度：").grid(row = 3, column = 2, padx=5)
ttk.Entry(option_frame, width = 5, textvariable = FaceLifting).grid(row = 3, column = 3, padx=5)
ttk.Label(option_frame, text = "大眼程度：").grid(row = 4, column = 2, padx=5)
ttk.Entry(option_frame, width = 5, textvariable = EyeEnlarging).grid(row = 4, column = 3, padx=5, pady=5)
tk.Button(main_window,text = "开\n始", width = 2, height = 3, relief = GROOVE, command = Beauty).grid(row = 3, column = 4, rowspan = 2, sticky = S)
ttk.Button(main_window,text = "提示", command = Tip).grid(row = 3, column = 5, sticky = S)
ttk.Button(main_window,text = "关于", command = About).grid(row = 4, column = 5, sticky = S)

main_window.mainloop()