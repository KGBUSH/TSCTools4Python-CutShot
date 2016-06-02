# encoding: utf-8


from Util.ExtractUtil import *
from Util.XMLUtil import *
from Util.WindowBuilder import *
from Entity.TimeWindow import *
from Entity.GlobalValue import *

import shutil


if __name__ == "__main__":
    # os.chdir("D:\\Develop\\workspace\\TSCTools4Python")
    project_path = GLOBAL_projectpath

    print 'GLOBAL_projectpath: ', GLOBAL_projectpath
    print 'GLOBAL_xmlpath: ',GLOBAL_xmlpath
    unsortedDanmakuList = XMLUtil.Extract_Danmakulist_Fromfile(GLOBAL_xmlpath)
    print 'GLOBAL_xmlpath: ',GLOBAL_xmlpath


    sorted_danmakuList = ExtractUtil.SortDanmakuList(unsortedDanmakuList)
    for danma in sorted_danmakuList:
        print danma.video_second, danma.content

    userIDList = ExtractUtil.ExtractUser(sorted_danmakuList)


    windowBuilder = WindowBuilder(GLOBAL_WINDOW_SIZE, GLOBAL_WINDOW_SLIDE_STEP)
    timeWindowClipList = windowBuilder.buildWindows(sorted_danmakuList)

    # 先清空GLOBAL_windowsTxtpath文件夹， 再创建
    if os.path.isdir(GLOBAL_windowsTxtpath):
        shutil.rmtree(GLOBAL_windowsTxtpath, True)
    os.makedirs(GLOBAL_windowsTxtpath)

    for timeWindow in timeWindowClipList:
        timeWindow.output()



    # # 测试TimeWindow.buildFromDanmaku
    # timeWindow = TimeWindow(1, 0, 10000)
    # timeWindow.buildFormDamaku(sorted_danmakuList)
    # print '\n\n'
    #
    # for danma in sorted_danmakuList:
    #     if danma.content == '无限小电视'.decode('utf-8'):
    #         sorted_danmakuList.remove(danma)
    #         break
    # for danma in sorted_danmakuList:
    #     print danma.video_second, danma.content