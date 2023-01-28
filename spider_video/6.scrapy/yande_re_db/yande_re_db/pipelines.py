# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os

# class YandeReDbPipeline:
#
#     def open_spider(self, spider):
#         if not os.path.exists('./source/public'):
#             os.makedirs('./source/public')
#     def process_item(self, item, spider):
#         filename = './source/public'+item['name']+'.jpeg'
#         with open(filename, 'rb') as f:
#             f.write(item['pic_data'])
#             print(filename+'保存完毕')
#
#         return item
import scrapy
from scrapy.pipelines.images import ImagesPipeline
class ImagePipeline(ImagesPipeline):

    # 重写父类方法，获取图片响应对象
    def get_media_requests(self, item, info):
        # print(scrapy.Request(item['src'])+'重写')
        yield scrapy.Request(item['src'])

    # 重写父类方法，获取图片存储路径
    def file_path(self, request, response=None, info=None, *, item=None):
        imgName = request.url.split('/')[-2] + '.jpeg'
        # print(imgName)
        return imgName

    # 重写父类方法，返回item给下一个管道
    def item_completed(self, results, item, info):
        return item
