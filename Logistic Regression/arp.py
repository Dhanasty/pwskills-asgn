import gdown

files = [
    {"id": 1, "url": "https://drive.google.com/file/d/1OjU2oOCoRPa3YM7Ziz44UdofEa1yiuFt"},
    {"id": 2, "url": "https://drive.google.com/file/d/1G9_qh8nTElpTRt30KVf3ueOMOEfIxWqu/view"},
    {"id": 3, "url": "https://drive.google.com/file/d/1A3k8whNd-qAgirixSDIxcq81d100SYRi/view"},
    {"id": 4, "url": "https://drive.google.com/file/d/12yPGOE_xCy-lpx1KMxrkV0M8WMs11-Kh/view"},
    {"id": 5, "url": "https://drive.google.com/file/d/1ha1d0CwtlzDwbudyMLjIvC-IrMGdk-YR/view"},
    {"id": 6, "url": "https://drive.google.com/file/d/1XSRs6NfpgVKWvDfXn3LkJYPgFfXMB3Ij/view"},
    {"id": 7, "url": "https://drive.google.com/file/d/1JdvmpmDxdRVQ0TcNh3c4FROib0Vl3I08/view"},
    {"id": 8, "url": "https://drive.google.com/file/d/1NTHxb11DDAz8TweZNpki-nv786RVE8NC/view"},
    {"id": 9, "url": "https://drive.google.com/file/d/1e29ezXnZFvrNfUd2MaX7id1DwR1rKXdu/view"},
    {"id": 10, "url": "https://drive.google.com/file/d/1OKeAs4tA44toEiJ1dfrtY5fmJHPsDBg3/view"},
    {"id": 11, "url": "https://drive.google.com/file/d/15YNYOGqI4GxXqAeonVWQ6sQlkks8aM7g/view"},
    {"id": 12, "url": "https://drive.google.com/file/d/1nsDQUdMHyZCb94_ja5GwNjLDqGNGOkdK/view"},
    {"id": 13, "url": "https://drive.google.com/file/d/1FoolFZv0zt2q0yY3t8S1vz-Ki3ehOgDK/view"},
    {"id": 14, "url": "https://drive.google.com/file/d/1mwactTgMv8mMUGonrrM41mzIvfKsHq02/view"},
    {"id": 15, "url": "https://drive.google.com/file/d/1Bc2tfrpyXA124_jixRngoYULtUZ085s9/view"},
    {"id": 16, "url": "https://drive.google.com/file/d/1QpP07BS0B538TP_EV2BH7qJv6ZftWG9q/view"},
    {"id": 17, "url": "https://drive.google.com/file/d/1goC1zw2eVN3CLfl006srSQi9VSIbwp2L/view"},
    {"id": 18, "url": "https://drive.google.com/file/d/1Z6sEvhWJXJSgyHBaww0xIRtAhZGTczS_/view"},
    {"id": 19, "url": "https://drive.google.com/file/d/1PvGqj4BMB8TyE-rGh17RHCJe8qqpucoB/view"},
    {"id": 20, "url": "https://drive.google.com/file/d/1EnJSlNneQWpFTfdFXSvoSYAcXgakXJJg/view"},
    {"id": 21, "url": "https://drive.google.com/file/d/1v6k7x5ebXbsZvPXO5AWIM3jrLxg1Zw3e/view"},
    {"id": 22, "url": "https://drive.google.com/file/d/1pD5a-q4bTq6ST1sxqiAqLUqbJdCVqHbU/view"},
    {"id": 23, "url": "https://drive.google.com/file/d/1msL9o1-a3ARfiPzY1u38LVbXWR7ptb35/view"},
    {"id": 24, "url": "https://drive.google.com/file/d/1QcUq_BatU6MjJwsGw5ZelLm_Gkczi4U6/view"},
    {"id": 25, "url": "https://drive.google.com/file/d/1wwXoHpI_IYHoVpqQSm8eT2vleZ1-mhaG/view"},
    {"id": 26, "url": "https://drive.google.com/file/d/1smRs4eAYFicvSUaTH1Rg3SrDNCsOEecn/view"},
    {"id": 27, "url": "https://drive.google.com/file/d/1r23gZWNyg85h6GULibmwTWx6UkisOQW0/view"},
    {"id": 28, "url": "https://drive.google.com/file/d/1j8qUbpegfue229w3d8n7JYTufwVKW5cH/view"},
    {"id": 29, "url": "https://drive.google.com/file/d/12tYoAqWFACK1m4_D0_OEnss8ZQbUVq6B/view"},
    {"id": 30, "url": "https://drive.google.com/file/d/12McUAXH9yu1ygJt7HQyj3tOhUnT0_-yg/view"},
    {"id": 31, "url": "https://drive.google.com/file/d/1sb1QGbcklqtCm0UiWdu12hYjjrtBg0jW/view"},
    {"id": 32, "url": "https://drive.google.com/file/d/1tbG4OHi-kPos05NklfXzou-tUd-sat9-/view"},
    {"id": 33, "url": "https://drive.google.com/file/d/1BhlH8O7E_2ZtxlA_BuP1gIZvrBHczngK/view"},
    {"id": 34, "url": "https://drive.google.com/file/d/1E2PZoA5R64npMztxKRuLGzqYk9Ovl53d/view"},
    {"id": 35, "url": "https://drive.google.com/file/d/1iynQJ_1ZYMYS-V3mThtMPFsqarhVI08m/view"},
]

for i in files:
    url = i['url']
    output = str(i['id'])+".pdf"
    gdown.download(url, output,fuzzy=True)