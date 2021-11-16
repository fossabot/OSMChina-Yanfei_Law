import argparse
import re
from keqing-sword import PyOsm, BaseOsmModel

# 做一个所有rule的主入口，由它按照rulelist去寻找和执行各条rule，不用用户一个个去翻找

def main(args: argparse.Namespace):
    pyosm = PyOsm()
    try:
        pyosm.from_file(args.src)
    except FileNotFoundError:
        print('文件%s不存在' % args.src)

    for node in pyosm.node_dict.values():
        process(node)
    for way in pyosm.way_dict.values():
        process(way)
    for relation in pyosm.relation_dict.values():
        process(relation)
    pyosm.write(args.dst)
    if args.pause:
        input('\n按任意键退出…')


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '--src',
        default='src.osm',
        help='待处理文件路径'
    )
    argparser.add_argument(
        '--dst',
        default='dst.osm',
        help='处理结果路径'
    )
    argparser.add_argument(
        '--pause',
        default='yes',
        help='运行完成后暂停，yes or no'
    )

    main(argparser.parse_args())
