
import requests
from bs4 import BeautifulSoup


def main():

    request_url = 'https://www.zhipin.com/job_detail/?query=%E9%87%8F%E5%8C%96%E4%BA%A4%E6%98%93&city=101010100&industry=&position='
    headers = {
        'Host': 'www.zhipin.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
        'Accept' :'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.zhipin.com/?sid=sem_pz_bdpc_dasou_title',
        'Connection': 'keep-alive',
        'Cookie': '__a=9226485.1520309455.1520389173.1562747836.10.4.2.2; lastCity=101010100; sid=sem_pz_bdpc_dasou_title; __c=1562747836; __g=sem_pz_bdpc_dasou_title; __l=l=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&r=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fDIFkY0IWPB0KZEgsALCzNI00000Kd7ZNC00000UtNsd3.THdBULP1doZA80K85ydEUhkGUhNxP7qbusK15yR4nHRsmHNbnj0sPjRYuhR0IHdKwWb3P1DvnDmknWFDnRc4PDc4fbF7fbfYPDm4f1n4nsK95gTqFhdWpyfqn1czPjmsPjnYrausThqbpyfqnHm0uHdCIZwsT1CEQLILIz4lpA-spy38mvqVQ1q1pyfqTvNVgLKlgvFbTAPxuA71ULNxIA-YUAR0mLFW5Hm1P1n%26tpl%3Dtpl_11534_19713_15764%26l%3D1511867677%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253DBoss%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E6%252588%252591%2525E8%2525A6%252581%2525E8%2525B7%25259F%2525E8%252580%252581%2525E6%25259D%2525BF%2525E8%2525B0%252588%2525EF%2525BC%252581%2526xp%253Did(%252522m3224604348_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D8%26ie%3Dutf-8%26f%3D8%26tn%3Dmonline_4_dg%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%26oq%3Dboss%2525E7%25259B%2525B4%2525E8%252581%252598%26rqlang%3Dcn%26bs%3Dboss%25E7%259B%25B4%25E8%2581%2598&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1562747836; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1562747851; _uab_collina=156274783600215086243045',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }

    result = requests.get(request_url, headers=headers)
    print(result.content.decode('utf-8'))


if __name__ == '__main__':
    main()
