import urllib.request

urls = [
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgf16ilntmsgVjcHFYoF85XcQuVlcz5W1i2tlirbe0yUU06KLGx6xUbM1Zg7OwX8XqvzFswgk8nDW8hzGl47Zsyq_AtzKDTSNvQjm_n3bvNjtpubsDyExDmtd1",
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQWOs64Fy97ct3OYhs6UZx2hAFovNoqHJ7Jy-pWR8MmAx_2cCVeGRYUZLM6v1lW98Kpo0eRiJBYRjVBZMAgb9j9cidElom9BRcGutGOQlM44O2yssRKM1f8nx8tUQCEfejhUb41ZQZPD-uOzkaptj89bmBFNTWPyCayb121QOa4v4AdZlM",
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0pC-xoys8HoJzQCzyfwZDHiNV2CIsFNoadL1_3IqUmo2SPd2BOCraGqKeaUGfE4G2zq4O9HF9u5NqUDqgowOEpUPNBPnftJluD3Ln4a7G1UKcU3aeUDPRFonCbPPJu81tEnZDxElJBDSIqaaNvcMFoNAoIkkm2vSxHAUCY7dkdtw=",
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy2I-8Un7lOJ8sB7fHjzDB5a2QePWDXE2BILQGF5Vv8p9H_ap1gifP777oMaHOCZ9nT_oB0dUtDOjZMRefY6TmdMIaapd5t78NtA6M2PqNCdQe6IOHJGHVAe_HV_iZtUz8V4U8XJhki-5hzk2xkgfSKc3ED95tLMa5yKtY6hF6ns6pz1hM"
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}, method='HEAD')
        resp = urllib.request.urlopen(req)
        print("Final URL:", resp.geturl())
    except urllib.error.HTTPError as e:
        print("Redirect loc:", e.headers.get('Location'))
    except Exception as e:
        print("Err:", e)
