from requests_html import HTMLSession


class BaiDuImg:
    session = HTMLSession()
    img_url_regex = '"thumbURL":"{}",'
    url = ''
    img_url_list = []

    def get_search(self):
        search = input('请输入你要搜索的图片')
        # 有点点偷懒参数没有好好分析全,只对关键参数处理
        self.url = f'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={search}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word={search}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&rn=30&gsm='

    def get_img_url_list(self):
        '&pn=30000'
        pn = 0
        try:
            while True:
                res = self.session.get(f'{self.url}&pn={pn}')
                print(res.json()['bdIsClustered'])
                if res.json()['bdIsClustered'] == '2':
                    break
                else:
                    pn += 30
                    for dic in res.json()['data']:
                        img_url = dic.get('thumbURL')
                        if img_url:
                            self.img_url_list.append(img_url)
        except Exception as e:
            pass

    def save_img(self):
        mun = 0
        for url in self.img_url_list:
            mun += 1
            # 访问图片链接
            response = self.session.get(url)
            # 保存二进制并保存至本地
            # 路径自己改
            with open(f'E:\\python\\spider\\picture\\第{mun}张.jpg', 'wb') as fw:
                fw.write(response.content)
                print(f'第{mun}张保存本地完毕')

    def run(self):
        self.get_search()
        self.get_img_url_list()
        print(len(self.img_url_list))
        self.save_img()


if __name__ == '__main__':
    baidu = BaiDuImg()
    baidu.run()