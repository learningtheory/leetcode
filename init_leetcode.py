# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/7/21 下午3:15
"""
#
import json
import requests

import os

from multiprocessing.pool import ThreadPool

path = os.path.dirname(__file__)

url = "https://leetcode-cn.com/graphql"

pool = ThreadPool(10)

headers = {
    'content-type': "application/json",
    'cookie': "_uab_collina=153201079094909515475695; gr_user_id=5e53e79d-a32a-4e74-ad5a-ea9258e2e920; csrftoken=SLeQ8Ln9mFEzLn2RqbOIwCow5UnMwxWpYb1yRP0qqbbOkVaoUggUjmjt6UvaMq5a; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1532010801,1532057578,1532057875,1532157764; gr_session_id_a2873925c34ecbd2=0b68d19e-ebfb-4a49-b6f5-e285969f6351; gr_session_id_a2873925c34ecbd2_0b68d19e-ebfb-4a49-b6f5-e285969f6351=true; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1532157780",
    'x-csrftoken': "SLeQ8Ln9mFEzLn2RqbOIwCow5UnMwxWpYb1yRP0qqbbOkVaoUggUjmjt6UvaMq5a",
    'referer': "https://leetcode-cn.com/problemset/all/",
    'cache-control': "no-cache",
    'postman-token': "eb00e837-26fe-88a3-cafe-ff4923b578fe"
}

session = requests.session()


#
def getKeys():
    url = "https://leetcode-cn.com/graphql"
    #
    payload = "{\"operationName\":\"getQuestionTranslation\",\"variables\":{},\"query\":\"query getQuestionTranslation($lang: String) {  translations: allAppliedQuestionTranslations(lang: $lang) {  title   question {    questionId      __typename  titleSlug   }    __typename  }}\"}"

    keys = []
    response = session.post(url, data=payload, headers=headers)
    translations = response.json().get('data').get('translations')
    for item in translations:
        keys.append(item.get('question').get('titleSlug'))

    return keys


payload = "{\n\t\"operationName\": \"getQuestionDetail\",\n\t\"variables\": {\n\t\t\"titleSlug\": \"two-sum\"\n\t},\n\t\"query\": \"query getQuestionDetail($titleSlug: String!) {  isCurrentUserAuthenticated  question(titleSlug: $titleSlug) {    questionId titleSlug   questionFrontendId    questionTitle    translatedTitle    questionTitleSlug    content    translatedContent    difficulty    stats    allowDiscuss    contributors    similarQuestions    mysqlSchemas    randomQuestionUrl    sessionId    categoryTitle    submitUrl    interpretUrl    codeDefinition    sampleTestCase    enableTestMode    metaData    enableRunCode    enableSubmit    judgerAvailable    infoVerified    envInfo    urlManager    article    questionDetailUrl    libraryUrl    companyTags {      name      slug      translatedName      __typename    }    companyTagStats    topicTags {      name      slug      translatedName      __typename    }    __typename  } }\"\n}"

di = {
    'cpp': '.cpp',
    'java': '.java',
    'python': '.py',
    'python3': '.py',
    'c': '.c',
    'csharp': '.sln',
    'javascript': '.js',
    'ruby': '.rb',
    'swift': '.swift',
    'golang': '.go',
    'scala': '.scala',
    'kotlin': '.kt',
    'mysql': '.html',
    'bash': '.sh',
    'mssql': '.html',
    'oraclesql': '.html',
}


def content(lag: str, question):
    if lag.startswith('p'):
        return """\"\"\"
{}\"\"\"


""".format(question.get('content') + question.get('translatedContent') + question.get(
            'translatedContent')).encode('utf-8')
    elif lag in ['c', 'cpp', 'javascript', 'csharp', 'golang', 'swift']:
        return """/*
{}*/


""".format(question.get('content') + question.get('translatedContent') + question.get(
            'translatedContent')).encode('utf-8')
        pass
    elif lag in ['java', 'kotlin', 'scala']:
        return """/**
{}**/


""".format(question.get('content') + question.get('translatedContent') + question.get(
            'translatedContent')).encode('utf-8')
    elif lag == 'ruby':
        return """=begin
{}
=end


""".format(question.get('content') + question.get('translatedContent') + question.get(
            'translatedContent')).encode('utf-8')
    elif lag == 'bash':
        return """<!--
{}
-->


""".format(question.get('content') + question.get('translatedContent') + question.get(
            'translatedContent')).encode('utf-8')
    else:
        return """<html lang="zh-cn">
<head>
<meta charset="utf-8"/>
</head>
<body>
{}
</body>
</html>


        """.format(question.get('content') + question.get('translatedContent') + question.get(
            'translatedContent')).encode('utf-8')


def getPayLoad(key):
    return payload.replace('two-sum', key)


def doRequest(key):
    try:
        response = session.post(url, data=getPayLoad(key), headers=headers)
        question = response.json().get('data').get('question')
        cc = json.loads(question.get('codeDefinition'))
        print(key)
        print(question.get('questionId'))
        for item in cc:
            cls = 'html' if item.get('value') is None else item.get('value')
            file_name = path + '/{}/{}.{}({}){}'.format(cls, question.get('questionId'), question.get('questionTitle'),
                                                        question.get('translatedTitle'), di.get(cls))

            with open(file_name, 'wb') as file:
                dd = content(cls, question) + item.get('defaultCode').encode('utf-8')
                file.write(dd)
    except Exception as e:
        print(e)


# doRequest('koko-eating-bananas')

# 17096561260

def init_path(key):
    try:
        os.mkdir(path=os.path.dirname(__file__) + '/{}'.format(key))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # 创建文件夹
    [init_path(x) for x in list(di.keys())]

    # 获取数据
    pool.map(doRequest, getKeys())
