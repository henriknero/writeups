# uncompyle6 version 3.6.0
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
# [GCC 8.3.0]
# Embedded file name: pybonhash.py
# Compiled at: 2020-03-28 14:11:38
# Size of source mod 2**32: 1017 bytes

wordlist = {
    b"5df00bead7ac804c719312ef0f9fa22f50b66f1131f390f89a1b01a2970219fa" : "16",
    b"d26866bab424a1f598e92cce0e33fd53018cff693813890735e6c6758db66708" : "19",
    b"7dffb319e98f050906cc68148897a478617f1d5c18d66f19deba389722b98c0b" : "1M",
    b"a16cfb3ae2cdba9c9c404a8a18d33c54ea58941aff98a7acce76169ba2824e7a" : "1P",
    b"5aa1615562ac27355240873af12b96fb30e2402db03ef5bd405d3ae903493e06" : "1l",
    b"cf8736efdebc6bcf483dd148a6b85623b46f72c54219d14f7a281f6d24713199" : "1m",
    b"23c8e014583d89b128bf33fe10178b8b776a919aeb69d1e31925ea3b67897e69" : "1{",
    b"6b5b200855c3baed4be3603aa661b689dac462726618891f597e4cab5d5cb1eb" : "41",
    b"3304a98dfa13aec5cd2d48208f8222b171f14beab134f1d469ed51a49f075b11" : "4I",
    b"9f246105c975017b2502d07ae43e126068f6753de7d3bae23f2850e6e3ebe826" : "4V",
    b"932f77d55078604b2c5878d198325f039aa00d3f5ee37b032b44a34183335830" : "6M",
    b"e58deba06beb261775eb248c483ca30cd57cee26a41ce586092648c7c3280f57" : "6T",
    b"04043a044d749b2980e626c3d7bb31dff57b8f613d40f1b1ef36223d37c91085" : "6d",
    b"028fae0cb35d85ec7b935a7bc6ba1c75383e516154642499461931a64184966a" : "6u",
    b"b78c70df06b2bf5895a7a7a606759a3b4d78c936f3be7f1252c62baba54968d1" : "I9",
    b"9ab79d1455cbd41586b8e40bb8e103b4654ef795997ebfff51d00f6de8b080c7" : "J4",
    b"3c8f0eb3d381ccef172dc5b390fc3ee8444580dbab4223ef7dba81b13aa37c65" : "JP",
    b"87a71322315e547418907a88aa0ba27b69c54b958e18c3e1c26e64313d446247" : "Jd",
    b"2b11dbff79a0555fce1cf6cd0a6f52639d3430dcf73dd4119e69a265b3992fdf" : "Jx",
    b"98db1d99d347ddc7f9533d6cc75f9fe0c981c9d2311c8dc8d43ae5f9cc9ecdad" : "NP",
    b"87b66a988c257e91aec3d9e9a7cc377ab6d49dca15b1f28e9ce2847387afb295" : "NP",
    b"36c2f1caab469cca23ffeae4a55815faa14fb7364b3297176a3a1373d3fabda5" : "Nh",
    b"e40d5c1a444b04765abe1435977cca24b1a0ed5e897b2b39300bb8c8c2ab5b4a" : "Nu",
    b"9cae5169389e3512f461195ec970cf74c3d8b144c4afe4bdf00a5540ca6af9a8" : "Nu",
    b"86629dc3526643a94b75cf55e3c89d612b19b3448b03ab80bb56e004a4cdead9" : "PQ",
    b"5ef9d8bce2063a7b528b1abdbbedb8277e0c50ec3f7ebb52ee236bfdee950e62" : "Pi",
    b"8569d76aebb4aba97e66e68b2dd512fa31c09c7551a5cbebd36bf67fc1572b80" : "QN",
    b"acfb29f13f033636c436f5a5e491a78426e1bb6efeaf91f47c136c2995641be7" : "Qe",
    b"c02acb2270ef35e852623233697961aa026efca58a2633c6885f0f2a783b6ec8" : "Qw",
    b"4d8e86348ad1db14d2c9d084649c90163d79690c65375f266ffb66e033e2af05" : "TT",
    b"73640568a1b5a346c76b0f11defbefacb04447f8ccc3bbce349400dfba800c72" : "Tj",
    b"7e289085f3a886058f49b1a566f9c3f43284c80ee6e90b6da99566cedb986841" : "Tj",
    b"69aa3d54cb57a7ccec4b40893daec35688d97835bcc762cb7c9cad8bc44076a5" : "Zd",
    b"e45a6bf6a91b34f9b19e6a3b702a54ff1b0c557f3e7861dcae0e1799743065aa" : "Zl",
    b"6e3a3def32329fab03318e183d9adb32709229f2449f5767ffaeebdf9163e29a" : "Zt",
    b"d432334783ab1cf73a364f93261f3d2a5ee1e2eabe0da982f7440c8620d7184b" : "Z}",
    b"9104732d65ba1bee7c8c397af1dc13447c199339a74592032da29b44c771c827" : "aa",
    b"b112fe07058e2589a81233aa19838f492fca289a0e877371666f8fa350608580" : "ah",
    b"6613015b88965fd49283aa59cff24ca4f7fba34435148dcfbc14b2ba45a99e45" : "aw",
    b"a83f529ef7cf1bb31f3078d66600e70c4dedae9c83575571e2653767c901f62f" : "d0",
    b"c5341492799861275d57f58209752bdeaee713ca94b9d4a6508e159a3b3f1f34" : "dI",
    b"4dc6f8d293ac35c2f08391e447974da02e81c33e2681937eb3d0e1c79113c3c3" : "dI",
    b"c4d0875569bbed307f8dc1725b120adaec2eb9828f2cc72fabc77f13a334444c" : "dP",
    b"90e5669dfb1c2c79714d78fb11ffb7055f0c0ace21c11e83b2567363ca9c87be" : "dd",
    b"5855311dacf96dc207db31c7b60c6d3b591276afa6f2e4b9d1b18f37160bacdd" : "dd",
    b"59a14e30f93cd08d8d4252803ce68666f909d80a5d166d7e8f65ee41d836ce4d" : "dh",
    b"bd758a61481b47bf8eac47f532b4c9f776c07f3aea105ec07afb8d30de19875e" : "d{",
    b"2742f2959cd6098fd38ba875711f5203547bd06bd948227dc9e29d5572c1a2ed" : "eM",
    b"7f2a47cd84256a81185d14591e9068cee124d0c0746c52b4e449e1bdd842bc2f" : "eM",
    b"f987fa59503bd93bb7783d9b585819ae33855f8d5d990b7af2de04982b9618db" : "ej",
    b"6a6c4a571774c1bc750abd231ffb958596f568d8e284091a2d4c2ae8f8154dfe" : "gZ",
    b"12cd9d491fda5271a7a533e2ed5a51c937655e4030e492b257ce871393199eed" : "gn",
    b"fb27d040a206983b633d9a1b5ecfe66b7a9f6b834dd65728b29a80d03f9b7892" : "gt",
    b"ed868342c9261a3a7c5965bd05c12ede442d1193844da029e7c7a1491024c5a2" : "gx",
    b"cce5aec00ef593517f641ef481a93b3e74e4966df0601cc459d7eb46b0f7fdb2" : "hl",
    b"cd1f6932f17a9beb67336435b74f95c2106114b014accbc4892672fe6ec06b44" : "hw",
    b"727309b16bf3700cd6a450c33d0967d19a1d247979efe83e794ff1d0b778560c" : "h{",
    b"c4b8415020a8b9d64f615692dc16ff522dd5e2e209cdf2d599332579f95c8f5a" : "i1",
    b"3718ae7d2077b416b3f9bbdd8ff232bbb57a0e2d3944578d7bebdcb64a436fcc" : "iI",
    b"b811fc12dabfe575de08a617e752405e2ac62b1389febf71aa6c9a5b09c29228" : "ii",
    b"0313b5b2599f170280da80a65aa03910f415c9aff86f0423fa0ae7b5801b002b" : "ix",
    b"6010ad250b81540f8dfd309e0a341a1fdb330d6f0815ca8e4baf67bfd845e24c" : "ix",
    b"f3b0fd4d41b82e504c6ff68ecb1dd7aa2d1f7153d625a541d2b866db94007982" : "ja",
    b"936042e279b4949cf9270eb98c4c2061b8ea5a439d0c05c47ceb2e4282380592" : "l0",
    b"65edfeb119ec73882f96e68abdba715c824822cb54bd5af334f2799d4b2b91a1" : "l0",
    b"394bef9e973851f2a598ef901ca7fa4639125c140e60f61b6bddeffc3351c923" : "ll",
    b"bb4011dad3ddd5b247500ed051568bc915249515f2a4330cd1f6a414ccc08072" : "ll",
    b"c1bdcf5138c78ad94aeb8c00220e7632041bfd86cfe9f131a07559e4abe2166a" : "l{",
    b"e651579ec6d08c67015e49b6ae49e344b714e8514cb5f973a27dd8bec0e65639" : "mP",
    b"f3218500b0e60d48039e3b3027e9b7ba22c8a9efaf440c197843ad277e3a143c" : "md",
    b"b8e717761544efccace111c2ea9723fc176d7cec0136674666ff94a3acec1a42" : "mi",
    b"af0457449fb8b6ab630de8c787bab6719bcf50c79d444bf414d3e93510ba488b" : "mw",
    b"80d89623c35f4ed0ccee62b61193f3d83d58126a90f4b4668d71552b98de42b5" : "ni",
    b"0104fae06fd9b0e9c5e407691c90a22db10f77f28d57ddee91c8aae8a1cf3fc5" : "nj",
    b"6327195fd408073c90d6edc4f27877a7de77a02ac0e1f3f8d3d81ab3f128145f" : "pz",
    b"3a88371a68da58dc546885900c9755ba98a026aea426751e618f79e11b0c4d62" : "tz",
    b"d5cb59a3d705df532cced04d1d680c7095bbcd77400da4275a0cda7ec2f99714" : "tz",
    b"1f4ecea587db92fdae1e0e23a1f61095a84a87f41376e878e5ba36e1d03f2f81" : "w0",
    b"a0738484f9fcbfc7a7eec81eb9b979d2410c7eb6d6104f64c3e2c4330c383991" : "w1",
    b"b9e105d6300cd8afb4ae81879443bb37f74808c6ca7fbf678cc49d831c7290ef" : "w6",
    b"ea73ac8aab1169c4ce9f7709cbc5576fe930184c153aa01f3945c5e2a43bb7ad" : "wd",
    b"265ce1cc3c3255cb0e571e1be49bff5bd42f8910f63bc03c808bdc54d6938ef5" : "wd",
    b"5b2dd6934d631ae9673add2f04550c03313a054c4a7fc23d2cdd8eac63bd666c" : "wl",
    b"1222fe0a0f89793f266a4497a373969017f73063ffa772b168c9d41fe09e282a" : "wp",
    b"16152975a81b662c76df625e6d6efe0fb4c2eea61c7bebf62174a49ee1288e0c" : "ww",
    b"296698361e5862139baaa69e3d62809fe54f8ff30ddfd11a91720b602eaeb063" : "ww",
    b"a078708962e272dfd617533d7308918c41c4f6ecac55c928ba727093cb562bb3" : "x0",
    b"e562075faa7fc6a8c802e275cf20747a6c55736058b984390134a0fbca712349" : "x6",
    b"14bfcb34b8d43c3818c33c87173b4894934e212c38dfb15649dc34cd7be63c5e" : "zI",
    b"c1a48f8e8c8237de59b7a5d7371d910b25f953c8d5f267faab3eae18ab50b4be" : "zJ",
    b"ecde0f47273b57f9ec768bf09ef636342521ecf49aadd69dd60f2f8d2d4e547f" : "zN",
    b"5e7edab7a1b7f94853f045c0c36c1667e699e21214ef59177b83ad8b689aa784" : "zZ",
    b"16c8ec400433e07c3e9caad8c0162557d1c3d9599728bbad4a07b450d36d399a" : "zj",
    b"a219349d3420fa0f79b694555ffb60710c0eaefd3eac4edbe8216a36d5ee6bb5" : "zw",
    b"8e5a1e863f26b1f11af7735c265b50573730c7e1100a8dc63ab0bd1a5386bcc4" : "zz",
    b"4b51e050e7b7fd82fd3737271f689b56ea503909ef14822c023b5fb815eab517" : "z{",
    b"92027d477bdba8bd4e6ee5d2c4c3110fd6b92a8213d23b5c4dfb317350568d33" : "{6",
    b"b3a643ef1db07add94163894e8225fb7a0e302b5f8af391cbc7babf98b7678d0" : "{l",
    b"40e5ea4a5f95810949cf9307a63c8e97a927c4c8956156d301c8891b5c64c962" : "}N",
    b"9427b44ace49d73d0a8ea350e132474998562667f9eb3cc2ba906d7ae034309d" : "}P",
    b"40f64e2a1bf6f9a897f6f44a96920a791c9eec814ec629158782e8ded48ca677" : "}i",
    b"8263208c6b5b02cc8f002b825b819cce41fed1c63dfc2602402dd49d4e8d19bf" : "}n"
}

key_2dot0 = list("\0"*42)
output = open("pybonhash/hash.txt").read()
fuck = [output[i:i+64] for i in range(0, len(output), 64)]

import string, sys, hashlib, binascii
from Crypto.Cipher import AES
from flag import key
assert len(key) == 42
data = bytes(str("A"*204).encode())#open(sys.argv[1], 'rb').read()
data_partial = list(data)
assert len(data) >= 191
FIBOFFSET = 4919
MAXFIBSIZE = len(key) + len(data) + FIBOFFSET

def fibseq(n):
    out = [
     0, 1]
    for i in range(2, n):
        out += [out[(i - 1)] + out[(i - 2)]]

    return out

known = [0,1,2,3,4,5,6,7,8,41]
FIB = fibseq(MAXFIBSIZE)
i = 0
output = ''
while i < len(data):
    data1 = data[(FIB[i] % len(data))]
    dataindex1=(FIB[i] % len(data))
    key1 = key[((i + FIB[(FIBOFFSET + i)]) % len(key))]
    keyindex1=((i + FIB[(FIBOFFSET + i)]) % len(key))
    i += 1
    data2 = data[(FIB[i] % len(data))]
    dataindex2=(FIB[i] % len(data))
    key2 = key[((i + FIB[(FIBOFFSET + i)]) % len(key))]
    keyindex2=((i + FIB[(FIBOFFSET + i)]) % len(key))
    i += 1
    tohash = bytes([data1, data2])
    toencrypt = hashlib.md5(tohash).hexdigest()
    thiskey = bytes([key1, key2]) * 16
    cipher = AES.new(thiskey, AES.MODE_ECB)
    enc = cipher.encrypt(toencrypt)
    key_2dot0[keyindex1] = wordlist[bytes(fuck[int((i-2)/2)],'ascii')][0]
    key_2dot0[keyindex2] = wordlist[bytes(fuck[int((i-2)/2)],'ascii')][1]

    output += binascii.hexlify(enc).decode('ascii')

#print(output)
print(''.join(key_2dot0))
# okay decompiling pybonhash/pybonhash.cpython-36.pyc
