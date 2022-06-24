import ipfshttpclient
import tkinter
from tkinter import filedialog
import json
from web3 import Web3

#取得錢包的nonce值
def getNonce():
    addr=str(entry.get())
    nonce = web3.eth.getTransactionCount(addr)
    return nonce
#設定交易參數 
def setTxp(n):
    noc=int(getNonce())
    addr=str(entry.get())
    tx_param={
        'gas': 1000000,
        'value': n * (10 ** 18),
        'gasPrice': web3.toWei('2', 'gwei'),
        'from': addr,
        'nonce': noc
    }
    return tx_param
#上傅檔案至IPFS，接收回傳值
def uploadc():
    file_path=filedialog.askopenfilename()
    if not file_path:
        label['text']='upload falied'
    else :
        res = str(client.add(file_path))
        fs='Hash'
        fe='Size'
        fsp=res.find(fs)+8
        ha=res[fsp:]
        fep=ha.find(fe)-4
        has=ha[:fep]
        label['text']=has
        ctext.set(has)
#查詢押﹑租金﹑契約地址    
def getData():
    label7['text']=contract.functions.getData().call()
#設定合約的押﹑租金﹑契約地址 
def setData():
    r=int(entry3.get())
    d=int(entry4.get())
    c=str(entry5.get())
    tx_param=setTxp(0)
    sd=contract.functions.setData(r,d,c).buildTransaction(tx_param)
    pk=str(entry2.get())
    signed_txn = web3.eth.account.signTransaction(sd,pk)
    txReport = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    label7['text']=txReport.hex()
#付押金，先用private key簽署合約，再用 sendRawTransaction()將簽署完的合約送出
def payd():
    v=int(entry6.get())
    tx_param=setTxp(v)
    sd=contract.functions.payDeposit().buildTransaction(tx_param)
    pk=str(entry2.get())
    signed_txn = web3.eth.account.signTransaction(sd,pk)
    txReport = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    label7['text']=txReport.hex()
 #付租金   
def payr():
    v=int(entry6.get())
    tx_param=setTxp(v)
    sd=contract.functions.payRent().buildTransaction(tx_param)
    pk=str(entry2.get())
    signed_txn = web3.eth.account.signTransaction(sd,pk)
    txReport = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    label7['text']=txReport.hex()
#屋主設定已簽署的契約    
def signO():
    sc=str(entry5.get())
    tx_param=setTxp(0)
    sd=contract.functions.signcontractO(sc).buildTransaction(tx_param)
    pk=str(entry2.get())
    signed_txn = web3.eth.account.signTransaction(sd,pk)
    txReport = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    label7['text']=txReport.hex()
#租客設定已簽署的契約        
def signT():
    sc=str(entry5.get())
    tx_param=setTxp(0)
    sd=contract.functions.signcontractT(sc).buildTransaction(tx_param)
    pk=str(entry2.get())
    signed_txn = web3.eth.account.signTransaction(sd,pk)
    txReport = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    label7['text']=txReport.hex()
 #查詢已簽署的契約  
def getDT():
    label7['text']=contract.functions.getDataForT().call()
    
def getDO():
    label7['text']=contract.functions.getDataForO().call()
#查詢合約存有的金額
def getB():
    label7['text']=contract.functions.getBalance().call()
#把合約的錢轉給屋主
def withD():
    tx_param=setTxp(0)
    sd=contract.functions.withdraw().buildTransaction(tx_param)
    pk=str(entry2.get())
    signed_txn = web3.eth.account.signTransaction(sd,pk)
    txReport = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    label7['text']=txReport.hex()
#返還押金
def returnd():
    tx_param=setTxp(0)
    sd=contract.functions.returnDeposit().buildTransaction(tx_param)
    pk=str(entry2.get())
    signed_txn = web3.eth.account.signTransaction(sd,pk)
    txReport = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    label7['text']=txReport.hex()
 
window=tkinter.Tk()
window.title('Rent Contract')
window.geometry("800x600")#設定視窗大小
priv_url="http://127.0.0.1:2545" #設定要連接的區塊鏈
web3 = Web3(Web3.HTTPProvider(priv_url))
client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')#連接IPFS

abi = json.loads('[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdraw","type":"event"},{"inputs":[],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getData","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"string","name":"","type":"string"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getDataForO","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"string","name":"","type":"string"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getDataForT","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"string","name":"","type":"string"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address payable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"payDeposit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"payRent","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"rdeposit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"returnDeposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"r","type":"uint256"},{"internalType":"uint256","name":"rd","type":"uint256"},{"internalType":"string","name":"rc","type":"string"}],"name":"setData","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"sc","type":"string"}],"name":"signcontractO","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"sc","type":"string"}],"name":"signcontractT","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"tenantAddr","outputs":[{"internalType":"address payable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
address = web3.toChecksumAddress("0xDd8655F32C59e1706D4c362150F497B0F8c1e2C1")
contract = web3.eth.contract(address=address,abi=abi)

label4=tkinter.Label(window,text='You are connecting to Contract:')
label4.pack()
label5=tkinter.Label(window,text='0xDd8655F32C59e1706D4c362150F497B0F8c1e2C1')
label5.pack()
button=tkinter.Button(window,text='upload to IPFS',command=uploadc)
button.pack()
label2 = tkinter.Label(window,text="IPFS hash:")
label2.pack()
label = tkinter.Label(window,text="")
label.pack()
label3=tkinter.Label(window,text='Your address:')
label3.pack()
entry=tkinter.Entry(window,width=50)
entry.pack() #entry.get()
label6=tkinter.Label(window,text='Your private key:')
label6.pack()
entry2=tkinter.Entry(window,width=50)
entry2.pack() 
button2=tkinter.Button(window,text='Get Contract Data',command=getData)
button2.pack()
label7=tkinter.Label(window,text='')
label7.pack()

entry3=tkinter.Entry(window,width=30)
entry3.insert(0, "Rent")
entry3.pack() 
entry4=tkinter.Entry(window,width=30)
entry4.insert(0, "Desposit")
entry4.pack() 
ctext = tkinter.StringVar()
ctext.set("Contract Address")
entry5=tkinter.Entry(window,width=50,textvariable = ctext)
entry5.pack() 
button3=tkinter.Button(window,text='Set Contract Data',command=setData)
button3.pack()
entry6=tkinter.Entry(window,width=30)
entry6.insert(0, "value")
entry6.pack() 
button4=tkinter.Button(window,text='PayDesposit',command=payd)
button4.pack()
button5=tkinter.Button(window,text='PayRent',command=payr)
button5.pack()
button10=tkinter.Button(window,text='Signed Contract For Owner',command=signO)
button10.pack()
button11=tkinter.Button(window,text='Signed Contract For Tenant',command=signT)
button11.pack()
#button6=tkinter.Button(window,text='Get Signed Contract For Owner',command=getDO)
#button6.pack()
#button7=tkinter.Button(window,text='Get Signed Contract For Tenant',command=getDT)
#button7.pack()
button8=tkinter.Button(window,text='Get Contract Balance',command=getB)
button8.pack()
button9=tkinter.Button(window,text='WithDraw',command=withD)
button9.pack()
button12=tkinter.Button(window,text='Return Deposit',command=returnd)
button12.pack()
window.mainloop()