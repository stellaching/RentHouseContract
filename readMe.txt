暫時只能用在本地私鏈
payRent,payDeposit因未知問題介面上暫不能使用，可以在solidity執行
雖然在house.sol有設定各種失敗的回應，但嘗未弄清如何接收，失敗請到cmd查看

1.先把house.sol在solidity部署至本地私鏈
2.打開final.py編輯
3.把118行的priv_url改成已部署智能合約的本地私鏈
4.123行的address = web3.toChecksumAddress('<已部署的智能合約地址>')
5.128行的text='<已部署的智能合約地址>'(可以不用改，不會影響運行)
6.跑final.py前請先把IPFS的客戶端打開及讓私鏈開始跑
7.cmd  cd <'final.py的放置位置'>
8.cmd  python final.py

9.按upload上傳檔案至IPFS，回傳的Hash會出現在下面的contract address框
10.輸入錢包地址和密鑰
11.在Rent和Deposit輸入金額
12.按setContractData把Rent,Deposit,contract address傳給智能合約並設定
13.按getContractData查詢智能合約中的Rent,Deposit,contract address
14.更換錢包地址和密鑰，重覆9，按signContractForTenant，讓智能合約記錄作為租客的錢包地址
15.(嘗未成功)在value輸入金額，按payRent,payDeposit轉帳到智能合約
	暫代方案>到solidity執行payRent,payDeposit
16.按getContractBalance查詢智能合約現有存放的金額
17.按withDraw後，智能合約會扣除押金金額再把現有存放的金額轉給屋主的錢包地址
18.按returnDeposit把智能合約內的押金還給租客的錢包地址
