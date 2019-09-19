from flask import jsonify, request
from app.forms.book import SearchFrom

from helper import is_isbn_or_key
from yushu_book import YuShuBook
from . import web
# 蓝图 blueprint


@web.route('/book/search')
def search(q, page):
    """
    q:普通关键字 or isbn(一组数字）--如何鉴别
    page:strat count
    ?q=金庸&page=1
    :return:
    """
    form = SearchFrom(request.args)
    if form.validate():
        q = form.q.data
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
        return jsonify(result)
    else:
        return jsonify({'msg':'参数校验失败'})




