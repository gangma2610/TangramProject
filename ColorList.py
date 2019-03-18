import collections
import numpy as np

def getColorList(id):  # flag=1表示模板颜色匹配
    """颜色字典"""
    dict = collections.defaultdict(list)
    # 黑色
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 46])
    color_list = []
    color_list.append(lower_black)
    color_list.append(upper_black)
    dict['black'] = color_list

    # 灰色
    lower_gray = np.array([0, 0, 46])
    upper_gray = np.array([180, 43, 220])
    color_list = []
    color_list.append(lower_gray)
    color_list.append(upper_gray)
    dict['gray'] = color_list

    # 白色
    if id == 0:
        lower_white = np.array([0, 0, 221])
        upper_white = np.array([180, 30, 255])
        color_list = []
        color_list.append(lower_white)
        color_list.append(upper_white)
        dict['white'] = color_list

    if id == 1:
        lower_pink = np.array([160, 86, 178])
        upper_pink = np.array([180, 165, 255])
        color_list = []
    else:
        # 粉色
        # H:340-360 S:30%-54% V:70%-100%
        lower_pink = np.array([165, 76, 191])
        upper_pink = np.array([180, 153, 255])
        color_list = []
    color_list.append(lower_pink)
    color_list.append(upper_pink)
    dict['pink'] = color_list

    # 红色
    # H:0-10 S: 65%-100% V:30%-100%
    lower_red = np.array([0, 165, 80])
    upper_red = np.array([3, 255, 255])
    # H:345-360 S:50%-100% V: 45%-100%
    lower_red2 = np.array([170, 140, 115])
    upper_red2 = np.array([180, 255, 255])
    color_list = []
    color_list.append(lower_red)
    color_list.append(upper_red)
    color_list.append(lower_red2)
    color_list.append(upper_red2)
    dict['red'] = color_list

    # 橙色
    if id:
        lower_orange = np.array([6, 43, 46])
        upper_orange = np.array([24, 255, 255])
    else:
        # H:0-6,S:45%-85%,V:60%-100%
        lower_orange = np.array([0, 115, 153])
        upper_orange = np.array([12, 217, 255])
    color_list = []
    color_list.append(lower_orange)
    color_list.append(upper_orange)
    dict['orange'] = color_list

    # 黄色
    if id:
        lower_yellow = np.array([25, 43, 46])
        upper_yellow = np.array([34, 255, 255])
    else:
        lower_yellow = np.array([24, 43, 180])
        upper_yellow = np.array([33, 255, 255])
    color_list = []
    color_list.append(lower_yellow)
    color_list.append(upper_yellow)
    dict['yellow'] = color_list

    # 绿色
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([77, 255, 255])
    color_list = []
    color_list.append(lower_green)
    color_list.append(upper_green)
    dict['green'] = color_list

    # 蓝色
    lower_blue = np.array([100, 102, 46])
    upper_blue = np.array([124, 255, 255])
    color_list = []
    color_list.append(lower_blue)
    color_list.append(upper_blue)
    dict['blue'] = color_list

    # 紫色
    if id:
        lower_purple = np.array([125, 43, 46])
        upper_purple = np.array([159, 255, 255])
    else:
        # H:270-350 S:30%-54%,V:25%-86%
        lower_purple = np.array([135, 65, 64])
        upper_purple = np.array([175, 138, 220])

        # lower_purple = np.array([135, 76, 64])
        # upper_purple = np.array([180, 138, 204])

    color_list = []
    color_list.append(lower_purple)
    color_list.append(upper_purple)
    dict['purple'] = color_list

    return dict