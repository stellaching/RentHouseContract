暫時只能用在本地私鏈
payRent,payDeposit因未知問題介面上暫不能使用，可以在solidity執行

1.先把house.sol在solidity部署至本地私鏈
2.打開final.py編輯
3.把118行的priv_url改成已部署智能合約的本地私鏈
4.123行的address = web3.toChecksumAddress('<已部署的智能合約地址>')
5.128行的text='<已部署的智能合約地址>'(可以不用改，不會影響運行)
6.跑final.py前請先把IPFS的客戶端打開及讓私鏈開始跑
7.cmd  cd <'final.py的放置位置'>
8.cmd  python final.py