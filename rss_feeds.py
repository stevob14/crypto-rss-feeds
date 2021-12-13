import feedparser
import json

def parseRSS(rss_url):
    parsed_feed = feedparser.parse(rss_url)
    return parsed_feed

def getHeadlines(rss_url,key,allheadlines,allitems):
    feed = parseRSS(rss_url)
    for newsitem in feed['items']:
        if newsitem['title'] not in allheadlines:
            allheadlines.append(newsitem['title'])
            allitems.append([newsitem,key])
    return allheadlines,allitems

def get_rss():
    allheadlines = []
    allitems = []
    newsurls = {
    ('cointelegraph','cryptonews'):    'https://cointelegraph.com/rss',
    ('coingape','cryptonews'):  'https://coingape.com/feed',
    ('newsbtc','cryptonews') : 'https://www.newsbtc.com/feed/',
    ('ethereumworldnews','cryptonews') : 'https://ethereumworldnews.com/feed/',
    ('coindoo','cryptonews') : 'https://coindoo.com/feed/',
    ('news.bitcoin','cryptonews') : 'https://news.bitcoin.com/feed/',
    ('cryptovest','cryptonews'): 'https://cryptovest.com/feed',
    ('cryptopotato','cryptonews'): 'https://cryptopotato.com/feed',
    ('coindesk','cryptonews'):           'https://coindesk.com/feed',
    ('btcmanager','cryptonews'):  'https://btcmanager.com/feed',
    ('dailyhodl','cryptonews'): 'https://dailyhodl.com/feed',
    ('cryptobriefing','cryptonews'): 'https://cryptobriefing.com/rss',
    ('cryptoslate','cryptonews'): 'https://cryptoslate.com/rss',
    ('decrypt.co','cryptonews'): 'https://decrypt.co/rss',
    ('bitcoinist','cryptonews'): 'https://bitcoinist.com/feed',
    ('cryptoglobe','cryptonews'): 'https://www.cryptoglobe.com/feed',
    ('trustnodes','cryptonews'): 'https://www.trustnodes.com/feed',
    ('beincrypto','cryptonews'): 'https://beincrypto.com/feed',
    ('ambcrypto','cryptonews'): 'https://ambcrypto.com/feed',
    ('theblockcrypto','cryptonews'): 'https://www.theblockcrypto.com/rss.xml',
    ('cryptoninjas','cryptonews'): 'https://www.cryptoninjas.net/feed',
    ('zycrypto','cryptonews'): 'https://www.zycrypto.com/feed',
    ('bitcoinnews','cryptonews'): 'https://bitcoinnews.com/feed/',
    ('coinspeaker','cryptonews'): 'https://www.coinspeaker.com/feed',
    ('bravenewcoin','cryptonews'): 'https://bravenewcoin.com/rss/insights',
    ('coinscribble','cryptonews'): 'https://coinscribble.com/feed',
    ('coinbound.io','cryptonews'): 'https://coinbound.io/post-category/cryptocurrency/feed',
    ('u.today','cryptonews'): 'https://u.today/rss.php',
    ('paperblockchain','cryptonews'): 'https://paperblockchain.com/feed',
    ('r/bitcoin','cryptoreddit'):           'https://www.reddit.com/r/Bitcoin/top/.rss',
    ('r/CryptoCurrency','cryptoreddit'): 'https://www.reddit.com/r/CryptoCurrency/top/.rss',
    ('r/ethereum','cryptoreddit'): 'https://www.reddit.com/r/ethereum/top/.rss',
    ('r/ethtrader','cryptoreddit'): 'https://www.reddit.com/r/ethtrader/top/.rss',
    ('r/CryptoMarkets','cryptoreddit'): 'https://www.reddit.com/r/CryptoMarkets/top/.rss',
    ('r/bitcoin','itemnews'):'https://www.reddit.com/r/Bitcoin/.rss',
    ('r/ethereum','itemnews'):'https://www.reddit.com/r/ethereum.rss',
    ('r/binancecoin','itemnews'):'https://www.reddit.com/r/binance.rss',
    ('r/cardano','itemnews'):'https://www.reddit.com/r/cardano.rss',
    ('r/ripple','itemnews'):'https://www.reddit.com/r/ripple.rss',
    ('r/solana','itemnews'):'https://www.reddit.com/r/solana.rss',
    ('r/dogecoin','itemnews'):'https://www.reddit.com/r/dogecoin/.rss',
    ('r/terra-luna','itemnews'):'https://www.reddit.com/r/terraluna/.rss',
    ('r/shiba-inu','itemnews'):'https://www.reddit.com/r/SHIBArmy/.rss',
    ('r/uniswap','itemnews'):'https://www.reddit.com/r/Uniswap.rss',
    ('r/avalanche-2','itemnews'):'https://www.reddit.com/r/Avax.rss',
    ('r/litecoin','itemnews'):'https://www.reddit.com/r/litecoin/.rss',
    ('r/chainlink','itemnews'):'https://www.reddit.com/r/Chainlink/.rss',
    ('r/internet-computer','itemnews'):'https://www.reddit.com/r/dfinity/.rss',
    ('r/bitcoin-cash','itemnews'):'https://www.reddit.com/r/btc.rss',
    ('r/cosmos','itemnews'):'https://www.reddit.com/r/cosmosnetwork.rss',
    ('r/stellar','itemnews'):'https://www.reddit.com/r/stellar.rss',
    ('r/matic-network','itemnews'):'https://www.reddit.com/r/maticnetwork/.rss',
    ('r/internet-computer','itemnews'):'https://www.reddit.com/r/dfinity/.rss',
    ('r/vechain','itemnews'):'https://www.reddit.com/r/Vechain.rss',
    ('r/tron','itemnews'):'https://www.reddit.com/r/Tronix.rss',
    ('r/ethereum-classic','itemnews'):'https://www.reddit.com/r/EthereumClassic.rss',
    ('r/dai','itemnews'):'https://www.reddit.com/r/MakerDAO.rss',
    ('r/tezos','itemnews'):'https://www.reddit.com/r/tezos.rss',
    ('r/compound-ether','itemnews'):'https://www.reddit.com/r/compound/.rss',
    ('r/fantom','itemnews'):'https://www.reddit.com/r/FantomFoundation/.rss',
    ('r/hedera-hashgraph','itemnews'):'https://www.reddit.com/r/Hedera/.rss',
    ('r/monero','itemnews'):'https://www.reddit.com/r/monero.rss',
    ('r/staked-ether','itemnews'):'https://www.reddit.com/r/lidofinance/.rss',
    ('r/elrond-erd-2','itemnews'):'https://www.reddit.com/r/elrondnetwork/.rss',
    ('r/crypto-com-chain','itemnews'):'https://www.reddit.com/r/Crypto_com/.rss',
    ('r/eos','itemnews'):'https://www.reddit.com/r/eos.rss',
    ('r/ecash','itemnews'):'https://www.reddit.com/r/ecash/.rss',
    ('r/klay-token','itemnews'):'https://www.reddit.com/r/klaytn/.rss',
    ('r/aave','itemnews'):'https://www.reddit.com/r/Aave_Official.rss',
    ('r/quant-network','itemnews'):'https://www.reddit.com/r/QuantNetwork/.rss',
    ('r/iota','itemnews'):'https://www.reddit.com/r/Iota.rss',
    ('r/the-graph','itemnews'):'https://www.reddit.com/r/thegraph.rss',
    ('r/olympus','itemnews'):'https://www.reddit.com/r/olympusdao/.rss',
    ('r/waves','itemnews'):'https://www.reddit.com/r/Wavesplatform/.rss',
    ('r/neo','itemnews'):'https://www.reddit.com/r/NEO.rss',
    ('r/cdai','itemnews'):'https://www.reddit.com/r/compound.rss',
    ('r/leo-token','itemnews'):'https://www.reddit.com/r/bitfinex/.rss',
    ('r/harmony','itemnews'):'https://www.reddit.com/r/harmony_one/.rss',
    ('r/bittorrent-2','itemnews'):'https://www.reddit.com/r/Bittorrent/.rss',
    ('r/celsius-degree-token','itemnews'):'https://www.reddit.com/r/CelsiusNetwork.rss',
    ('r/maker','itemnews'):'https://www.reddit.com/r/MakerDAO.rss',
    ('r/thorchain','itemnews'):'https://www.reddit.com/r/thorchain.rss',
    ('r/helium','itemnews'):'https://www.reddit.com/r/HeliumNetwork.rss',
    ('r/dash','itemnews'):'https://www.reddit.com/r/dashpay.rss',
    ('r/decred','itemnews'):'https://www.reddit.com/r/decred.rss',
    ('r/havven','itemnews'):'https://www.reddit.com/r/synthetix_io/.rss',
    ('r/holotoken','itemnews'):'https://www.reddit.com/r/holochain.rss',
    ('r/theta-fuel','itemnews'):'https://www.reddit.com/r/theta_network/.rss',
    ('r/nem','itemnews'):'https://www.reddit.com/r/nem.rss',
    ('r/enjincoin','itemnews'):'https://www.reddit.com/r/EnjinCoin.rss',
    ('r/xdce-crowd-sale','itemnews'):'https://www.reddit.com/r/xinfin/.rss',
    ('r/icon','itemnews'):'https://www.reddit.com/r/helloicon.rss',
    ('r/zcash','itemnews'):'https://www.reddit.com/r/zec.rss',
    ('r/qtum','itemnews'):'https://www.reddit.com/r/Qtum.rss',
    ('r/dydx','itemnews'):'https://www.reddit.comr/dydxprotocol/.rss',
    ('r/yearn-finance','itemnews'):'https://www.reddit.com/r/yearn_finance/.rss',
    ('r/iostoken','itemnews'):'https://www.reddit.com/r/IOStoken/.rss',
    ('r/huobi-token','itemnews'):'https://www.reddit.com/r/huobi/.rss',
    ('r/zilliqa','itemnews'):'https://www.reddit.com/r/zilliqa/.rss',
    ('r/mina-protocol','itemnews'):'https://www.reddit.com/r/MinaProtocol/.rss',
    ('r/telcoin','itemnews'):'https://www.reddit.com/r/Telcoin/.rss',
    ('r/ravencoin','itemnews'):'https://www.reddit.com/r/Ravencoin.rss',
    ('r/basic-attention-token','itemnews'):'https://www.reddit.com/r/BATProject.rss',
    ('r/decentraland','itemnews'):'https://www.reddit.com/r/decentraland.rss',
    ('r/safemoon','itemnews'):'https://www.reddit.com/r/SafeMoon/.rss',
    ('r/republic-protocol','itemnews'):'https://www.reddit.com/r/republicprotocol/.rss',
    ('r/renbtc','itemnews'):'https://www.reddit.com/r/RenProject/.rss',
    ('r/nexo','itemnews'):'https://www.reddit.com/r/Nexo/.rss',
    ('r/siacoin','itemnews'):'https://www.reddit.com/r/siacoin.rss',
    ('r/kucoin-shares','itemnews'):'https://www.reddit.com/r/kucoin.rss',
    ('r/bancor','itemnews'):'https://www.reddit.com/r/Bancor.rss',
    ('r/0x','itemnews'):'https://www.reddit.com/r/0xProject/.rss',
    ('r/zencash','itemnews'):'https://www.reddit.com/r/Horizen.rss',
    ('r/audius','itemnews'):'https://www.reddit.com/r/audius/.rss',
    ('r/ontology','itemnews'):'https://www.reddit.com/r/OntologyNetwork/.rss',
    ('r/compound-usdt','itemnews'):'https://www.reddit.com/r/Compound.rss',
    ('r/digibyte','itemnews'):'https://www.reddit.com/r/Digibyte.rss',
    ('r/nano','itemnews'):'https://www.reddit.com/r/nanocurrency.rss',
    ('r/liquity-usd','itemnews'):'https://www.reddit.com/r/Liquity/.rss',
    ('r/iotex','itemnews'):'https://www.reddit.com/r/IoTeX.rss',
    ('r/polymath','itemnews'):'https://www.reddit.com/r/PolymathNetwork/.rss',
    ('r/skale','itemnews'):'https://www.reddit.com/r/SKALEnetwork/.rss',
    ('r/swissborg','itemnews'):'https://www.reddit.com/r/swissborg/.rss',
    ('r/golem','itemnews'):'https://www.reddit.com/r/GolemProject.rss',
    ('r/constellation-labs','itemnews'):'https://www.reddit.com/r/constellation/.rss',
    ('r/dent','itemnews'):'https://www.reddit.com/r/dent/.rss',
    ('r/wax','itemnews'):'https://www.reddit.com/r/WAX_io.rss',
    ('r/moonriver','itemnews'):'https://www.reddit.com/r/moonbeam/.rss',
    ('r/fetch-ai','itemnews'):'https://www.reddit.com/r/FetchAI_Community/.rss',
    ('r/rocket-pool','itemnews'):'https://www.reddit.com/r/rocketpool.rss',
    ('r/loopring','itemnews'):'https://www.reddit.com/r/loopringorg/.rss',
    ('r/gnosis','itemnews'):'https://www.reddit.com/r/gnosisPM.rss',
    ('r/lisk','itemnews'):'https://www.reddit.com/r/Lisk.rss',
    ('r/ergo','itemnews'):'https://www.reddit.com/r/ergonauts/.rss',
    ('r/livepeer','itemnews'):'https://www.reddit.com/r/livepeer.rss',
    ('r/bitcoin-diamond','itemnews'):'https://www.reddit.com/r/Bitcoin-Diamond/.rss',
    ('r/digitalbits','itemnews'):'https://www.reddit.com/r/DigitalBitsOrg/.rss',
    ('r/coti','itemnews'):'https://www.reddit.com/r/cotinetwork.rss',
    ('r/pirate-chain','itemnews'):'https://www.reddit.com/r/piratechain.rss',
    ('r/wink','itemnews'):'https://www.reddit.com/r/WINk_org/.rss',
    ('r/nervos-network','itemnews'):'https://www.reddit.com/r/NervosNetwork/.rss',
    ('r/energy-web-token','itemnews'):'https://www.reddit.com/r/EnergyWeb/.rss',
    ('r/medibloc','itemnews'):'https://www.reddit.com/r/MediBloc.rss',
    ('r/radio-caca','itemnews'):'https://www.reddit.com/r/RadioCacaNFT.rss',
    ('r/trust-wallet-token','itemnews'):'https://www.reddit.com/r/trustapp/.rss',
    ('r/injective-protocol','itemnews'):'https://www.reddit.com/r/injective/.rss',
    ('r/persistence','itemnews'):'https://www.reddit.com/r/PersistenceOne/.rss',
    ('r/vectorspace','itemnews'):'https://www.reddit.com/r/VectorspaceAI/.rss',
    ('r/xyo-network','itemnews'):'https://www.reddit.com/r/XYONetwork/.rss',
    ('r/verge','itemnews'):'https://www.reddit.com/r/vergecurrency.rss',
    ('r/seth','itemnews'):'https://www.reddit.com/r/synthetix_io.rss',
    ('r/vethor-token','itemnews'):'https://www.reddit.com/r/Vechain/.rss',
    ('r/pundi-x','itemnews'):'https://www.reddit.com/r/PundiX/.rss',
    ('r/orbs','itemnews'):'https://www.reddit.com/r/ORBS_Network/.rss',
    ('r/status','itemnews'):'https://www.reddit.com/r/statusim/.rss',
    ('r/ardor','itemnews'):'https://www.reddit.com/r/Ardor/.rss',
    ('r/lukso-token','itemnews'):'https://www.reddit.com/r/lukso/.rss',
    ('r/electroneum','itemnews'):'https://www.reddit.com/r/Electroneum.rss',
    ('r/ocean-protocol','itemnews'):'https://www.reddit.com/r/oceanprotocol/.rss',
    ('r/civic','itemnews'):'https://www.reddit.com/r/civicplatform.rss',
    ('r/akash-network','itemnews'):'https://www.reddit.com/r/akashnetwork/.rss',
    ('r/velas','itemnews'):'https://www.reddit.com/r/Velas/.rss',
    ('r/conflux-token','itemnews'):'https://www.reddit.com/r/Conflux_Network/.rss',
    ('r/unibright','itemnews'):'https://www.reddit.com/r/Unibright/.rss',
    ('r/asd','itemnews'):'https://www.reddit.com/r/Ascendex/.rss',
    ('r/band-protocol','itemnews'):'https://www.reddit.com/r/bandprotocol.rss',
    ('r/singularitynet','itemnews'):'https://www.reddit.com/r/SingularityNetsub/.rss',
    ('r/dodo','itemnews'):'https://www.reddit.com/r/DodoEx/.rss',
    ('r/superrare','itemnews'):'https://www.reddit.com/r/SuperRare/.rss',
    ('r/oasis-network','itemnews'):'https://www.reddit.com/r/oasislabs/.rss',
    ('r/mask-network','itemnews'):'https://www.reddit.com/r/MaskNetwork/.rss',
    ('r/hive','itemnews'):'https://www.reddit.com/r/hiveblocks.rss',
    ('r/chia','itemnews'):'https://www.reddit.com/r/chia/.rss',
    ('r/aelf','itemnews'):'https://www.reddit.com/r/aelfofficial/.rss',
    ('r/storm','itemnews'):'https://www.reddit.com/r/stormxio.rss',
    ('r/iexec-rlc','itemnews'):'https://www.reddit.com/r/iexec.rss',
    ('r/reef-finance','itemnews'):'https://www.reddit.com/r/ReefDeFi/.rss',
    ('r/origin-protocol','itemnews'):'https://www.reddit.com/r/originprotocol/.rss',
    ('r/numeraire','itemnews'):'https://www.reddit.com/r/numerai.rss',
    ('r/ark','itemnews'):'https://www.reddit.com/r/ArkEcosystem.rss',
    ('r/cartesi','itemnews'):'https://www.reddit.com/r/cartesi/.rss',
    ('r/maidsafecoin','itemnews'):'https://www.reddit.com/r/safenetwork.rss',
    ('r/dopex','itemnews'):'https://www.reddit.com/r/Dopex/.rss',
    ('r/dero','itemnews'):'https://www.reddit.com/r/DeroProject/.rss',
    }
    for key,url in newsurls.items():
        try:
            allheadlines,allitems=(getHeadlines(url,key,allheadlines,allitems))
        except(KeyError):
            pass

    return allitems

allheadlines = get_rss()
for hl in allheadlines[:]:
    try:
        updated = hl[0]['updated_parsed']
    except(KeyError):
        allheadlines.remove(hl)

allheadlines.sort(key=lambda hl:hl[0]['updated_parsed'], reverse=True)


title = allheadlines[0][0]['title']
link = allheadlines[0][0]['link']
latest = [title,link]

##finally, save news to file
with open('feed_data.txt','w') as outfile:
    json.dump(allheadlines,outfile)
