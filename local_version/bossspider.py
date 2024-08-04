#!/usr/bin/env python
# coding=utf-8
import time
import requests
from data_define import cookie

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'cache-control': 'no-cache',
    'cookie': cookie,
    # 'upgrade-insecure-requests': '1', 不知道有啥用
    'user-agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit'
                  r'/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
}

# 定义BOSS消息中的字段
zp_data = "zpData"
data = "data"
job_status = "jobStatus"
encrypt_id = "encryptId"


class BossSpider:
    # 从自己的工作列表中获取工作信息
    def request_get_job_id(self):
        request_result = requests.get(
            r"https://www.zhipin.com/wapi/zpjob/job/data/list?position=0&type=0&searchStr=&comId=&tagIdStr=&"
            r"page=1&_=1722780550499",
            headers=headers).json()
        print(request_result)
        job_data_list = request_result[zp_data][data]
        job_ids_opened = []
        for job in job_data_list:
            if job[job_status] == 0:
                job_ids_opened.append(job[encrypt_id])
        return job_ids_opened

    # 在推荐牛人页面筛选结果
    def request_get_candidates(self, job_id):
        age_max = 28
        url = f"https://www.zhipin.com/wapi/zpjob/rec/geek/list?age=16,{age_max}&major=0&activation=0&gender=0&recentNotView=0&exchangeResumeWithColleague=0&school=0&switchJobFrequency=0&experience=0&degree=203,204&salary=0&intention=701,704&jobId={job_id}&page=1&coverScreenMemory=1&cardType=0"
        request_result = requests.get(url, headers=headers).json()
        print(request_result)

    # 向牛人发送简历申请
    def request_resume_to_job_seeker(self, uid):
        request_resume_result = requests.get(
            'https://www.zhipin.com/chat/requestResume.json?to=' + str(uid) + '&_=' + str(
                int(round(time.time() * 1000))), headers=headers).json()
        print(request_resume_result)

    # 接受牛人简历
    def accept_resume_of_job_seeker(self, uid):
        accept_resume_result = requests.get(
            'https://www.zhipin.com/chat/acceptResume.json?to=' + str(uid) + '&mid=' + str(
                38834193982) + '&aid=41&action=0&extend=&_=' + str(int(round(time.time() * 1000))),
            headers=headers).json()
        print(accept_resume_result)


if __name__ == '__main__':
    a = BossSpider()
    tmp = a.request_get_job_id()
    print(tmp)
    for i in tmp:
        a.request_get_candidates(i)
