# coding=gbk
# author:��ţ
# datetime:2020/11/18 16:54

import os


def genSizeFile(fileName, fileSize):
    # file path
    filePath = "Data" + fileName + ".csv"
    text = "֣��ú���е���Źɷ����޹�˾(�������й�˾601717)ʼ����1958�꣬���й���һ̨Һѹ֧�ܵĵ����أ�ǰ��Ϊ֣��ú���е��(����ú̿��)���ǹ���\"һ��\"�ƻ��ص���Ŀ��1998�껮�����ʡú̿��ҵ����ֹ������ʲ�30��Ԫ�����ʲ�Լ6.6��Ԫ������9�������ֳ���������ռ�����Լ45��ƽ���ף�ӵ���ڸ�Ա��4000���ˣ�רҵ������Ա800���ˣ��߼�������Ա200���ˣ�6�����ܹ���������������ۼ�����֧���߶ȴ�0.55�׵�7�ף�֧��ǿ�ȴ�1600kN��16800kN�ĸ���Һѹ֧��11����ܡ���Ʒ�鲼ȫ�������ҵ���ţ������ڶ���˹��ӡ�ȡ�������ȹ��ҡ�"

    # ���ɹ̶���С���ļ�
    # date size
    ds = 0
    with open(filePath, "w", encoding="utf8") as f:
        while ds < fileSize:
            f.write(text)
            f.write("\n")
            ds = os.path.getsize(filePath)
    # print(os.path.getsize(filePath))


# start here.
genSizeFile("test-2G", 2*1024 * 1024 * 1024)
