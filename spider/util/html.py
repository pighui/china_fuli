import re


def to_html(resp_bytes, charset='utf-8'):
    # 将http 响应的字节码数据转成文本的html
    html = None
    try:
        # 在Window10中utf-8-sig
        html = resp_bytes.decode(charset)
    except:
        try:
            if charset == 'utf-8':
                html = resp_bytes.decode('gb2312')
            else:
                html = resp_bytes.decode('utf-8')
        except:
            html = resp_bytes.decode('gbk')
    return html


def get_charset(content_type):
    # 从Content-Type的请求头的信息中提取charset字符集
    # 修复utf-8中的"-"不包含在\w中,要改成 "."
    charset = re.findall(r'charset=(.+)', content_type)
    if charset:
        charset = charset[0]
    else:
        charset = 'utf-8'
    return charset
