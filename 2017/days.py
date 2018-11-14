import math
from collections import defaultdict
import re
import numpy as np

# day 2

s = """1208	412	743	57	1097	53	71	1029	719	133	258	69	1104	373	367	365
4011	4316	1755	4992	228	240	3333	208	247	3319	4555	717	1483	4608	1387	3542
675	134	106	115	204	437	1035	1142	195	1115	569	140	1133	190	701	1016
4455	2184	5109	221	3794	246	5214	4572	3571	3395	2054	5050	216	878	237	3880
4185	5959	292	2293	118	5603	2167	5436	3079	167	243	256	5382	207	5258	4234
94	402	126	1293	801	1604	1481	1292	1428	1051	345	1510	1417	684	133	119
120	1921	115	3188	82	334	366	3467	103	863	3060	2123	3429	1974	557	3090
53	446	994	71	872	898	89	982	957	789	1040	100	133	82	84	791
2297	733	575	2896	1470	169	2925	1901	195	2757	1627	1216	148	3037	392	221
1343	483	67	1655	57	71	1562	447	58	1561	889	1741	1338	88	1363	560
2387	3991	3394	6300	2281	6976	234	204	6244	854	1564	210	195	7007	3773	3623
1523	77	1236	1277	112	171	70	1198	86	1664	1767	75	315	143	1450	1610
168	2683	1480	200	1666	1999	3418	2177	156	430	2959	3264	2989	136	110	3526
8702	6973	203	4401	8135	7752	1704	8890	182	9315	255	229	6539	647	6431	6178
2290	157	2759	3771	4112	2063	153	3538	3740	130	3474	1013	180	2164	170	189
525	1263	146	954	188	232	1019	918	268	172	1196	1091	1128	234	650	420"""
sum = 0
for line in s.splitlines():
    sum += max(map(int, line.split())) - min(map(int, line.split()))
print(sum)

sum = 0
for line in s.splitlines():
    splitLine = list(map(int, line.split()))
    for i in range(len(splitLine)):
        num = splitLine[i]
        for other in splitLine[i+1:]:
            if num % other == 0:
                sum += num / other
            if other % num == 0:
                sum += other / num
print(sum)

# day 3


def round_down_to_odd(f):
    return np.ceil(f) // 2 * 2 - 1


n = 289326
squareRootOfPreviousCorner = round_down_to_odd(math.sqrt(n))
numbersInFourthOfCurrentSpiral = squareRootOfPreviousCorner + 1
previousCornerNum = squareRootOfPreviousCorner ** 2
remainder = n - previousCornerNum
remainderModded = remainder % numbersInFourthOfCurrentSpiral
answer = numbersInFourthOfCurrentSpiral - 1   # start @ startingNumberInSequence

for i in range(1, int(remainderModded)):
    if i >= numbersInFourthOfCurrentSpiral//2:
        answer += 1
    else:
        answer -= 1

print(answer)

n = 289326
m = {(0, 0): 1}
spot = (1, 0)

if (0, 1) not in m:
    print("suh")

# day 4

s = """bdwdjjo avricm cjbmj ran lmfsom ivsof
mxonybc fndyzzi gmdp gdfyoi inrvhr kpuueel wdpga vkq
bneh ylltsc vhryov lsd hmruxy ebnh pdln vdprrky
fumay zbccai qymavw zwoove hqpd rcxyvy
bcuo khhkkro mpt dxrebym qwum zqp lhmbma esmr qiyomu
qjs giedut mzsubkn rcbugk voxk yrlp rqxfvz kspz vxg zskp
srceh xdwao reshc shecr
dcao isz wwse bbdgn ewsw qkze pwu
lbnvl lviftmr zqiv iadanl fdhrldn dlaani lxy dhfndrl fkoukx
raovmz pdysjsw hqps orsyqw rrwnzcz vrzoam jjljt
wgt gzi icpwp qeefgbe msadakj jbbrma sbj dufuujx zex
cfzx bvyu eswr hafcfy klw bgnhynv qrf aop
rzlq atrzcpb hpl pajjw cdxep ean aptzcrb rzcbapt
xogpf ucc nsukoz umtfbw xfvth ozusnk fopxg ubp iflb
xot nqcdyu kpwix szo cyxv hpmp hwtrc zso nyuqdc aha
mkzf cat tkjprc izxdggf obspan lmlbg bsyspf twox
lfmfrd ooclx tcl clt
dxvnyd nxwojj arutn eyqocj swzao tmh juvpezm
teu eman rlmdmk xkbodv fvrcm zorgy wmwe
hmo fdayx duciqf cgt duciqf
imjnv vfmsha cyrusow xjswoq nclrmjy sjxowq ynjrcml
rwbsay alsi bmzpvw ozq aduui nihwx glwdiz ixmkgfx
vtjzc ntkh zekj qrbkjhn zekj lyfnbg
afaig jqhli oie lhwyduh kqfnraz nfrzaqk mayfg iljqh
inb zum zmu dnl zjxg vrdziq ypdnsvt
uhbzmre mpdxm alkbmsq aopjmkl mqxenry ayvkrf zxvs qkfqva
fimjr ccv cnug crdsv
bqyve lhxdj ydu qbyve vihwjr vyodhc
vmng dyttyf noagpji tdtyfy ewiest ogg
kgscfj klmsv vmksl vmlks
qlvh veo wruft wtm fbrlvjr evo wvwmny dhp bvrlrfj lvt vgzuyyw
mxuro orxmu tivu tjdq ojjvju cdd
kjexme gxbysxp yxrum hinrklv fxehytd qkt tqk umryx nim
kywnux wab tzrft dsaz jgwuw dubarmi fle wjguvr umjp uzncwj mzz
qokwh zrda xywufk tbxhhj eejqaoa hwoqk zer hwt hbjxth xyf hmh
eregs qdx tdequa agrlrg mwwpba qjie yrjvhr txujk
iyot fxwdcb zvwfv vfzwv wvkw ncwbr wdejrr ltcdza
waix eza znmonya ldfghws ialwfvc dey ubsz uhbnh svgekg nonzyam
bryz tfbqn xznfmw xiplgww wwxigpl jxzcgxl rzyb
cqvl rrcoqxs staeuqr hzzow cwv tsvol dio coc ddavii uuojy
txbn qvkkyh gbqnjtq ndpkqr srt bkpqfmm ytycev ypcv bpqmmfk
uqkjmul dour zgq ztango yrrjhrg ufxnmuw
ekxbcv vkxbec xbcevk jiq bar
wczff qdu cwffz hhk wlvyg
zjlconc osgsro dajzo hqih ehml
hnio shccluw cpu ivaby tormn vkef abv vkef ivaby
xgbdeso xiizs omqwy sbtnnt khago evviclw xyu dtvg wsyxfuc humewp
cnzu bia vdyqrf wwb qveum hmh ouupgc owli
pjpmfxa dvd lxgh ndy gwph oebfkqv vtlxdg efl ekj dyn
mvan nmdkc ucyshia mavn ecst poo
oybm pjwm bmyo wovgu xykziaq obmy eiirhqd
xkvomx yxvv oxxpth elh vxvy lhe ycn
okxglw gmaangx gnxaamg yduzrr nzwxtnd rcxcu xjjvno yat cin gaxnamg yss
oicgs rrol zvnbna rrol
abb edpnxuo peoudxn bab ceay
ncpkfz gvwunb fckpzn caafx pkcfzn tsfl
fnrt ymenkpq wodubcm niv nvi ziluu cuowbdm zocg pdakwt mlzxkex nuxqclo
uouxcgl stgua otadr ideannq wizxunv iqsdpj mxddt ldst ucxogul
rbrwyhk wqoz zqwo ikwgexl atpu iza
smo yolp pcahlu muljxkq cbkljmz zlbcmkj zvbmgz eaiv ncv zplifm yplo
ocutdhz zmnaap llgv llzpl loavju guzkfq saay rxyhng cwxzx lcv anrnzs
etyzx tcm upxrtvd imyoiu rdpj fed dmm
gonqa szteh szteh razdqh phyff upf knfqfaf knfqfaf fpsgl kakag
mcju mixskop isrwat lcr nfyi lcr aaevr nfyi pqrbk gnful
xfmr fkmnq fbnhd mxrf litniid xbae frxm zcenf
yuh lzojtj rqsh hyu
vbjgql yeshsuv lokt efqota wpwjfu ykyq rxc fxxh ycqfkk gndts vdf
wnylmr kkuruxm azr xukrkum dohkwx dmdb
bjiyrwf dvf fdv vdf gnokekr
jsaq hcww iayqtu llv gdpxdrd hwlo nosjit wpm lcab fcgwr
fxjp bys nnf xzllckh bys hvojw zcwtgwz wye ccyvjv
grafa hbb ghk wkdpsf ufa uoqmysd
yvacf kssbff iovrm mvrio cfbpb avh zzje
gqd qmsen wkvrfz vhtsa zrwfkv gul zkvwrf
hrbi svaogb aogsvb bgrk hibr jbtkr
ljl ryc mrewrge yky
fcqyymt emk qcmyytf mcfvusb luy qany cbsvumf
oknt mcozuc ccmuoz uoccmz
uziil xobutwf acnof iqgwl diso
sekq fxbtsuv ddnnqg rnemlt dngnqd hhgjfus stxvubf
lajcp qgiw fyz blrlcd pviwv buh wnkk
wolqfk nvpapfc rwcqxfz xobno yzjfz irpj wolqfk wbnwjt
vmabj noiljne hhqf holxkbk swwzx ylgj lnmxy lqodhk abjvm bmsrf
bpnp yrz pjepxxs jlmhuy vihlx zacm inuazhc xsxjepp
tryl kryh eonvaad ucevssk umkxg lqej nswopjj svkeucs bmh stosxxz
cfdwd dmfdrvm ibuhsz nwtgmb pjt dmfdrvm cqdcm fzjjz afa ibuhsz
erwp abn jwx ynmkkj rhgg abn epd atqhs rst rhgg
jtnp cegdsoy gfuvfbg gdmn ahlsc
jgrp diu jrgp onjnml nojmnl vxockc
lakqyuw khq dcpiwt ykwlqua hkq plklx ujbckec hjcvur jnp pvyf
usuvoo jkih ylafyy yhio jureyj
uazisdf cnwlfnf ewodatr woaddkd wbla qmn atdrowe
bnyepaa ntqh xppe ydtsw ppex
yewjwsp jxylmtk ijese ewry ijese kbja nfml zeuwcsh juimz
qbvmf nca zsfreo uurgaiz twe fbqmv ncwi etdcsk atowfp
jeotslx kgdpzp wxlcww pdd dcn ddp
macllv ldl kyluine lbt hbxbr wxcaspp ezwvc qxkeu
ivg gxv zsf ucr uff yrz
tdlwbny bqlrlz tbynwdl lwtbdny
tnekq pdaievs ttwpfh xfm fcaa
zqqhl zbf fbz uqrv bfz ffwavhk foccg
vcw ebqdd cwv eddbq nrmq
hpiusz sizphu xzq sgyehk wgagkv hsygek
vagkxa iou frqdnnr ipcg uxvh vvh eskf katgpiq aqktigp gzvseyi
xkwgd kzfxk pgdy fmtvq ngf rshx zti pamviob ely knz
hwo rteohu qzwoe rotuhe wzb
bsqgg tid dti gtats dit
sjtux djwxv dljwjq xwvjd xnqfvx veqdrtl uxtsj nnkjn wnhilaf unirrp
fruuqjk gtote gooklg bzwhim zfnccmm ezipnf cxwdxa wfu fdca
zcyxb byzxc cxbyz pgcqco ivlxz
wrjh zfdinsf ihw xwosiah hdg xpiabno bilyy azdeczg javuwa
rinlv dcpt qhencba mmb njxw gadc
qwcpua qzyzt cxjsgh kumh byiimas qhsgf qytzz rqqruwp ismyiba xydcxz rwkscqa
xbzefi hltca ibzxfe fkx xizbfe wvaynts
oyuce vzk ouxvj gfh efgbv ubc nyb bxnbhd mtwboe whksy ovmrt
ljrebp tacn bpjler utphw wmfw rcnha
drdnic eyodes rcnidd yseeod
umxmsf kfroz ukhjin awpnnnu ooyyohh tuv rafano jze
bakz lfzpjyg gfkqcgn kzh zwpvk gqfngck
jpaony ojpnya hmro xaaz tovary aaxz iel pbg
swvbgc bbhjp yvrcddd rhj clfu eao afrkegn qvvb yvcx nxjmdo rcvtx
conbjy jeqtri wvujt jeqtri rkhllgw tsdt zowreo qxr qbpragn kuzmplw wvujt
jrpxyp hchljy rkowqb eeaf ltllebb gtksrwx iazx vnsfmc zzrxw hlcjyh
piehb cjdzt eqn kuje rls oaewoz lrqwt lcrrq
hdjowxv uknhlv hluknv pokxg
txiqxfr fyyp pyyf xfxtrqi tvm rtvby cfx trx nwrf kqrxtat alwot
wdaadr stexpow ardawd uejqxc
wwgwjel wwgwjel mtjt wwgwjel
mczx uua lgceb dqru vkcea tcet ruz
jkt yroojr qdrtdu wze ovwz fdmqnr xxsyfd kchytwl hctlkwy gyd
eif irnrce iamhxgh bmis uxye azrwdi sznv yuowb vdlqqxu
dxdjyj hngqwzs yhwku qhsctfe rhbc rchb tqhcfse
fxyxnzs qtxevin rvtxtc iqnxtve
zgbpk mwzxx bgpkz wkpkn
rjiym iub lcyw agbtlb bzhx osv rbtf
emmyu uoflio tinih skpqaj rbor gezbhhv ine mij qlqte uuj ycns
owmwc uhxv pyho ftjh jzsg blqn bszyo bob trbycy mkru
mwgz bbqsmpp fgzs bihhg bbn pjxxexs qrqmt htsxfwo qltqp vqqaxi
lpr wcvy sxjqq ltd rftdgv pdnog ymu
qhcos shuy icdhucu lrikh rwslv yxbgibl rcomhn wakirz
civdmee owlzocl vedecim rogmjnn pix pohcmk dsjm yworm
vzdpxp lvt inufv yofqt omm qfoty qrlseqy amkt kjcvg vgkjc
huhq quhh levzsws sjuun ofgqr cjhp nfxbbft rnt wtbd tbzab
tjftkx xpfcv hvftvhw lpypbjg batrn fhwhtvv uthl arbtn brb sthv
ogr uyuxdco bpjgir edztxv sxtgu jzfmx ihnauz zwegqkr kvkw
mhxthf pervvn gshy jig ezjteq ckkcpy gww
tiljyki rpe prcojy tjkylii moxu
pjsdqc lgqydfd lohck emrtejw axwmo wuuv rfi qzyncmw gjijdfb bljfd xrs
ywjab gynzi relf kziy xmsby izyk ocwoho kqnyh bwayj
bhjlz uonz jhmzuq eiajoos zjnbj tomj bmyv hjlbz fgw jjbnz
kszz xzw xzw prtznyb
ghzk vxhwt thxwv slwpayp qxegmi dawdwo kgzh
ibpcvuf wnuwxu sbf jsj bfjynl cdp jbylnf
epaxr vfhf hvff azepadz pwf sbo pgfzya hslyo rqqj rmklw hwtta
yyolko pwbvxvg xdwl yfje hftep kzzsr kho jeyf yvslxpw kfyv
xmk juyjxy eqno mdwklum reg dgn cirh wmxfyj bnxlgo dlobk
oyv gshqyot jgcqe dsf gyohqst gqgeojo egoogjq dmqpyp
sypianq yss lmhu ulmh itilh ndkda lhiit
qbxxl bxxql ikald nfap qixwbqq
jtqhqty ljysnl nwoj toa bmmyj pal
ahktew sxody nkvsf pbxyt baws wgwfwej bevgzm jus hcvajfy kzrb jwgwewf
jzsb szbj ujngwf nfuuf lfiuxdu uufnf orsy
vgo hto isstyul gau wsmxoqw
uxw itwf epaw hec wape hemol rpwyosc xzxmrll eetz zui kagca
mjncux muv rygdeis rygdeis
qgkqjvf iprzibd fkvqqgj llcrl vbh vlf lllrc zwrunt
dslsa wvoex eqbwj tjem gbx ayn xcan fnacl xggxon gnwjlh
yzosv hcxjiz yvon gcgd
bixpny ecln sda eymt bjiwk
rlcad lrdca adoqfzs rgty mds pwb kmwj
wkai pmryffq rrdmodc wgyx taz yxwg nkap
auynzwc vzg uapdv qkrh
ldmuysp oyu kpn ejbl mfifa bzs hwyn brlw qpzqx uyilao ysdumpl
czoxoj pwnultl wezolbw lyk aonesgb
nqy nhb nle yycp lgtbo ojf dytwyh ufa
rwr eph obg peh pejret prjtee ovgz
vdqf vdqf ycjrg ovzl lelbe vdqf
gvagdqm gvdgqam dmb zaxe nepzwn
emwh bkkbgec qwdgk mhvfsrf wmdfpp ekzuua
mbqw lgkyazt ckyhvnq uladwo owt
qwiwd pbo tkjoqda zapo dygqopv zzdlwfn
qty dhb iinncba ytq kvh idgoevt chx waq
ulffsvk vplsz ulffsvk uxsh cpwgxd ikgcacx nrirke uowcjvn
gknmxr grkxnm fco dilyyj grmxkn
saqxkh uhue nvu fef xsuxq ekyyoc bcaavd
qltwqa vrmpv vhra nof yprauc vkreojm eaq igiy mec
wvheiyg uthy gpvcs nhnjrne mqaejr tfnsly zfbhn entcc nystfl cpq
zxv jzk dwsjgrd gqqxhp xqxu naunwc yeh qzpkz awcnnu aoosa icadax
vpmqmg qmvpgm tqs mvpqmg
inehzu zwxeoy jxia fcyzxc hwikd
bzwnp kamsen ajpn kdls bzh xqcb bzwnp cmjnfa wmgx
hbuhc qgvhxy smzkxh zzebox hbcuh net wyrdppc yvgxqh
oeum oemu iyags xaipdi euom
tqljgoq ghtdhw xhnni lux qltojqg lki zxztda pcqjif acpzvwy
ydijaq kbyjxpu onyd hsfgz geqvbg
rwoih xog dtbzyr ryzbdt tdbyzr
vcdxf zosw pardxfz bmb mscmain lwfc jvq hbszcqh fxomsmm ahnugx
zutsemg pqzil ddv nsstz gmeuzst bedvy xkzzjpw xlqbd
xxf ltnnu yeb hbml agj meovtjr qrul kexerkw xxf
tqrpd hhcx bmdv nlmr pnu pajdtc rpatqi yekedx oeiuew epsshog
ttbfpv plairk toh jagfsg njnqpa tmwh vwqp irtxv
vdky uwc tkkkztp vdky vdky qlcw lza
rzie yundymy pwgx wtwtbg kpiw mewnb liveysj uvsbn
jgfvyny hacg pzra arpz uowswu puzsfu hoe heo vrq naup
hqv vrl uko qgpikho lligvxa wdld qgpikho
whvby yomxwj dieffc jkprinh dsaqy yfrnba woyq yexeb mjn cbszn xeswvvo
wowtgu rciyg rlas bra quyfec ihe thuu asxhscu bsbdpbi ogxosu
vydsaet tvnkjq piedkzj foeiqz zqivt iatsju tjnqvk drauaf vqitz invoz
cppn jqzw zmxr qksuas iifmjg xtkgf cppn cppn jpsd
nkifpsq cxdx bokxhm ebww kghagrp bofhrl grc cheuzyj
ibgrlvm hrcx jjuoh ipmt
hcoqkh fzt rgravb cimauj jxjq blct qhc vjxw pqpg qzp
jycxz xcv czxjy vxc
liljaur cgmg neldxb xfummcq yfhiukd dnqhl iolxn cmewhb
hpvoihj fkwokod txy uuktw vmqqb dpldzh yxmcay cyaxmy xycaym wekr
ccnaf wuxc ecadb vbgpt ccntf sezo skjdkbf fnctc
hqdtwho kdhyman bjtcjvr bwllva ncyffyr
xprn jrrvmj pdw yvexm ewbflbe eapml rvrmjj xmevy rxyzhf
wjcbpy qdgtcp cfjh muww fhg sgfdleo nelpte yucqa aavev
rci vqypsqt xmg rzii
gramh wwprtc ampdhw dajr
ovrm mdyhpbl mdylbph aykz
cbmo fxs nuugu guunu upt ljjuhjw nituh utp kxqc
rhabal rhabal rhabal vah lfrs
nrq qway ftzp rtjcks mbygdtd hsiqbh wypqb rtjcks cllp hsiqbh
ywa anhcf nvd puqkwg molrwck wsctx xvd molrwck
wox jzq jfen wcvus cswvu oxw irg lmu tpj viahm jesic
qenad neqad smlgi ydwzq ppdemvs ucyuf qtunm eoqx jlgv
sucpl nrdwbl ltvetok npbw ozzw hafyay sjmui sjmui jkqlq pyn pbuopx
nxgaiu ybyl meo kgh saqjaz xhbqr otelcyp vkwc
iqrl ldjlwvl ajhrl dnhutr gkknyqs mcvluet fgyu ogiz cxo aiunl orb
psd cyq xpoyqny yqc kozqh vonfd uhozwz pds hcpw
tvaxder tulwmw qiw avddbmh irog vynjzcc refx efxr emnvk
myjx npqk whm egw kpy igrrohg ukglx ldnuqw caqg ynx fckhnsh
dafv bkdoqg zcqvbco xgikoac cvbqczo
rtzhpwk ukuyp bayhzp upkuy ahbpyz
oarcuv pnlkxvw fqdkj hwzsz nauwl lpufibz vzfbgc unkluxy rwh xuknuyl
vxhsaj ppdxw qrswqtu ulwv uqtqwsr ppxwd
cww cww cww scu
wiiikwa bfpewt zbgxfkl iqpk tpbwfe aazdcxj ipqk icggn fwn fjr
net ovxuwpz yvzmzd yvzmzd
xgar czuhp vuhisaq fgrqxy evvrtf mnmar lsk
hld mxuedug itswju vmmejqx snzslqj toe bbmugph mgubhpb mowj nrjnzu
qbz ouhye hsldmp lcf hyhlrb ewvle zko
cke mupaq quapm eck
owu zdt lales tzd apjjo fhpx bmuktbw dvehpz
libvl zxypk azazc vtsom ohdzycb
kiowxnc scxygrf ckxnwio ycxsrgf
vcjj fqz lfawfx mps zhv qykch vhz psu zud spu fnpvkx
scfvum fuktgk tua ieosetl wwmjtt exnsw wwmttj plvd pfb kku pdbom
wkfw snukd wkfw gyaojdf bjw htagy cdsp
beh gatqxcu ibrooxr ssww orrioxb eenkqz
jlv affah mtbemf tylh aafhf
zqfajd uwzrw csouuip qzadjf
gsnlrw tcel hha tfbzrp ild aenqa
iirfxef kdux yvj vbzgj
ibx pfll rgkp nancij llpf xib gbkfy
uvw kkbavj pznsnk okigtxl ogitxkl eobbs xhaz wroabn ltogxki
bivdf lotvmoh vrb kpaeeue tdab qhukcb qmy kuqf kesu
egs hbsfeu esg twxko uib
ocraimu qilp ijmx eco nhevqp juxf ksejr bcqqau uhpt
pyx jmpglf juokd dxszjw cml vcjge pfg
gxwrt btmimse dkpbha idmz mtignka ngakmti
dpjhm jyalra hukf imocr lkgt rqywn quhe fukh
nbau xyc bdh yni xaawxm cyx xwaaxm akx gyodqe htbifc
bywdxe bfrp rvb rndl onal jghiwb nuta aint qlciwcx
fpic yrqce land soxhci qzc zoebsq hcdohcc fzhcl iyxb dqinum hchdcoc
zok ghgp zok lmk
ozfz zofz dkdekzb sqc
gfti zuqvg cexmtyl qwuqnj stepb erduqhy cuoizcs qudyreh kqvfdd guzqv
jrugz jzugr lmqu jgihgo hjfbz duxkn unxkd
ckiys dbqmi ckiys ckiys
iylp uvvdp pluifaa djo
esxec rwvel djxppqf jymwt ilm aiz upn aiz wrfefwi rwvel
nitgjr pokxuy puhdwg qtxpb veylp zqvzkbd lrvpcgu zuy rnigjt ibci
jboyzq ogcldr hlon ywav jqqtz qjzqt vyaw cok
aqdw jxn hqknh azbylg
jya qpxtmsj hqrtsgg qjtpxsm
pofcs sxw dlvru dlvur swx
yphvvb qqyyfsp sjkbff dqyerxe jxzes oof
pwbya txk bbwsj ywgimd kmdpc bawpy lbnt
bkbazff ldmaq tyfl acqurpy ndnrp
asw ctiv mnxzyc weeuwb gsn bzk irbyhxl cgqomj izy zbk
yrxcrbt bcrryxt pofe wwzl
vuaqez kbtuyai vuaqez dxqud uvo gmhtg dxqud
tpzs gqdxpxo zzpgta uurjx xpqxodg
cil lsv vznqw vro zqzvjhm jhgauzw uxnwk lci zpgpu frjvyzo tsv
zfvcuim gwn gnw dxfppok
btb goof iwadca aac tbb jha uvzi
qah ned ipmure kyta ffhrwe njz paq kaag xmlui
rkmw vrblwyy gpax hxsf zpbza gypuwf jbib ypcjwd vrlybyw
yfjljn uxpvg huik jsnah nkhsg yfjljn lqzsz
hagjlqx agnax jqalxgh rvjgtc mjrmph azznzcq gxajlqh
ipki bhoabp rmiyl dmjyxl zzsmap aju
tyjrr rigrf ciq qic avmwu jtr wpq
vuf cosgytm toycgms ufv qzpcbrs
epzgxr lydrsj ezxrpg expzgr
ecm prj kmak makk jpr
ccwyq txy okj matxa socoa
zrjphq gigayv ywkfmru yrwukmf fxjjrha gqkxx zhjy tisutx kufrywm izjfj igg
lfhgsro gsroflh wrpo lofhgsr
kgkgj wkhnab ubrjaoa ubrjaoa ubrjaoa ggdgh
hztutpn epnqmz ffcroq mnqpez niibpn kdloak xjui ozttj lyzsc pzgq inpnib
kruz sjqp mmd hhdxjgc mauouma asevvo upjwqi hxcgjhd etqzagp
zylf qime cho oraid svytv gqrjufv mker cho vnkyiin tjms
dotjul qyv hnh cibtg gdpauyx wzp
fabtira ejxoeor cqyethv ndjrq hnxn joq otng lrr csytrub
txhgepd fwdaanm nawdamf pxine qqrn pronw exnip qwkimt rvy
kuxzhi jln urzxtw rzu ebsuylm tscru qwlhfgq nnu nuchvz vuht
cqgu camlr umkltcf stx izp rtdwxff wkfvs
jhje cxix lefcrsu nebv idfzhic xqri xkft
utzxb znb ietupd uqgbhje aobip oawjwm hetyan uqtqv hpwzyri kwxyu
jvzvbt xuyvp aegdkb srbw bzabpf lyfriez cruyfu
nhi nih aeb ihn
hcf zypt djcm pkjx pvhh
rhvxcfk exydvk ids hybme hnk yfchvs mjbo meocn
rpboxr rxoprb hdzje zhedj
ziildbo apzvatr vsv isndq ebxyy ntm tdttg wkvdh qnids vkdhw xxolip
ywu uyw ipcjz pjzci xjn kvgk vsocprw
euzo njlpv ndrlhi drlnhi ivmjkb fjrtxta skvgmrd
gbyvj dkck gevpfvb lhadhx rgjcdn yraxh bdk oen vqryd bkr
vgkp hncttxb wgxh gdyjo bbdfzvc xhgw rznzgda yxrrlo gxhw
ifjlb fpecyic svhjp ilmj oxgr svhaf
vbqky lhccj xtmm xzjyykn oqmdq qywir bswly
euxxziv totzer vsxfx leo djho uoeaz edaig fbu lumbi
ooqtwq pvo kid vpo jxin bod btqc fbyuz
jhabi mronu htqqyz umjcbv sgnbp wyn cetmt pcjf
tnrkcyl dduuhxh rylkctn pwj rtynkcl mzzfomr
rxx ldqffi ulappk nltawbn tplhb kyb cqyi
vzkw gviooah vxh xeae ohvcad oaiwcj dkx
sdofdjt hcifv dqws sia mlwm vfich kavh myzue roops mzuye
uxs nlbmjp nlbmjp tlaxa tlaxa
ynnisp twx xtw jgkc yinpns
kumorsm wav xhx bpvz clqc ffmadzl ndny ymslo lobv
ljzabj tqhves mezh pwn wue dwfqq lynvtt boeknvi xqbd pkud tzlanis
lgq qiikzl oihnsr pivtjmu qhic yvmeebg rxu qgl yuxnqse dvu faxqez
ldk mlwja vmdqr yzlxiua amlubt ejmzfx nonm zhkxbn gaqbnqq
ttc ctt kneknx smtnaft abljip tct
uybhbiw zwojzlm cfxoopp abulenj znz zzn opllzmm yufk witwxzp
qvkybwi rdbxb qiuizmo fqgne jgot jxz dqhapn
vzinf ehaley amnk laheye invfz
pedakl ivld agzyhr wmzba tzzzg bazwm wjwgux thrnxkn
cmyhae nwfs nfsw kmh pxkaffq
vdf szupev tyunp qiiu deevxmy wozvtt nelnr kgdexy gparqj hajavz biizn
pwspk skpwp ontbjee pkspw cfbj
ihsmh djxtak wkzllao oyr djxtak prc
uhvihqq jrgf hdfek pdrfpt tghz gthz awae wcygi wujti svq fhedk
gnfhsj odqlt netmsul rviio nkzw nkzw
xyvc clxw cyxv lxcw
duegck pkviu npwsp zdx wpvn dmxgnv ixv fybs xteru
vih kgk hads boaddu daiwo hozoufv nef vtcplc isiw
tzqoo dqlgvno jzlay sywx ecej addt ecej addt mnfcu
ymgmby zegudpx ipsjai ger wcwjw brzebb
eqekxlx itra xekelxq exqkexl
rciu ojaa ircu nxjga puvmwou remgu
sltth pprimb slnxopq avtir hvpv ppww fhfap wisn kzs jcuuuuf
xbppc ydpbq zhjh oym iljzvk vsb
ueye shtps uccehi ccheiu dqm yeeu
gwywf lcpv qza qza gzuovj jfzffyh oybfxqv
aawi ynsvdco azdoz cqr tnyquq xlyvbx eca kcalpes
zumgzhy rou kguqa vubw bwgd qprxcg etnbev nqmi
fyd tuoz uwclqn cgl lrpkf irz dizv nxze clg jghx jbpt
kwuanos eorjr tcahp kwuanos cyrpfji zxayggd kwuanos jkqt qqvbork lizk
vtu ovje vhg ovje vtu zcy hrhtr puawfgv
bliz exp wot svxv epx
jiqgxwj yips hjsatc jgsrno msfp vxvbt bba bqmw xjgpgog
vpvypp ggwp wggp gndp hedpse afji hcqgof
hxueubt hiynoa qqzaj ohb qway
akq nfnes sdrlza nfnes weq
udxpdpx gctuv llhxuow rqtetm hdbnpte oebapv civy oeobu ftgivd pykj
pbgbvn jgmr xrz dfn gosjobw ndf
gnf dtbsnc fwcmml tscdnb fgn qgadusl eifpk
vmnv yuxrup qcphi tanc tnca kjrv cphqi
hclggs sghglc fgplp odn pfglp emkrulf whwtmbs qnuyg
wcxtr ani ain sha hsa zxbkf bzxokat qezo ljqxi xqcwfmd dxo
waiq smpbu dbyka uibxjrg nze wiqa rfpts ddjsjv jqqjez bpusm
lpcxf vsbj owjwc tuqj vkrgrh jsjdepv oil lxrjox frsxsi clr
vzunp prwk nnd rfs vpuzn
pqpqv lvsk sqxf nhobsm hakbn ywj
xxu uxx szqnmi lnwtmx
akq nmlw fupwsth jduvhva
nac wwlxqck hpbce vxxqa fyp xvxqa kxwclqw yvlmv bfwi
pzxjbj nvwv mdooiez vvftp enjrsck iypu uhru fpx omtd
llxgp qwf pwaj cuhb scloot hbcu jgp vjw ooclst
sisd akawvzd wvdzkaa gyoij ikt eeeosb jiwiup
tche vxj sbctqv jvx gosur usgor ibo yqxo qqgd zspl
cidd welisl fxblxqk qxbklfx fbdoqcz glhq iylodvz zvds ghlq
cnsa hrxst mrnkqtj bptq jmi cpbcofs kveyeur uzmga modphm rtx kntqjrm
dvyup usfaq rtghoec bvcos fqsua zohwwg
onf vncybi dlaxni oqyqqkn
okfwa qyyx ebnv llql nphq etdt ytgivlo jwgwz kiob
ann vqnqvpx wth lpwid bjvzw xpwqxcj azg ioeyzzp onwf
smy epzomx xep yid zctvrfj astdj cfg fgc eriuxt
rljqgin wzobzrh cuwtx vcsbx tmg tuysq vxipgho
ewp rsrnsj wgeyin lrji ddgt utol xxwut fjiwopa
upu ftvqbk tfkvbq fdwga rmu puu hbiasjw
cfl lmqkb lfc wbtlfi uqsjs ejgmphi tbliwf nzcela gzb
zop unwmiu acull mkwh hvruknw rfk mmhaz iqmenq fifino
iczua bjut tlgf zicau jtbu
mtka ipd mdifj kps
irqkysw xfsjl tedx yckkbx iktxb sqxn pbfvubv uudzppz
mdrn cihat wcext kufs awwtjok pfjg
wdevt tyo zzbp pqlqq wdevt
yhatqkv ntuhw tdfd buxazh xbcsv bas gkv rbzi tddf jbj bsa
malip hiiy qezz yhii wlfojre
zqnfll bssveq lprwbep bhqml tztbt
npnxotu yupdytb jptqo klfydfe fpucmfq svxcqr unopxnt
gdpz gwj iytiohu efk ctjzf asade abhotq brmhu tbtdur zzksbh
kxft klzslf tjdzciy lzslkf
ejei ezmemvg xlt zte tbwhz dgnfpao zotck wus uaz gbwbb
dgednf vypmbs eiytot empfmny
uopmui uehue wdvzt adpfcif mutl ifaztka vydi xumtz orstno
dleero olxiq gxnlfm nfmxlg wloeavr olhrwg hrjd yicj ymyeex qav gxyjgfq
hevj rqcne zycgb qgqtn rqcne ptfvu yyyu zlm hevj
zrkhuh sttnkt hkuzhr vqtu
ppsfm kcao qjq dgadglx cxaawjn pbucfu fed qgioarc dfe ricoaqg
vmawf oktunea zraoir gkt zraoir jcvkqoq
mqgml ecawug ugwace szwul iwbmooj owmiojb
auggaw cypcuw npci vuyxijd pofswjx vdkrgx xylk rom ksj
qmwx jgsrdj ikva xzxw avik
zzhcqu rbg pywjdn wyndpj zchuqz
wzd wqycftu yldezp zovuy oydia hovewe
kfid qkkk thak qhbf rvzlzvu uuxh pbj hkat gow oeqcw knqqzha
sua itv hfpg bdqye bznlrk hfpg bdqye kvir kaai ggtz jqn
ulggl guitamm tkpckso fupacz otxtqpd jxnqc
ueesb ndyik vjftz jgqqv nrcf
krh dqpmsw fybzynl zhjbvkw exefc rhs neq ldprb bhhvxm pjwirun
ymavl qwxr yavml wagwc ekokrpq zewppw iumcgin cxdvwx
wwdukav kuawvwd kowv dkwvuwa
eazot bil tzu vdwwbm fvauwrq
esq tixokph yspf ztoxfut lgzush pwv swh pwv auqhuu tixokph
pdbeyxi poio mugfkb brwbbx aao uszw fokjeb uswz
sbs ryjr ptispi tvnhu htunv vthnu
czjmg hbdjhvi jrkoy fpgwc syafy aar kvnq eaecsb wqzpx
twtp dvl uvyje qtlzj dsvyr qpjnj eyoigx bhgpccy gwn dtuf
mxit xunctu vbyks wmqc jriuupl ybvks uncutx nsoxwrb ykt prc
yye mgf uhc irowpc dsdv iwaxod ftavlj dxzp tcch tcch mefz
rxe xwrrgl xwrrgl duu rxe xbbgoe
ucsz akswcd ojrmqq cox hgfh lxwu ltnnf cenikcp
opjhdp svwezr svwezr opjhdp
qojlkl ircxqnt utfmdg fcvr vehkcvt ufmzcpv xwlh ddavv xel bwlz fii
rzkayeh iursm zhily hdnq fqydfvt uwoy hptpiqu tdqy bgr xdr
ymruz umzry hbltwya jhwhzk flh tahylbw bdbaimb qscbp ntkuf
uxpato owsqyao vaog oenomkc usrmnc epua vzkppls
qxqczbk qyguz alawj xgjawtw wxtjgwa snfcdmz
fjfgos rmpd mgs vbk dlls jkljao eoovdfb ucdvaoq qmjmqku ney porr
nmcrqz zcoxpk dlnzksd ymh zyg spxss ruyk bychq gsgv eusiuid mnrqcz
jbzadnx lzl sdamer okoico frqisrm lxet agriw
xceoqr qai vahc jjzifsn exg
igjpn wfy ukn aag quro wklsq cjq bgtjrdz gmub wyhh
fzlwnm mygfn vkzwvw zvhsex gfki
ijvzgai ebmeq wssfmbq uguh sfuutm nwkgmex dxael liakdxs rnf sky yowpxc
bjzkyjh fced nji esowk qxsubsk qgtts
nkdgo bbjfq fgnxnhd gfjchl jetdb xubsgj eiju ldlm oxsx znft bbqfj
xovcnob pxfe pmstes yzkdm iqlvha nmcziix fexp ivqalh rxecqps
xpyew xudfud wwqe qhfjlcu epv fnrbgyv ihli qngtx yjlfg ozqbzn esp
timl gcohx vqzic gzm shwlkkv icqzv urchuc
xpqq gaqzwo cci dowahsr gaqzwo
jjsagdl umbpxre kyre zvaryft tmw pxpnjy
aqovcz nunq nnuq xjrvvh autjmit jiatumt
elg lps lge zjjot hwz tmqrup xaxxmo zlbzp uftd fukdad kvpymsm
iokwzal ywti zbdmzbu lprywe wbgbwza ypogbga kzliwao wstqi eqm keaeaj gbabwwz
lwfpk mhufe eddzgd ljxyqy vhzkct uemhf
lwqil fzugdo faq feppo usl llwqi
nje hthr ropq qvcepu bexszfj avmzjvv zajmvvv fhcd xnc cnx qnuaux
kvksn dphbyz nsx wrcc ccrw
nzpa pzzunfv ygzjy gxrrtcj hrt trh pwxpg yifgjmo fnupzzv wbzx
aepti rbojui ypvhe ubojri tcema aan dntkw qjx bfvmyos tcm hvoqytn
qpwq exu jvsiwj gsw avr vbemldy
xsbzpf xbzyvx xax sxh vpxt gccy xxa zhgbwoa hwwxoky fhvdxfc pvtx
pnsa ovtjolz tyutl eyjjzt jvtoolz owbypvr tytlu ewtzgec
cyg dwwk eihsp aeuk bbnay aluwyz hdmv uaek mwt ihpse wjhnkeg
fhzx vjetz vjub tejvz
ewwyb jidhu pyvyenn igtnyd tiwr akwkkbi myz xxjwb jjrdeg
jbkuw kwir rkiw ubwkj
bltffuw lftwufb hhsh wfbtulf nrxaa rlszi toijxnz czlci
bqrm pga zgblgcw pgwhhn lcgzwbg bcgzlgw yqb
mhjj vjoa gnjlc kclcr ito ofksy giavy fpqeioj
bkiqmif izidbui sttxxi bswhkxp sduuw
mjgnvw mjgwnv ojzyuv gvj
qxn kkhc whd fgwk auzugg augzgu kqfov wfgk
spdxbnu xpfofsb bpfsoxf ahjywql spbxoff
bwqxhlm wbqlxmh kqgpl fyzgf guhkvgx ovk qhmp gnrmu wvd wedj
vvwf hcnc vvwsngj qedzoxm hcnc qedzoxm kjthdi cbwqep qtvu
gio iqklmro noqablo bab jiqc rwebyg rqkloim wzmgs uunl amqs iwj
snxj szobqt zcgvwv wiyqknu
uto jteikwd cew gqsks hmvjtcy sach
zpgl qnkoex amhufmr figns upv xezrl rjleak nwrna
pzkvrdz dtonazj gtr gfxucuf lstjl lsjtl rgkope kzpdzrv lyptn zfxjys ttk
ddxgm lumlgki jhv doft kok swy ckds swy ddxgm lbfbdv
qfs rcufzgz iaiqw qfs qfs
nvkbo sgv mquwb ritpye nbkov poex hraorm qrrr qdt qefl
irxannd fiud ehyb ggx plqg pvvn uuptop tcvbm abuf bcfnmw
qwya ukblz epmbfr vmlon yqwa
hlo mmv vmm mvm
svzpxun yugbbe sbbpxs dmy xspbbs zhpovyf fyovhzp cpbt pke
zgk gft zybs zrgcoo ypu bue htgo
xnesq srsx pkzaoh cfqzugh
lntd nvxetbv clykjpd svmibpx evxtvnb yldkpjc
jsqq tzwak hephg eqwczd ioisa yim tmdifn mceip
kuwqz wzkqu zwchmj lfec uexne iztp llityt
kvamkpc pvbryqh ion cwizjde gln kcpvmak pzzlw gnl
ydeqf bfaab sydqhbp smsxdjr pynrs cqymt
onb eiab bno nob
mqslq scnelxv hyllrf scnelxv mqslq wmnbk
pttu kubby lgop bbyuk gsk skg ikktlbb inbyvz
xznvl zwtdj vbxdyd clhw
hgy zudelp ickc drfjgn iyws xhc
zzv wik iorhat qkb kjb lykdz vrce yjsjwj
gyw xzgbi efus uuy
hwcy ujdun bjjuvd jbdvju onnk xeyy mmp onkn qyzl
jwfm ptjwrbl hhuv uolz adyweh qpj wxyogp igvnojq jmfw pqs fsnirby"""


def goodPass(line):
    for i in range(len(line.split())):
        word = line.split()[i]
        for other in line.split()[i + 1:]:
            if sorted(word) == sorted(other):
                return False
    return True


sum = 0
for line in s.splitlines():
    if goodPass(line):
        sum += 1
print(sum)

# day 5

s = """0
2
2
-2
-2
-2
1
2
2
-1
-4
-8
-7
-11
0
-13
-8
-7
-13
-11
-15
-4
-10
-10
-22
-22
-1
-9
1
2
-23
-4
-31
-3
2
-34
-28
-28
-16
-1
-34
-13
-25
1
-14
-40
-11
-32
-25
-17
-43
-23
-3
-52
-31
-8
-15
-48
-13
-56
-37
-24
-25
-47
-38
0
-35
-65
-63
-40
-18
-55
-11
-8
-18
-53
-39
-20
0
-6
-75
-22
-36
-71
-61
-74
-11
-14
-35
-54
-41
-59
-51
-45
-62
-53
-8
-26
-22
-16
-66
-87
-11
-59
-9
-44
-73
-76
-3
-78
-4
-45
-10
-38
-20
-102
-114
-44
-21
-111
-118
0
-80
-65
-28
-51
-95
-42
-31
-41
-98
-39
-89
-116
-115
-30
-68
-52
-21
-17
-92
-136
-24
-16
-13
-110
-10
-44
1
-89
-110
-99
-4
-106
-35
-7
-152
-147
-38
-17
-44
-148
-144
-48
-78
-154
-141
-23
-145
-55
-87
-97
-20
-66
-172
-82
-23
-23
-145
-37
-103
-138
-111
-105
-148
-67
-163
-59
-127
-130
-24
-102
-153
-149
-58
-33
-37
-28
-75
-103
-10
1
-36
-130
-59
-70
-76
-181
-196
-165
-131
-71
-142
-183
-65
-55
-50
-112
-153
-59
-35
-198
-175
-197
-89
-197
-99
-52
-187
-55
-158
-117
-164
-205
-91
-68
-126
-158
-172
-217
-111
-106
-42
-135
-82
-213
-22
-1
-238
-204
-77
-123
-174
-29
-30
-90
-98
-5
-30
-52
-150
-155
-23
-14
-102
-47
-215
-112
-51
-2
0
-62
-138
-255
-227
-17
-114
-34
-28
-139
-226
-258
-18
0
-24
-161
-170
-12
-25
-12
-122
-238
-249
-81
-267
-236
-145
-242
-124
-78
-122
-141
-135
-9
-195
-98
-269
-221
-154
-106
-247
-88
-221
-9
-97
-207
-61
-102
-130
-54
-112
-61
-65
-82
-35
-150
-114
-180
-314
-317
-305
-28
-305
-294
-90
-133
-11
-1
-108
-1
-268
-257
-117
-245
-94
-313
-293
-174
-312
-61
-205
-3
-199
-95
-323
-34
-176
-241
-89
-346
-208
-270
-77
-253
-86
-167
-318
-70
-258
-76
-203
-91
-62
-329
-156
-235
-239
-191
-119
-285
-128
-155
-82
-36
-351
-373
-8
-36
-132
-183
-311
-274
-111
-175
-193
-72
-340
-64
-26
-378
-202
-194
-188
-169
-71
-197
-344
-193
-6
-63
-368
-313
-376
-42
-241
-50
-64
-354
-338
-177
-154
-420
-418
-349
-383
-340
-177
-227
-332
-145
-402
-66
-290
-274
-287
-68
-91
-49
-312
-106
-264
-173
-362
-252
-138
-218
-211
-39
-271
-261
-306
-372
-391
-408
-108
-308
-418
-395
-413
-208
-13
-41
-249
-297
-21
-274
-440
-205
-272
-371
-155
-357
-34
-97
-121
-221
-173
-364
-168
-83
-317
-414
-427
-90
-216
-91
-306
-467
-366
-486
-461
-34
-327
-474
-164
-160
-410
-366
-467
-206
-435
-167
-326
-423
-241
-45
-18
-59
-498
-483
-380
-431
-256
-254
-415
-18
-461
-223
-152
-179
-8
-169
-41
-452
-302
-172
-249
-5
-40
-97
-39
-492
-40
-460
-276
-442
-413
-220
-376
-389
-446
-133
-228
-364
-215
-133
-304
-234
-275
-463
-267
-147
-162
-227
-532
-216
-479
-61
-409
-376
-389
-283
-332
-97
-66
-486
-223
-522
-359
-340
-211
-401
-98
-249
-511
-238
-72
-473
-132
-450
-321
-455
-451
-140
-495
-212
-235
-213
-22
-111
-236
-390
-104
-230
-569
-45
-43
-264
-561
-552
-32
-403
-17
-288
-255
-436
-363
-495
-19
-358
-250
-59
-172
-77
-558
-211
-555
-65
-419
-282
-472
-72
-462
-276
-508
-489
-184
-486
-500
-143
-627
-506
-84
-368
-355
-467
-515
-415
-314
-386
-114
-319
-237
-113
-611
-17
-532
-181
-568
-132
-178
-276
-258
-384
-295
-208
-471
-622
-173
-531
-192
-231
-338
-427
-416
-591
-112
-511
-538
-357
-189
-186
-100
-458
-331
-85
-294
-375
-206
-377
-92
-504
-558
-26
-73
-103
-455
-397
-164
-683
-615
-321
-310
-76
-576
-291
-523
-163
-452
-236
-488
-588
-24
-52
-673
-176
-282
-642
-668
-517
-575
-173
-517
-565
-385
-202
-587
-519
-694
-493
-181
-241
-630
-597
-377
-560
-646
-100
-544
-135
-695
-460
-621
-97
-376
-511
-413
-613
-238
-160
-141
-329
-682
-664
-439
-730
-646
-266
-477
-233
-722
-687
-605
-483
-648
-685
-735
-739
-630
-644
-498
-652
-493
-508
-108
-32
-620
-185
-422
-187
-112
-263
-568
-599
-751
-768
-640
-440
-451
-760
-156
-425
-662
-764
-503
-521
-140
-425
-72
-242
-403
-778
-689
-693
-541
-674
-93
-545
-601
-730
-305
-743
-563
-315
-637
-126
-260
-463
-309
-538
-59
-368
-382
-355
-414
-97
-93
-475
-445
-319
-783
-411
-338
-480
-755
-149
-821
-813
-229
-116
-488
-741
-669
-442
-627
-403
-129
-829
-664
-357
-686
-835
-172
-80
-367
-789
-573
-199
-795
-221
-177
-543
-117
-651
-382
-731
-842
-125
-397
-328
-69
-388
-381
1
-737
-199
-181
-264
-577
-63
-616
-333
-413
-616
-189
-315
-237
-608
-497
-348
-285
-863
-97
-745
-716
-666
-165
-522
-631
-438
-639
-443
-122
-521
-48
-501
-895
-205
-57
-576
-644
-442
-143
-215
-661
-749
-247
-298
-387
-601
-525
-383
-9
-64
-416
-423
-522
-631
-890
-867
-649
-525
-228
-544
-54
-878
-277
-924
-838
-885
-477
-256
-330
-301
-815
-722
-646
-677
-70
-917
-126
-832
-479
-849
-591
-66
-260
-524
-603
-86
-397
-63
-299
-417
-375
-909
-489
-872
-930
-638
-280
-440
-788
-818
-398
-765
-229
-346
-864
-155
-57
-686
-850
-84
-783
-191
-923
-740
-454
-118
-807
-662
-859
-99
-139
-272
-640
-166
-935
-805
-351
-413
-467
-535
-377
-97
-204
-262
-4
-704
-516
-459
-702
-718
-241
-534
-318
-955
-519
-675
-766
-671
-843
-861
-214
-4
-828
-638
-833
-953
-521
-17
-87
-393
-951
-17
-529
-49
-299
-673
-119
-185
-601
-187
-399
-646
-812
-627
-121
-535
-155
-601
-196
-365
-366
-409
-596
-803
-508
-988
-529
-925"""
lines = list(map(int, s.splitlines()))
current, jumps = 0, 0
while current in range(0, len(lines)):
    jumps += 1
    old = current
    current += lines[current]
    if lines[old] < 3:
        lines[old] += 1
    else:
        lines[old] -= 1
print(jumps)

# day 6

s = '10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6'
l = list(map(int, s.split()))


def doRound(l):
    maxIndex = l.index(max(l))
    maxValue = max(l)
    l[maxIndex] = 0
    for i in range(maxValue):
        l[(maxIndex+1+i) % len(l)] += 1


stored = []
count = 0
while True:
    stored.append(list(l))
    doRound(l)
    count += 1
    if l in stored:
        print(count - stored.index(l))
        break

# day 7

s = """nzyiue (57)
pdmkag (39)
bogbg (13)
nubay (45)
dukzh (17)
kpjxln (44) -> dzzbvkv, gzdxgvj, wsocb, jidxg
cxjyxl (83)
vusplt (151) -> mcfst, orrwx
mxrfq (98)
bdoez (62)
vrajpg (78)
qzsowpu (90)
nrxoha (51)
xtjrkv (351) -> jlbhafs, pyocxtt
rlnii (18986) -> xjosf, ljvpv, wkumzkr
ddrrgp (23)
wladmn (42)
ryskzh (209) -> wsyya, xbqpjo
jbjkp (34)
fnfiur (86)
zxzkl (82)
hbmxey (1869) -> khkuxc, mjuwde, tztycfl, miauii
zjyqcfa (97)
zbtck (48)
mgsasl (39)
cemygp (34)
iolrkmv (139) -> rntjx, itxtmhb
jzmqzl (1446) -> pptocz, mwfryd, utgkveb, sflwom
wagpkyw (88)
saiyjff (67)
kwwhb (219) -> htvpmr, rojhup
huspq (74)
mzrafi (44)
fchlc (89)
ezkddph (62)
zehnmg (5)
tgirh (50)
xantdh (73)
zicvvl (10)
kcimi (86) -> uwizfa, kmhyz, wagpkyw, iuovz
wsocb (64)
aemffo (284) -> dukzh, vczudlu, tpubu
gfgoc (18)
bmovg (80)
trsnrjd (89) -> oujkd, fstzdn
bmqiwai (12928) -> yqeaqcn, cgzyc, bwgkn, giftd, hdhvzi
ktehtif (151) -> fvplhrm, jesphm
jkfyg (76) -> ajeisgv, jfrooen, hvhtokr
dkfepj (1970) -> tgirh, mnsqjxv
jjseenh (99)
jvpecm (7) -> dpyuayl, lyigbhi, bflxonp, tvcyh, tddik
silklk (59)
swscfel (68)
dilefzx (89)
spthyf (75)
tiiwbg (17)
ayqgp (58)
qhygx (14)
hqccsb (26) -> bdkfx, srrxb
lbojqfo (34)
arbebt (32)
fsvkj (115) -> ftqtzxk, twzgms, otvvje
sdigtox (39)
awsphe (79)
lftlc (35)
apzabs (68)
aboilvw (452)
rntylx (44)
xhhfsuw (280)
yucwtc (41)
qlgkqk (54) -> sqfrw, acdkw, ycinfxk, wcinck, hyfswg
thneyz (57)
pplkoa (79)
vsxzpf (197) -> spyxh, yvcbk, fkmccg
miymiit (1002) -> lmmeg, jxulvx, yqergs
jaamgi (45)
tvwosmc (1462) -> frvmu, qmfmfxh, jemmk
ngemsu (85)
ohiftl (143) -> loggp, xhwfcu
bztor (157) -> gjfkx, grsdifs, spchmoq
tifkr (52)
kgctcau (82)
yvcbk (32)
srvwd (1234) -> dxerl, pzjsf, yqyyoj
xrise (358)
biwdu (70) -> kvpju, hlullj, bfpvsfz, fvfitqc
utgkveb (76) -> fmhjs, pplkoa, mznkfco
mvhqou (22) -> njgzn, okfcek, zjyqcfa, culvtcm
gadyi (398) -> ndxim, efwhif
ujzofuy (39)
jjgem (852) -> hnvybq, gnffzh, fbuklc
rbucosf (122) -> jvpgl, yuhioxl
ffxnegs (222) -> zfcylzq, xjxjaq, cocau, vusplt, cjlxgf, yjonn, iazte
wrtyhxg (403) -> zqckoxe, vindf, jbvugg, idivffq
imbpvgl (52)
frrvvai (193) -> gxcnp, zvjrwke
ywlrls (31) -> gqdxrur, dfyqo, cxndroi, gbpcav
olzdhtj (42)
thvjlgo (76) -> cufudi, jdyspx
jearhat (57)
jxanwhq (27)
wsyya (98)
tahstqe (37)
dyvooj (80)
yuypmb (98)
uehdbi (26)
inspqeu (34)
nxqqsza (119) -> guxwd, iyxkzat
jgkmy (86)
hllzej (154) -> sodrm, ekfpabq, utqxb
gcbvf (68)
ctoxz (98)
advlxrg (22)
eetxll (37)
lmpauyz (72)
lwxts (76)
rkuyxrc (55)
pitdti (55)
ucjew (91)
gynwftf (91)
czojwyg (15)
uigoxw (75)
rcjqfuo (129) -> lgoak, zcomcn
vvkbav (56)
npcyutn (35)
jfaoy (57)
iqcgwzk (58) -> pdepl, zxeopkg, dukqd, gxdtiob, ylnvdoq
rqnsxm (2056) -> jaxig, bolxwme, dgsse
bsyiv (38)
hhnpg (164) -> dmvajb, pvwdkm
oydoajo (87)
fowpeur (85)
ycnih (17)
zwpyj (12)
wpprf (97) -> fdthu, sxslizl
icqsww (55)
ckedyqu (54)
ageyuq (19)
ebrgtq (112) -> bochc, wqdvql, ogafygg
ygteuy (89)
tuhxr (76)
rvuvico (91)
ecjujqu (92)
tvhgbau (79)
zvsnz (26)
fquywyi (308)
gqrgh (24)
zcfswa (37)
hkbxj (55)
cnknlru (70) -> udfuty, sawqp
jljnags (38)
tztycfl (939) -> rrtqyew, gqzemw, hsfxq
xzyri (187) -> yakzm, zkikhk
sdzoy (51)
ojtrl (130) -> hpgktb, pjkwlmk, phkvcix, zguqo
lyhok (95) -> hdpemqh, nfvsrpa, bwthm, bilzbf, nrlvovz, iqcgwzk, sljgt
hpanc (17)
ykvtr (51)
qbbmsf (97)
ppfyonm (98) -> ylwniqh, ecjrblb
jdsdqzd (32)
oujkd (97)
dpija (23)
pdjnnzd (85)
ghzqyv (37)
yvlxoom (58) -> yxoqwg, wgwkss
gjupqe (180) -> oszyw, zyqqzou
qmfmfxh (7) -> rkgxu, unrhnl
hxlefwp (268) -> yablonq, ouxjkf
fdthu (86)
voonmio (63)
uxlcvt (143) -> scipnb, veutu
xybcccw (7)
inomnjg (91)
gfuxooq (221) -> aceiy, axtzeb
xirqz (71)
tuqzsn (73) -> hueqfk, hcyohc, nerlvh
jaxig (82) -> llofnny, snvqyqb
czztmlk (61)
ffrilz (148) -> qnvzqc, ckedyqu
ejslpy (5616) -> wwcih, jzdmjdf, gnrqrsj, ayirpk, kvifa, bapvub
bfwbkxq (493) -> hiqhe, ouqwmnj, wqxcn, jkfyg
upftju (48)
bqcizg (67)
mkyqul (5)
wjjar (296) -> ywutc, nsvrfae
pabgfh (244) -> bogbg, hgcxyx, siisskc
oltky (7)
aeapmwq (76)
btjxv (35) -> wpgyc, ripmztc
onuxzz (247)
ahayh (54732) -> byrvfhp, rokie, ejslpy
idooz (192) -> owxuzp, uehdbi
ghjpcv (162) -> xucdiz, ygrbgm, yxqesmi, ebktv
zhffrzu (42)
bpygf (26)
tojpm (42)
iihzs (67) -> hkbxj, enekg
ydpihb (46)
rgssc (27)
dkgsvl (82)
qrfhxne (65)
sntuz (68)
oznhe (98) -> tgvdjhh, cpvlq
evfqyvl (304)
qftqq (27)
yxcbn (11)
buifcn (15)
xbpqmua (25)
vjroix (85)
evqrr (48)
unrhnl (88)
ihuzl (35)
giftd (1250) -> zbedu, vyaoad, qcolnc
uqjmbb (17)
egulpbe (80)
fpmwz (218)
nihmyu (98)
avaoo (176) -> xxshup, xsufhnb
fmqon (61)
mbokr (57)
gprznw (41)
bflxonp (105) -> pdmsm, jearhat
oylgfzb (65) -> rugzyaj, hbgyu, rlnii, gwznzk, bmqiwai
cepqh (19)
hfjhadi (58)
ajtkddh (60)
vyadxnv (94) -> pyntdrr, mdpcfvu, cbvjwlo, ijleirw, sltrdk, adueu, qlkqplv
anvvug (1847) -> tfuxhhz, kgctcau
tjobe (129) -> hdspavt, mcduq
qvgeei (273)
dkxsqjt (1416) -> cuwqi, fcoxtp, yvlxoom
urwgjd (39)
vxqcf (105) -> gfnapwr, lmpauyz
etnkepp (5)
koyke (15)
qqhjlu (78)
glguoq (75)
hdvfyp (7) -> eoaprcr, cksyln, hknzmvs
pqvid (15)
jesphm (6)
bdkfx (81)
gqdxrur (77)
fmifd (94)
ijiqjtf (63)
dfyqo (77)
spchmoq (31)
tvcyh (149) -> lqbtnb, matcdld
ilzwrk (64)
tdtznh (64) -> phacwjs, offas
tygst (91)
uzjoys (198) -> bgcjrf, zdrfiw
wfbuzbg (47) -> qpuyqq, ajrcal
kwqcbe (19)
qdovgra (303) -> zziyhz, gfgoc
vfcbliu (19)
fwtfkp (325)
rmdqvgh (61)
dtjzr (28)
cocau (77) -> ficmghd, nkejtw, qowyx
aftsom (70)
fsmzljm (123) -> tatjry, hnfeims
lwufmc (45)
fzzcxvm (61)
cxokosi (70) -> sszzop, gatdr
mmlra (32) -> wdlwryo, wpprf, jexreg, lzowumq, rcjqfuo, lhnevgo, smuybnw
tydlqpq (160) -> fsbojm, mjlmuca
oevvote (68) -> silklk, polrzc, erysec, xoyjtol
fxsatsm (83) -> sntuz, qgxcbt
cvvtz (80) -> vpjhl, rgssc
feonsg (74)
htvpmr (7)
gqzemw (43) -> pxdgkik, jtvntr
pvpqoq (17)
ldfmurk (88) -> fubtwbq, ycawl, sqsqge, aemffo, mszwp
aufym (51)
ldflo (188)
izyjved (5)
zgydn (72)
cqfri (9)
ytnti (150) -> lamtp, fugeht
appkqpe (95)
sjxbk (117) -> tinbqcj, amwtic
fbvvrqt (81)
vlwjehz (22)
lwhev (44) -> zesvlul, wmwzhjg, hpjgrb, sxbusu
hugfkt (42)
tnobvt (18)
zesvlul (73)
gfnapwr (72)
tabzzo (62) -> rvuvico, inomnjg
ixdcgsa (177) -> gmhxee, cogovv
fnvgp (85)
awhwxdm (91)
frgot (59)
boete (78) -> ionnnfx, vytdgko, ouhfxyf
ikxewmm (14)
qfkka (49)
xidye (11)
krdlzf (115)
hxjhcuc (694) -> miuvc, iolrkmv, trsnrjd
ikbkb (136) -> uigoxw, spthyf
yqeaqcn (53) -> qysdgq, mkjvhl, evfqyvl, bhzbv, usuujhq, hxlefwp
dnrxyh (887) -> xthhlfy, fxsatsm, cqpns, xzyri
siswh (41)
pfxrf (51)
dlzgufq (7462) -> ldfmurk, dnrxyh, dzetsz
whlfwr (46)
gbiluq (11)
euaceg (42)
iwdesog (152) -> cqyluwl, dbeskg
afjmzb (15)
sofxmjx (83)
ortcrq (18)
phacwjs (58)
uiwgpi (995) -> hqvvrd, caihc, rvxed
oiyxr (86) -> zibbm, sbklnq
yukoxaw (27)
orrwx (47)
tlxbtng (44)
ayirpk (1850) -> cdkcn, wbllfh, xounvb
lqjznss (67)
mldkiku (55)
dyfhy (58)
jxulvx (34) -> ujzjt, ykmej
yuhioxl (20)
uwiza (106) -> lddiw, hxaza, bnvjmae, oltky
hpsxqdm (41) -> luzcpkn, azdklp, rupdbwl, vwqog
fubtwbq (211) -> bdoez, ezkddph
cwgbjaq (41)
kmhyz (88)
tpubu (17)
bfrbwb (27)
mgwauar (8)
ixwyi (13)
ljugvh (7) -> nxrkz, gnwjseo, ibjbozh, iaiywwa, pcdtne, nvtbk, vobfi
rcongvf (20)
csqyn (46)
ygbyt (15)
gwznzk (11) -> ehqavsc, yimottm, heuyaxx, yirkbjn, fqhag, ovqhdvy, zzxlo
wwcih (1585) -> dyveac, pejho, cyfuwdb, tojnst
alqog (157) -> dyvooj, wvkaie
qecgvu (19)
jexreg (209) -> bonnse, phgkg
vbisx (49)
bcukkvc (72)
trcbs (90)
xjxjaq (211) -> kfhwxyy, vnmxsi
uptgby (16) -> eocoy, lqjznss, petluuh
rjnht (63)
urhwog (146) -> mxscf, fwqru
caihc (158) -> kzjkjz, rjijdre
mwjtydb (15)
eqahcc (73)
rntjx (72)
ripmztc (96)
cksyln (93)
ktfeae (20) -> asoirn, jbxnffu, feonsg
bdukt (71)
jtxbfm (55)
ebwtpod (66)
fjerhwe (50)
xxshup (66)
jdyspx (97)
nyxiai (73) -> pjmci, ejvaoj, fbiqxqk
dxznun (49)
umwial (183)
mnsqjxv (50)
wtoive (80) -> nfcru, goicjt
zkzefwh (22)
oszyw (78)
ekxdjlp (60)
tymor (6)
jbydxyp (66)
dzlqgrt (43)
grsdifs (31)
pdepl (238) -> ulezwmd, fhlul
mbunh (8)
iwajy (70)
lknchr (68) -> nercz, skmvkj
klpctiz (75)
lazlx (8)
fbuhz (159) -> aarioi, fbrvfk
kvifa (69) -> fquywyi, ndmcgpn, vczcept, rjhfcl, jatvkwy, fodud, avaoo
ilydn (74)
nerlvh (85)
qqduoo (735) -> wgglzpb, tcrkcu, boete
gfxnuuk (34)
amwtic (72)
ltpban (87)
klyso (67) -> qenjyl, egabi, hmdwqdq
jotxc (57)
cqyluwl (9)
siyuvy (52)
bbsomm (61) -> izonhi, jjseenh
pzjsf (49) -> etnuzv, hrrampl
vshekb (34)
zvjrwke (27)
xekggcw (89) -> tvwosmc, dpfov, anvvug, fneqe
hsulvq (78)
idivffq (292)
bapvub (821) -> acnvtg, lvkpx, zeopgv, dcpnyer
ziwkz (331) -> eqzuic, qrtwjv
bvock (81)
vsyuckp (54)
bsoef (40)
ncjhpa (247)
axtzeb (13)
yotlucw (134) -> jbydxyp, ebwtpod
ceqfbbl (33)
qhbotj (62)
hrmpq (90)
pgznzly (13)
vgndgst (72)
auvla (65)
ylnvdoq (350)
fgxst (8)
pptocz (287) -> werriw, hglhjt
lqbtnb (35)
xvuri (293)
dbeskg (9)
crkapwa (87) -> ogpka, npdwg
bilzbf (803) -> brkux, qcoyrha, cplvif
byrvfhp (80) -> gqgewi, csear, vyadxnv, rqnsxm, cgjula, luuxtc, jzmqzl
cqiipxn (84)
oryrq (103) -> cabsaub, zfthi, palqky
gkzeqaw (38) -> iyflfx, hntdp
xqnrp (33)
zcomcn (70)
tjcpka (87)
nfcru (41)
vfpdqlb (43)
msdff (82)
tddik (43) -> vlthh, btbses
qlmojkv (264) -> tymor, xkfuzi, ligpl
sodrm (37)
mvvgro (84)
cbvjwlo (270) -> nsqzndf, synjm
kowco (46) -> gqrgh, nhxmab
xrapmvb (150)
iifltp (95) -> fowpeur, vjroix
tinbqcj (72)
lbjuqcd (19)
hlhomy (30) -> oylgfzb, ahayh, razvskj, hvtvcpz, teyrfjn, lqirhg, dxxty
veutu (53)
tfuxhhz (82)
oenrkia (44)
oipjwtz (40) -> tgqpp, mjbjv
ndcjr (75)
oermd (94)
xsmgj (99)
cfmhi (107) -> obrwb, hoelsa
nwyftp (72)
nmdhmy (39)
qslgo (92)
mjbjv (89)
hhvqa (41)
erysec (59)
xdnuvji (20)
bfxezgb (8)
njmrq (192) -> uufrda, pdmkag
gutukz (70)
acjtwvt (98)
kddchk (71)
apzjw (149) -> jetfvjc, peomyg
xzhvvy (431) -> ehxkgh, alcpfsx, kvjqli, tjdap
sowzlz (19)
ucvgxii (85)
uzprmq (83) -> ygteuy, exhxs, pfzqe
bvaor (35)
gekcx (78)
cxlip (44)
psnkhtd (157)
yimottm (2101) -> fsmzljm, uptgby, tvhfxfo, ickxyrm, nxqqsza
ocbxx (66)
acnvtg (277) -> wbbfe, nchjk
vangx (51) -> xobyzo, jdhiflw
sfoivjz (17)
lunbob (66)
ecabcm (190) -> vlwjehz, advlxrg
qarjx (7)
gyktq (98)
imfog (52)
zsdvfrk (1190) -> vxqcf, fvivhx, oxyxy
zssgj (44)
efbffd (20)
etdofb (62)
juakl (67)
iltti (60)
ffgoyk (74) -> jgdumgz, ltpban
lamtp (89)
loggp (75)
pejho (106) -> mqaajk, tnobvt, gxhia
enekg (55)
cplvif (95) -> xfanpad, uhepxt, lebqr, hqipq
dgsse (88) -> nwztmzp, akrgdse
rwjzc (107) -> qrfhxne, lcufpmj, paqlttl
drszzbe (132) -> ucjew, unfgdb, tokvgmd
vtnpx (79)
rrkhcl (26) -> seazs, koemv, qnxnatu
ekfpabq (37)
pwvmmda (278) -> rntylx, hrkswsk, zssgj
vqekr (85)
luccp (175) -> ebrgtq, rvuktmb, pslyfi
xkfuzi (6)
obaorae (45)
dpfov (96) -> roqnodm, adasbyp, uorpbn, zyonam, zjcdwr
lzowumq (41) -> sjthmr, mtboq, aeapmwq
pynxen (152) -> omzpkv, rwuxn, dpija, xgogpx
itxtmhb (72)
hanbscg (21) -> npsza, jdjaem, lvuzab, fffxc
teyrfjn (62414) -> ilfgats, qlgkqk, vyvcb, rnsxz
pocxfrt (39)
mqecf (76)
cpacyeu (67)
gycde (88)
tlhgrte (2388) -> xijwk, mmlra, ejtoqaj
jumdfk (64)
swsffrv (13)
fujvp (155) -> gwxkdy, hsftfol
dyxcd (87)
ljvpv (452) -> huutnfp, hoauxku, euvkg
xydxl (88)
ibdiplp (20)
xvwqzt (70) -> ppdsem, pyhqixj, rjnht
djmoed (90)
raioiq (134) -> ipdbccy, inspqeu
bwywt (67)
jfvquxv (70)
mtxzcd (282) -> ucvgxii, ngemsu
lfgmv (87)
lcufpmj (65)
pvwdkm (50)
dbnstqf (56)
jwgjnuu (33)
ndmcgpn (256) -> zvsnz, bpygf
rktkzfw (35)
zxeopkg (218) -> yjyipdp, drnyyes
nutlr (116) -> ybuhf, fjerhwe, xmrcq
cdkcn (39) -> dzlqgrt, vfpdqlb
jfrooen (95)
xmrcq (50)
qpuyqq (83)
hiqhe (361)
xuxlspe (44)
apvfi (59)
wahwi (303) -> lnnii, boxvu
affxphr (22)
lhtzrh (213)
yeewxiw (50)
zyxjqs (65)
kqgqdyg (69) -> yqctq, tcihaf
sqnfwo (67)
mbqkm (12)
mqaajk (18)
nxhetg (60)
hrxfpx (65)
wjfsiec (19) -> znpqzc, xvuri, vsxzpf, doazn, tjbyhjw, czxbmp, vqqrb
hsfxq (99) -> jtxbfm, lzhdsyq
lbiigt (26)
bwgkn (1005) -> uzily, urxxlfo, yqnbqgc, cgnibii
hpjgrb (73)
ajpcyv (42)
pirivl (144) -> bmovg, yexyj
szuiho (73)
lnhiiq (64)
yacaqwf (82)
nqcadtp (310) -> kzvwk, akatbi, gncvcwi
bvgfpab (15)
cxndroi (77)
efwhif (6)
njkxyjn (12)
kvpju (39)
gyyqk (5845) -> jeshqdv, xzhvvy, ynwpoz, jtlhia, gzykr, coyroy, tqjpfzx
jwpqgy (168) -> jxanwhq, fsixon, lnsyuz
jwxff (95) -> ihtomiz, xeprhhl
yycux (15)
fmhjs (79)
wvieaw (67)
iancjuu (39)
vczcept (112) -> muavtro, ipeig
mwtusu (81)
moewgvz (89)
gmfktbe (31)
dcpnyer (67) -> fmjyudw, wuhyc, icccxzg, nufpcxh
hnfeims (47)
rouiui (30) -> tqlentr, zdkil, veqahi, txnzg, euiig, qlmojkv
bppos (37)
hoauxku (219)
ficmghd (56)
lxpshey (95)
hglhjt (13)
oqbet (58)
bsmxm (88) -> trcbs, ewsrnsd, qzsowpu
dxerl (79) -> kdujkg, njkxyjn
gxhia (18)
eqifs (3869) -> aqjkcss, uiwgpi, cmeqx, jwlaj
hqipq (60)
upbmqk (18)
culvtcm (97)
cgdbu (90)
tnrpi (241) -> zjtid, xybcccw
hlullj (39)
ihcbt (44)
wfjgqqm (55)
dmzwm (86)
hvtvcpz (81171) -> dxcpj, eqifs, mdfbhs
uufrda (39)
lsfdgam (77)
huutnfp (57) -> blrzef, ihllda
vnmxsi (17)
tjbyhjw (161) -> ihcbt, tlxbtng, cxlip
fshvy (84) -> indgw, gynwftf
agsjzih (10)
ppdsem (63)
skmvkj (33)
oxyxy (205) -> aawxzzs, tdnzc
ywavdk (67)
pkxhxdz (70) -> gklur, vqekr, fnvgp
xsufhnb (66)
ouhfxyf (97)
dukqd (50) -> opyzwha, sfxsn, ndcjr, uystf
zybvpry (20)
wwobe (34)
bolxwme (74) -> jfvquxv, rsqexkv
adhilml (299) -> cqfri, mhassfj
icrnru (160) -> gutukz, fuega
oagluxi (40)
ligpl (6)
fttsg (255) -> gmfktbe, ebtbnei
ihtomiz (99)
gblxcsj (251) -> kuaeh, pmfpitp
lrvxyg (91) -> lfgmv, ohtzuf
wuhyc (71)
qjuud (160) -> ckexdc, oencfz
jbfzjha (305) -> vbmhjxo, txvuv, mkyqul, zehnmg
xjosf (89) -> dfdgoj, xagwh, xkpulvc, tnrpi
zkcwgx (22)
ilbopwx (87)
akatbi (222) -> qjazr, pizkx
uxuscb (249) -> jpeprwv, mdrir
hbgyu (19007) -> nqcadtp, tkeoe, jvpecm
kjzsi (56)
cduzde (13)
edoftkj (84)
lxisjl (86) -> euqvd, hugfkt
owxuzp (26)
nalhhj (4471) -> dkfepj, wjfsiec, egrga, dkxsqjt
vcaekf (67)
evwne (21) -> czztmlk, fmqon, fzzcxvm, rmdqvgh
crojfnw (171)
upiow (82) -> hukskkk, ilbopwx
srgua (120) -> koyke, hvefi
rcywun (81) -> moewgvz, fchlc
qlkqplv (138) -> hsulvq, ghuoa, ozwaa
czxbmp (197) -> ieeqmzl, yzivqv, arbebt
jjmyu (80)
cyfuwdb (40) -> mywmo, nppdvs, fwafvkf
hmdwqdq (79)
oencfz (10)
pjkjcy (20)
sxxhmpb (8)
uwpwbgy (213) -> gbiluq, xidye
mywmo (40)
rbmmiy (833) -> rwbhl, vtono, shkfk, umwial
dmvajb (50)
smuybnw (89) -> uktqwa, vdistyb
uagezb (984) -> hdvfyp, kwtukd, ikbkb
nrlvovz (840) -> qoipc, oznhe, uvhmzj, kebff
vbmhjxo (5)
ckafg (86)
ovqhdvy (2715) -> psnkhtd, zxqix, trnjhsl
uktqwa (90)
lzhdsyq (55)
kofvzz (66)
mcduq (60)
qnsnc (62)
kwtukd (232) -> nhzmidl, bfrbwb
zzavd (13)
fmjyudw (71)
vcnph (161) -> wqgpm, nnvpkf
lgamzp (64)
ukqcayx (92)
diduy (116) -> xwphya, msdff
izonhi (99)
jetfvjc (16)
rjhfcl (308)
vqqrb (179) -> jfaoy, jhgxtg
tulxdf (308) -> bcukkvc, zgydn
rxuqpgb (144) -> aqogxi, aicncxc
spyxh (32)
yqergs (100) -> kitsxb, woeoaa
bthswyg (34)
rfaxua (81) -> zugxr, dtyxosg
fcoxtp (42) -> aqqdnpb, nkgmg
jbxnffu (74)
bwthm (929) -> jwxff, ohiftl, aqtml
ionnnfx (97)
urigx (141) -> xsmgj, eyozeel
nsggol (249)
mgeseyn (267) -> hvacjk, pvgay
eqzuic (37)
pxdgkik (83)
zjqbfd (188) -> viklkmp, vfcbliu
wivwqm (74)
nowyhln (52)
sqsqge (219) -> amaeuv, paqvyfa
vynvu (87)
ovysqnt (86)
brfocu (230) -> zicvvl, zbhahq, agsjzih, ydhfmt
dgumiir (40) -> olzdhtj, inezd, kqrjpgl
vpjhl (27)
aqqdnpb (88)
qaszsa (94)
ajeisgv (95)
aoscme (73)
owlyge (65)
kdqslsn (73)
hukskkk (87)
vindf (73) -> szuiho, aoscme, fbdfh
kosxb (140) -> tcpujhx, itlsv
oeaqbvl (142) -> bsyiv, fiqzxhc
lyigbhi (105) -> pqmye, nzyiue
trnjhsl (73) -> iinql, yhzwdu, dtjzr
mkucbvs (138) -> ikxewmm, qhygx
fvplhrm (6)
qnvzqc (54)
jdbub (48)
opyzwha (75)
xeprhhl (99)
xounvb (101) -> mbqkm, zwpyj
aswpgvv (42)
razvskj (60626) -> dlzgufq, xwifd, nalhhj, lyhok
ygrbgm (172)
tcrkcu (329) -> ibdiplp, efbffd
mijxl (63)
ajfkd (9)
aaaak (6) -> mdopg, mzrafi
qgnah (42)
emppnct (78)
qysdgq (154) -> uutlw, klpctiz
hkewsbw (89)
lcfundi (52)
iccpjfn (92)
modzqb (30)
nsqzndf (51)
dpyuayl (18) -> wvieaw, cpacyeu, hwkwp
eocoy (67)
fbuklc (82) -> lcyuk, klzfl
ieeqmzl (32)
qcoyrha (255) -> kjqiop, oagluxi
lbfgh (123) -> obaorae, yktqkyl
payoa (194) -> khbvu, nrxoha
ywutc (71)
fodud (178) -> axmjgih, auvla
actggv (65)
jngcap (845) -> tydlqpq, ebdxuo, ktfeae
hcgbmwl (60)
lqirhg (70965) -> hbmxey, tlhgrte, xekggcw, lxffhxk, knhst
ifntl (26) -> emfbheo, heicvby, vcnph, qvgeei, gcylwr, uxuscb, ubrrbmk
uiasar (15)
sfkzoax (46)
bqtppn (236) -> xqnrp, fsguvid
peomyg (16)
sqincn (80)
zjtid (7)
cpvlq (72)
nwbmwa (17)
yjonn (185) -> rbhdx, cbnef, bvgfpab, czojwyg
jafdtcn (79)
uqofam (245) -> lxpshey, qwdppks
nkejtw (56)
tcihaf (28)
jwkgg (17)
hsftfol (46)
ehqavsc (22) -> aboilvw, diavsdh, nuybvi, ziyyvk, wyule, mtxzcd, tulxdf
dyveac (96) -> jdsdqzd, lhmjc
yfztc (74)
nuybvi (452)
ymfosm (38) -> hdkpuyx, ckafg, dmzwm
vrjea (1809) -> stcaf, hemnmbr, zuxvjpc
qteruty (8) -> mwtusu, pvpyhb
cpmcrx (13)
ouxjkf (18)
rvuktmb (147) -> yhlbg, cwgbjaq
blrzef (81)
guxwd (49)
yyyqzje (225) -> fnfiur, jfngjl
qbkipp (92)
wdlwryo (149) -> nxhetg, iltti
tjdap (240)
udxegjf (44) -> lzbbin, atfpsi, tuqzsn, ytnti, zdade, skotajh
aeliqqs (26)
shkfk (183)
adueu (372)
zbhahq (10)
jbtzoy (80)
pkcakwk (300)
hwkwp (67)
gatxz (45)
qizvid (38)
cbqebx (152) -> ornybn, zcfswa
ppmjzx (267) -> whlfwr, sfkzoax, csqyn
rwuxn (23)
pcdtne (6) -> fbuhz, alqog, hanbscg, fttsg, gblxcsj, cujhtj, adhilml
fvfitqc (39)
rgfur (104) -> aswpgvv, qgnah
jhgxtg (57)
pkotpki (86)
ujzjt (92)
zkikhk (16)
skotajh (328)
ycinfxk (1450) -> kosxb, cwvkon, nyxiai, bztor
gnffzh (234) -> tiiwbg, sfoivjz
juvwj (79)
ckcaugr (62) -> zebdkqz, xuxlspe
gjfkx (31)
blome (73) -> jjmyu, bljfcim
yqctq (28)
gpzaa (68) -> sqfopc, lxxfgli, yyyqzje, cjkoxak
qoipc (68) -> tjcpka, oydoajo
olhuxt (7)
zdade (166) -> oyfob, bvock
ihllda (81)
sbklnq (85)
yyblsz (54) -> nrmvc, dszjyr, bppos, tahstqe
qenjyl (79)
zukgdrx (79)
fszrgv (34)
ulezwmd (56)
xgogpx (23)
gwxkdy (46)
knhst (5583) -> ghjpcv, szvrql, ojtrl
mblvffb (79)
qowyx (56)
yablonq (18)
mwfryd (93) -> mldkiku, sveuu, kzjfme, kzwbhrg
xjafd (17)
njgzn (97)
jpeprwv (12)
lnnii (18)
tsetywu (22)
gdutjjl (73)
lnsyuz (27)
qyypm (417) -> uqofam, xtvyh, ajpujs
uutlw (75)
cbnef (15)
gikqie (90) -> qpwfl, pxhbe, yxcbn, lftlpr
nkuesm (60)
znpqzc (53) -> ekxdjlp, skvytv, nkuesm, ajtkddh
mszwp (53) -> qaszsa, tupro, otljqmh
stcaf (54) -> cufaveh, foblbqu
nmlykny (112) -> uitef, lsfdgam
frlmoih (92)
hqvvrd (34) -> juvwj, ayafxml
unzzng (22)
xucelzn (49) -> jumdfk, ilzwrk
nyjmiyq (91)
zfjpii (181) -> btjxv, rfhjgxy, digfyo
vyvcb (4479) -> jsniger, rbmmiy, zvildgh, kvtvmi, ogiie
fwqru (62)
skvytv (60)
ujogppt (95)
mgzotal (125) -> frgot, sjcbxp
ytpiey (83)
bfqba (872) -> vopeoj, gfknji, iwdesog, qteruty, lxisjl
foblbqu (20)
bzlgar (37)
dszjyr (37)
nrpyfqd (39) -> nihmyu, acjtwvt
vgvvr (66)
hzsgvc (8)
lddiw (7)
ydhfmt (10)
uspvnv (94)
seazs (92)
zrydf (108) -> zzavd, ppbevc
pkglsge (93)
oamrbi (33)
bendlfs (92)
rkgxu (88)
fqhag (2673) -> vangx, crojfnw, njrzjdt
wesyh (26)
jbaazop (19)
tgvdjhh (72)
ebdxuo (242)
xthhlfy (61) -> jafdtcn, kbout
vlthh (88)
sqfrw (830) -> ppmjzx, vixlf, ryskzh, ynkkomw
kzjfme (55)
heicvby (145) -> akrsjfc, lnhiiq
cuaect (114) -> ftdkas, jwgjnuu
oyjtku (93)
eyozeel (99)
rfhjgxy (227)
eoasnfq (94) -> idszh, vshekb
phgkg (30)
dxgnqsj (34)
egrga (1130) -> nrpyfqd, cfmhi, uwpwbgy, zqtok
sljgt (1013) -> iifltp, igfjvkm, rxefab
bszcup (56)
kkyfjh (83)
frvmu (143) -> xdnuvji, vwhynu
fsbojm (41)
mavbgo (91)
digfyo (188) -> tkejpfe, ynirne, swsffrv
xoyjtol (59)
qvbuj (1045) -> dgumiir, ofnmnyy, mkucbvs
dzetsz (1418) -> nsbli, ulxsa, krdlzf
zguqo (92) -> ripgc, oenrkia
klgsk (6)
yktqkyl (45)
jhcurc (50)
teuzi (57)
gfknji (26) -> nwyftp, vgndgst
gcylwr (221) -> wesyh, lsycscb
hxaza (7)
asoirn (74)
ofnmnyy (36) -> sziwpzi, zyxjqs
xobyzo (60)
azdklp (43)
mcfst (47)
vwqog (43)
tupro (94)
lytukj (25)
roqnodm (92) -> qbbmsf, oxewutr, pdcaqbr
axmjgih (65)
ezztp (87)
luuxtc (2600) -> qfkka, dxznun
pvzyops (94) -> oiyxr, ffrilz, upiow
adasbyp (237) -> kdqslsn, xantdh
iaiywwa (1850) -> nhxfu, boiic, kqgqdyg
zdkil (214) -> cemygp, bgctgn
pslyfi (7) -> ilydn, birahww, yfztc
wbllfh (43) -> xwmnaj, gprznw
drnyyes (66)
coyroy (175) -> oevvote, zzwtuu, klyso, pirivl
ddkgzi (19)
btbses (88)
mhassfj (9)
rbhdx (15)
kfhwxyy (17)
ozwaa (78)
lhmjc (32)
lftlpr (11)
ncaoc (58)
zacywmu (12)
vixlf (45) -> cgdbu, djmoed, npfkpts, eisrj
vwtmps (142) -> jljnags, qizvid
fsguvid (33)
gxdtiob (203) -> vbisx, gzter, bzkwsro
xwphya (82)
jtujnwo (37)
wyule (401) -> nwbmwa, pvpqoq, jwkgg
wpgyc (96)
jbvugg (224) -> dxgnqsj, fsfuluo
tojnst (160)
jeshqdv (1303) -> affxphr, lyhxuh, zkcwgx, cqdtav
icncbl (48)
kqiraxg (54)
aicncxc (29)
zbedu (209)
pdmsm (57)
kictlpo (37)
brkux (335)
zrbkrdx (41)
otljqmh (94)
kcreb (48) -> ihuzl, bvaor, popymuq
muavtro (98)
ayypg (56)
vdistyb (90)
euvkg (203) -> mgwauar, lazlx
ayafxml (79)
bnvjmae (7)
ogpka (80)
gnrqrsj (2189) -> ortcrq, upbmqk
rxefab (131) -> vcaekf, sqnfwo
pgpnvo (931) -> eahos, kcreb, lwefm, bbdimns
bphrvm (64)
doazn (211) -> siswh, hhvqa
sawqp (32)
mwdvbr (68)
mtboq (76)
dxcpj (93) -> afcgdxg, kzwgln, wkydaz, spkeqv, udxegjf
lyhxuh (22)
iuovz (88)
csear (1969) -> fnijmph, mgzotal, evmblgk
rojhup (7)
ebtbnei (31)
lhnevgo (269)
zibbm (85)
nrmvc (37)
txxpej (280) -> actggv, krqxe
lhvtmoo (130) -> icncbl, zbtck
wgwkss (80)
aawxzzs (22)
aarioi (79)
cabsaub (60)
otymybu (223) -> ddkgzi, viafs
cbgfg (58)
wcinck (20) -> ziwkz, wfeupmd, drszzbe, mgeseyn, xasioks, xtjrkv
orkcq (65) -> iujqo, ehdax
okfcek (97)
ybbrr (247)
iatmtm (55) -> lwxts, mqecf, tuhxr
yyxmp (80)
ysvjxvz (78)
birahww (74)
mxxfu (57) -> qdovgra, ywlrls, wahwi, mzjwcds, axrojbs, urigx
xbqpjo (98)
kqmhotc (94) -> rkuyxrc, wfjgqqm, xdylc
qwtodu (71)
qdxteam (61) -> ybbrr, frrvvai, ncjhpa, onuxzz, jvepbal, qznpwb
fbiqxqk (59)
rokie (9708) -> vmgqltz, qdxteam, srvwd, qvbuj, pgpnvo, hxjhcuc
ovmvvkl (24) -> tvhgbau, exgsmmj, uwvbon
qnxnatu (92)
hrkswsk (44)
ndodv (296)
koemv (92)
hfqjj (37)
yexyj (80)
fhlul (56)
dzzbvkv (64)
gmhxee (74)
jbgqlat (65)
qclpa (84)
indgw (91)
krqxe (65)
lmmeg (26) -> ummcw, zqhdiwz
bgmwpam (68)
wpfbdof (151) -> sbutyr, klgsk
qznpwb (153) -> vfmwzb, haicg
hdpemqh (168) -> txxpej, pwvmmda, gadyi, mvhqou
gpfaupm (13)
iqfmvz (67)
pdcaqbr (97)
qfkow (64)
exhxs (89)
zebdkqz (44)
rrtqyew (191) -> zbxakfn, ajfkd
ukrki (39)
hvacjk (69)
udfuty (32)
mrgccl (85)
uzily (82) -> swscfel, apzabs
lxffhxk (1245) -> bfqba, cpxgct, rouiui, qyypm
jfngjl (86)
ceevpgx (47)
sziwpzi (65)
pqmye (57)
phkvcix (90) -> nubay, jaamgi
gxcnp (27)
wmwzhjg (73)
miuvc (283)
nvtbk (1775) -> srgua, ckcaugr, xrapmvb
zfthi (60)
inezd (42)
irzuowk (90) -> ayqgp, zruqij, oqbet, fdckzry
zuxvjpc (62) -> mbunh, mgvoh, bfxezgb, sxxhmpb
wmyvz (59)
tqjpfzx (47) -> gjupqe, lwhev, bxhjjd, fmquyhw
xhwfcu (75)
tnltvzk (90) -> cevkjvr, hrmpq
uhepxt (60)
sjixg (25)
kuaeh (33)
uwvbon (79)
jzoue (94)
hdspavt (60)
kosgqpu (50)
mznkfco (79)
xfanpad (60)
zcpyr (81)
gutifk (228)
scipnb (53)
ejvaoj (59)
ybuhf (50)
bpmkexj (166) -> mbokr, ytbtswy
ogafygg (39)
fooowuf (42)
yiwdaj (86) -> iwajy, aftsom
hoelsa (64)
cjvdngb (91) -> qedkzuz, vtamjj
rsqexkv (70)
ftqtzxk (43)
azgjimy (92)
bochc (39)
qfsue (35)
objqgkm (146) -> tsiuz, glguoq
tatjry (47)
tcpujhx (55)
nnvpkf (56)
gatdr (89)
jcmviuv (37)
pzhyoh (3960) -> bkset, bfwbkxq, zsdvfrk, wrobpcw, ffxnegs, ifntl
svyojyu (60) -> qslgo, ukqcayx
sxbusu (73)
jtikaai (194) -> yukoxaw, qftqq
nkgmg (88)
zolmsue (66)
ziyyvk (60) -> yuypmb, ctoxz, dcwpsvy, mxrfq
bgcjrf (80)
qlqqlq (350)
npsza (74)
eahos (19) -> ywavdk, iqfmvz
cpxgct (14) -> tabzzo, svyojyu, pynxen, idooz, nzorg, zudqkt, fsvkj
nxrkz (1541) -> gutifk, avqjqdf, mgyfdm
twzgms (43)
uwizfa (88)
tiush (60)
cqpns (123) -> tfnem, kqguihx
necmih (10) -> dppzdx, zvelptp, tpsgt
ehxkgh (172) -> bthswyg, lbojqfo
yxoqwg (80)
emfbheo (85) -> uspvnv, oermd
siisskc (13)
icccxzg (71)
pjvpqmg (64)
dxxty (64884) -> ljugvh, gyyqk, pzhyoh
neladb (11)
polrzc (59)
snvqyqb (66)
lebqr (60)
shfjyzk (68)
acdkw (1907) -> apzjw, ialtabg, cjvdngb
xdylc (55)
hknzmvs (93)
obrwb (64)
werriw (13)
jjjfkf (19)
zqckoxe (118) -> vynvu, zgnwz
mgvoh (8)
oxewutr (97)
qqydcts (62)
pjkwlmk (56) -> etdofb, qqydcts
kzwbhrg (55)
cgzyc (669) -> bqtppn, rwjzc, bwylliz, rrkhcl
sltrdk (88) -> qwtodu, rpkpa, kddchk, xirqz
aqjkcss (77) -> rfaxua, nsggol, uxlcvt, jwpqgy, tjobe, ovrkpd
xagwh (99) -> sdigtox, pocxfrt, iancjuu, iefyz
apjxafk (1513) -> rznyr, oamrbi
uturjs (85)
qwxrsa (261)
cgjula (2020) -> lhvtmoo, yiwdaj, biwdu
yakzm (16)
ejtoqaj (1426) -> whggku, ktehtif, wpfbdof
eoaprcr (93)
otaty (141) -> ydpihb, ouabc
rjijdre (17)
atfpsi (196) -> qoqydb, vgvvr
qjazr (21)
petluuh (67)
xdupyte (19)
rpkpa (71)
aytjryx (25)
pfmor (80)
rfbdpc (66) -> payoa, ymfosm, ndodv, thutxib, objqgkm, gjjfju
kkciirc (71)
hfnijbd (234) -> qarjx, olhuxt
mrvdvga (54)
vwhynu (20)
nnsyc (59)
rlwvuj (280)
vtono (37) -> gdutjjl, eqahcc
jdjaem (74)
hgcxyx (13)
mkjvhl (282) -> neladb, tsrrzuc
cmeqx (521) -> uzprmq, xjmrcc, qlqqlq
fffxc (74)
sbutyr (6)
jikzxd (50)
zvildgh (1079) -> wtoive, rbucosf, eoasnfq
unfgdb (91)
npdwg (80)
ftdkas (33)
ewdpntl (66)
akrgdse (63)
vczudlu (17)
ablvgzq (58)
kbout (79)
aqogxi (29)
igfjvkm (265)
rkbtnzd (40)
jatvkwy (92) -> kqiraxg, vsyuckp, zwjds, mrvdvga
mjuwde (888) -> cbqebx, kihxgg, zjqbfd
ytbtswy (57)
rugzyaj (16029) -> apjxafk, jngcap, wrtyhxg, hblcbb
fuega (70)
lejoaru (64)
zvelptp (28)
mdfbhs (5185) -> miymiit, jjgem, gpzaa
xwifd (7225) -> rfbdpc, qqduoo, uagezb
bxhjjd (172) -> yacaqwf, ngksxux
xduga (88)
rwbhl (183)
cpazla (101) -> ayypg, kjzsi
ttmei (19)
hblcbb (5) -> qwxrsa, ovmvvkl, orkcq, otymybu, sjxbk, frqtkkr
lzbbin (250) -> ujzofuy, urwgjd
bgctgn (34)
uaqik (15)
kvpztt (93)
zeopgv (312) -> pgznzly, ixwyi, tefcd
oyfob (81)
yhzwdu (28)
xwmnaj (41)
ngksxux (82)
brmtxo (300)
kdujkg (12)
cjlxgf (165) -> bsoef, rkbtnzd
tefcd (13)
jsniger (680) -> lycpdcu, iihzs, aubhuwo, xucelzn, qykoae
thutxib (138) -> mblvffb, zukgdrx
npfkpts (90)
yqbkjg (51)
tsiuz (75)
otvvje (43)
boxvu (18)
etnuzv (27)
fkmccg (32)
zzxlo (2220) -> zhiai, oqhwa, irzuowk
haicg (47)
veqahi (50) -> yugjkuz, ncaoc, hfjhadi, cmzoogc
uystf (75)
wqxcn (292) -> ddrrgp, sxvlfn, ipmbqts
jlbhafs (27)
lvuzab (74)
hrfyodg (84)
apctfnv (246) -> baygmx, zacywmu
wafjawl (56)
dlsss (88) -> mijxl, voonmio
nlrobhq (87)
jzdmjdf (1849) -> aaaak, necmih, fmifd, kowco
yzivqv (32)
cufudi (97)
zwjds (54)
pizkx (21)
fbdfh (73)
cwvkon (193) -> cepqh, jjjfkf, xdupyte
wqgpm (56)
vopeoj (14) -> sgqaiyz, ysvjxvz
zqtok (151) -> fhgnht, fooowuf
fugeht (89)
mgyfdm (60) -> mvvgro, hrfyodg
wqdvql (39)
ogiie (573) -> hfnijbd, cxokosi, jtikaai, ffgoyk
tgqpp (89)
fdaddso (15)
cmzoogc (58)
gjjfju (270) -> kndcyxb, cpmcrx
wowkfnh (64)
lwefm (115) -> ageyuq, jbaazop
qykoae (61) -> cbgfg, dyfhy
ipeig (98)
iyjcoy (63)
omzpkv (23)
kqguihx (48)
qrtwjv (37)
sgqaiyz (78)
gzdxgvj (64)
wfeupmd (65) -> pdjnnzd, mrgccl, uturjs, yfszfef
vmgqltz (841) -> ecabcm, vigvho, ppfyonm
txvuv (5)
zfcylzq (113) -> ocbxx, kofvzz
vigvho (76) -> vtnpx, hjdms
njrzjdt (171)
iyflfx (90)
spkeqv (1828) -> qbkipp, bendlfs
dqiyfw (21) -> mliwyi, kvpztt, oyjtku
nufpcxh (71)
ppbevc (13)
bljfcim (80)
hjdms (79)
mcfrv (19)
zruqij (58)
gmurq (89)
zyqqzou (78)
pyocxtt (27)
akrsjfc (64)
nzorg (102) -> bdukt, kkciirc
vobfi (734) -> lbfgh, wfbuzbg, kklix, hpsxqdm, lhtzrh, cpazla, skhmac
zugxr (84)
ldwhpl (324) -> takkbk, thneyz
kzwgln (1217) -> evwne, lrvxyg, hllzej
heuyaxx (2337) -> iatmtm, pabgfh, oryrq
kzjkjz (17)
ykmej (92)
sqfopc (33) -> mavbgo, uucyyr, nyjmiyq, tygst
qcpuch (270)
qcolnc (11) -> ewdpntl, zolmsue, lunbob
tfxyjz (87)
fiqzxhc (38)
hvhtokr (95)
ledgpb (132) -> kqltx, wivwqm
bonnse (30)
dcwpsvy (98)
xjmrcc (268) -> yucwtc, ilueo
bzkwsro (49)
zziyhz (18)
qoqydb (66)
ubrrbmk (87) -> pkglsge, gjorp
cgnibii (188) -> pqvid, uiasar
sxvlfn (23)
gqgewi (2538) -> ndxuv, egulpbe
qosqq (47)
jkczp (37)
pxhbe (11)
vpjmvzd (37)
rvjzxtg (86)
pfzqe (89)
uvhmzj (114) -> bphrvm, lgamzp
gklur (85)
wbbfe (37)
wkumzkr (1049) -> nxtyiha, modzqb
pyhqixj (63)
ohtzuf (87)
lsycscb (26)
bdsibf (87)
gzter (49)
ogelzdv (87)
fstzdn (97)
ebktv (146) -> gpfaupm, cduzde
iinql (28)
tdurwbh (58)
hnvybq (268)
sfxsn (75)
jgdumgz (87)
zqhdiwz (96)
rznyr (33)
ouqwmnj (265) -> jdbub, evqrr
tiuag (62) -> xhbjag, bmehz
fdckzry (58)
hdkpuyx (86)
hemnmbr (16) -> ukrki, mgsasl
rupdbwl (43)
bbdimns (57) -> upftju, iracqt
ipdbccy (34)
fbrvfk (79)
hueqfk (85)
bxrkfwo (67)
fwafvkf (40)
nsbli (47) -> hpanc, xjafd, uqjmbb, ycnih
ifhpy (79)
fneqe (1219) -> vmatvgx, bofjde, hhnpg
mliwyi (93)
utqxb (37)
fvivhx (75) -> nwlyt, dyxcd
whggku (97) -> vomrnc, ceqfbbl
kndcyxb (13)
ynwpoz (785) -> raioiq, yyblsz, rxuqpgb
hrrampl (27)
kkftjia (87)
rvxed (122) -> rktkzfw, qfsue
miauii (66) -> kpjxln, icrnru, dqiyfw, brmtxo, pkcakwk
bkset (857) -> brfocu, thvjlgo, urhwog, apctfnv
nhxfu (35) -> lwufmc, gatxz
skhmac (101) -> dbnstqf, wafjawl
bdwswow (65)
lgoak (70)
mdrob (51)
fsixon (27)
hcyohc (85)
kihxgg (44) -> awhwxdm, sbgtiqe
hdhvzi (1759) -> kzhpyr, apvfi
bwylliz (110) -> kwvybk, ftexc
xijwk (841) -> bsmxm, xrise, uzjoys
xkpulvc (93) -> fbvvrqt, zcpyr
xhbjag (76)
azrpi (92)
lxxfgli (49) -> nlrobhq, ogelzdv, tfxyjz, bdsibf
qedkzuz (45)
bmehz (76)
exgsmmj (79)
ijcxfx (136) -> jbgqlat, bdwswow
nsvrfae (71)
offas (58)
ipofw (15)
matcdld (35)
gjorp (93)
bofjde (152) -> jcuiffa, vvkbav
yxqesmi (172)
eisrj (90)
pjmci (59)
palqky (60)
aipmq (41)
ripgc (44)
ehdax (98)
jtlhia (749) -> tiuag, bdbxp, dlsss
uucyyr (91)
dtqbtvx (223) -> izyjved, etnkepp
yhlbg (41)
kwvybk (96)
fhgnht (42)
ummcw (96)
khkuxc (1254) -> qqhjlu, gekcx, vrajpg, emppnct
nwlyt (87)
txnzg (74) -> lcfundi, tifkr, imfog, imbpvgl
dkzitf (20)
bdbxp (80) -> fcvpdiz, bxrkfwo
degnsd (177) -> eetxll, jkczp, ghzqyv, kictlpo
zudqkt (142) -> fszrgv, wwobe, jbjkp
zjcdwr (249) -> bqcizg, saiyjff
sjthmr (76)
kryoh (144) -> jcmviuv, hfqjj
ghuoa (78)
uitef (77)
cjkoxak (340) -> sowzlz, ttmei, lajyaur
pczkz (88)
itlsv (55)
nwztmzp (63)
tsrrzuc (11)
rxrzt (65) -> krembdy, zrbkrdx, aipmq
frqtkkr (185) -> qecgvu, lbjuqcd, mcfrv, kwqcbe
mdrir (12)
vytdgko (97)
tkeoe (865) -> wzcgi, awsphe, ifhpy
orwbp (96) -> ecjujqu, iccpjfn
ckexdc (10)
popymuq (35)
euiig (166) -> ablvgzq, tdurwbh
ibjbozh (895) -> ijcxfx, nmlykny, fshvy, nutlr, yotlucw
idszh (34)
tfnem (48)
kqrjpgl (42)
ewsrnsd (90)
rnsxz (9718) -> pvzyops, zfjpii, luccp
avqjqdf (50) -> dilefzx, dulpw
euqvd (42)
dulpw (89)
nppdvs (40)
gncvcwi (104) -> pfmor, yyxmp
fmquyhw (188) -> hwqvzw, huspq
hpgktb (60) -> hcgbmwl, tiush
iyxkzat (49)
seyed (86)
zzwtuu (260) -> unzzng, ebsxx
nfvsrpa (876) -> kwwhb, blome, otaty, dtqbtvx
mnwhky (1339) -> hqccsb, ldflo, rgfur, rxrzt
kebff (242)
cogovv (74)
takkbk (57)
yyswun (98)
ecjrblb (68)
ycawl (224) -> vpjmvzd, bzlgar, jtujnwo
dppzdx (28)
alcpfsx (136) -> siyuvy, nowyhln
dfdgoj (153) -> aufym, pfxrf
jcuiffa (56)
yjyipdp (66)
ilueo (41)
iazte (201) -> tsetywu, zkzefwh
diavsdh (326) -> wladmn, zudqxa, ajpcyv
llofnny (66)
kitsxb (59)
kqltx (74)
klzfl (93)
tpdcb (84)
afcgdxg (1202) -> qcpuch, njmrq, tnltvzk
gnwjseo (600) -> pkxhxdz, jbfzjha, ixdcgsa, degnsd, fwtfkp
yqnbqgc (178) -> dkzitf, zybvpry
ialtabg (21) -> jbtzoy, sqincn
uorpbn (353) -> ygbyt, afjmzb
jdhiflw (60)
qpwfl (11)
xasioks (405)
lajyaur (19)
ajpujs (271) -> zxzkl, dkgsvl
ovrkpd (147) -> sdzoy, mdrob
sveuu (55)
jtvntr (83)
pvgay (69)
boiic (80) -> ipofw, ggjmhab, mwjtydb
sjcbxp (59)
uvzwdly (20)
sbgtiqe (91)
luzcpkn (43)
ndxuv (80)
tkejpfe (13)
ggjmhab (15)
szvrql (46) -> cnknlru, zrydf, cvvtz, uwiza, gikqie, lknchr
lvkpx (233) -> wmyvz, nnsyc
bhzbv (28) -> azgjimy, frlmoih, azrpi
cujhtj (193) -> qhbotj, qnsnc
vmatvgx (90) -> uaavvo, ezztp
pvpyhb (81)
mdpcfvu (176) -> gyktq, yyswun
aubhuwo (99) -> yyqleqa, nmdhmy
wgglzpb (191) -> gmurq, hkewsbw
amaeuv (58)
ijleirw (172) -> jikzxd, yeewxiw, jhcurc, kosgqpu
tvhfxfo (105) -> wnzdcc, bszcup
kzvwk (74) -> ujogppt, appkqpe
qgxcbt (68)
ipmbqts (23)
woeoaa (59)
yfszfef (85)
ickxyrm (87) -> hrxfpx, owlyge
mjlmuca (41)
iracqt (48)
dtyxosg (84)
vyaoad (83) -> tojpm, euaceg, zhffrzu
jemmk (47) -> mwdvbr, shfjyzk
viafs (19)
iefyz (39)
wkydaz (332) -> orwbp, xhhfsuw, ledgpb, rlwvuj, bpmkexj, diduy
zhiai (228) -> qosqq, ceevpgx
aydmhhv (87)
vtamjj (45)
egabi (79)
zgnwz (87)
kvtvmi (39) -> fpmwz, oeaqbvl, oipjwtz, usevgds, vwtmps, kryoh, gkzeqaw
sszzop (89)
uaavvo (87)
xtvyh (83) -> pczkz, xydxl, xduga, gycde
fpgciql (51)
ynkkomw (279) -> iyjcoy, ijiqjtf
yirkbjn (1872) -> wjjar, ldwhpl, kcimi
paqvyfa (58)
khbvu (51)
jvpgl (20)
sxslizl (86)
gbpcav (77)
kjqiop (40)
ulxsa (115)
nhzmidl (27)
nchjk (37)
yokqfgn (94)
qwdppks (95)
fnijmph (90) -> yqbkjg, ykvtr, fpgciql
xucdiz (6) -> kkyfjh, cxjyxl
ftexc (96)
krembdy (41)
gzykr (1135) -> lejoaru, qfkow, wowkfnh, pjvpqmg
srrxb (81)
ylwniqh (68)
usuujhq (46) -> pkotpki, seyed, jgkmy
ilfgats (6031) -> mxxfu, vrjea, mnwhky
urxxlfo (84) -> juakl, bwywt
fsfuluo (34)
staqwo (8)
ynirne (13)
zyonam (217) -> sofxmjx, ytpiey
ornybn (37)
jvepbal (79) -> cqiipxn, qclpa
goicjt (41)
bfpvsfz (39)
zbxakfn (9)
cqdtav (22)
cufaveh (20)
zxqix (157)
zudqxa (42)
fcvpdiz (67)
kzhpyr (59)
cuwqi (104) -> jotxc, teuzi
mdopg (44)
pyntdrr (320) -> lbiigt, aeliqqs
ouabc (46)
wnzdcc (56)
wvkaie (80)
axrojbs (239) -> aytjryx, xbpqmua, sjixg, lytukj
lcyuk (93)
tdnzc (22)
wrobpcw (1196) -> fujvp, gfuxooq, crkapwa
hyfswg (1414) -> rcywun, kqmhotc, xvwqzt, bbsomm
yugjkuz (58)
tokvgmd (91)
yyqleqa (39)
pmfpitp (33)
nhxmab (24)
hwqvzw (74)
hntdp (90)
nercz (33)
kvjqli (72) -> tpdcb, edoftkj
zdrfiw (80)
viklkmp (19)
evmblgk (183) -> yycux, buifcn, uaqik, fdaddso
wzcgi (55) -> hzsgvc, staqwo, fgxst
baygmx (12)
mxscf (62)
oqhwa (186) -> gcbvf, bgmwpam
sflwom (253) -> uvzwdly, pjkjcy, rcongvf
ajrcal (83)
yqyyoj (33) -> lftlc, npcyutn
tpsgt (28)
ebsxx (22)
aceiy (13)
jwlaj (1031) -> qjuud, tdtznh, cuaect
hvefi (15)
nxtyiha (30)
mzjwcds (229) -> icqsww, pitdti
ndxim (6)
vomrnc (33)
vfmwzb (47)
jidxg (64)
aqtml (293)
cevkjvr (90)
lycpdcu (5) -> rvjzxtg, ovysqnt
thmlk (34)
iujqo (98)
synjm (51)
paqlttl (65)
kklix (25) -> jzoue, yokqfgn
usevgds (44) -> aydmhhv, kkftjia
tqlentr (214) -> gfxnuuk, thmlk"""


def clean(s):
    return s.replace('(', '').replace(')', '')


numberOfOccurences, tree = {}, {}
for line in s.splitlines():
    line = line.replace(',', '').split(' ')
    tree[line[0]] = line
    for elem in line:
        if "->" not in elem and "(" not in elem:
            numberOfOccurences[elem] = numberOfOccurences.get(elem, 0) + 1
print(min(numberOfOccurences, key=numberOfOccurences.get))

for node in tree[min(numberOfOccurences, key=numberOfOccurences.get)][3:]:
    print(node + str(tree[node][1:]) + clean(tree[node][1]))

# day 8

s = """n dec 271 if az < 3
f inc -978 if nm <= 9
g inc -336 if ga < 2
egk dec 437 if y < 5
z dec -550 if g == -336
mx dec 12 if bqr == 0
mx dec 433 if ns == 0
ic inc 506 if g <= -327
ga dec -560 if ic != 506
bqr dec 570 if az >= -9
g dec 372 if egk != -429
f dec -863 if b >= -9
gyc inc 844 if av >= 7
cr inc -781 if mx >= -453
ga dec 346 if cr == -781
b inc -162 if z < 554
nno inc 504 if g <= -700
mx dec -32 if vkg <= 6
mx dec -961 if nno < 509
az dec 320 if ic < 510
nm dec 594 if ga != -354
cr inc -784 if az <= -311
bqr inc -321 if mx > 547
y inc -951 if egk > -438
y inc 703 if y <= -950
vkg inc -852 if g > -716
n dec -596 if az < -316
n dec 410 if e <= 4
f inc -693 if ic <= 510
egk dec 498 if zqo != 7
rn inc 626 if u == 0
bqr dec -770 if bqr > -898
n dec 193 if ic == 506
egk inc -263 if e == 0
cr dec -473 if mx <= 554
vkg inc 667 if e != 10
ga dec 793 if v <= 5
f dec -673 if v != 0
g inc 797 if g >= -708
n inc 361 if v == 0
y inc 399 if zqo == 0
av dec -894 if zqo == 0
az dec 785 if z <= 559
y inc -121 if nm < -593
v inc 873 if vkg > -189
ns inc -205 if n >= 80
cr dec 452 if ns != -202
nm dec -35 if f < -799
ic inc 790 if zqo > 3
gyc dec 456 if nm <= -565
rn inc 198 if y != 32
y dec -917 if f == -806
e dec -694 if zqo != 7
nno inc 676 if rn < 825
u inc 414 if ns >= -213
f dec -405 if bqr <= -113
g dec 456 if ga > -1145
by inc 613 if nno != 1185
n dec 414 if ga >= -1131
ga dec 844 if u <= 418
av dec -404 if ga >= -1974
g dec -171 if ns > -208
av dec -302 if f == -403
ic inc -935 if y >= 30
u inc -807 if bqr > -126
az inc -536 if v >= 865
vkg dec -77 if vkg == -185
n dec 209 if n == 83
u inc -92 if y >= 26
ic dec 43 if u != -491
ic inc 701 if z == 550
bqr inc -473 if e != 699
av dec -44 if egk != -1198
e dec 134 if ga == -1974
v dec 479 if mx <= 544
n inc -748 if y >= 21
bqr inc 726 if u >= -492
z dec -368 if ns == -205
y inc -296 if e >= 694
f inc 271 if nno >= 1177
y dec -881 if cr < -1535
nno inc -493 if az > -1649
z dec -434 if v != 882
bqr inc 783 if e <= 694
gyc inc 930 if gyc != -1
nm dec -712 if e < 696
mx inc -342 if nno > 685
av inc -292 if gyc > 927
rn inc -269 if rn <= 831
vkg dec -799 if nno == 687
v inc 31 if vkg < 694
egk dec -227 if v != 913
ga inc -248 if u == -485
ga dec -655 if ic >= 228
nm inc 335 if by != 613
av inc 251 if u >= -477
bqr inc 834 if ns >= -209
gyc dec -580 if rn > 549
u dec 390 if e < 701
cr inc -936 if b > -170
nm dec -60 if g < -188
ic inc -226 if by < 615
y dec -698 if zqo != 0
vkg inc -938 if av == 904
vkg inc -131 if zqo == 0
y inc -792 if zqo < -3
gyc dec -43 if ns < -211
ga dec 783 if az <= -1637
az inc -359 if cr <= -2479
e inc -117 if v != 908
rn inc 231 if av < 898
nno inc -594 if z != 1354
egk inc -119 if b >= -170
mx dec 866 if mx != 214
g inc -688 if mx < -655
ga inc 451 if z <= 1352
bqr inc 315 if g != -876
vkg dec -636 if egk != -1090
bqr inc -395 if by < 610
mx inc 914 if ga < -1908
by dec -623 if egk > -1090
ns dec 219 if vkg >= -380
egk dec -976 if av >= 896
egk dec -681 if ic != -1
vkg inc 971 if nno < 101
nno dec 490 if bqr > 2060
u inc 479 if z <= 1358
z dec -552 if nno < -389
y inc 696 if nno <= -405
nm dec 876 if nno >= -399
f dec 197 if nm > -670
f inc 584 if e <= 575
av dec -548 if y <= 616
cr dec -975 if mx >= -664
vkg dec -532 if egk > 567
cr inc 115 if zqo <= 2
e inc 315 if nm <= -663
e inc -850 if ns > -430
vkg inc -72 if z < 1906
b inc 7 if y != 618
cr dec -270 if by < 613
v inc 505 if ns > -430
ga dec 51 if nm != -670
z dec -657 if zqo <= 1
u inc -777 if nm == -663
y dec -37 if nno < -396
gyc inc 62 if f < -322
z inc -565 if az > -1996
e dec -223 if vkg <= 516
nno inc 481 if e == 34
rn inc 316 if nno >= -406
e dec 531 if ns <= -423
vkg inc -940 if v >= 1408
by inc 935 if b <= -152
rn inc 254 if ns < -416
gyc dec 822 if zqo > -6
n inc 334 if b < -155
by inc 987 if nno == -397
gyc dec -701 if ic >= -6
nno inc -764 if z <= 2568
nno inc -541 if mx == -660
ns dec -327 if ns != -424
z inc -328 if bqr == 2064
cr inc 550 if cr != -1385
ga dec -441 if rn <= 1123
gyc inc -461 if zqo == 0
egk dec 554 if ic < -6
av inc 300 if zqo == 0
nno dec 324 if av <= 1754
y dec 235 if b > -165
rn inc -1 if v < 1415
b dec 230 if y > 413
mx inc -836 if b <= -384
av dec 464 if zqo != -7
rn inc 208 if egk >= 563
e dec 385 if v >= 1413
g dec -443 if z < 2240
v dec 296 if nno < -2027
nm dec 394 if az != -1992
u dec 609 if nno == -2026
nno dec -178 if ns > -428
f dec -340 if z >= 2231
e dec 124 if u > -1783
bqr dec -221 if bqr == 2064
rn dec -427 if by != 2539
n dec -242 if cr == -840
az dec 267 if y < 418
by inc 737 if cr <= -833
rn inc -938 if ic >= 1
az inc 181 if zqo >= -6
f inc -874 if z >= 2233
cr inc -867 if vkg <= -414
mx inc 424 if ic >= -6
f inc -125 if g <= -435
az inc 30 if n < -625
av inc -575 if y < 418
ga dec -726 if ns <= -418
u dec 1000 if b >= -393
ns inc -88 if av < 720
ns inc -80 if f < -983
z dec 73 if e != -613
bqr dec 350 if nm > -1065
az inc 247 if gyc > 980
v dec -156 if g != -435
mx inc 32 if f > -996
b dec 349 if mx < -1032
mx dec -934 if nm != -1067
ga inc -502 if egk < 573
gyc inc -106 if nm == -1057
ga inc 669 if mx != -102
nno dec -335 if g >= -438
g dec -757 if v != 1566
cr dec -887 if z == 2233
rn dec -768 if by < 3280
bqr dec -289 if gyc < 890
u inc 817 if by > 3265
nm dec -136 if by <= 3270
b dec 192 if y == 417
f inc -787 if b <= -929
f dec 188 if f == -988
cr inc -488 if nno != -1846
nno inc -116 if az > -1807
cr inc 899 if by < 3278
nno dec -454 if b >= -928
f dec 237 if cr != -409
e inc -910 if b != -926
zqo dec -710 if egk > 564
v dec 651 if cr != -407
z inc 45 if ic < 10
rn inc -16 if n > -633
u dec -433 if n != -636
z inc -55 if vkg >= -425
y inc 536 if v <= 916
nm dec 269 if cr == -409
vkg inc -811 if gyc > 875
y inc -269 if rn <= 1576
rn inc -445 if av >= 709
av inc -131 if ic != 1
egk dec -35 if y <= 687
mx dec -947 if nm == -1326
bqr inc -296 if nno >= -1399
vkg inc -176 if az == -1809
z inc -7 if ga <= -1058
v dec -105 if v != 908
by dec -935 if g > 315
y dec -674 if rn <= 1132
ga dec -482 if v <= 1026
nm dec 500 if f >= -1176
by dec 653 if f < -1177
cr dec 156 if mx == 841
ns inc 446 if u > -1535
e inc 256 if mx < 840
av dec -883 if nm == -1826
gyc inc 204 if by < 4198
g dec 158 if av > 1456
z dec -314 if av <= 1466
egk inc -367 if cr > -568
by dec -847 if f <= -1171
f dec -361 if z < 2532
z dec 647 if ns == -146
z inc -416 if z <= 1892
e dec 138 if cr <= -571
ic inc -393 if gyc < 891
zqo dec 338 if e < -605
zqo dec -644 if ic == -390
ns inc -790 if b != -917
az dec 136 if av == 1465
nm inc 971 if gyc != 884
av inc 171 if ic != -390
u inc -715 if zqo <= 1024
av inc 27 if zqo != 1021
n inc 845 if zqo < 1023
cr inc -576 if v == 1019
y inc 456 if ga >= -583
mx dec 843 if f > -823
v dec -589 if ns != -926
e dec -797 if nno > -1395
g dec 828 if bqr >= 1925
vkg inc 176 if az > -1949
nno inc 261 if zqo < 1017
f inc -429 if b == -926
f dec 658 if mx == -2
e dec -221 if gyc < 890
y dec 362 if v < 1605
rn inc 849 if v != 1610
b inc -650 if y <= 1363
ic inc 39 if g != -668
by dec -365 if u > -2248
nm dec 779 if u == -2247
nm inc -482 if cr <= -1137
ns dec -873 if nm == -3087
e dec -993 if rn <= 1979
vkg dec 291 if n <= 220
nno inc 937 if nno > -1139
bqr inc -321 if b <= -1570
av inc 86 if v < 1612
by inc 872 if gyc > 878
egk inc 858 if bqr > 1603
e inc -199 if ns <= -62
az dec 600 if v >= 1615
nno inc -115 if g < -660
ga inc 614 if f > -1910
g inc 950 if zqo > 1009
f dec -319 if cr == -1141
gyc dec 498 if nm <= -3078
u inc 61 if z != 1464
av inc 127 if zqo > 1012
ic inc -78 if f < -1573
b dec -601 if nm <= -3082
av inc -475 if gyc < 396
av dec 613 if gyc < 383
vkg inc 425 if rn <= 1981
nno inc 543 if az >= -1946
rn dec 280 if vkg >= -1096
ns dec -366 if gyc <= 388
v dec -558 if egk == 1093
vkg inc -446 if ns <= 301
y dec 617 if b <= -970
n dec -890 if az != -1947
vkg dec -102 if nm != -3092
e inc -668 if ga < 33
zqo inc -305 if e >= 529
vkg inc -97 if vkg != -997
rn inc 188 if nm < -3087
cr dec 613 if rn < 1700
v dec 647 if g < 284
az dec -205 if e == 531
av inc -359 if vkg == -1091
y dec 252 if ns >= 301
n inc 251 if f != -1593
mx inc 438 if gyc < 385
by dec -984 if nm != -3087
mx dec 354 if ic < -425
by dec 395 if ns > 298
egk inc 119 if b == -966
gyc inc -887 if vkg == -1091
rn inc 898 if ga != 30
mx dec 35 if y >= 485
e inc 889 if ns != 300
ga dec 992 if b > -968
g dec 432 if cr > -1755
nno dec -669 if gyc > -504
bqr inc -442 if rn == 1697
u inc -44 if b > -976
u inc 5 if gyc <= -497
gyc inc 36 if ns <= 304
nm inc -528 if b >= -973
y inc -617 if mx <= -400
g dec 47 if e >= 1418
b inc 292 if egk != 1083
vkg inc 734 if ga <= 30
n inc -678 if b != -691
ic dec 581 if vkg >= -365
u dec 562 if b == -683
nno dec 751 if cr > -1757
egk inc 709 if gyc != -461
n inc -347 if rn == 1697
gyc inc 960 if cr <= -1751
z dec 627 if ns < 310
gyc dec -190 if z < 842
v inc 868 if mx == -398
n inc -280 if b != -683
n inc -302 if e == 1420
av dec -389 if g != -209
nm inc 241 if ic == -1018
n inc -493 if nno <= 157
f dec -932 if n == -466
u inc -880 if y >= 480
y dec -697 if egk < 1807
az dec 332 if nno != 149
g dec 971 if z <= 848
by inc -510 if z >= 849
u inc 103 if bqr < 1161
av inc -830 if gyc > 678
rn inc 110 if ns < 306
b dec 616 if ga < 40
egk inc -749 if y <= 1176
z inc 669 if ns != 301
n dec 365 if nno >= 152
ns inc -464 if egk > 1801
e inc -516 if by > 5894
bqr inc 934 if g < -1165
nno inc 224 if cr < -1744
f inc -480 if n >= -456
gyc inc 101 if g > -1168
cr inc 501 if e == 905
z dec -836 if f < -643
ic dec 750 if rn != 1808
u dec -318 if gyc <= 687
ga inc -631 if av >= 430
nno inc -261 if ga > -606
b dec 723 if by >= 5889
ns inc -109 if bqr != 2095
cr dec 731 if e >= 903
nno dec -251 if b >= -2024
mx dec -206 if rn > 1810
ns dec 249 if rn > 1799
u inc 201 if egk < 1809
vkg dec 283 if z > 2338
rn dec -759 if u >= -3141
f dec 540 if y != 1186
by dec -523 if z == 2345
by inc -894 if ga > -608
rn inc -418 if cr >= -2489
bqr inc -837 if nno > 361
cr inc -485 if zqo == 711
y dec -672 if nno == 364
g inc 159 if nm == -3087
vkg inc 873 if az >= -2074
b inc 83 if z != 2347
gyc inc 321 if e < 904
e dec 283 if gyc < 689
f dec 257 if b >= -1948
by inc -526 if az < -2063
cr dec 119 if b == -1939
e inc -534 if g <= -1016
bqr dec 923 if av == 430
gyc dec 513 if bqr > 334
u inc -756 if z > 2339
nm dec 343 if gyc >= 165
bqr inc -114 if ga <= -601
gyc inc 355 if cr >= -3091
gyc dec -458 if mx >= -398
by dec 24 if v != 1519
cr inc -155 if v <= 1526
v dec 512 if av >= 427
f dec 297 if f > -911
nno dec 783 if ns <= -524
az inc 985 if ga > -592
cr inc 300 if egk >= 1800
vkg dec 542 if mx == -391
zqo dec -844 if bqr == 218
av inc 860 if gyc == 985
nno dec -253 if nno != 366
v dec 542 if b >= -1941
z dec -76 if ns > -526
y inc -336 if az == -2073
nm inc 995 if egk > 1793
f inc -95 if e < 622
zqo inc -46 if rn > 1379
b dec 470 if av <= 1299
gyc inc 839 if f >= -1304
bqr inc -766 if bqr < 227
n inc 980 if v < 460
bqr dec -757 if ns >= -528
g dec -507 if f > -1308
mx inc 249 if ns > -522
av dec 524 if g < -507
e dec -962 if rn > 1397
ns inc 139 if zqo < 666
av inc -443 if zqo <= 656
z dec -753 if rn != 1391
g inc 616 if v <= 474
ga dec 196 if nno < 618
av dec -317 if gyc > 1826
f dec -673 if cr < -2939
b inc -670 if zqo > 670
cr inc -948 if ga <= -795
av dec -977 if zqo == 665
f dec 521 if ic != -1764
ga inc 342 if nno != 618
av dec -989 if gyc >= 1823
rn inc -118 if mx < -137
ic inc 874 if nm < -2429
cr dec 441 if by > 4996
az dec 920 if cr == -4333
by inc 486 if z >= 3168
zqo dec -614 if u <= -3897
zqo inc -359 if g > 105
cr inc 725 if av <= 3257
nm dec 816 if mx >= -133
f inc -174 if az < -2996
n dec -832 if egk <= 1803
z dec -351 if av > 3257
rn inc 814 if egk == 1802
rn dec 516 if bqr > 206
ic inc -181 if ns >= -383
cr dec 476 if av < 3261
rn dec -446 if mx > -141
rn dec 966 if bqr > 213
u dec 426 if b != -2408
ic inc 841 if ic >= -1071
u inc -990 if n < 371
gyc inc -436 if az != -2991
egk inc 673 if by == 5485
g dec -510 if egk >= 2474
v inc -104 if ic != -225
b dec 862 if ga != -452
n dec -733 if mx != -132
b dec -726 if nno > 618
f dec -259 if rn == 597
e inc 51 if nm == -2435
y inc -251 if ns >= -388
bqr inc -684 if u >= -5325
bqr inc -427 if b > -3278
n inc 526 if mx >= -149
f inc -727 if egk != 2475
ga inc 345 if g >= 622
ic dec -398 if ga > -113
rn dec 581 if egk < 2478
rn inc 926 if g < 614
ns inc 469 if nno != 615
n inc -870 if vkg > -311
mx inc 124 if ga <= -103
z dec -983 if ns != 96
vkg dec 530 if mx < -18
rn dec -899 if g < 625
gyc dec 98 if g < 627
av inc -497 if n < 760
nno dec -115 if egk >= 2470
z inc 610 if z > 4156
mx inc -184 if ns > 91
cr dec 724 if nm != -2438
ns dec 527 if nno > 727
ns inc -177 if cr >= -4811
v dec 423 if rn != 921
vkg dec 658 if av >= 2755
y inc -464 if bqr > -890
nm dec 440 if e < 673
ic dec -963 if mx == -18
n dec -613 if by < 5488
v inc -412 if egk < 2482
vkg inc -278 if y < 1609
by inc 200 if e == 672
ns inc -627 if v == -51
n dec -176 if e == 672
n inc -511 if gyc <= 1289
zqo inc 589 if ga == -108
v dec 533 if egk < 2485
zqo dec -93 if n > 1536
e dec -618 if nno < 742
gyc inc 258 if f != -1139
ga inc 562 if vkg >= -1254
n inc -492 if f > -1158
rn dec -267 if nno < 738
v dec -263 if y < 1603
vkg inc 206 if mx == -18
av dec -610 if n <= 1060
by dec -352 if mx <= -24
zqo dec 74 if vkg >= -1046
ns inc -251 if ga > 457
cr dec 531 if n != 1047
ga inc 892 if by < 5683
vkg inc -687 if b >= -3273
av inc -208 if v <= -580
g dec 550 if az != -2985
ga dec -595 if gyc >= 1548
egk dec -240 if zqo >= 930
b dec 262 if az == -2992
egk dec 831 if ga < 1055
zqo inc 928 if ga > 1044
nno inc -90 if gyc >= 1542
e inc -47 if f < -1144
u dec 131 if zqo > 1871
g dec 268 if f != -1148
b dec -964 if n <= 1045
gyc dec -952 if az > -3001
egk inc 324 if vkg != -1735
by inc -460 if av == 3167
bqr inc 494 if nm >= -2878
by inc -616 if rn < 1191
ga dec -150 if u != -5312
ns dec -535 if av == 3161
rn inc -720 if ic > 1135
n inc -821 if gyc < 2508
n inc 670 if ns < -705
f inc 419 if ga == 1197
mx dec -96 if nm >= -2876
vkg inc -270 if n < 909
z dec -907 if ns < -700
ns inc 160 if gyc >= 2491
av dec -250 if e > 1240
f inc 768 if ns >= -542
ga inc 443 if gyc > 2498
rn dec 107 if g == 72
ga inc -420 if mx != 74
mx dec -763 if ic == 1140
b inc 586 if gyc <= 2505
mx dec -948 if gyc > 2509
zqo dec -384 if vkg < -1991
z dec 234 if rn > 1072
gyc dec -821 if v > -590
z inc 83 if v == -584
egk dec -835 if b <= -2941
cr dec -495 if v > -590
by inc 259 if cr <= -4852
cr inc 530 if mx != 77
vkg inc 381 if g <= 80
by dec -71 if az == -2992
mx inc -453 if g > 64
ic inc 410 if vkg > -1618
f inc 945 if n == 901
y dec 409 if nm >= -2884
z inc 870 if vkg >= -1606
av inc 187 if z >= 5521
nno inc -852 if ga > 1212
cr inc 788 if av < 3608
e dec -182 if by != 5143
nno inc -706 if ga >= 1228
vkg inc 782 if z < 5532
mx dec 839 if nno > -219
v dec 267 if b > -2952
v inc 901 if gyc == 3321
g dec -820 if rn != 1079
ic dec -221 if zqo <= 2259
ga inc -784 if e == 1425
ga inc -569 if bqr >= -404
u inc -206 if mx <= -1212
gyc inc -685 if nm == -2881
e dec 269 if mx <= -1208
av dec -207 if by >= 5137
nno inc -109 if ga != -131
ga dec 3 if ic != 1761
zqo inc 181 if nm < -2866
y inc -15 if by >= 5140
rn dec -617 if g != 884
g dec 574 if mx < -1213
ga dec -775 if bqr >= -404
ic dec 186 if v < 55
gyc dec 497 if ns >= -552
z dec 619 if nno >= -319
b dec -753 if av == 3809
by inc -890 if n != 901
b inc -714 if z == 4902
n inc 927 if v <= 43
b inc -107 if b <= -2947
nno dec 707 if y == 1183
vkg dec 199 if az <= -2996
gyc inc -684 if cr <= -3523
z dec -518 if zqo == 2429
ga inc -220 if cr >= -3527
zqo inc -922 if y <= 1183
rn dec 852 if gyc != 2138
nno inc 419 if ic == 1577
rn dec -951 if by <= 5130
av inc -557 if z == 4904
mx dec 599 if g > 327
az dec -594 if u != -5525
gyc dec 187 if y > 1173
v dec 2 if e >= 1153
gyc inc -814 if ns < -540
zqo dec -401 if av != 3249
ic dec -511 if g == 318
g dec -447 if g == 318
zqo dec 965 if by != 5146
gyc inc 658 if vkg != -824
nm inc -663 if e > 1156
n inc -974 if zqo <= 954
n dec 363 if az <= -2389
ga dec 300 if v <= 53
n inc -402 if y > 1186
b dec 839 if bqr >= -406
rn inc -188 if v > 57
av inc 952 if rn < 852
bqr inc 973 if v == 56
f dec -234 if b > -3899
nm dec -96 if zqo != 949
e dec 141 if ic != 2084
ga dec 146 if g > 755
av inc -333 if ga > -33
z dec 698 if e == 1015
e dec -493 if z >= 4200
v dec 234 if v >= 48
az dec 572 if vkg < -831
vkg dec 164 if u >= -5527
ga dec -933 if rn != 846
gyc inc -180 if ic > 2081
vkg dec -305 if z >= 4198
ic inc 50 if cr == -3526
egk inc -956 if zqo <= 939
n inc 265 if z >= 4215
az inc -574 if nm <= -2776
bqr dec -19 if ic == 2141
ga inc -682 if cr != -3525
g dec 864 if g > 764
ns inc -746 if f < 452
g inc -969 if f >= 450
ga inc -127 if e < 1518
v inc -903 if egk == 3043
cr dec 714 if nm < -2775
f inc 33 if ga != -835
bqr inc 919 if bqr != -382
nm dec -489 if z < 4210
vkg dec 962 if gyc != 1611
z inc -698 if ga >= -844
z dec 645 if e <= 1510
ns dec -501 if y != 1174
az inc -314 if av < 3868
mx inc -207 if ns == -792
z inc -604 if zqo < 952
g inc 466 if g > -1067
b inc -704 if nm >= -2295
nno dec 284 if e != 1500
cr dec 58 if z < 2263
rn dec 494 if ic > 2148
nm dec 211 if by < 5141
by inc 150 if av >= 3862
gyc inc -716 if b <= -4596
u dec 466 if ns > -798
mx inc -935 if cr == -4288
bqr inc 275 if b < -4587
v dec 771 if egk == 3043
vkg inc -902 if u != -6000
b dec -683 if nno == -1311
egk dec 525 if v == -1860
az inc 708 if by > 5284
y inc -820 if ic >= 2137
az inc -720 if zqo <= 940
u inc -299 if zqo < 955
bqr inc 248 if rn == 846
g inc 148 if n > -441
nm dec 213 if egk >= 2509
ic inc -840 if g < -928
f inc 98 if by >= 5287
nm inc 909 if v != -1863
vkg dec -856 if y >= 360
v inc -156 if zqo == 946
bqr dec 908 if gyc >= 900
zqo inc 836 if f == 581
ns inc -157 if ns == -792
egk inc -899 if z == 2259
ga dec 658 if ic < 2142
nno inc -278 if by < 5291
egk inc 502 if f > 580
z dec 807 if y >= 363
nm dec 612 if nno == -1583
y inc 914 if ns <= -942
gyc inc 419 if v != -2013
g inc 897 if v <= -2015
gyc inc 107 if vkg >= -1709
bqr inc 224 if z < 1460
mx dec 809 if ga < -1488
cr inc -401 if av < 3875
ns inc -521 if by == 5290
az inc -269 if ga == -1494
b dec -688 if by != 5294
n inc -746 if mx < -2225
y inc -452 if e < 1509
z dec 495 if n <= -1175
av dec 204 if egk != 2117
cr inc 30 if ga >= -1498
y dec -821 if gyc < 1437
av dec -105 if bqr != -543
by inc -897 if egk < 2130
az inc 392 if vkg != -1703
egk inc -34 if ga <= -1490
mx dec -635 if av >= 3658
gyc inc 307 if zqo < 1787
v dec 263 if v >= -2018
n dec 574 if f < 582
f inc -432 if g < -28
z dec 259 if av == 3663
zqo inc 472 if b == -3909
e inc -779 if bqr > -545
zqo inc 187 if v > -2282
e dec -395 if y != 1652
y inc 312 if az < -3021
ga dec -324 if egk < 2082
cr dec -409 if az < -3023
nm inc -790 if bqr != -533
ga dec 252 if ga <= -1493
ic inc -932 if u <= -6292
e inc -547 if vkg >= -1698
nno inc -171 if b != -3909
g dec -891 if vkg < -1690
ga inc 441 if egk < 2089
z dec -708 if ic != 2147
nm inc -402 if b == -3919
f inc -374 if u != -6291
ic inc -48 if ga >= -1312
egk dec -19 if b > -3911
av dec 305 if ga >= -1313
g inc -475 if mx < -1588
vkg inc -269 if vkg == -1700
gyc inc -535 if f > 572
nno dec -382 if ns >= -1475
nno dec 650 if y <= 1959
y inc 148 if zqo <= 2442
by dec -223 if u != -6286
y inc -319 if ga > -1313
nno dec 13 if av == 3358
ga inc -402 if gyc > 1198
rn inc 37 if f == 581
gyc inc -884 if rn > 882
ic dec 676 if zqo <= 2438
u inc 417 if ic != 2098
n inc 930 if zqo <= 2449
av inc 509 if ns >= -1477
y dec -981 if y < 1779
az inc -780 if ns < -1472
f dec -834 if by != 4622
ic inc 721 if av == 3867
e dec 916 if g <= 400
zqo inc 169 if cr > -4254
nno inc -685 if z == 1406
v dec -920 if zqo > 2440
nno inc 91 if gyc < 317
n inc -395 if nno != -2459
egk inc -746 if v == -1359
av inc 66 if cr == -4260
gyc inc 40 if ga > -1711
egk inc 914 if y < 1788
g dec 176 if u != -5869
b dec -550 if vkg >= -1974
g inc -545 if ic < 2824
nm inc -645 if cr <= -4256
b inc -103 if ns >= -1477
g dec 166 if zqo >= 2436
nno dec 665 if by <= 4618
rn dec 622 if nno > -3130
nno inc -591 if b < -3461
az inc -807 if egk >= 2272
g dec -417 if f >= 1425
by dec 547 if by != 4606
cr inc -579 if e != 212
nm dec 650 if e == 208
b dec -65 if by > 4064
b inc -263 if ns <= -1473
az inc -784 if g >= -494
b dec -193 if z > 1415
bqr dec 143 if zqo >= 2443
nno dec 385 if g >= -496
v dec 352 if ic != 2814
nno dec -521 if by != 4065
ga dec 198 if az <= -4612
by inc 926 if b > -3404
bqr inc -697 if zqo == 2441
vkg inc 124 if mx < -1588
u dec -564 if bqr < -1237
v inc -763 if ic >= 2812
egk inc 339 if az > -4611
z dec -617 if mx <= -1588
av inc -876 if cr >= -4837
n dec -600 if mx == -1595
v inc -354 if vkg > -1850
v inc 194 if vkg <= -1841
bqr dec -206 if av <= 3934
rn dec 547 if z != 2033
b inc 217 if u <= -5305
v dec -230 if egk != 2264
n inc -447 if b != -3180
az inc 497 if g >= -499
e inc -527 if v < -2051
u inc -889 if by == 4995
b inc 74 if egk < 2282
ga dec -65 if v == -2052
nno inc 156 if av != 3933
rn inc -880 if av != 3934
cr dec 825 if ga == -1840
y inc 499 if e == -319
b inc 525 if mx > -1604
f inc -731 if zqo >= 2437
cr inc 398 if gyc < 360
f inc 286 if vkg > -1846
zqo inc 761 if ic > 2816
y dec -877 if rn != -1166
vkg inc -405 if ga != -1838
vkg dec -522 if v <= -2060
mx inc 281 if nno > -3586
vkg dec -203 if bqr >= -1043
vkg inc 278 if az >= -4125
rn dec 544 if b < -2573
av dec 730 if mx > -1318
ic inc 49 if n < -620
f dec -599 if nno != -3583
e inc -871 if gyc == 355
e dec -735 if mx != -1307
n dec -73 if rn <= -1707
ns inc 896 if g >= -502
z dec -480 if z <= 2023
zqo inc 595 if v < -2043
mx dec 647 if vkg == -1769
n inc 743 if nno > -3589
gyc inc 129 if cr > -5267
vkg inc 703 if mx > -1966
bqr inc 378 if g <= -487
ga dec 852 if zqo > 3035
zqo dec -43 if y > 2280
ga dec 849 if cr != -5259
gyc inc -363 if av >= 3203
vkg dec 481 if nm <= -3884
g dec 609 if f < 964
av inc -951 if n != 187
ns inc -676 if zqo == 3079
nno dec -998 if av == 2252
n dec -624 if vkg > -1544
y inc -262 if ns == -1250
av dec 248 if ns < -1250
f dec 351 if z == 2503
bqr inc 535 if ic > 2858
f inc -725 if nno > -2589
ic inc 860 if v == -2052
nno inc -211 if v >= -2055
ic dec -324 if bqr <= -126
az dec 746 if f <= -99
g dec 985 if e <= -454
f dec 434 if z < 2495
egk dec 842 if bqr == -121
gyc inc 715 if y >= 2022
ns inc -573 if nm != -3888
b dec 415 if mx >= -1951
by inc -719 if ga == -3551
n dec -783 if cr >= -5268
nm dec 409 if by > 4988
u inc -72 if av >= 2246
ns inc 338 if v <= -2050
e inc 12 if rn < -1706
ns dec -354 if nm == -4299
egk inc -589 if zqo >= 3084
egk dec 856 if vkg != -1555
ns inc -439 if zqo >= 3076
by inc -942 if cr != -5272
z inc 119 if b >= -2588
cr inc -864 if ga != -3537
nno inc -333 if gyc > 828
z inc -530 if e > -451
nno inc -113 if u > -6271
g inc -213 if mx <= -1953
y inc 107 if ga < -3536
y dec -971 if az < -4859
n dec -424 if av < 2258
ic dec 632 if rn <= -1705
az dec -701 if ns > -1576
by dec -45 if egk > 581
z inc 111 if vkg == -1547
ic dec -737 if u <= -6266
v dec 13 if nm != -4289
b inc -616 if ic < 3838
av inc 266 if b <= -3190
nno dec -699 if gyc >= 834
y dec 400 if gyc >= 835
y dec -119 if ns <= -1567
n dec 452 if rn < -1703
egk inc -254 if vkg == -1556
az inc 568 if ns <= -1580
f dec -399 if bqr < -115
zqo dec 948 if nno > -2440
rn inc 154 if zqo == 2131
f dec -21 if b != -3190
nno inc -204 if g > -1683
v dec 190 if az >= -4168
bqr inc 236 if v > -2263
cr dec 554 if nm >= -4303
gyc inc -657 if e > -449
e inc 65 if nm != -4306
v inc 340 if az > -4171
mx dec 527 if nm <= -4296
g dec -426 if ic > 3819
b dec -766 if z < 2205
ic inc 822 if cr < -6677
cr inc -733 if n != 958
rn inc -759 if vkg == -1547
nm dec 588 if rn == -2315
n dec 310 if ic < 4641
n dec -24 if g >= -1274
n dec 341 if nm == -4887
cr dec 131 if av > 2513
zqo inc -78 if gyc < 181
mx inc 368 if vkg < -1537
gyc inc 157 if zqo >= 2053
rn inc -871 if vkg <= -1544
bqr dec 299 if egk == 576
cr dec 27 if b <= -2423
rn dec 848 if az < -4170
av dec 836 if egk <= 577
v dec -334 if cr < -7576
f dec -820 if u == -6271
az dec -367 if egk == 576
by inc -267 if bqr != -192
bqr dec 95 if cr == -7575
ga dec -641 if bqr == -279
ns inc -776 if y != 2821
by dec 177 if cr != -7575
nno dec 656 if g >= -1261
z inc -641 if az >= -3789
rn dec 93 if v != -1911
az dec -664 if f > 1139
ic dec -565 if e >= -380
by inc -600 if ga == -2894
zqo dec 580 if g <= -1263
zqo dec -324 if by != 3784
gyc dec -987 if ns != -1570
gyc dec -921 if mx >= -2111
by inc -529 if ic < 5211
av dec 272 if ic == 5210
nno inc 745 if e < -374
ga inc 893 if by >= 3782
egk dec -936 if bqr >= -284
vkg dec -146 if nno <= -1679
y inc -686 if ga != -2000
b dec -659 if u < -6265
b dec 418 if n < 629
az inc 613 if ns == -1563
vkg inc 385 if ga != -2017
egk dec 54 if az == -3802
vkg inc 330 if by == 3786
f inc -243 if u != -6271
gyc dec 751 if ns != -1574
nno dec -285 if ga <= -2006
vkg inc -257 if v >= -1921"""

maximum = 0
dic = defaultdict(lambda: 0)
op = {"inc": "+=", "dec": "-="}
for line in s.splitlines():
    arr = line.split()
    if eval(str(dic[arr[4]]) + arr[5] + arr[6]):
        exec("dic['" + arr[0] + "']" + op[arr[1]] + arr[2])
    if max(dic.values()) > maximum:
        maximum = max(dic.values())
print(max(dic.values()))
print(maximum)

# day 9

s = """{{{{{{{{<a}!!!aa!!!>ua,a,!>{!>!!!>a>,<!>,!!!!,!!!"!,!a!e}!>!>,<!!oi!!}>},<!!'u"!!!!!>,<e>}},{{<}eaa'<!>},<<>},<}<!},!>},<e>}}},{{{{}}},{{{<,!>,<!!}!>!!!>!!!>!>!>a!!,!!',>},<e,!!!!!><'!<,>},{{{<!<!>i'u">}},<!e!!!>!!eo!!""'!>,<a!i!!!>!!,,>}}},{{{{{{<o!!''!!!>!>,<e}a!>},<>}}},{{<aeo!!!>!!!!<!!!!!!!>,<uu!>},<{!!!>>},{<>}}},{{{<},!!'>}},{{<!"}}!!!ooe'!o!!!!<>},{<u!'aoa!!u{!o!>!>},<!!!>'>}},{{{<!>,<!!!>}!!!>u>},<'a,!>,<!{<!!!>e!>!u>},{{{{},<!>e!""!!'e">},<{e!!!>!}'}o!>,<,o!>},<!!}!>,<i>},<!>},<!oo'!>},<}}<'o}!>,<'!!!>'>},{<{e>,{}}}},{{},{}}},{{<uu!!!!o!>,<!<!!o!!!>!>e"'!>},<!!e!,!!!u!!!>>},<,!>}}<<!!!>,<ai!>{!e>}},{{{<a'!>},<o{ie!>},<!!!>{}au!>},<!!!!iu!ai>,{<!!{',>}},{<eu!o,!<}!>i!"!!!>a,uu!ao>},{<!!!>,<oe!>{e!!!>},<!!!!!!!>!!!>!ei!!io}!>},<"!!o!}>,<!!!><!!!><!!!!!!!>"!!!o!>,<!"!!!>,<!>},<>}},{},{{{{{<"!!!!!>>}}}},{<{!>},<}i'!!i!>!'}<!'!{}>,{{<!!!>ioi"u>}}}}}},{{{<{"'e<e!>},<!o!!,!,'!!!!!>>}},{{{{<ia'oa!!i<o,!>u!!!>ao'a>},{}},<!>},<!!!>!>},<!!!>"!>!>},<u,!>,<eauu}!!}o">},{{{<}',"'>},{{}}},<{<>},{<{!!"}!!!>!!!>{!,"!>},<!>,<!}!!!>ae}'>,<!!<u{!!!>!!!>},<o!!!!<!>,<!!}>}}},{{{{<o!!}!>},<a!>i!!!>},<e!e<,>}},{{{<"iao,}>},{{{}},{{{}},{<!>},<!!i'!>},<o!!{e'!{e"!!u"!!!>>}},{{<>,{<!>o"!>!>},<,ea>}},{{<e'>},{}},{<!<!!!>!>},<!>},<{!e,!>},<},e>,<!!!>"!!u{u{!>,<!uuuoi!!!>!>,<>}}}},{{{{<!!!>},<<"!!!>},<iu!>}e<io>},<e!>,<!!}}>},<!>a{{!!!>,<{!a}ua<',!!!o!!!>e,!!!>>},<!!{a!>},<e'oe!!{u!!u>}}},{{{<ai!!{}ai'>,<}!>{!>o!>},<!!!!!!!e!>'}<!a>},{<!!o}!!!>"!!ou!!o>,{<!>},<!>},<>}}},{{<io>}}},{{{<"!eui!>},<!!!>!>o!!!}>,{<o!!<ie!>!!!!!>!i!'!!e>}},{{<!!!!!>i!>,<,""}a}{!!!>{u!>,<!!'>},<!!!>,a!!!>,<!!iu<}!!!>>},{{{<!!!!'!<ao!>,<}>,<e!>!!!!!>i>},{<,a!{{{!>,<!>!!a!>},<i,!!'>},{{},{}}},{{<!!!!!>u!>'!>!!!>,o!>,<!>a!!,<!>},<!!',>}},{{<!'u}{>},<'!{'u!>,<!>},<!>,<!!!>},<>}}},{{{<!!e!>'>},<!!!><!"e!!!!ea<,ue>},{{<i!><u>}},{{<!>a>,<<"e,u!!!'i!'!!!!!!}!>}i"aa>}}},{{{<u!>ai!!!>!!!>'!>},<e!>!>u"i>,<aeiu}>}},{{{<,i!!!>!!e"au!!'"u>},{}},{}}}}},{{{{},{{<,!>},<<!!!>"!>,<!>,<<!>!!!!"!>,<!>,<>},<"<<{},!!!o,o!!!>!!!>!>},<>}},{{<{,<!!e!>{>},<"oi,!!e!!!>i!>,<{!>,<!>},<!!!!o>}},{{{<,{!>'i!>!!!>!!!!!>},<'i{u>},<!>},<!>uo!!o!>,<o!!e!ae!!',!>,<>},{{{<u!!!!!>"u!!{>},{<!<{uo!>},<<!>},<>}},{}}},{{},{{{{{<,,>},{}},{{<i'!!!>!>!!e!>o!!!!!!!e'!!!><!"",!!!>"u>}},{{<iiu!!{!!!>'aa!!!>},<!!!>!'}!!!>>}}}},{{{<i!!ae<!!u<a!!"''!>,<>},{<!!!!!>!!o!>a,<!!{!>!>,<,!!!!>}}},{{{{{}},{{<!!'eo!>!o<,e!>,<!>},<!!>},{{<<u',}!!!>!<!i!>},<!>>},{<e<e!>},<}!>,<ii!!<"!>},<!!!>>}}},{{<{}!>!>i!>,<!>!!!>!!!!"{!>,<,'!>},<>,{<!iee!!!!"ao{",!>u"!{!!!!}>}},{<{>,{<!>},<!e">}},{<a!!!>},<u>}}},{{{{<!>},<>},{{<!<e!!!!!!u!!!!!ea!!ue!!u}!>},<!>,<!>},<!!!>a>}}},{{<a!>,<ua<!>},<'e>},{<a!!!!!!!>>}}},{{<i!!!!<!>,<'{,!{!!!!!!}}e!!{<io>},{{<,o"e!>},<!>},<i{i!>},<!!>}}},{{{<a!>}!!'a"<ou>}}}}},{{},{<,!>},<>}},{{{},{<>}},{<!a!!!>u!!a>}},{{},{<!!,'>,<}o!!!>!!!>>},{{{<<,,!!!>!!!>!>},<e!!{<!>i!!!>o!!!>'!>},<!!!>>}}}}}},{{{<!"!"!,!>},<!!!>a{e!!!>!!!!!>>,<!>,<!>},<!!"!>,<ii'!!{'>},{<!>},<,>}},{<o!!,!i"'!>,<>,<ie,!<"oeu,'!!!>!>},<'i'>},{{<!!,!!{!!eai!!!aa!!!>'<!>},<!!>},<!>},<o!!!>,<iu}">}}}},{{{{<e>},{{{}},<!i!>,<i'!i!!!>!!!!}!!!>'<!>},<uo!>>}},{<,!!!!!a!>},<!uo!!!>,<!!e!!!>>,<>},{<>}},{{<e!!u!a<{u>,<<!!!>!>},<{!!!>,{!!!!o!u",!!!>'o!!!!a!'!!,>},{<}!>,<u!!,{!e'!!!>,<e!>!!!>u!!!!!>!>},<!!!>a!!!>!>>}},{{{},{<uueua!!!>!>},<!!!!!><!>,<!!!>e}<>,<}{uuo"!!o!e>}},{{{<}!>"!!!>{o!!!!<>},{},{{}}},{},{{<{!!!>eo!>},<,>},<!!{<!>,<{iu{!,!!oi!!"!{'!!>}}}}},{{{{<!!u!!!!!>e,"!!e!>!!,'!>,<>},{{{<<!>},<!!!>u>},{<!!!!!>"<u!'!!!<!>,<a{!!!>,<>}}}},{{<!>,<!>i!!a!>},<e"!>>},{{<<''o!>!!!>>}}},{{<!!!!u!!!!a,!!<"!>{ao>},{<<o!!!'!>,<u!>,<o!u!>{!!>,{<},,o}!!"ioo!>,<}!!,o}i!>,<<a">,{<!!!>!!!!!!!>!>},<,{!!ia!>,<!!!>!!!>a!!{}o>}}},{<a>,<!>!!o>}},{{{{{<{o!!e'}{,<!!u>}},{{<o"<!!!>!>},<i{!!a!!!>}'o{!'{>},<!!{u!a!>,<"!!{>}},{{<!!!>!!o!!<!>!>},<"!>a{!>},<'!>},<!>},<!!!uo">,{<}!>},<!!i!>,<!!!>},<!!!>!>},<!!!a!<!>i!!!>>}},{<}ia"!!!>o,<",!,>}}},{{<!>,<<a!>,<>,<}a<!!!!}!>},<u'"!!!>},<'!e>},{<!ue!!!>},<oe>},{{}}},{{}},{{{{}},{{<<<,!!o!!!!e!!!>}!!!>!>,<ia'"'"!>},<e{>}},{{<,oe!a}!>>},{<{!>},<!!e!!!>!>!!o!!!>u'"!>,<!>>}}},{{{<<'!>},<e!!!>!!!!!u!{e!!i!>,<!>},<'!!}!>,<!>},<!>,<!!!!!>e>},{<"!!!>,<!!!>},<!>}'!!"!>},<!"a<!!!>,e!}oe>}},{<">}}}}},{{{<!!}'!!{a!>,<!>a>},{<!!i!}!!!!!>!>,<e!!!,}!>{!>,<u!a!>,<>}},{{{{<!>!>,<>},{{<">}}},{{{<,i!!!>}!>,<!>!>,<!!!>},<e!>},<!>''!>>},{}},{{<!>,<{!!!>'!ai!!!>,<>}}},{{{{{<!'!!ei,!>!!!>!>,<!>{!}'o!>!!ui}>}},{{<!!!>!!!>,<e!ou{!>},<ei!!!>!uu!a!>},<>}}},{<<o{{"!!!>o!>,<!!}!!<!>,<}o'!>>,<}!,,},!>},<o!!{<"">}},{<!!!>{<!!!>,<'!>,<i!!!>o!'o>,{}},{<ui!ou!{o>}},{{<,!>},<!!!><"!!!!!>''>},{{<ou}!>,<!!}'!!"<!!u!!!}!!e!!"!>,<!{!>!!!!!>},<!!!!!>,<!!!!!>>}},{{<e!'>},<o{a!!!>,!!'!>},<!>},<!>,<ue""!><<<i>}}},{{{<<!>},<<!!!>,<"oai,<o!!!>!>>},{<'ue!!!><!!!>{!>},<e!!,!!">}}},{},{{{},{}},{<!u!>,<!"!>},<{o!!">,<>}}},{{{}},{{},{<,u!!'!>!>!>},<}!!e!{!!u!!!>},<!>!>},<,>}},{<>}},{{{<u}!"!!'u!!i!>,<!!!>}!!!>!''!>!!>},<!!u!!{,ui!{!!!!!>!!!>},<!!!!>},{<iie,!!!!!!!>'>,<!!a!!e',!>u{'!!,<!!!>'>},{}}},{{{{{{},{}}}},{}}},{{{{{<!!u!!}!u!!!>!>},<!>!!u!!{{e<'!>},<'!>!>},<>},{<"o!>,<!>,<!,!>,<u>}}}}},{{{{<e{<e{!!!>!>,<ii},}!>,<a>}},{<'au!>},<{{aaiu!!>},{<!i,ui!!!!!>i"!!iiiu}>}},{},{{<}!!'<ua!!!!!!o}a!>,<!>},<>,{}}},{{{{<i!>iie!o"!!,!>,<!>,<!>,<>},{<i{!>e!>'>}},{}},{{<'!>},<'!!}!!a!>},<e!!a}!{{'!>e>}},{{<}i"'!>,<!!!>!>},<!ae{!!o!!!>!!,!!!!!>,<!!>},{{<i<!!a,!'>,{<"i!>},<!,!>'euu!!!>,<,>}}}}}}},{{{{{{<'u!}!>!>},<a>}}},{{{<!!ee!!"}>,{<eu,!!!!'!!!>!>,<,{oee}<!>},<i,>}}},{{{<u!>,<!!!>ai!>},<""e!!!>!>,<!u>},<!!!!!!'!!'!!i!!"ei,}!!!i<,!>},<!>>},{<a!!!>aui!>},<e!<!>}"}!>,<,!!!>!>},<!!!>!!>},{{{}},{<!>!ue"a,!!!!!>e!!,!>!>,<<>}}},{{{<!>,<"!!{,<!><!>},<<!!iio!>},<>},{}},{{},<a,"!>,<}!>,<a!!!>e!!">},{{<!>!o!!uu!,!>,<u>},{<!a!!!>!>,<iu!o!!ia!!!>!>,<!!!>,<,o!!!>!>!!!>e{>}}},{{{<!>o!!!>}oa"!!!>!a"!{>,<i>},{{<'>},{<ee!!!>!!!a!!ia!,!>,<!!!!}!!ui!>u<u>}},{{}}},{{<a<!e!!e!!!!!>!u!!!>"!>,<o!!}!>>}}}},{{{{}},{{{<!!}{o!u{!<o'}u!>,<!!!!<>}}},{{{<e!!!>!>},<!>!>},<!u>}},<i'ei'!>},<!!oo<i!>},<!!!>,o{!>>}},{<"e!>,ia"!>},<u!!!a"!}<ea!!<!{>}},{{}}},{{{{{<!{aiioi<!ei!>!!!>},<a!!a!>},<!u!!!!!!,!}<a>,{<'oo!!!>!>,<!!!!!>!u!>},<>}},<"},!!!>,!>!!!>!!!i,>},{{<{!!u">,<{,{!>},<{!}'>},{{<<o!{'!!!>,<>},{<i'oo!{u!!">}},{<oo>,<<>}},{{{{<i{!>,<!>},<"<!!!>e<e!>,<!!!""<!!'o>}},{{},<e"a!>},<au,>}},<!!i{!>,<!!!!<>}},{{<"<o}'e!!!!,<>,{<>}},{<>,<!o!>},<"!!!!!>!"{{"''au!!o,<!!!,>},{{<!!!>!>!e<o!>,<>,<>},{<>}}}},{{{{{{<"}>},{{<!!{u!!!>,<!>},<<!!!!"'>},{<!>},<'"}o,o!>},<!!o!>},<!!ie'!>}!>,<a,>}},{<{'e,a!>i!>,<!!!>,<!!!!"'a,o>}},{{<i"i"!>},<!!,!!!>!>'a!{!>,<!!!>,<!>},<e>},{{<!>,<>}}},{{<'i!>,<,o,!!i'i!!e<!}o>},<!>}e{!!o<!!!>o!!,!>},<,!>,<!>},<!>},<o!!{>}}},{{<!i{!!,u}'u!ea>,{{<!!oo>},{<,>}}},{{<!>,<!!i!!!>'!!u}!!,,u}<!!,!ea>},{{<!!i!!,"!>'o"{ou,'}>},<!!!>>}}},{{<e'!!<u>},<!>,<i}!>!>,<<!!!>"{u<uo>}},{{{},{{<u!!euu!>},<>}}},{{},{<!!!>a<<}{""'!!!>>}}},{{<}!{'!!}}e,'e!!'}!>},<!!e>},{{{<u!a,eoo!>,<{!!,<>},{<!>,<>}}},{<!<}uei}o,io!>,<{!!!>,<!>>,<!!{oioi!>,<!!,!>},<iu!>},<!!o,}!u<>}}},{{{{{<!!!!!!e!>},<u!!i!!!>a!">,<a!>},<}>},{{},{<e!!!>>}}},{{},{<i!!>,{}},{<""{!a>}}},{{{<a,"!!!>!!'!au',a!'aie'!>,<{o>,{<<<<!!e<>}},{{<e'"!!a""!!>},{<a!oe!>},<,<>}},{{<}i'<!>!>,<}!!oa!!eeu!>},<a>}}},{{},{{{{}},{<!>!!<!!}>}}}},{<!!!!'i,<!>},<"{!!"},>,{<!e'!>},<,!><!!{"!>!"!>!!'>}}},{{{<!!io!>,<ioi,>},{<i{!!!>,<!>!<!!!!{ae!!!>!>},<e!>!!!>'a,"!>},<>}}},{{{<>}}}},{{{{{{<{!>},<!!!!ua!!{e!>a>}},{<oa!!u{,!>},<e!>,<!>'o'u>,{<!!"!!!>,<}!>!!}!!<"ui!>,<!"!>},<,ou>}},{<o!>>,<!>},<{!!,a!>,<!,aa!>'!!!!!>"!o!>,a>}},{{<!"!!!e!>,!o,'<ea'i!>>,{<!>},<'!,!>},<e}>}}},{{{<!>,<!!}!!!>,<a!!<e}!o!>i,!>},<,>},<o,>}}},{{{},{{<!a!!!>!>},<o!!e<!!oa!!}!!>},<}!>!!!!i{>}},{<<"!>!>,<<<!!!>,!!!>!!!"{a>,<!>,<!!,!!!!!>>}},{{{{<>,{<{o{i'<{!!"i<!>,<u!>>}}},{{<u!>,<!>,<!!,!}!ee,!!!!'<'!<!><>}},{{{{<!>},<'!!!>ue!o!>!!<!>},<<!!>},<!!!>}>},<!>!>u<>},{{},{<!>},<!o!>,<i<e}>}},{{<u"u<,u"'a}<i!!!!!>e}>,{<!>,<!!!>>}},{}}}},{{{<!>,!!!>e>}}},{{<,oe>},{{<<!o!!!>},<!>,<u!!}!!!>'!!'"!!!!!>>}},{{{}}}}},{{{<!>},<!!a!>,<!>!!}a"<'>,{<!''u!!!>},<!!'aa!>i!!o'e!!!a>}},{<!>},<o!>i'!a!!<aa>,<'<e>},{{<'!!!>},<}i{i!!!>!!{!!a,!,>}}},{{}}}}},{{{{<e}!!>,{<e!!!>!!!!!'u{!!"!!!}o!'aou!!!!!>a>,<!!o}}ai!>,<i>}},{<!>},<!>,<'!!!>u!o{oo{'!!!>>,{}},{{<!!{!""o,}!!!!{!o<!,ii!!<,!!u,<>}}},{{{<<!>,<!>},<!>,<!!}!!!a,<,o!>},<!!a}!>,<!{}>}},{<"}{!>,<!a<<o!{u}!!!!!!!!"<!>,<!!<!>>},{{<<!!,"!>!!<!>,<a!>},<e,!>},<<{!!>},{<<!>,<!!{!!!o!}!>,<!!!>},<!o>,<oo>}}}},{{<{o!!!!!>{!>,<}>},{{}}},{{<{!!!>,<<!>!!!!u!>!!!>'i{,}u>}}},{{{{{<!>},<!!!>e!>},<oui">}},{<,,!'!>,<o!!!>ua<!>>}},{{{<{!,!>,<!!!>"!!!!<!>,<<!!<a!!''!>>}},{{}}},{{{<!!u}{!>"!!!>},<>},{<!!!>u'ea!>eu!u!!!><u"e,>}}}},{{{{{},<!!!>!u!!!>},<,{oi!>,<'!!!>,<>}},{{{{<!>,<"u}!!">,{}}},{<i!i,{{!>,<{!!!>!>!!uuo!>,<'!>,<>,<!!!!!><ioe!<!!ae'!!!>},<,>},{}},{{<<}!!{!{!!>},{<!!!>!ioaau!>!>},<ou,oo>,{<!>{e<,iei!!au!!!><u{!>},<>,<!!!!!>'!""!!!>e{!!!>u>}}}},{<!!o!!!,<!'!!!i>}}}},{{{{<a!!!!!!,iai!!!{!!o!!e<uo!!!><>},<}!!'!>,<<a,!!},!>,<!!!!!>}'!>,<!>u>},{<!!!>!<o!!!>{o!uaa,!!!>{!!!!}<o!!!>!>},<>,{<,"{ae!>},<!>},<!!!!!>!!!>!!!>}e,>}}},{{{<<"!>'a'!!uu>},<,!>!>a!>!!>},{<!!!!'!!!>e!!!!!}uu<!!"!o!{ie!>"eo>,{}},{{},{{{},{}},{<!>,<'!>e!}!!a<o>}}}},{{<!!!!!>},u!!!>e<{!!u">},{}},{{<,'i!!!>>,<"e<,'e{u!!!!o}"!""uu!!!!!>!>},<'o>},{{{}},<o!>},<!!!>!!!>e,!!!>,<!>},<,!!!>,<a>}}}},{{{},{{}},{{{<>}},{<>}}},{{},{{{<ueao>,<ou!!!>},<!>!>ei"e<i!!>},{<!!!>,<!>,<u<,!!a}<!>,<e>}}}},{{{{{{{<"!>">}}},{{<{!,}!>!!!>,<"!>},<!!!i!>},<i!!'!!uau!!!>!>},<>,{{}}}},{{{<>,<!>,<!>,<!!!!ioi!!!><{{}!!!!!!'>}},{<!!'!!{o!!i!!i}o!!!>},,>,{}},{{{<>,{{{<e!}{!!o""!>u!!!>">},<!!'{!!!>"!!!!!u!!!<,!!!>>}}},{<!!!>!!a!>},<}u!!!><!>,<o!!!>!uo}"u!{!>!!<>}},{{<a!>,<ui!!<!!!!{o!>}}!>},<"e,>,{<a<aeu"a!!"u!!i!!u!>},<!>,<!>,<'"<a<>,<>}},{<!>},<}"e'a!>},<!!'!>,<e!a!!!!o'!{!>},<!>},<'>}},{{{{},<<<o!>},<!>,<!!}!!!}>},{{},{<u!!'}i!!!!>}},{{}}}}}},{{{<"!!e!>},<i}!>i>,<!>},<!>!>},<>},{<!!oeou!>},<i!au{ai!!!!!>!>!>,<!!!>>,{{{}}}}},{{{{{<e!,,,!!u}i!>,<e,}}o!'>}},{<!!!>>}},{<{},!!iue''o!!!!!>!>},<>}},{{}},{<a!>e'!!,!!!>},<>}}}},{{<>}},{{{<'}{ae>},{<!e!>,<<}!!!>a!>},<!>,<!!!>!!!>a!!o>,{<!>},<<{a,e,,i}o!>,<>}}},{{}},{<ui!!!!ui!>,<{!>},<>,{}}}},{{{{{},<!!!!!>,<a''ao!>},<{!",>},{<!>!!u!!!!!>a!!!!!>,>,{<!>!>,<!!!!!>i}u!!!>!!!>,<!!uu!>},<!!>}}},{{{{<iai,!>'!>,<,u!!!>},<!!!>!!ao>},{<!!!>{!!!u!!',a!!!!!>u!>,<{>}},{{{}}}}},{{}}},{{{<i!>,<"!>,<{>},{{<e!!a!!!!!!}!!!>!!i<!!!>{>},{<!!!>!!!>}!!a!{,e!>a!!,!!!>>}},{}}},{{{{{<e!!iue<e!!,>}}},{{<o!>},<,!>,<>,{<i,,"{a!'}{o>}},<!!!>,!{!!!>},<!!oa!!,oa{!>>}},{{},{{<!!!!e'!>},<{!>,<!!i!}{a!!!><uu,!!!>},<}!!">,{}},<!!eo!>,<!>,<,o!>,<!>},<,!!!>}"o<!>,<i!!!!!!!>},<>}},{{{},<oae!!!e!>,<>}}}}}}}},{{{{}}},{{},{<!{'ie'!!!>,<!>,<ou!>,<!!!>},<{ea!u!>a!!!><>,{{<o!!!!!<,i<!>},<i!}!}!!!>,<!>u{!!!>>}}},{<!!!>a!>,<<{e{!>},<}}!>>}},{{<!>,<e>,{<!>},<!a!>a!!!>!!!>o!uio{o>}},{{<!!!>!!o!!iu!<"}!!o{'!{ooio<>},<e>}}},{}},{{{{<>},{{{},{<!!!>},<i!!!!!>!iaa,}e!>!!o}a!!!>},<>,<e!>},<!>,<!!i,,,"'uo>}}},{{<>,<>}}},{{{<!ee!!!!!>!>},<'!!!>!>i>}}}},{{}},{{{<}!!!>{!!>},{<'a,!{i!!,!>!!'!>}u>}},{<!!"!>!>,<">,{<<<!><o!>},<!>},<e!!<"!>>}},{}},{{{<!!!!!>!!!!!!<"<!"{}!>},<!!!!!!!>e}'!!{!!i>}},{{<!!i!>>,<o"!{'!>!>'!>,<!!<i!>},<o!>},<!!!>,<!!}a!>,<!!>},{{},{<!!a">}}},{<!>,<ii!!,>,{<a<o"!>>}}}},{{{<!>,<o!!!>}>},{{{<u>}},{<!>},<!>},<>}},{{<!!!!!>ao!>},<<!>},<!>,<!>,<!',o!>,<!!{!>,<!>},<!>},<{>}}},{{{<}!>},<<a>},<,!!!>ua!>!>,<o{u!!!i!>>},{{<'o>}},{{<e!>},<!!!>>},<!>!>,<"<!!!!i}>}},{{{{},{{<!!<o<!>},<>,{<>}},{{}},{}},{{{<>},<eoeuo!>,<>},{{{<o!!,!>,<!>"o!>,<,!!!>o'!!<oe>},{{{},{}},{}},{{<!>!>},<eo>},<>}},{{<!>!>",!!!>,<!!<,!>>},<!!!>{!>},<}<uo!!oe!o<o!>,<"{"<>},{}},{{},<!!{!!!!!>!>i!>'{ei!!!a!!!><!!{!!!!!>}<>}},{{{{}},{<i!!!>!>},<!>a!>},<"}!!,u,'{a!>},<{>,<!!!>io!!<!!{o!!!!!,e,>},{{<e>},{}}}}},{{{{{<u!>,<">,{<<!>uo!>,<>}}}},{<<u}"!<{{!!}!!a!!">},{{<}!!!>},<i!>},<!>},<}>},{<!!ui>,{}}}},{{<}"o!<ae!!'!>},<!>},<'u'!>},<<>},{{{<ai,}io!!!>e!>,<a,>}},{{<!>!><a!!!>o!!!>},<,{,a<u!!}e>}},{{{<'!>}!!'u,!!!i!!u>}},{<!>,<o!>!,>}}},{{{{}}},{{<!!!>,a!!<iae!!!>{<!!ao!!!u>},<!!!>!!<!>i"!>,<!!!>!!iu!>},<!!"'"!}!>,<<,>}}},{{{{{<iu!>},<'aae!o!!!>{aa,!>!!!>,<>},{<u!!!>,io<{u!!!!u>,{}}},{<}!<!!}!!!>!>},<}!>!>!>!!i,!>'!>,<,">,<{ioo!>},<!!!>{}a'e"!o>},{}},{}},{{{{}},{{<!!ue<>},{{}}},{{<a!,>,{}}}},{{{}}},{},{{{<o!!!>!>,<!>i!>},<,e!!!u<!>},<>,{<{<!!!>a!!!!'oi<!!!>!!}!>},<!!!>{>}}},{{{{<!!'u,>,<!!"!!}"!!{!i>}},{{<!>},<{!!<}<e>,<u!>,<!!!>!!!>!>,<a<!!!a!!u!a"!!,!!''>},{{{{},{{<!>!!!>!>,<e!!}!><!>,<!!!>,<'!>e!>!!ee,>}},{{{<,o!,,o<!!i!u!>>,{<!!!!ii"{}!!!>',>}},<!><"a!!!!{a!>},<e{!!!>}}>},{{{<"',!a>},<!>},<'!>,<!>,<{i!>},<!}!!!!!!!>!>,<i!>!'!!}<>},<{!o"o>},{{{{<i!!!!'{>}},{{<!{!}!>e!!!>!!!>i'e,,a}!>u">},{<!>},<u!>,i!i!!!>!>,<,a!!'"",uu>}}},{{},{{<!u!>a"}>},{{<!<iu!!!!!!u'''>}}}}}}},{},{<'!oue!!!>oa!u!>,<}e!>{o>}},{{},{{{<!!!!!eii!!!>},<>}},{{<}!>},<e<!>!!!>i,!!!>},<!e!!!!!>e!!!!!>">}}}},{}}},{{{<!!!>"!,!>,<!>!!!>,!!!!!>!!!!!!!!'oa!!u{a"!!!>e>},{<{,!!!>!>,<<!!!>,<"!!!>!>},<!!a"o}'>}},{{<>},{{<!>},<"!!!!!>'!>,<!>>},{<!!!>!>,<e{,a!!e}!>,<u<}!!i!>},<!!!>'>}}}}},{{{{<!!!>o<!!!>!!!!e"!!",!!!!!!i!!!!!>!'>},{<!!e!>,<'!!!>>}},{}},{{{<!'!!!>!ao!>,<!!ia!>},<!>i!>},<'!>,<>}},{{{<o!!,>},{{}}}},{{{<"!>,<!<<!>,<'>}}},{{},{<"!a!>},<ia{!>!!!>{!!!>},<!!}a"!!'!!'"u>},{{<a"!!!>},<'!!!>i!>,<',}}>},{}}}},{{},{{<o!!!>!!!>!i}''eu!>},<!!a,!!!>>},{<{!!!>o'u'oa!!e,>}}},{{<!>,<!}<}"!!!>u,!>!!!!!!!>!!!!o>,{<{!>},<!>'e!!"!!e>}},{{},{}}}},{{{<!>,<!!!>",!>oo{!>},<e'!!!!!>>},{<!>'a!>,<eu!!!>u}!!!!u">}}}},{{<!o'!i!>,<,!!",a!>},<>,{<{}oe!!!>}{!>},<,{'!>},<u!!!!!>,<>}},{{<'ao'a!!,!!<i!!!>>},{<i}!>,<'e>}}},{{{<<!!!>,<i!!!!!!!>}>}}}}}},{{{{{{{<{!>,<o"u}!!!>{o>},{<ue!!{>}},{<!!i!>},<o,!}eo'!!ue!>},<e>}},{{<{{!!i{!>},<!!!>!!!!!>},<e'<'!!{!>},<>,{<a!>,<'!>{!!!>"!}"<a}!!!>!!e!!ii!>>}}},{{{{{}},{<!!!'!!!!!>!,!>,<i,,i"{,e!>,<!>,<,>}}},{{<<ai!!!!!!!>!!!>},<"'o!>,<o'!!!>,<!!{}>,{}},{{<!!!>!>},<i!>},<i>},{}}},{{<<{>},{<!!!>,!!i!!ea<}!!!!o{}a!>,<,}!>>}}}},{{<"a!>},<ee,!>,<}!!!!!>'eoi{!!}!>},<>},{<!!i}!>!>},<!u!>!>,<}",!!'!><!>!<>},{}},{{{<u!>,<ae!i!>,<!!e!!!>iia>},{<!>,<!!!>a{u}ieu!!a}!!!!e!>},<o!>},<!>u!!u!>},<>}},{{<!!!>>,{<'>}}},{<!!u!>},<,!!o!!!>!!a!!!>!!}>}},{{},{{}}}},{}},{{{<e'o!>},<!!iie!>,<,!>,<!>!!e!>},<!!!!!!!>,<>,{<!!!!!>u!>,<e!o!e!>!!!>!e>}}},{<<!>,<i"!!}!!o!!!>!e{aaoui>,{<,}i'i"}"ou>}}},{{{<>},{<!!i,oa!!!>!!!!!>}}}eu>}},{<iaa!!!!i>},{{{},<<u!!!>!!o!>,<',!!!>u!!!>!!'{!>'!!,e>},{}}}}},{{{<}!>,<!>!!!>},<>},{{{}},{{<{,!>u"!!a"',<}!!!>u!!!!!>a!><!e>}},{<!>,<!!"'}!oa}uu}!{e'ei!!oa{!!!!!>>}}},{}},{{{},{{{<!!e">}},{{{<!!!>!!,">}},{},{{<a"oe!!!>"<!>,<!>,<">},{<a!>,<i!>!'!!!>u'!>,<,!>,<o,>}}}},{<"<!!!>iii!>!!!>},<<!>,<!!!>},<!!o!>,<!!!>ui">,<<i<a!!'"}<e!!!><!!!!!"}e,,!a>}},{<euo<!!!>},<u>,{<!!,!!u{!!!>!!!!!!!!}e<>}},{{<'}i!>},<a"e!!!>ue!!'oa>},<!e!!!>>}}}},{{{<'{!>,<a!ai'!!!!!><u!>,<"!>},<>},<a}!>},<}eo!!!>ai!>},<e',!>,<a!>!a"}>},{{<}o!>ao"!}<<>},{{<>}}}}},{{{{{<!!!>!>},<!ai!!>},{<{>}},{}},{{{},<i},ue!!!!ou!ee!'e'!!'>}}},{{<!>},<ii!!!>!>,<!>},<<}!>},<!,!>},<"}a>},{<,!!!>}!>},<!!,!>},<!>u<i!!"!>,<'u!>,<!>,<!!!>>}},{{{{{<"e!!!!!!u!!!>!!"!!!>"!}!oo!!!>,<>},{<!>},<!<!'u!>,<ae>}},{{},{<i!{>}}},{{{<{'!!<}!>,<,i,!>},<!>,<o!!!>,<}!!!!o>},<!!!>!e}a!e!>}!!o>},{<!o!!ae,a!>},<}}!>},<}{!!>},{<ea!>io"'{!<!>,<>,<o,"a'!>,<i!!!>}}!!!>,<!!<!>,<!}{a'>}},{{{{},{<{!!!!!>!!u'!!!!!!!<}e"a}>}},{<!>},<!!!>io!!!!!>},<,e,}!>!>!!e}!>},<ui<>,{{<i}o!!!>!!!!,{!!ee!>,<,!!>}}},{<!>},<,!>},<>,{{<{!>,<{"a}!!!>!!!>!!a!!ai!u>,{<ie"!"i>}}}}},{{{{<!"!!!>!}!!a!!>,<!>u!!!>!!,o!!,<!!<!>,<"!>,<e!!!>,{}!>},<!">}},{{}}},{{{<!>},<a"!!oo!!!!i>,{<uoo!>},<!!!>!!e,e!!u!u,i!!i,>,{}}},{{{<!>,<'i!>},<{e!{!!i>}},{<uiua{!!<e>}},{}},{<io!>e>,{{<i,!}!e>},<,!>{!!!>!a!}>}},{{},{{<a!>,<a!>!>,<oi!!!!!>,<!>!"!!a!!!>!<!<>}}}},{{<"ioe!>,<!!a<!o"!>!!i{!!!>,<!>!!o>}},{{{},{}},{<>,{<'!!'!>!i<!>>}},{{<!>,<!!!>,a<o<{!,}!a!!!>,!!!>>}}}}}},{{<"'",<'>},{{<u},!!!>",!>},<e{e!!!>!!!>!>,<!!'o}i>,<!>,<{{}i"a{!!!!!!!>,<}o,>},<!ii>},{{<{!>,<!!o{>}}},{},{{<'uo!>ui{!!!>!>,<!'!!'!"eo!<!!{!i>,{<!!,{{i!!!>,<!o>}},{{},{<o>}}}},{{{{{{},{}},{}},{{<e!>e!!o!!!>ue"{!!!>!!!>!>>}}},{{<>,{<i",a!"">}},{{<!i!>,<!!!"e!!u!!!!!!!>o}e"}>},{}}}},{{{<},!>,<!!!>uu!!'}!!!>o!!}<{!!!>,<u!}>,{{{},{{},{<<a!<!>},<u!!i{<!>},<>}}}}},{{<!>!>o!!!>!>,<<,!"!!}">}},{{<!!!!'o>},{}}},{<ao!!!>!!!>!!!>!>},<!"aao"{!>},<!>>},{{<'oa{!u}!o!!e!>},<!!'>}}}}},{{{{{<!>},<o}o!!!>,<'>}},{}},{}},{{{},<!>,<i!!e!>},<<<!>,<e{aa!iouie>},{<!!!>,>,<{!!!>,<'!!!>},<"!>"}!>},<!!!>,<!>!!!!!e!!!!,!>,<>},{{<!!!>,<>}}},{{<!>!>},<<<!!e!!!!!>>},{{<}!>},<'>}}}}}}"""

s = re.sub("!.", '', s)
lengthOfString9before = len(s)
groupsRemoved = len(re.findall("<.*?>", s))
s = re.sub("<.*?>", '', s)
print(lengthOfString9before - len(s) - 2 * groupsRemoved)  # part 2
s = re.sub(",", '', s)
sum = 0
level = 1
for c in s:
    if c == '{':
        sum += level
        level += 1
    if c == '}':
        level -= 1
print(sum)

# day 11

input11 = '''n,nw,nw,nw,sw,sw,sw,ne,s,s,nw,s,s,ne,se,s,s,nw,s,se,se,se,se,ne,se,ne,ne,ne,ne,ne,ne,ne,ne,sw,se,ne,sw,n,s,ne,ne,sw,n,ne,sw,nw,n,n,ne,ne,ne,ne,n,se,n,n,n,n,n,n,n,n,n,n,nw,n,n,sw,nw,n,nw,s,nw,n,n,s,nw,ne,n,se,nw,nw,nw,nw,se,s,s,s,s,s,sw,nw,n,nw,nw,se,nw,nw,nw,nw,nw,nw,sw,nw,nw,nw,se,nw,nw,nw,nw,nw,s,nw,sw,nw,nw,sw,sw,sw,n,s,nw,sw,sw,nw,nw,nw,s,n,n,sw,sw,nw,nw,sw,sw,sw,n,nw,sw,sw,sw,sw,sw,sw,sw,sw,n,sw,sw,sw,sw,sw,sw,nw,ne,sw,s,sw,sw,sw,sw,sw,sw,s,sw,sw,sw,sw,sw,sw,sw,sw,sw,s,sw,s,s,sw,sw,s,s,s,se,nw,sw,s,s,se,sw,nw,s,se,s,sw,sw,sw,s,sw,s,s,s,s,s,s,s,s,s,sw,s,s,ne,s,s,ne,s,nw,sw,s,s,s,nw,s,se,s,ne,s,s,s,s,s,s,s,s,s,s,s,s,n,s,s,ne,nw,s,s,s,se,se,s,s,nw,se,s,se,s,s,s,s,sw,sw,s,s,s,se,n,se,s,ne,se,s,se,nw,s,ne,se,se,se,se,se,s,s,se,ne,s,nw,se,s,se,sw,se,se,se,se,se,s,s,n,ne,se,s,se,n,nw,s,se,se,s,s,s,se,se,se,s,sw,se,se,se,sw,se,se,s,se,se,se,se,se,se,ne,se,se,ne,s,se,n,se,se,se,se,se,ne,se,n,se,ne,se,ne,se,ne,ne,nw,se,ne,s,ne,n,se,sw,se,se,nw,se,ne,se,se,s,ne,n,se,se,se,s,ne,se,se,ne,se,se,se,ne,ne,sw,ne,se,s,ne,nw,nw,ne,n,ne,se,nw,s,ne,se,ne,ne,se,ne,n,ne,ne,ne,ne,ne,se,ne,sw,ne,sw,ne,ne,ne,ne,se,ne,ne,n,ne,ne,ne,se,n,se,ne,se,nw,se,ne,ne,ne,ne,ne,se,s,nw,ne,ne,ne,ne,ne,ne,ne,se,ne,n,ne,ne,ne,se,ne,s,ne,ne,ne,sw,ne,ne,ne,ne,ne,ne,ne,ne,se,ne,ne,n,sw,nw,se,ne,ne,sw,ne,nw,ne,ne,ne,n,s,ne,ne,ne,n,ne,ne,ne,se,n,ne,se,se,s,ne,ne,nw,ne,ne,sw,ne,se,n,ne,ne,s,n,ne,ne,ne,n,ne,ne,n,nw,ne,ne,ne,n,ne,n,s,ne,se,s,ne,ne,ne,ne,ne,nw,s,ne,sw,n,ne,n,ne,ne,nw,se,n,ne,ne,ne,n,n,ne,n,ne,ne,ne,n,nw,ne,n,ne,n,ne,n,ne,ne,ne,nw,n,s,ne,ne,sw,n,ne,n,ne,s,sw,ne,ne,ne,ne,ne,ne,n,n,ne,ne,n,s,n,ne,nw,ne,n,ne,n,s,ne,ne,ne,n,n,s,se,nw,n,ne,n,ne,n,n,n,s,n,s,n,n,ne,n,n,n,n,ne,n,n,n,n,sw,n,n,n,n,n,n,sw,nw,sw,n,n,n,n,n,n,ne,n,s,nw,n,nw,n,ne,n,n,n,n,s,n,n,n,n,n,n,n,n,n,sw,s,n,ne,n,n,n,n,s,sw,n,ne,n,n,n,n,n,n,n,se,s,n,n,sw,n,se,n,n,n,n,n,n,n,s,s,sw,n,n,n,n,n,n,sw,nw,n,n,sw,s,nw,sw,se,n,n,n,n,s,n,nw,nw,nw,n,sw,nw,n,sw,s,sw,nw,n,n,n,ne,n,nw,nw,n,n,n,n,s,nw,se,n,n,se,n,nw,nw,n,n,n,s,n,s,nw,n,nw,nw,nw,nw,nw,sw,nw,ne,n,nw,n,n,n,nw,se,sw,n,n,s,ne,n,nw,nw,nw,nw,n,n,nw,se,n,n,n,se,n,nw,n,sw,se,nw,n,n,nw,nw,n,nw,n,nw,nw,n,n,nw,n,n,nw,n,n,n,n,n,n,n,n,nw,nw,nw,nw,sw,n,n,nw,nw,n,se,s,n,nw,n,nw,nw,n,n,nw,n,n,n,nw,nw,nw,n,nw,se,nw,n,n,nw,n,n,n,n,n,nw,n,se,s,ne,n,nw,ne,nw,nw,nw,n,nw,nw,n,se,n,nw,se,s,n,ne,n,nw,se,s,n,n,ne,n,nw,se,nw,nw,n,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,n,n,nw,nw,n,nw,n,nw,nw,nw,n,ne,nw,nw,nw,n,nw,nw,sw,n,nw,sw,nw,nw,n,nw,nw,nw,n,n,nw,nw,s,nw,sw,nw,se,nw,nw,nw,nw,s,nw,n,nw,nw,n,nw,nw,nw,nw,n,ne,nw,nw,nw,nw,nw,nw,sw,nw,s,sw,nw,nw,nw,nw,nw,nw,nw,nw,ne,nw,nw,sw,nw,nw,nw,nw,nw,nw,s,nw,s,nw,nw,nw,nw,ne,nw,s,nw,nw,nw,nw,nw,sw,nw,nw,s,nw,sw,se,sw,nw,nw,s,n,nw,nw,nw,s,nw,nw,nw,nw,se,nw,ne,nw,nw,n,nw,nw,nw,sw,sw,n,nw,nw,sw,nw,sw,nw,nw,nw,n,nw,nw,sw,nw,s,sw,se,nw,nw,nw,nw,nw,nw,nw,sw,nw,nw,ne,sw,nw,nw,n,nw,sw,sw,se,nw,nw,nw,n,nw,nw,nw,nw,s,se,ne,sw,nw,nw,nw,nw,nw,nw,nw,nw,nw,sw,sw,n,se,s,s,nw,n,sw,s,s,sw,sw,s,nw,nw,sw,sw,nw,sw,nw,nw,nw,n,sw,sw,s,nw,ne,ne,sw,n,se,nw,sw,sw,nw,sw,nw,ne,nw,nw,sw,nw,nw,n,nw,se,sw,nw,nw,se,sw,sw,se,sw,nw,se,nw,nw,nw,nw,nw,nw,sw,nw,sw,sw,sw,n,sw,sw,nw,nw,sw,sw,nw,sw,nw,nw,nw,nw,ne,se,nw,nw,sw,nw,sw,nw,sw,nw,nw,nw,sw,nw,sw,se,sw,nw,sw,n,ne,sw,sw,sw,sw,se,nw,se,sw,sw,nw,sw,sw,nw,sw,nw,sw,sw,sw,sw,sw,sw,nw,sw,sw,sw,sw,nw,sw,sw,nw,nw,sw,se,sw,nw,sw,sw,sw,nw,s,ne,n,s,n,sw,sw,sw,sw,se,sw,nw,nw,se,nw,sw,nw,se,sw,sw,nw,sw,ne,sw,s,n,se,se,sw,s,s,sw,sw,nw,s,se,sw,sw,sw,sw,s,nw,n,nw,sw,sw,sw,nw,sw,sw,s,n,sw,nw,nw,nw,se,sw,sw,nw,se,sw,sw,sw,sw,sw,nw,n,sw,nw,ne,sw,se,sw,nw,n,sw,se,sw,sw,se,nw,s,sw,sw,nw,nw,sw,ne,n,se,sw,se,sw,nw,sw,sw,sw,sw,sw,nw,se,sw,sw,ne,sw,sw,se,ne,sw,sw,n,sw,nw,sw,n,sw,sw,ne,sw,sw,nw,sw,sw,sw,sw,sw,sw,nw,s,sw,sw,sw,sw,se,sw,sw,sw,sw,sw,sw,sw,sw,nw,sw,sw,sw,se,sw,sw,n,sw,s,sw,sw,n,se,sw,sw,ne,n,se,sw,sw,sw,sw,sw,sw,nw,sw,s,sw,se,nw,s,sw,sw,sw,sw,sw,sw,sw,sw,sw,se,se,sw,sw,sw,sw,sw,sw,sw,sw,sw,n,sw,sw,sw,sw,sw,n,sw,s,s,sw,se,sw,ne,sw,s,sw,sw,sw,sw,ne,se,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,s,s,se,se,s,sw,sw,nw,sw,s,sw,sw,nw,s,se,nw,sw,sw,sw,s,sw,sw,sw,s,sw,ne,sw,sw,se,sw,sw,sw,sw,s,sw,n,sw,sw,nw,s,s,s,sw,se,sw,sw,sw,sw,sw,s,sw,nw,se,se,nw,sw,sw,n,ne,sw,s,sw,se,s,sw,sw,sw,sw,sw,sw,se,se,s,sw,sw,sw,sw,s,sw,s,nw,sw,sw,s,sw,s,sw,sw,s,s,sw,sw,s,ne,sw,sw,sw,s,s,s,sw,nw,nw,s,sw,sw,ne,s,sw,sw,sw,s,se,s,s,sw,sw,sw,se,sw,sw,nw,sw,s,sw,sw,n,sw,sw,sw,sw,s,s,s,s,s,ne,se,sw,s,n,sw,se,se,s,sw,sw,s,s,s,s,sw,s,s,s,s,sw,sw,s,s,s,sw,s,sw,n,s,nw,nw,sw,sw,sw,sw,s,se,sw,sw,s,sw,s,s,sw,s,sw,sw,sw,sw,s,se,se,n,ne,ne,s,sw,sw,sw,s,sw,nw,nw,n,nw,s,sw,sw,ne,s,sw,sw,n,s,s,s,s,se,s,sw,se,sw,s,sw,s,nw,se,sw,s,sw,sw,sw,s,n,sw,ne,se,s,s,n,s,s,s,sw,s,sw,sw,sw,s,nw,ne,n,s,s,sw,ne,s,sw,s,s,sw,sw,sw,s,s,nw,s,nw,s,s,sw,ne,s,s,s,ne,s,sw,s,se,s,s,s,s,s,s,s,s,s,ne,sw,n,s,s,s,s,s,ne,s,sw,s,s,n,s,s,s,s,s,s,s,s,s,s,s,s,sw,n,s,se,ne,s,s,s,s,sw,s,nw,s,s,s,s,s,s,s,se,s,sw,s,sw,n,s,sw,s,sw,sw,s,sw,s,ne,sw,s,se,s,sw,s,s,sw,ne,nw,s,s,sw,sw,s,s,s,se,s,s,s,n,sw,sw,ne,ne,sw,nw,s,s,sw,s,s,sw,s,s,s,s,nw,sw,s,s,s,s,sw,s,s,s,sw,s,s,s,sw,s,s,s,s,s,s,s,s,s,s,s,s,sw,s,s,se,s,s,n,s,ne,s,s,se,s,s,s,s,s,s,s,ne,s,s,s,s,n,s,s,s,n,s,n,s,sw,s,n,sw,nw,s,s,ne,s,s,s,s,s,s,n,s,nw,s,sw,s,s,s,s,s,s,s,n,s,s,s,s,s,se,s,s,s,s,s,n,s,s,ne,s,s,s,s,n,s,ne,s,s,s,nw,se,ne,se,se,s,ne,nw,s,s,n,s,s,s,s,n,s,s,s,s,se,s,sw,se,ne,s,s,s,n,n,s,se,se,ne,s,s,s,s,s,se,s,s,s,s,nw,s,se,s,s,s,s,s,s,se,s,s,s,sw,n,s,sw,s,s,s,se,s,s,s,s,s,s,s,s,s,s,nw,s,s,ne,s,s,sw,s,ne,s,s,ne,s,sw,n,s,nw,s,se,se,s,s,s,sw,nw,s,s,s,s,s,ne,s,se,s,s,s,s,s,s,s,s,se,n,s,sw,s,s,ne,se,s,s,se,se,se,s,se,nw,s,s,s,se,nw,sw,s,s,s,ne,s,s,se,s,ne,s,s,s,nw,n,se,s,s,se,s,s,se,se,s,s,s,s,nw,s,s,s,nw,s,s,n,se,nw,s,s,sw,se,s,n,n,s,sw,s,s,nw,s,n,nw,nw,s,se,s,s,se,s,s,ne,s,s,s,sw,sw,s,se,s,s,se,se,s,nw,s,se,s,s,nw,s,n,se,ne,sw,se,s,s,s,s,ne,se,n,se,s,se,s,s,nw,s,se,s,ne,s,s,se,s,se,n,sw,sw,s,nw,s,se,s,se,nw,se,s,se,s,sw,n,s,se,se,s,s,ne,s,n,s,se,se,ne,s,s,s,s,se,se,se,se,sw,s,se,sw,s,s,s,s,se,se,s,nw,s,se,se,s,ne,s,se,s,s,s,s,s,s,se,se,s,se,se,se,se,se,ne,nw,s,n,ne,s,se,s,s,s,nw,se,se,nw,s,se,nw,s,se,se,s,s,se,se,se,sw,se,s,se,ne,sw,s,se,s,s,s,s,s,s,s,nw,n,ne,se,sw,s,se,s,se,s,se,n,se,s,se,se,se,se,se,s,se,ne,se,s,se,n,s,s,ne,s,s,se,s,s,s,s,sw,se,s,se,sw,sw,s,sw,nw,se,nw,se,s,s,ne,se,s,s,s,s,s,se,s,se,se,nw,se,nw,s,sw,s,n,sw,se,se,s,se,nw,se,sw,s,se,se,nw,s,s,s,s,sw,nw,n,se,s,sw,se,se,s,se,ne,s,s,se,s,se,s,ne,se,s,se,se,se,se,se,s,se,se,se,s,se,s,se,s,s,s,s,s,se,nw,se,nw,se,se,s,se,se,se,s,sw,se,se,se,se,sw,se,se,se,s,n,s,sw,se,n,se,s,se,se,se,s,nw,s,se,se,nw,se,se,se,s,se,se,se,se,se,nw,sw,se,s,s,sw,se,se,nw,s,se,s,s,se,ne,se,nw,se,s,se,se,s,se,se,se,se,sw,n,se,ne,se,se,s,se,se,s,se,s,se,se,s,se,s,se,n,s,se,s,s,s,se,se,se,se,se,n,se,se,se,se,ne,s,sw,se,se,se,n,se,se,se,s,se,se,se,se,n,ne,se,se,se,se,se,se,se,se,se,se,s,sw,se,se,se,se,se,se,se,se,s,se,se,se,se,se,s,se,se,se,se,se,se,se,se,se,nw,s,se,s,se,se,se,se,se,s,s,ne,se,se,se,ne,se,se,se,se,se,se,s,se,se,se,se,se,se,se,se,se,s,se,se,se,s,s,s,s,se,ne,sw,se,se,se,se,se,s,ne,se,se,se,se,s,sw,se,se,sw,se,s,sw,se,nw,se,se,s,se,se,nw,s,s,se,s,se,se,se,nw,se,ne,se,se,n,se,se,se,se,n,ne,se,se,sw,se,sw,se,se,se,se,se,se,se,n,nw,se,s,sw,n,ne,se,se,se,se,n,sw,se,se,se,se,se,n,se,nw,se,nw,sw,se,n,se,ne,se,se,se,se,se,se,sw,n,se,se,nw,se,se,s,se,se,se,se,ne,se,se,s,se,se,se,se,se,nw,n,se,se,se,s,se,se,nw,ne,nw,se,se,se,se,se,se,se,se,se,se,se,se,s,ne,ne,se,se,nw,se,se,se,se,se,se,nw,se,sw,se,sw,se,se,nw,se,se,se,se,ne,se,se,se,se,se,nw,nw,se,se,se,se,se,se,se,se,se,se,nw,se,se,se,se,se,se,nw,se,se,se,se,se,se,nw,se,se,se,se,se,se,se,se,se,se,s,se,se,se,ne,s,sw,s,se,ne,se,ne,se,se,se,se,ne,se,se,nw,se,se,se,se,se,se,se,se,n,s,se,nw,se,se,n,nw,sw,s,se,se,se,sw,se,se,ne,se,s,nw,se,se,n,se,se,sw,ne,se,se,se,ne,se,se,se,se,se,nw,se,se,s,se,ne,se,se,se,nw,sw,se,n,se,ne,s,ne,nw,n,ne,se,ne,se,ne,se,se,ne,se,sw,se,se,n,s,se,nw,ne,se,se,ne,se,ne,se,se,nw,se,se,s,ne,ne,se,se,se,se,se,se,se,se,se,ne,se,se,ne,se,se,se,nw,nw,se,se,se,n,se,se,s,ne,se,se,se,s,se,ne,se,ne,se,se,se,se,ne,se,n,se,se,se,ne,n,se,se,s,se,se,nw,se,se,sw,se,se,ne,se,se,se,se,se,se,s,ne,sw,ne,se,se,se,se,nw,se,se,ne,se,s,se,se,se,ne,ne,nw,se,se,se,s,sw,se,ne,sw,se,n,ne,se,sw,se,ne,se,se,ne,se,s,se,ne,se,se,se,ne,sw,ne,se,se,se,ne,ne,ne,ne,se,se,se,se,se,se,sw,se,ne,se,sw,ne,se,se,se,se,se,se,ne,se,sw,se,ne,n,ne,se,se,se,ne,se,se,se,ne,se,n,ne,nw,se,se,ne,ne,ne,ne,nw,se,ne,se,nw,se,se,se,ne,se,se,se,se,ne,ne,ne,nw,se,se,sw,se,ne,se,nw,n,s,s,se,ne,ne,sw,ne,se,ne,ne,ne,sw,se,se,se,nw,nw,ne,se,se,s,se,ne,sw,se,se,se,se,ne,se,ne,se,ne,se,se,se,se,ne,se,ne,se,se,ne,ne,se,n,sw,se,sw,se,sw,ne,ne,se,nw,se,sw,ne,se,nw,ne,se,ne,se,se,se,se,se,ne,ne,ne,ne,se,ne,nw,se,sw,se,nw,ne,se,se,ne,se,se,ne,se,se,se,nw,ne,ne,se,ne,se,sw,se,se,nw,ne,ne,ne,n,n,nw,nw,se,ne,ne,se,n,ne,se,ne,se,n,se,se,se,ne,ne,se,se,nw,se,se,se,se,se,ne,ne,se,n,se,ne,se,ne,nw,se,se,se,n,ne,ne,se,se,se,se,se,ne,n,ne,ne,ne,n,se,se,se,se,se,ne,ne,se,ne,se,ne,nw,se,se,ne,ne,ne,ne,ne,se,se,ne,se,ne,ne,ne,ne,sw,ne,se,ne,se,nw,ne,ne,se,ne,ne,se,se,ne,se,sw,ne,ne,se,ne,se,s,ne,ne,se,ne,ne,sw,se,se,s,nw,se,n,s,s,ne,se,se,ne,se,se,ne,s,se,se,se,nw,ne,se,ne,se,ne,ne,se,se,se,se,ne,sw,ne,se,s,ne,ne,ne,ne,n,se,sw,s,se,ne,se,se,ne,ne,se,se,nw,ne,ne,ne,sw,se,ne,ne,ne,ne,se,se,se,se,ne,se,se,se,se,sw,s,se,ne,ne,ne,ne,ne,se,ne,ne,ne,se,ne,ne,sw,nw,nw,n,ne,se,se,s,se,s,n,ne,se,se,se,ne,se,ne,sw,nw,nw,ne,ne,se,ne,ne,ne,ne,ne,se,ne,n,ne,se,se,se,se,se,ne,ne,se,se,ne,n,n,ne,se,ne,se,nw,se,ne,se,ne,ne,se,ne,se,ne,se,se,nw,se,nw,ne,ne,ne,ne,s,s,ne,ne,se,ne,se,ne,ne,n,sw,ne,ne,s,nw,ne,ne,se,ne,nw,ne,se,s,se,ne,sw,ne,sw,se,ne,n,nw,ne,nw,ne,se,n,se,ne,se,ne,ne,se,ne,se,ne,n,se,se,ne,ne,sw,se,ne,ne,ne,ne,ne,ne,nw,ne,se,se,se,ne,se,ne,s,se,se,ne,sw,se,s,ne,n,ne,se,ne,se,se,ne,ne,ne,nw,sw,se,ne,se,ne,ne,se,n,s,ne,n,ne,ne,se,ne,ne,se,ne,ne,ne,ne,ne,ne,ne,ne,ne,s,nw,ne,ne,ne,ne,n,ne,ne,ne,se,ne,ne,sw,ne,ne,se,se,se,ne,ne,nw,ne,ne,ne,se,n,se,sw,ne,se,se,ne,nw,n,se,ne,s,ne,n,ne,ne,se,ne,ne,se,ne,ne,ne,n,ne,n,sw,sw,ne,n,se,ne,se,n,s,ne,ne,ne,sw,ne,ne,ne,ne,ne,ne,nw,ne,nw,se,ne,sw,ne,ne,ne,ne,n,ne,n,ne,ne,ne,ne,ne,ne,n,ne,ne,ne,ne,ne,ne,ne,ne,n,se,ne,ne,ne,sw,ne,ne,se,ne,ne,se,n,ne,ne,s,se,nw,ne,ne,ne,s,se,sw,ne,ne,ne,ne,n,s,se,se,ne,ne,ne,ne,ne,ne,s,sw,sw,ne,ne,ne,ne,ne,sw,ne,n,ne,ne,sw,ne,n,ne,ne,ne,ne,s,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,sw,se,ne,ne,ne,ne,ne,sw,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,sw,ne,se,sw,ne,ne,ne,ne,ne,ne,ne,ne,n,ne,ne,nw,ne,ne,ne,n,ne,nw,ne,ne,ne,ne,ne,ne,sw,ne,ne,ne,n,sw,s,nw,nw,sw,s,nw,ne,ne,sw,ne,ne,se,ne,ne,ne,s,ne,sw,nw,ne,ne,s,ne,ne,ne,ne,se,ne,ne,sw,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,n,ne,se,ne,sw,se,ne,ne,nw,ne,ne,s,ne,ne,ne,nw,ne,nw,ne,ne,n,ne,ne,ne,ne,s,ne,ne,ne,se,n,ne,ne,ne,ne,s,se,ne,nw,ne,se,n,nw,ne,ne,ne,ne,ne,ne,n,ne,se,ne,ne,n,ne,ne,ne,ne,s,ne,ne,ne,n,n,ne,n,ne,ne,ne,ne,ne,n,nw,ne,ne,ne,se,ne,ne,ne,s,se,ne,ne,ne,ne,ne,ne,ne,ne,n,ne,sw,ne,ne,ne,nw,nw,ne,ne,nw,ne,ne,ne,n,ne,ne,ne,n,ne,ne,ne,ne,se,se,n,ne,ne,ne,n,ne,ne,ne,s,se,ne,ne,ne,n,ne,ne,ne,nw,ne,ne,ne,nw,ne,ne,ne,ne,ne,se,ne,ne,ne,n,ne,ne,nw,ne,ne,ne,n,ne,nw,ne,ne,ne,se,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,nw,ne,ne,ne,ne,se,ne,se,ne,ne,ne,ne,ne,ne,sw,ne,ne,ne,ne,n,n,se,ne,n,ne,ne,n,ne,ne,ne,nw,ne,ne,ne,n,ne,s,ne,n,n,ne,ne,ne,ne,n,ne,sw,ne,ne,ne,nw,ne,ne,ne,se,s,nw,ne,ne,ne,ne,n,ne,ne,ne,ne,ne,n,nw,ne,ne,ne,ne,ne,ne,ne,ne,n,ne,n,ne,ne,ne,ne,nw,n,ne,ne,ne,n,n,n,se,ne,sw,ne,nw,ne,ne,ne,n,ne,ne,ne,ne,sw,n,ne,ne,se,ne,nw,s,ne,ne,ne,s,n,ne,ne,ne,ne,se,ne,ne,sw,ne,ne,n,ne,ne,ne,ne,ne,n,n,nw,n,ne,ne,n,s,sw,n,ne,ne,ne,n,n,ne,ne,ne,sw,ne,ne,ne,nw,ne,ne,n,ne,ne,n,se,ne,ne,n,se,n,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,se,n,ne,ne,nw,s,n,n,n,ne,n,n,ne,n,ne,n,ne,ne,ne,nw,s,ne,ne,ne,ne,ne,se,nw,ne,ne,s,se,n,n,ne,ne,ne,ne,n,ne,ne,ne,n,n,ne,ne,ne,nw,ne,ne,ne,n,ne,n,ne,sw,ne,ne,n,ne,ne,ne,n,n,n,n,n,sw,ne,nw,n,se,s,ne,ne,ne,s,ne,sw,n,ne,se,ne,ne,ne,ne,ne,se,n,n,ne,ne,n,n,n,ne,ne,n,n,ne,s,ne,ne,se,ne,se,n,sw,ne,ne,ne,s,ne,ne,sw,nw,ne,se,n,ne,n,ne,n,n,ne,n,s,ne,n,s,ne,ne,ne,n,n,ne,n,sw,sw,ne,n,ne,ne,sw,n,n,n,ne,ne,se,ne,ne,n,ne,ne,ne,sw,ne,nw,sw,ne,s,ne,ne,ne,s,ne,sw,ne,n,ne,n,n,ne,nw,ne,s,n,n,ne,nw,ne,n,ne,ne,ne,ne,ne,se,nw,ne,sw,ne,ne,ne,sw,n,n,ne,ne,ne,ne,ne,nw,ne,ne,nw,ne,sw,ne,ne,sw,ne,ne,ne,n,ne,se,ne,n,n,se,n,s,n,n,ne,ne,ne,ne,ne,ne,ne,n,n,ne,ne,se,ne,ne,n,ne,nw,ne,n,se,nw,ne,ne,n,ne,n,nw,ne,ne,n,ne,n,n,ne,n,n,n,ne,ne,ne,ne,ne,n,n,nw,ne,ne,ne,nw,ne,ne,ne,ne,n,sw,ne,ne,n,n,ne,n,se,n,ne,n,n,nw,ne,ne,n,sw,ne,ne,ne,sw,ne,ne,n,s,n,nw,ne,s,ne,n,n,n,ne,s,ne,s,ne,sw,ne,se,ne,n,ne,n,n,n,ne,n,ne,n,ne,ne,ne,se,ne,ne,n,n,n,ne,n,n,ne,ne,ne,ne,sw,ne,ne,n,n,ne,n,n,n,ne,ne,ne,nw,sw,sw,n,ne,ne,n,ne,n,ne,sw,ne,n,n,se,n,n,ne,ne,sw,n,n,n,s,ne,n,ne,sw,ne,n,ne,ne,ne,ne,ne,ne,ne,n,n,n,se,ne,nw,n,ne,n,ne,sw,nw,n,se,ne,ne,n,n,s,n,n,n,ne,sw,ne,ne,se,n,n,ne,n,ne,n,ne,ne,ne,n,nw,n,n,n,nw,n,n,n,n,nw,ne,n,s,sw,ne,n,n,ne,n,nw,n,ne,s,sw,n,n,se,n,n,n,se,n,se,ne,se,n,n,n,n,s,ne,n,n,n,ne,ne,nw,n,n,sw,ne,n,n,n,n,ne,n,n,n,ne,ne,ne,n,ne,sw,ne,n,n,ne,n,n,n,ne,s,nw,n,ne,nw,n,n,ne,s,n,ne,ne,ne,ne,ne,n,ne,n,n,nw,ne,n,n,ne,n,n,n,se,sw,n,ne,s,n,n,ne,s,ne,n,n,sw,n,n,n,n,se,n,n,n,ne,n,n,se,ne,ne,sw,n,ne,n,n,ne,n,ne,n,s,s,n,s,n,n,n,n,ne,n,n,sw,nw,n,n,sw,ne,n,s,n,n,n,n,nw,n,n,ne,ne,ne,sw,ne,nw,n,ne,n,ne,n,n,n,nw,ne,nw,n,ne,sw,n,sw,s,ne,n,n,n,ne,n,s,n,n,n,n,ne,n,n,ne,se,se,n,ne,n,n,ne,n,ne,ne,ne,s,n,n,ne,ne,n,n,sw,ne,n,n,n,n,n,ne,ne,n,n,ne,n,n,n,n,ne,n,ne,n,n,ne,nw,n,sw,sw,nw,n,se,sw,ne,n,ne,n,ne,ne,s,n,ne,s,ne,s,ne,n,n,n,n,ne,n,ne,nw,n,n,n,n,n,ne,n,ne,ne,nw,sw,s,se,n,n,s,n,n,n,n,ne,n,ne,n,n,sw,ne,ne,n,n,n,ne,ne,n,n,n,n,nw,n,ne,s,n,ne,ne,n,sw,se,n,ne,ne,ne,s,ne,n,n,ne,n,nw,nw,ne,n,n,nw,n,n,ne,s,n,nw,n,n,n,nw,n,n,sw,n,n,n,s,n,n,n,n,ne,se,n,n,n,ne,nw,n,n,n,ne,n,ne,n,n,n,n,n,n,n,n,n,n,ne,n,n,ne,ne,n,n,s,n,s,n,n,n,nw,ne,n,n,ne,n,n,ne,n,n,n,ne,n,n,n,n,n,n,n,ne,n,nw,n,ne,n,ne,n,n,n,n,sw,ne,ne,ne,n,s,ne,ne,n,ne,n,n,n,n,n,n,n,n,s,n,ne,s,n,n,ne,ne,ne,ne,nw,s,n,n,n,ne,sw,n,n,s,n,n,n,n,ne,n,n,s,ne,n,n,n,se,nw,ne,ne,ne,n,ne,n,ne,n,n,n,se,n,s,n,ne,se,n,ne,n,ne,n,n,ne,n,nw,ne,n,ne,nw,n,n,s,sw,se,n,n,n,ne,nw,n,n,n,n,se,n,ne,ne,n,nw,n,n,nw,n,ne,n,n,n,ne,sw,n,n,se,n,n,sw,ne,nw,n,n,n,n,n,n,ne,n,n,n,n,ne,ne,ne,s,n,n,ne,sw,n,n,n,se,n,ne,sw,sw,sw,n,n,n,sw,n,ne,n,sw,n,ne,n,se,ne,n,n,n,n,n,n,n,n,s,n,n,sw,ne,n,n,n,se,se,n,n,n,s,n,n,n,sw,n,n,n,nw,sw,n,n,n,nw,n,ne,ne,n,se,n,n,n,n,se,ne,sw,n,n,sw,n,sw,n,s,ne,n,n,s,se,n,n,se,n,n,n,ne,sw,n,nw,n,ne,n,n,n,n,se,n,s,n,n,n,se,n,n,n,nw,n,n,n,n,n,n,nw,n,n,n,n,sw,s,s,n,n,n,se,ne,n,n,ne,ne,ne,n,n,n,n,n,sw,n,ne,n,n,n,n,n,se,n,n,n,nw,se,n,nw,n,ne,n,n,n,s,n,n,n,n,n,n,n,n,n,n,ne,n,ne,n,n,n,ne,n,n,n,s,n,n,n,n,n,n,n,n,n,n,n,n,n,ne,s,n,n,n,ne,n,n,n,sw,n,ne,s,n,n,n,n,sw,n,n,n,n,n,se,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,se,sw,n,n,ne,se,s,se,s,s,s,s,s,sw,sw,sw,nw,nw,sw,nw,se,ne,nw,nw,sw,nw,nw,n,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,se,n,ne,n,n,sw,ne,n,n,n,sw,n,ne,s,n,ne,ne,ne,ne,n,ne,n,n,se,ne,ne,ne,se,ne,ne,ne,ne,ne,ne,sw,ne,ne,se,ne,ne,ne,ne,ne,se,ne,se,se,se,ne,ne,ne,se,ne,se,ne,se,ne,se,se,n,se,se,n,se,se,nw,se,se,se,se,se,s,se,se,se,s,se,se,se,se,s,s,nw,s,se,s,se,se,s,s,se,sw,s,se,nw,s,s,ne,n,sw,se,s,se,s,se,s,s,s,s,s,ne,s,s,sw,s,s,s,s,s,s,n,s,s,s,sw,s,s,s,sw,sw,nw,sw,s,sw,n,s,s,s,s,sw,sw,s,n,s,sw,ne,sw,sw,s,s,sw,s,s,s,s,s,ne,nw,sw,sw,s,s,sw,sw,sw,sw,sw,sw,n,sw,s,sw,sw,sw,s,se,n,sw,s,s,n,sw,sw,sw,sw,sw,sw,sw,se,sw,sw,sw,sw,sw,sw,sw,sw,sw,nw,nw,sw,sw,sw,sw,se,sw,se,sw,sw,sw,sw,sw,sw,sw,sw,sw,ne,s,sw,nw,nw,sw,sw,sw,nw,n,sw,sw,nw,nw,se,sw,sw,sw,nw,sw,sw,sw,sw,n,sw,nw,nw,sw,ne,sw,nw,sw,nw,sw,sw,nw,s,nw,n,nw,nw,nw,nw,nw,nw,sw,s,n,se,nw,nw,nw,nw,ne,nw,n,nw,nw,sw,n,ne,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,s,nw,nw,sw,n,se,sw,sw,ne,nw,nw,nw,nw,ne,nw,nw,nw,sw,nw,ne,nw,nw,nw,ne,nw,ne,n,n,nw,ne,nw,nw,nw,nw,nw,n,nw,nw,nw,nw,n,nw,s,se,nw,nw,nw,nw,n,n,sw,n,nw,nw,nw,nw,n,nw,n,sw,nw,nw,n,nw,se,nw,nw,n,n,n,n,nw,n,sw,n,n,nw,sw,sw,nw,nw,s,nw,nw,nw,sw,n,n,nw,nw,n,n,n,s,nw,se,n,n,n,nw,nw,nw,n,n,n,n,nw,n,ne,n,n,sw,se,n,nw,s,s,n,se,n,s,n,ne,nw,n,n,n,ne,n,n,nw,nw,ne,n,nw,nw,se,n,n,nw,n,n,n,n,n,ne,n,n,n,n,se,n,n,n,n,ne,n,sw,n,n,n,n,n,ne,n,se,n,n,n,nw,n,ne,n,n,ne,n,nw,n,s,n,n,ne,n,n,n,n,ne,s,n,n,se,n,n,se,n,n,sw,ne,s,n,nw,s,n,ne,nw,n,n,ne,n,n,n,se,n,n,n,n,s,se,n,n,ne,s,se,ne,n,ne,ne,n,ne,ne,ne,ne,ne,se,ne,n,n,ne,ne,ne,ne,n,sw,n,n,sw,ne,ne,ne,nw,nw,ne,ne,se,sw,n,n,ne,n,n,ne,n,n,ne,n,n,ne,n,ne,n,nw,ne,se,ne,sw,se,s,n,n,ne,ne,n,ne,nw,n,ne,n,ne,ne,ne,ne,ne,ne,ne,ne,se,sw,ne,se,ne,ne,n,ne,ne,ne,s,ne,ne,ne,ne,ne,n,se,ne,n,ne,ne,sw,se,ne,ne,ne,ne,ne,ne,ne,ne,n,ne,ne,s,ne,ne,sw,nw,n,ne,ne,ne,n,s,n,se,ne,ne,sw,se,ne,ne,ne,s,ne,se,ne,ne,ne,ne,ne,n,ne,ne,ne,ne,ne,sw,ne,ne,ne,sw,ne,se,ne,ne,ne,nw,ne,ne,se,ne,ne,ne,ne,ne,s,ne,ne,ne,ne,ne,se,se,ne,ne,ne,sw,ne,n,ne,ne,ne,ne,s,nw,ne,ne,ne,ne,ne,ne,ne,se,ne,se,ne,ne,ne,se,se,ne,ne,sw,ne,ne,s,se,ne,n,ne,s,s,ne,s,nw,se,ne,ne,sw,ne,ne,se,ne,ne,ne,ne,se,ne,ne,sw,se,ne,ne,ne,n,sw,ne,ne,se,se,se,se,s,nw,se,ne,se,nw,se,ne,ne,se,ne,ne,ne,ne,sw,ne,ne,n,ne,se,sw,ne,ne,se,se,se,nw,ne,ne,ne,ne,se,se,sw,ne,se,se,se,ne,se,nw,ne,ne,ne,ne,nw,ne,se,se,ne,se,se,se,n,ne,ne,se,n,se,ne,se,se,se,se,se,se,ne,s,se,ne,se,se,ne,sw,ne,se,n,ne,se,ne,se,se,ne,se,ne,ne,se,nw,se,se,se,ne,se,ne,se,se,se,ne,se,se,ne,se,se,sw,se,se,ne,se,se,se,se,se,se,se,nw,s,ne,ne,ne,se,sw,se,se,ne,se,n,se,se,se,se,se,se,s,se,se,se,se,ne,s,se,se,ne,se,se,se,sw,se,se,n,ne,ne,se,ne,n,se,se,ne,s,se,se,nw,se,n,se,ne,se,se,ne,sw,se,se,se,nw,se,se,ne,ne,se,nw,se,se,se,se,se,se,se,se,se,se,se,se,se,n,sw,se,se,se,n,se,se,se,sw,se,sw,se,s,nw,se,se,se,se,sw,se,se,se,se,se,se,se,ne,se,se,se,se,nw,n,sw,se,ne,se,se,se,sw,se,se,se,sw,n,se,se,sw,se,se,s,se,se,se,s,se,se,ne,s,se,se,se,se,s,se,s,se,se,s,se,ne,se,se,se,se,se,ne,se,se,se,ne,s,se,s,ne,n,nw,se,sw,se,se,s,se,se,s,se,s,nw,s,s,s,ne,s,se,se,se,n,s,s,se,se,se,ne,sw,se,se,se,se,se,s,s,s,se,se,ne,se,ne,se,nw,se,se,se,ne,s,se,se,se,nw,se,se,s,se,s,s,s,nw,ne,se,s,se,s,sw,nw,se,s,ne,se,n,se,s,se,ne,se,s,s,se,s,se,s,s,ne,se,se,se,se,s,ne,se,s,se,s,s,s,s,se,se,se,s,s,s,se,se,sw,s,se,se,s,se,se,s,sw,sw,s,s,nw,s,s,ne,s,ne,s,s,n,se,s,s,sw,s,n,n,s,s,ne,se,s,s,s,ne,s,s,se,s,sw,se,n,se,s,ne,n,s,s,se,s,sw,s,nw,se,n,n,s,s,s,s,n,s,s,sw,s,se,s,se,s,se,se,s,s,sw,s,se,s,ne,s,s,s,s,s,sw,nw,s,s,nw,s,s,s,se,s,se,s,n,se,s,s,se,s,ne,s,n,s,s,s,s,se,s,n,s,s,s,s,s,s,s,s,s,nw,s,se,nw,se,sw,se,se,s,se,s,s,s,s,s,ne,nw,n,s,s,s,n,s,s,nw,s,s,s,s,s,s,s,n,se,ne,s,se,s,s,se,s,s,ne,s,s,s,s,s,s,sw,nw,se,se,s,s,s,s,sw,s,s,s,nw,se,s,se,sw,s,s,s,nw,sw,s,ne,s,s,s,nw,s,s,s,s,s,s,s,s,s,s,s,s,s,ne,s,s,s,s,ne,s,n,se,s,s,s,s,s,n,s,nw,s,s,s,sw,s,s,s,s,s,sw,s,s,s,sw,s,s,s,ne,sw,s,s,ne,s,ne,s,s,s,s,s,s,s,s,nw,ne,nw,s,se,s,s,sw,s,n,s,sw,s,sw,s,se,sw,sw,sw,s,s,s,nw,sw,s,s,s,ne,s,se,s,sw,sw,s,sw,s,sw,s,s,s,s,s,s,sw,se,s,s,sw,sw,s,s,s,s,sw,s,s,se,nw,sw,s,nw,s,s,s,sw,se,s,s,sw,sw,n,sw,s,sw,s,s,sw,s,s,s,sw,se,s,s,s,s,se,s,s,s,s,s,s,s,s,s,s,ne,s,s,s,s,s,nw,sw,s,s,sw,sw,s,nw,s,s,s,sw,se,nw,ne,s,n,s,se,s,s,s,s,nw,s,s,s,ne,s,sw,s,s,ne,sw,s,ne,sw,nw,sw,s,s,s,s,s,sw,s,sw,sw,nw,s,n,s,sw,s,s,sw,s,n,sw,sw,s,s,s,s,s,nw,nw,s,sw,s,nw,sw,nw,s,s,sw,sw,sw,nw,s,nw,n,sw,sw,sw,sw,n,sw,s,sw,sw,sw,s,sw,sw,sw,s,s,ne,ne,sw,sw,s,se,s,s,nw,s,n,s,s,s,n,s,s,s,s,se,ne,se,nw,ne,sw,sw,s,n,n,s,s,s,ne,s,sw,sw,sw,sw,s,sw,s,sw,sw,s,sw,sw,nw,s,sw,sw,s,nw,sw,s,n,s,s,s,se,sw,s,s,s,s,s,s,sw,sw,sw,sw,nw,sw,sw,ne,nw,nw,n,s,sw,sw,sw,ne,s,s,sw,s,s,sw,sw,se,sw,sw,sw,n,n,s,sw,se,s,sw,ne,sw,se,s,sw,sw,s,s,s,sw,s,sw,s,sw,s,s,s,s,sw,sw,s,sw,s,sw,sw,sw,s,s,sw,s,s,sw,s,sw,ne,s,sw,s,sw,sw,s,s,sw,sw,n,n,s,sw,s,sw,s,s,sw,sw,s,s,sw,sw,sw,sw,sw,n,s,sw,sw,sw,sw,s,sw,se,sw,s,s,n,s,s,sw,sw,ne,sw,se,sw,sw,s,s,sw,sw,s,sw,s,sw,sw,nw,sw,s,nw,n,sw,n,se,sw,sw,sw,se,ne,sw,sw,sw,sw,n,sw,sw,sw,sw,n,sw,sw,sw,s,sw,se,sw,nw,sw,sw,se,sw,sw,sw,s,sw,sw,sw,sw,ne,se,sw,s,sw,s,s,nw,sw,n,se,s,s,sw,sw,s,s,sw,sw,sw,nw,sw,sw,sw,s,n,se,sw,sw,sw,sw,n,sw,sw,sw,sw,sw,sw,sw,sw,s,sw,sw,s,sw,sw,sw,sw,sw,sw,ne,sw,sw,sw,sw,sw,sw,sw,sw,sw,s,sw,sw,sw,sw,sw,sw,n,sw,n,sw,sw,sw,sw,sw,sw,sw,sw,sw,s,sw,sw,n,sw,sw,sw,sw,sw,sw,sw,sw,se,s,sw,ne,sw,ne,sw,sw,sw,sw,sw,sw,sw,sw,nw,sw,sw,sw,n,nw,s,sw,sw,sw,sw,sw,n,n,sw,sw,sw,sw,se,sw,sw,sw,sw,sw,sw,sw,sw,nw,sw,sw,sw,nw,sw,sw,sw,sw,sw,sw,sw,sw,n,sw,sw,sw,s,sw,sw,ne,sw,nw,sw,sw,sw,sw,sw,s,s,sw,nw,sw,sw,sw,se,sw,s,sw,s,se,sw,sw,s,sw,ne,sw,sw,sw,sw,nw,sw,n,sw,sw,s,nw,nw,nw,sw,se,nw,ne,sw,sw,sw,n,sw,se,sw,sw,sw,sw,sw,sw,se,nw,sw,nw,nw,sw,sw,n,sw,sw,s,nw,sw,sw,sw,nw,sw,s,sw,s,sw,sw,sw,se,sw,sw,se,se,sw,sw,nw,sw,nw,sw,sw,sw,nw,n,ne,sw,nw,ne,sw,ne,sw,nw,ne,sw,sw,ne,nw,sw,nw,ne,sw,sw,sw,sw,s,sw,n,nw,nw,nw,nw,nw,nw,s,s,sw,nw,sw,sw,sw,nw,sw,nw,sw,nw,sw,nw,sw,sw,nw,nw,nw,sw,nw,sw,sw,nw,sw,sw,sw,sw,sw,sw,sw,sw,se,sw,sw,sw,n,s,ne,sw,nw,nw,sw,sw,ne,sw,sw,nw,nw,sw,nw,nw,sw,se,sw,s,sw,n,sw,sw,nw,ne,sw,sw,se,nw,sw,sw,nw,nw,sw,sw,nw,nw,sw,sw,nw,ne,sw,sw,ne,sw,sw,nw,ne,nw,sw,sw,nw,sw,s,ne,nw,nw,n,sw,nw,nw,sw,nw,sw,sw,ne,sw,sw,sw,sw,se,sw,nw,sw,sw,nw,nw,sw,sw,nw,n,sw,n,nw,nw,nw,nw,s,se,nw,sw,nw,sw,sw,nw,sw,nw,sw,n,nw,sw,nw,sw,sw,sw,sw,nw,n,sw,sw,sw,nw,sw,sw,s,nw,nw,nw,nw,sw,nw,sw,sw,nw,sw,nw,sw,nw,nw,nw,sw,sw,s,ne,sw,nw,sw,nw,n,nw,sw,nw,nw,nw,nw,nw,ne,n,sw,nw,se,sw,sw,nw,sw,nw,sw,sw,sw,sw,sw,nw,n,s,ne,ne,sw,sw,sw,nw,nw,sw,se,sw,nw,ne,nw,sw,s,nw,nw,sw,ne,nw,se,ne,sw,s,sw,nw,nw,s,nw,sw,sw,sw,sw,nw,nw,nw,nw,sw,sw,s,sw,nw,sw,ne,nw,sw,se,sw,nw,ne,nw,nw,nw,nw,nw,sw,nw,nw,nw,nw,sw,se,nw,ne,nw,nw,n,sw,sw,sw,se,sw,nw,nw,nw,n,nw,nw,nw,nw,nw,nw,nw,nw,ne,ne,nw,ne,sw,sw,nw,n,se,sw,nw,nw,sw,sw,nw,nw,nw,sw,nw,nw,se,n,sw,sw,sw,sw,s,nw,sw,nw,n,sw,sw,sw,sw,n,sw,nw,se,nw,s,sw,nw,nw,nw,nw,s,nw,sw,sw,nw,sw,n,s,nw,s,nw,sw,s,nw,sw,s,n,nw,sw,nw,nw,nw,nw,s,sw,nw,nw,nw,sw,sw,ne,se,sw,sw,nw,nw,nw,nw,sw,sw,sw,nw,sw,n,nw,nw,nw,nw,sw,nw,nw,s,nw,nw,sw,sw,nw,nw,sw,nw,nw,nw,nw,nw,nw,se,nw,nw,s,nw,nw,s,nw,n,nw,nw,nw,n,n,nw,nw,nw,nw,nw,nw,nw,n,ne,nw,nw,nw,sw,nw,se,sw,nw,sw,nw,sw,n,nw,nw,sw,nw,nw,s,nw,nw,sw,sw,nw,nw,nw,nw,nw,s,sw,nw,se,nw,nw,nw,ne,se,nw,s,nw,sw,nw,sw,ne,nw,nw,sw,nw,sw,n,nw,nw,nw,s,s,nw,nw,nw,nw,nw,nw,nw,nw,nw,se,nw,s,nw,nw,nw,nw,nw,nw,nw,se,nw,nw,nw,nw,nw,nw,nw,se,sw,se,nw,nw,se,se,nw,n,nw,nw,se,nw,nw,n,nw,s,nw,nw,nw,sw,nw,nw,nw,nw,sw,nw,nw,nw,ne,nw,nw,nw,nw,nw,nw,nw,nw,se,nw,s,s,nw,nw,nw,nw,nw,nw,nw,nw,s,nw,ne,nw,nw,nw,se,nw,nw,ne,nw,nw,se,nw,se,nw,n,n,nw,ne,sw,nw,nw,nw,nw,nw,nw,nw,s,nw,nw,nw,nw,nw,nw,nw,se,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,ne,nw,nw,nw'''

s = input11.split(',').count('s')-input11.split(',').count('n')
ne = input11.split(',').count('ne')-input11.split(',').count('sw')
se = input11.split(',').count('se')-input11.split(',').count('nw')

print(ne + se)

# day 12

in12 = '''0 <-> 1352, 1864
1 <-> 430
2 <-> 1202, 1416
3 <-> 303, 363, 635
4 <-> 1041, 1383
5 <-> 143, 1513
6 <-> 6
7 <-> 619
8 <-> 167, 1246, 1822
9 <-> 577, 1274, 1347
10 <-> 10, 899
11 <-> 790
12 <-> 606
13 <-> 1134, 1894
14 <-> 539, 1974
15 <-> 683, 1783
16 <-> 438, 1235
17 <-> 17
18 <-> 760, 1162
19 <-> 1146
20 <-> 678, 1235, 1397, 1911
21 <-> 127, 615, 980
22 <-> 22, 187
23 <-> 192, 552
24 <-> 169
25 <-> 471
26 <-> 1030, 1329, 1333
27 <-> 1404
28 <-> 1249
29 <-> 1755
30 <-> 198
31 <-> 510, 1884
32 <-> 1088
33 <-> 54, 372, 616, 938, 1548
34 <-> 1574
35 <-> 238, 1411
36 <-> 114
37 <-> 1962
38 <-> 1554, 1633
39 <-> 72, 486, 1002
40 <-> 40, 1224, 1342, 1511, 1886
41 <-> 1244, 1644
42 <-> 1784
43 <-> 169, 1142
44 <-> 96, 827
45 <-> 842, 1512
46 <-> 1248
47 <-> 283, 1125, 1130
48 <-> 212, 327, 1922
49 <-> 490
50 <-> 359, 1386
51 <-> 1186
52 <-> 414
53 <-> 808
54 <-> 33, 673
55 <-> 614
56 <-> 56
57 <-> 257
58 <-> 482, 701, 1702, 1921
59 <-> 515, 695, 1073
60 <-> 809
61 <-> 865
62 <-> 106, 764
63 <-> 416, 1119, 1360
64 <-> 552
65 <-> 978, 1042
66 <-> 97, 130, 168
67 <-> 180, 339
68 <-> 1076
69 <-> 1550, 1621
70 <-> 1163, 1574, 1834
71 <-> 163, 1789
72 <-> 39, 1461, 1693
73 <-> 266, 652, 1612, 1877
74 <-> 860, 936, 1685
75 <-> 502, 768
76 <-> 1064
77 <-> 1685, 1967
78 <-> 501
79 <-> 743, 1261, 1608
80 <-> 80, 1901
81 <-> 1684
82 <-> 82
83 <-> 234, 504, 1159
84 <-> 1529
85 <-> 705
86 <-> 362, 644
87 <-> 223
88 <-> 1870
89 <-> 1412, 1633
90 <-> 191, 1141, 1993, 1999
91 <-> 588
92 <-> 92
93 <-> 918
94 <-> 972, 1401
95 <-> 1043, 1299
96 <-> 44
97 <-> 66, 1089
98 <-> 1300
99 <-> 243, 1220, 1957
100 <-> 1327
101 <-> 815, 1700, 1782
102 <-> 427, 723, 780, 1033
103 <-> 589, 1586
104 <-> 486
105 <-> 1296
106 <-> 62, 1677
107 <-> 1855
108 <-> 174, 1792
109 <-> 1518
110 <-> 1943
111 <-> 1799
112 <-> 112, 845
113 <-> 1189
114 <-> 36, 1895
115 <-> 775, 894, 987, 1832
116 <-> 455, 1317
117 <-> 436, 630, 944, 1229
118 <-> 1316
119 <-> 282
120 <-> 1022
121 <-> 446, 685
122 <-> 908, 1189
123 <-> 850, 1058, 1400
124 <-> 124, 867
125 <-> 316, 1198
126 <-> 1938
127 <-> 21
128 <-> 514, 871
129 <-> 597
130 <-> 66, 187, 541, 952
131 <-> 637, 728, 1951
132 <-> 1480
133 <-> 921, 1443
134 <-> 506, 576
135 <-> 1510
136 <-> 755
137 <-> 842
138 <-> 1077, 1219
139 <-> 1284, 1664
140 <-> 403
141 <-> 452, 1400
142 <-> 142, 442, 1462, 1463
143 <-> 5, 331, 492
144 <-> 144
145 <-> 844
146 <-> 774, 1141
147 <-> 351, 458
148 <-> 1984
149 <-> 499, 909, 935
150 <-> 153, 1300
151 <-> 151
152 <-> 1331
153 <-> 150
154 <-> 783
155 <-> 155, 1985
156 <-> 1752
157 <-> 716, 1144
158 <-> 647, 750
159 <-> 583
160 <-> 493, 770, 1669, 1675
161 <-> 161, 291, 1890
162 <-> 744, 1088, 1250
163 <-> 71, 803
164 <-> 231
165 <-> 1799
166 <-> 1101
167 <-> 8, 167
168 <-> 66, 441
169 <-> 24, 43, 1015
170 <-> 414, 509, 1222, 1392, 1947
171 <-> 180, 260, 1448
172 <-> 1894
173 <-> 585, 1662
174 <-> 108, 1300, 1304, 1789
175 <-> 574, 1245
176 <-> 1776, 1809
177 <-> 1625
178 <-> 1463
179 <-> 1469, 1648
180 <-> 67, 171
181 <-> 506, 1333
182 <-> 1703
183 <-> 370, 745, 816, 961
184 <-> 1143, 1608, 1696
185 <-> 431, 447, 633
186 <-> 352, 752
187 <-> 22, 130, 201, 232, 279
188 <-> 921
189 <-> 1460
190 <-> 445, 891, 972
191 <-> 90, 1078, 1383, 1957
192 <-> 23, 1057
193 <-> 1438
194 <-> 196, 819, 873
195 <-> 1403
196 <-> 194, 508
197 <-> 865, 1625
198 <-> 30, 855, 1397
199 <-> 399, 401
200 <-> 458
201 <-> 187, 457, 796
202 <-> 754, 964, 1736, 1737
203 <-> 937, 1890
204 <-> 676, 1148, 1472
205 <-> 205
206 <-> 206, 872, 1504
207 <-> 1575, 1717
208 <-> 1349, 1582, 1619, 1952
209 <-> 375, 523
210 <-> 1029
211 <-> 588, 623
212 <-> 48, 404, 820
213 <-> 213
214 <-> 1370
215 <-> 360, 412, 1507, 1800, 1874
216 <-> 287, 634, 1023, 1986
217 <-> 662, 1863
218 <-> 417, 1154
219 <-> 1250, 1442, 1962
220 <-> 595, 935, 1153, 1181
221 <-> 290
222 <-> 1328, 1407
223 <-> 87, 464, 925, 1131
224 <-> 1398
225 <-> 225, 768
226 <-> 999
227 <-> 311, 581, 697
228 <-> 983, 1019
229 <-> 719, 1469, 1820
230 <-> 453, 806, 1205, 1449
231 <-> 164, 451, 1741
232 <-> 187
233 <-> 664, 1419
234 <-> 83, 295, 482, 1684
235 <-> 622
236 <-> 236, 1662
237 <-> 287
238 <-> 35, 1308, 1608, 1805
239 <-> 1365
240 <-> 1177
241 <-> 387, 778, 1051
242 <-> 1233
243 <-> 99, 806, 1614
244 <-> 609, 1468
245 <-> 625, 1618
246 <-> 841, 1835
247 <-> 1720
248 <-> 1382, 1859
249 <-> 601, 1882
250 <-> 250, 1189, 1603, 1673, 1793
251 <-> 511
252 <-> 627
253 <-> 1195
254 <-> 400, 1562, 1893, 1951
255 <-> 285, 588, 1180
256 <-> 1408, 1468
257 <-> 57, 1211, 1940
258 <-> 695, 1174
259 <-> 610, 1176, 1516
260 <-> 171
261 <-> 268
262 <-> 502, 837, 1963
263 <-> 263
264 <-> 622, 638, 1815, 1945
265 <-> 570, 1590
266 <-> 73
267 <-> 336, 1040
268 <-> 261, 1815
269 <-> 652, 966, 1487
270 <-> 508, 522
271 <-> 1259, 1298, 1477, 1767
272 <-> 553, 1103, 1982
273 <-> 593, 1919
274 <-> 934, 1361
275 <-> 1839
276 <-> 329
277 <-> 1017, 1047
278 <-> 671
279 <-> 187, 853
280 <-> 1097, 1370
281 <-> 629
282 <-> 119, 1431
283 <-> 47, 974
284 <-> 1359, 1471
285 <-> 255
286 <-> 321, 883
287 <-> 216, 237
288 <-> 630, 880
289 <-> 289, 1853
290 <-> 221, 1307
291 <-> 161, 691, 1213
292 <-> 808
293 <-> 877, 1031, 1192
294 <-> 294, 1935
295 <-> 234
296 <-> 520, 1725
297 <-> 578, 702, 1184, 1209, 1431
298 <-> 979
299 <-> 1297, 1506
300 <-> 540, 995, 1187, 1774
301 <-> 675
302 <-> 739, 842
303 <-> 3, 1149, 1369, 1484
304 <-> 690
305 <-> 1306
306 <-> 481
307 <-> 474, 1723
308 <-> 323
309 <-> 995
310 <-> 544, 797, 1000
311 <-> 227, 927, 1127
312 <-> 1519
313 <-> 1989
314 <-> 314
315 <-> 536, 560, 1758
316 <-> 125, 582, 679, 1362
317 <-> 317, 510
318 <-> 1382, 1678
319 <-> 682
320 <-> 1733
321 <-> 286, 575
322 <-> 905, 1898
323 <-> 308, 366, 788, 1022, 1119, 1615
324 <-> 1151, 1390, 1540
325 <-> 1022
326 <-> 335, 1858
327 <-> 48
328 <-> 1076, 1456
329 <-> 276, 329, 1268
330 <-> 796, 919, 1330, 1565, 1926
331 <-> 143, 1522
332 <-> 831
333 <-> 1746
334 <-> 1254, 1844
335 <-> 326
336 <-> 267, 913
337 <-> 454, 1365, 1618
338 <-> 1800
339 <-> 67
340 <-> 1061
341 <-> 957
342 <-> 1130, 1242
343 <-> 782, 1629
344 <-> 350, 1216
345 <-> 898
346 <-> 586, 1372
347 <-> 1537
348 <-> 1899
349 <-> 378
350 <-> 344
351 <-> 147, 381, 993
352 <-> 186
353 <-> 353, 646, 913
354 <-> 465
355 <-> 1423, 1695
356 <-> 573, 1241
357 <-> 1695
358 <-> 1100, 1271
359 <-> 50, 1472, 1910
360 <-> 215
361 <-> 1512
362 <-> 86, 1768, 1997
363 <-> 3, 1731
364 <-> 657, 1713, 1992
365 <-> 475, 1490, 1968
366 <-> 323, 1482, 1765
367 <-> 831
368 <-> 1393
369 <-> 1135
370 <-> 183, 592
371 <-> 637, 1518
372 <-> 33
373 <-> 1494
374 <-> 1761
375 <-> 209
376 <-> 1587
377 <-> 1522
378 <-> 349, 686, 1006, 1946
379 <-> 379, 487
380 <-> 1763
381 <-> 351, 1048
382 <-> 1895
383 <-> 1623
384 <-> 1423, 1450
385 <-> 1350, 1770
386 <-> 798, 890
387 <-> 241, 894
388 <-> 1756
389 <-> 629
390 <-> 507
391 <-> 1780
392 <-> 1144
393 <-> 1240, 1279
394 <-> 1227
395 <-> 1361
396 <-> 396
397 <-> 397, 1228
398 <-> 454
399 <-> 199
400 <-> 254, 1147
401 <-> 199, 1068, 1445, 1918
402 <-> 636, 1601, 1934
403 <-> 140, 921
404 <-> 212, 430, 468, 1064, 1346, 1434
405 <-> 633
406 <-> 949
407 <-> 512, 951
408 <-> 1900, 1908
409 <-> 409
410 <-> 1724
411 <-> 624, 733
412 <-> 215, 1455
413 <-> 1612
414 <-> 52, 170
415 <-> 907, 1600
416 <-> 63
417 <-> 218, 835
418 <-> 418, 1116
419 <-> 1531
420 <-> 1154, 1538
421 <-> 485, 511
422 <-> 422
423 <-> 665
424 <-> 1891
425 <-> 1140
426 <-> 1409
427 <-> 102
428 <-> 463
429 <-> 575, 1432, 1779
430 <-> 1, 404
431 <-> 185, 1473
432 <-> 1065, 1720
433 <-> 1554
434 <-> 965
435 <-> 562, 1577
436 <-> 117
437 <-> 960
438 <-> 16, 926, 1342
439 <-> 1171
440 <-> 1198, 1622
441 <-> 168
442 <-> 142
443 <-> 443
444 <-> 1399, 1836
445 <-> 190
446 <-> 121
447 <-> 185, 1249
448 <-> 1505
449 <-> 542, 1433
450 <-> 1859
451 <-> 231, 590, 1641, 1651
452 <-> 141, 452
453 <-> 230
454 <-> 337, 398, 511
455 <-> 116, 455
456 <-> 1231, 1368
457 <-> 201, 1294
458 <-> 147, 200, 1799
459 <-> 1113
460 <-> 1521, 1841
461 <-> 882
462 <-> 683, 1744, 1887
463 <-> 428, 1221
464 <-> 223, 1310
465 <-> 354, 880
466 <-> 960, 1216
467 <-> 511, 1185
468 <-> 404
469 <-> 469
470 <-> 470
471 <-> 25, 494, 747, 1078
472 <-> 855, 1358
473 <-> 473
474 <-> 307, 1288
475 <-> 365, 688, 1881
476 <-> 1129, 1496, 1753
477 <-> 828, 1032, 1376
478 <-> 1474, 1950
479 <-> 479
480 <-> 480, 1318
481 <-> 306, 487
482 <-> 58, 234, 902, 1003
483 <-> 1681, 1730
484 <-> 484, 1071
485 <-> 421, 800, 975, 1124
486 <-> 39, 104
487 <-> 379, 481, 918
488 <-> 488, 1297
489 <-> 897, 1216, 1384
490 <-> 49, 1286
491 <-> 1283
492 <-> 143, 1098
493 <-> 160, 1120
494 <-> 471, 1781
495 <-> 495, 642, 714, 1004
496 <-> 1227
497 <-> 513, 1349, 1382
498 <-> 1846
499 <-> 149, 499
500 <-> 621, 1005, 1640
501 <-> 78, 1254
502 <-> 75, 262, 1008, 1404, 1915
503 <-> 1707
504 <-> 83
505 <-> 1809
506 <-> 134, 181, 506
507 <-> 390, 621, 1630
508 <-> 196, 270
509 <-> 170, 1819
510 <-> 31, 317, 656
511 <-> 251, 421, 454, 467, 1532
512 <-> 407, 1258, 1430
513 <-> 497
514 <-> 128, 840
515 <-> 59, 619, 662
516 <-> 1649
517 <-> 517
518 <-> 731
519 <-> 1522
520 <-> 296, 847
521 <-> 1667
522 <-> 270, 690, 1047, 1246
523 <-> 209, 1087
524 <-> 1267
525 <-> 714, 1126, 1896
526 <-> 1788
527 <-> 1660, 1733
528 <-> 1309, 1955
529 <-> 1912
530 <-> 838
531 <-> 1167, 1515
532 <-> 532, 1128
533 <-> 1602
534 <-> 564, 1108
535 <-> 535, 810
536 <-> 315, 1842
537 <-> 1947
538 <-> 1208, 1445
539 <-> 14, 825
540 <-> 300
541 <-> 130, 1188
542 <-> 449, 1197
543 <-> 1302
544 <-> 310, 1131
545 <-> 1409
546 <-> 772
547 <-> 1954
548 <-> 1662
549 <-> 1601
550 <-> 875, 1899
551 <-> 1208
552 <-> 23, 64, 1140
553 <-> 272, 1616, 1632, 1988
554 <-> 554, 622, 1169
555 <-> 555, 705, 772
556 <-> 625
557 <-> 867, 1210
558 <-> 870, 1039, 1320, 1509, 1995
559 <-> 835, 968
560 <-> 315
561 <-> 1335
562 <-> 435
563 <-> 658
564 <-> 534, 640, 1456, 1610
565 <-> 1130
566 <-> 741
567 <-> 1018
568 <-> 839
569 <-> 1544, 1767
570 <-> 265
571 <-> 1006, 1852
572 <-> 1320
573 <-> 356, 787, 816, 1947
574 <-> 175, 1287, 1381, 1413
575 <-> 321, 429
576 <-> 134
577 <-> 9, 668, 1979
578 <-> 297, 1576
579 <-> 1779
580 <-> 798
581 <-> 227, 832
582 <-> 316, 1033
583 <-> 159, 1550
584 <-> 1988
585 <-> 173, 1275
586 <-> 346, 1343
587 <-> 1499, 1911
588 <-> 91, 211, 255
589 <-> 103, 703
590 <-> 451, 1686
591 <-> 828, 1746
592 <-> 370
593 <-> 273
594 <-> 1358, 1607
595 <-> 220
596 <-> 1050, 1375
597 <-> 129, 1463
598 <-> 598, 1804
599 <-> 1606, 1671
600 <-> 1930
601 <-> 249, 869, 1233, 1336
602 <-> 1150, 1203
603 <-> 603
604 <-> 604, 620
605 <-> 835, 1556, 1770
606 <-> 12, 696, 1634, 1897
607 <-> 1629
608 <-> 608
609 <-> 244, 738
610 <-> 259, 684, 1309
611 <-> 1398
612 <-> 612, 1178, 1808
613 <-> 1245
614 <-> 55, 1701, 1969
615 <-> 21, 759
616 <-> 33, 1160
617 <-> 617, 824
618 <-> 725, 840
619 <-> 7, 515
620 <-> 604, 1247
621 <-> 500, 507, 1039
622 <-> 235, 264, 554, 665, 1476
623 <-> 211, 773, 1382, 1839
624 <-> 411, 943
625 <-> 245, 556, 794, 1277
626 <-> 988, 1429, 1495
627 <-> 252, 708, 1780
628 <-> 981
629 <-> 281, 389, 1132
630 <-> 117, 288, 802, 1438, 1492
631 <-> 753, 1279, 1716, 1843
632 <-> 1715
633 <-> 185, 405
634 <-> 216
635 <-> 3
636 <-> 402, 1983
637 <-> 131, 371
638 <-> 264, 1157
639 <-> 815
640 <-> 564
641 <-> 1473, 1727
642 <-> 495
643 <-> 967, 1996
644 <-> 86, 1586
645 <-> 1063, 1994
646 <-> 353
647 <-> 158, 1732
648 <-> 910, 1758
649 <-> 685, 704
650 <-> 1443, 1490
651 <-> 891
652 <-> 73, 269, 1374
653 <-> 756
654 <-> 1026
655 <-> 1177
656 <-> 510
657 <-> 364
658 <-> 563, 1264, 1402, 1457, 1617
659 <-> 899, 1543
660 <-> 874, 1691
661 <-> 1979
662 <-> 217, 515
663 <-> 953, 1147
664 <-> 233, 820, 1152
665 <-> 423, 622, 856
666 <-> 1020
667 <-> 1093, 1611
668 <-> 577, 892
669 <-> 1563
670 <-> 984, 1927
671 <-> 278, 803, 982
672 <-> 1143
673 <-> 54, 1650, 1902
674 <-> 1624, 1694
675 <-> 301, 1473
676 <-> 204, 1726
677 <-> 786, 1772
678 <-> 20
679 <-> 316
680 <-> 722, 1885
681 <-> 845
682 <-> 319, 777, 1935
683 <-> 15, 462
684 <-> 610
685 <-> 121, 649, 836, 1137
686 <-> 378, 1709
687 <-> 687
688 <-> 475
689 <-> 1950
690 <-> 304, 522, 1357, 1814
691 <-> 291
692 <-> 838, 1183
693 <-> 1298
694 <-> 1493
695 <-> 59, 258, 1529
696 <-> 606
697 <-> 227, 1590
698 <-> 870
699 <-> 1699
700 <-> 1740
701 <-> 58, 1535
702 <-> 297
703 <-> 589, 703
704 <-> 649, 1289, 1652
705 <-> 85, 555
706 <-> 1523
707 <-> 1606
708 <-> 627, 710, 1498, 1598
709 <-> 852, 1835
710 <-> 708
711 <-> 711
712 <-> 1786
713 <-> 991, 1558
714 <-> 495, 525
715 <-> 1185, 1473
716 <-> 157
717 <-> 1425
718 <-> 718, 1316
719 <-> 229, 1568
720 <-> 1977
721 <-> 721, 1272
722 <-> 680, 734, 1547
723 <-> 102
724 <-> 1982
725 <-> 618, 807
726 <-> 1771
727 <-> 1447
728 <-> 131, 1232, 1972
729 <-> 1345, 1875
730 <-> 730, 991
731 <-> 518, 1201, 1484
732 <-> 1972
733 <-> 411, 1596
734 <-> 722
735 <-> 1253
736 <-> 936, 1160
737 <-> 799, 865, 957, 1319
738 <-> 609
739 <-> 302, 1047
740 <-> 1532
741 <-> 566, 1226, 1395
742 <-> 742, 1215
743 <-> 79, 1552
744 <-> 162, 1110
745 <-> 183
746 <-> 1861
747 <-> 471
748 <-> 1671
749 <-> 1099, 1899
750 <-> 158
751 <-> 751
752 <-> 186, 804, 1013, 1403
753 <-> 631, 753
754 <-> 202, 1423, 1670
755 <-> 136, 803, 1343
756 <-> 653, 756
757 <-> 819
758 <-> 758
759 <-> 615
760 <-> 18, 1044
761 <-> 1636
762 <-> 1184, 1251
763 <-> 879, 1227
764 <-> 62, 1486
765 <-> 1993
766 <-> 966, 1665
767 <-> 773, 925, 1295
768 <-> 75, 225
769 <-> 1675
770 <-> 160
771 <-> 801, 916, 985, 996, 1984
772 <-> 546, 555
773 <-> 623, 767, 927, 1447
774 <-> 146, 979, 1583
775 <-> 115, 947
776 <-> 1055
777 <-> 682, 1114, 1480
778 <-> 241
779 <-> 1735
780 <-> 102, 781, 1942
781 <-> 780, 1062
782 <-> 343, 809, 881, 1766
783 <-> 154, 1389, 1763
784 <-> 1168, 1935
785 <-> 1286
786 <-> 677, 833, 1140
787 <-> 573, 1801
788 <-> 323, 1036
789 <-> 983, 1599
790 <-> 11, 1322, 1503, 1667
791 <-> 956
792 <-> 1708
793 <-> 1431
794 <-> 625, 1842
795 <-> 795
796 <-> 201, 330
797 <-> 310, 1425, 1749
798 <-> 386, 580
799 <-> 737, 1561, 1722
800 <-> 485
801 <-> 771
802 <-> 630, 1363
803 <-> 163, 671, 755, 1897, 1953
804 <-> 752, 1356
805 <-> 1459
806 <-> 230, 243
807 <-> 725, 855
808 <-> 53, 292, 1303, 1494
809 <-> 60, 782
810 <-> 535, 1713
811 <-> 1670
812 <-> 1910
813 <-> 1458
814 <-> 896, 1098
815 <-> 101, 639, 815, 898
816 <-> 183, 573
817 <-> 817, 1021, 1262
818 <-> 818, 1077
819 <-> 194, 757, 861
820 <-> 212, 664, 1944
821 <-> 1081, 1109
822 <-> 1769
823 <-> 1758
824 <-> 617
825 <-> 539
826 <-> 1150, 1844
827 <-> 44, 831
828 <-> 477, 591
829 <-> 1947
830 <-> 1165, 1669
831 <-> 332, 367, 827
832 <-> 581
833 <-> 786
834 <-> 1022, 1530
835 <-> 417, 559, 605
836 <-> 685, 1647
837 <-> 262, 1560, 1944
838 <-> 530, 692, 1717
839 <-> 568, 843, 1021, 1788
840 <-> 514, 618, 1390
841 <-> 246, 1190, 1646
842 <-> 45, 137, 302, 1306
843 <-> 839
844 <-> 145, 1715, 1833
845 <-> 112, 681
846 <-> 1136, 1718
847 <-> 520, 1818
848 <-> 1916
849 <-> 1641
850 <-> 123
851 <-> 1072
852 <-> 709
853 <-> 279, 941
854 <-> 1188
855 <-> 198, 472, 807, 1469
856 <-> 665
857 <-> 1318
858 <-> 1608
859 <-> 1901
860 <-> 74
861 <-> 819, 920
862 <-> 1378
863 <-> 1683
864 <-> 1880
865 <-> 61, 197, 737, 1289
866 <-> 866, 1221
867 <-> 124, 557
868 <-> 1485
869 <-> 601, 1029
870 <-> 558, 698
871 <-> 128, 1738
872 <-> 206
873 <-> 194
874 <-> 660, 1100
875 <-> 550, 900
876 <-> 1029
877 <-> 293, 1087, 1486
878 <-> 1726
879 <-> 763, 1252, 1597
880 <-> 288, 465
881 <-> 782
882 <-> 461, 1223, 1252, 1585
883 <-> 286, 954, 1046, 1491
884 <-> 1184
885 <-> 1393, 1487
886 <-> 907, 995, 1123
887 <-> 988, 997
888 <-> 1218, 1679
889 <-> 1544
890 <-> 386, 1867
891 <-> 190, 651, 917, 1593
892 <-> 668
893 <-> 893
894 <-> 115, 387
895 <-> 1378, 1857
896 <-> 814
897 <-> 489, 1829
898 <-> 345, 815
899 <-> 10, 659
900 <-> 875
901 <-> 901, 1132, 1550
902 <-> 482
903 <-> 1172, 1271, 1657
904 <-> 1954
905 <-> 322
906 <-> 1716
907 <-> 415, 886, 1929
908 <-> 122
909 <-> 149
910 <-> 648
911 <-> 911
912 <-> 1292, 1962
913 <-> 336, 353
914 <-> 914
915 <-> 1744
916 <-> 771, 1421
917 <-> 891, 1084, 1428
918 <-> 93, 487
919 <-> 330, 1672
920 <-> 861
921 <-> 133, 188, 403, 1418, 1921
922 <-> 1020, 1515
923 <-> 1597
924 <-> 1102
925 <-> 223, 767, 1175, 1920
926 <-> 438
927 <-> 311, 773
928 <-> 1162, 1317, 1571
929 <-> 929
930 <-> 1485, 1875
931 <-> 1809
932 <-> 1130, 1190, 1553
933 <-> 1303
934 <-> 274
935 <-> 149, 220
936 <-> 74, 736, 1574
937 <-> 203, 1942
938 <-> 33
939 <-> 1616
940 <-> 940, 1577
941 <-> 853
942 <-> 1315, 1345
943 <-> 624
944 <-> 117, 1531
945 <-> 1130
946 <-> 1789
947 <-> 775
948 <-> 1275
949 <-> 406, 1279, 1795
950 <-> 1803
951 <-> 407, 1440, 1785
952 <-> 130
953 <-> 663, 1460
954 <-> 883
955 <-> 1954
956 <-> 791, 1625
957 <-> 341, 737
958 <-> 1932
959 <-> 1624
960 <-> 437, 466, 1501
961 <-> 183, 994
962 <-> 1663
963 <-> 963, 1734
964 <-> 202, 1784
965 <-> 434, 1240
966 <-> 269, 766, 1395
967 <-> 643, 1414
968 <-> 559, 1523
969 <-> 1664
970 <-> 1670
971 <-> 1485
972 <-> 94, 190
973 <-> 984
974 <-> 283
975 <-> 485, 1584
976 <-> 1835
977 <-> 977
978 <-> 65
979 <-> 298, 774
980 <-> 21, 1217, 1897
981 <-> 628, 981
982 <-> 671
983 <-> 228, 789, 1321, 1933
984 <-> 670, 973, 1105
985 <-> 771, 1703
986 <-> 1478
987 <-> 115, 1725
988 <-> 626, 887, 1266
989 <-> 1366, 1601, 1964
990 <-> 1990
991 <-> 713, 730, 1932
992 <-> 1183
993 <-> 351
994 <-> 961
995 <-> 300, 309, 886, 995, 1305
996 <-> 771, 1048, 1203
997 <-> 887
998 <-> 1787
999 <-> 226, 1093, 1367
1000 <-> 310
1001 <-> 1468, 1913
1002 <-> 39, 1718
1003 <-> 482
1004 <-> 495
1005 <-> 500
1006 <-> 378, 571
1007 <-> 1256
1008 <-> 502
1009 <-> 1127
1010 <-> 1567
1011 <-> 1011, 1122, 1840
1012 <-> 1012
1013 <-> 752
1014 <-> 1538, 1775
1015 <-> 169, 1426
1016 <-> 1016, 1960
1017 <-> 277
1018 <-> 567, 1619
1019 <-> 228, 1495
1020 <-> 666, 922
1021 <-> 817, 839
1022 <-> 120, 323, 325, 834
1023 <-> 216, 1271
1024 <-> 1502
1025 <-> 1097
1026 <-> 654, 1455, 1739
1027 <-> 1823, 1906
1028 <-> 1903
1029 <-> 210, 869, 876, 1474, 1756
1030 <-> 26
1031 <-> 293, 1458
1032 <-> 477
1033 <-> 102, 582
1034 <-> 1984
1035 <-> 1977
1036 <-> 788
1037 <-> 1037
1038 <-> 1312, 1796, 1855
1039 <-> 558, 621, 1831
1040 <-> 267, 1478, 1776
1041 <-> 4
1042 <-> 65, 1881
1043 <-> 95, 1202, 1794
1044 <-> 760
1045 <-> 1426
1046 <-> 883
1047 <-> 277, 522, 739
1048 <-> 381, 996, 1578
1049 <-> 1554, 1779
1050 <-> 596
1051 <-> 241, 1117
1052 <-> 1533, 1637
1053 <-> 1797
1054 <-> 1814
1055 <-> 776, 1380
1056 <-> 1732, 1965
1057 <-> 192
1058 <-> 123
1059 <-> 1114
1060 <-> 1282
1061 <-> 340, 1325, 1517
1062 <-> 781, 1810
1063 <-> 645, 1567
1064 <-> 76, 404
1065 <-> 432
1066 <-> 1081, 1384, 1592
1067 <-> 1139
1068 <-> 401
1069 <-> 1327, 1873
1070 <-> 1070
1071 <-> 484, 1334
1072 <-> 851, 1072
1073 <-> 59
1074 <-> 1948
1075 <-> 1227
1076 <-> 68, 328, 1076
1077 <-> 138, 818, 1906
1078 <-> 191, 471, 1966
1079 <-> 1869
1080 <-> 1735, 1811, 1855
1081 <-> 821, 1066, 1895
1082 <-> 1740
1083 <-> 1083
1084 <-> 917
1085 <-> 1111
1086 <-> 1440, 1916
1087 <-> 523, 877
1088 <-> 32, 162
1089 <-> 97, 1854, 1948
1090 <-> 1102, 1896
1091 <-> 1466
1092 <-> 1655
1093 <-> 667, 999, 1159
1094 <-> 1248, 1961
1095 <-> 1243
1096 <-> 1635
1097 <-> 280, 1025
1098 <-> 492, 814
1099 <-> 749
1100 <-> 358, 874
1101 <-> 166, 1846
1102 <-> 924, 1090
1103 <-> 272, 1766
1104 <-> 1712
1105 <-> 984, 1105
1106 <-> 1106, 1620
1107 <-> 1107
1108 <-> 534, 1529
1109 <-> 821
1110 <-> 744
1111 <-> 1085, 1111, 1207
1112 <-> 1373
1113 <-> 459, 1430
1114 <-> 777, 1059
1115 <-> 1115
1116 <-> 418
1117 <-> 1051
1118 <-> 1474, 1583
1119 <-> 63, 323, 1194, 1302
1120 <-> 493
1121 <-> 1464
1122 <-> 1011
1123 <-> 886, 1848
1124 <-> 485
1125 <-> 47, 1705
1126 <-> 525
1127 <-> 311, 1009, 1566
1128 <-> 532
1129 <-> 476
1130 <-> 47, 342, 565, 932, 945
1131 <-> 223, 544
1132 <-> 629, 901
1133 <-> 1133, 1526
1134 <-> 13, 1913
1135 <-> 369, 1871
1136 <-> 846, 1879
1137 <-> 685
1138 <-> 1752
1139 <-> 1067, 1202
1140 <-> 425, 552, 786
1141 <-> 90, 146
1142 <-> 43, 1818
1143 <-> 184, 672, 1411
1144 <-> 157, 392, 1851
1145 <-> 1145, 1628
1146 <-> 19, 1574
1147 <-> 400, 663, 1265
1148 <-> 204, 1289, 1499, 1899
1149 <-> 303, 1797
1150 <-> 602, 826
1151 <-> 324
1152 <-> 664, 1518
1153 <-> 220, 1990
1154 <-> 218, 420, 1811
1155 <-> 1658
1156 <-> 1581, 1778, 1865
1157 <-> 638, 1849
1158 <-> 1445
1159 <-> 83, 1093, 1680
1160 <-> 616, 736
1161 <-> 1161
1162 <-> 18, 928
1163 <-> 70
1164 <-> 1868
1165 <-> 830, 1769
1166 <-> 1687
1167 <-> 531
1168 <-> 784, 1761
1169 <-> 554
1170 <-> 1206, 1327, 1754
1171 <-> 439, 1307, 1525
1172 <-> 903, 1172, 1542
1173 <-> 1173
1174 <-> 258
1175 <-> 925, 1869
1176 <-> 259
1177 <-> 240, 655, 1738
1178 <-> 612
1179 <-> 1537
1180 <-> 255, 1675
1181 <-> 220
1182 <-> 1377, 1877
1183 <-> 692, 992
1184 <-> 297, 762, 884, 1718
1185 <-> 467, 715, 1369
1186 <-> 51, 1600
1187 <-> 300
1188 <-> 541, 854
1189 <-> 113, 122, 250, 1653
1190 <-> 841, 932, 1448
1191 <-> 1225, 1345, 1427
1192 <-> 293, 1927
1193 <-> 1193, 1436
1194 <-> 1119
1195 <-> 253, 1864
1196 <-> 1432
1197 <-> 542, 1368, 1825
1198 <-> 125, 440
1199 <-> 1199, 1570, 1740
1200 <-> 1565
1201 <-> 731
1202 <-> 2, 1043, 1139, 1303
1203 <-> 602, 996, 1250
1204 <-> 1204
1205 <-> 230, 1514
1206 <-> 1170
1207 <-> 1111
1208 <-> 538, 551, 1904
1209 <-> 297
1210 <-> 557
1211 <-> 257, 1629
1212 <-> 1999
1213 <-> 291
1214 <-> 1977
1215 <-> 742, 1311, 1502, 1721
1216 <-> 344, 466, 489, 1457, 1810
1217 <-> 980
1218 <-> 888, 1294
1219 <-> 138
1220 <-> 99
1221 <-> 463, 866
1222 <-> 170
1223 <-> 882, 1817
1224 <-> 40, 1267
1225 <-> 1191, 1857
1226 <-> 741, 1309
1227 <-> 394, 496, 763, 1075, 1673
1228 <-> 397
1229 <-> 117, 1237
1230 <-> 1435, 1551, 1555
1231 <-> 456, 1885
1232 <-> 728
1233 <-> 242, 601
1234 <-> 1699
1235 <-> 16, 20, 1335
1236 <-> 1417
1237 <-> 1229, 1554
1238 <-> 1561
1239 <-> 1731, 1864
1240 <-> 393, 965, 1624
1241 <-> 356, 1241
1242 <-> 342
1243 <-> 1095, 1540
1244 <-> 41, 1802
1245 <-> 175, 613
1246 <-> 8, 522
1247 <-> 620
1248 <-> 46, 1094, 1430
1249 <-> 28, 447
1250 <-> 162, 219, 1203
1251 <-> 762
1252 <-> 879, 882
1253 <-> 735, 1867
1254 <-> 334, 501
1255 <-> 1396
1256 <-> 1007, 1366, 1636
1257 <-> 1257
1258 <-> 512, 1488
1259 <-> 271
1260 <-> 1898, 1978
1261 <-> 79
1262 <-> 817
1263 <-> 1387, 1405, 1580
1264 <-> 658
1265 <-> 1147, 1943
1266 <-> 988
1267 <-> 524, 1224
1268 <-> 329
1269 <-> 1537, 1608
1270 <-> 1540
1271 <-> 358, 903, 1023, 1398
1272 <-> 721, 1410
1273 <-> 1379
1274 <-> 9
1275 <-> 585, 948
1276 <-> 1920
1277 <-> 625
1278 <-> 1483
1279 <-> 393, 631, 949
1280 <-> 1572, 1842
1281 <-> 1281, 1833
1282 <-> 1060, 1283, 1422
1283 <-> 491, 1282
1284 <-> 139
1285 <-> 1893
1286 <-> 490, 785, 1598, 1661
1287 <-> 574
1288 <-> 474, 1600, 1824
1289 <-> 704, 865, 1148, 1681
1290 <-> 1660
1291 <-> 1291, 1301
1292 <-> 912, 1416
1293 <-> 1293, 1605
1294 <-> 457, 1218
1295 <-> 767
1296 <-> 105, 1859
1297 <-> 299, 488
1298 <-> 271, 693
1299 <-> 95, 1445
1300 <-> 98, 150, 174, 1422
1301 <-> 1291
1302 <-> 543, 1119
1303 <-> 808, 933, 1202, 1883
1304 <-> 174
1305 <-> 995
1306 <-> 305, 842
1307 <-> 290, 1171
1308 <-> 238, 1385
1309 <-> 528, 610, 1226
1310 <-> 464, 1520
1311 <-> 1215, 1830
1312 <-> 1038
1313 <-> 1835
1314 <-> 1916
1315 <-> 942
1316 <-> 118, 718
1317 <-> 116, 928
1318 <-> 480, 857
1319 <-> 737
1320 <-> 558, 572
1321 <-> 983
1322 <-> 790, 1368
1323 <-> 1846
1324 <-> 1920
1325 <-> 1061, 1409, 1459
1326 <-> 1486
1327 <-> 100, 1069, 1170, 1441, 1641
1328 <-> 222, 1328
1329 <-> 26
1330 <-> 330
1331 <-> 152, 1358, 1380, 1690, 1888
1332 <-> 1776
1333 <-> 26, 181
1334 <-> 1071
1335 <-> 561, 1235
1336 <-> 601
1337 <-> 1689
1338 <-> 1528, 1689
1339 <-> 1422, 1588
1340 <-> 1911, 1964
1341 <-> 1887
1342 <-> 40, 438
1343 <-> 586, 755, 1806, 1956
1344 <-> 1344, 1354, 1623, 1923
1345 <-> 729, 942, 1191
1346 <-> 404
1347 <-> 9, 1524, 1757, 1945, 1978
1348 <-> 1828
1349 <-> 208, 497
1350 <-> 385
1351 <-> 1399
1352 <-> 0
1353 <-> 1731
1354 <-> 1344, 1587, 1870
1355 <-> 1522, 1625
1356 <-> 804, 1356
1357 <-> 690
1358 <-> 472, 594, 1331
1359 <-> 284, 1934
1360 <-> 63, 1403
1361 <-> 274, 395, 1361
1362 <-> 316
1363 <-> 802, 1779, 1975
1364 <-> 1377
1365 <-> 239, 337
1366 <-> 989, 1256, 1420
1367 <-> 999, 1483
1368 <-> 456, 1197, 1322
1369 <-> 303, 1185
1370 <-> 214, 280, 1747, 1764
1371 <-> 1371
1372 <-> 346, 1546
1373 <-> 1112, 1665
1374 <-> 652
1375 <-> 596, 1375
1376 <-> 477, 1730, 1807
1377 <-> 1182, 1364
1378 <-> 862, 895, 1378, 1391
1379 <-> 1273, 1698, 1715
1380 <-> 1055, 1331, 1847
1381 <-> 574, 1654
1382 <-> 248, 318, 497, 623
1383 <-> 4, 191
1384 <-> 489, 1066
1385 <-> 1308
1386 <-> 50
1387 <-> 1263
1388 <-> 1567
1389 <-> 783
1390 <-> 324, 840, 1772
1391 <-> 1378
1392 <-> 170, 1641
1393 <-> 368, 885
1394 <-> 1645, 1655
1395 <-> 741, 966
1396 <-> 1255, 1396, 1965
1397 <-> 20, 198
1398 <-> 224, 611, 1271, 1549
1399 <-> 444, 1351, 1660
1400 <-> 123, 141
1401 <-> 94
1402 <-> 658
1403 <-> 195, 752, 1360
1404 <-> 27, 502
1405 <-> 1263
1406 <-> 1514
1407 <-> 222
1408 <-> 256
1409 <-> 426, 545, 1325, 1980, 1981
1410 <-> 1272
1411 <-> 35, 1143, 1444
1412 <-> 89
1413 <-> 574
1414 <-> 967, 1680
1415 <-> 1593
1416 <-> 2, 1292
1417 <-> 1236, 1599
1418 <-> 921, 1464
1419 <-> 233
1420 <-> 1366, 1564
1421 <-> 916
1422 <-> 1282, 1300, 1339
1423 <-> 355, 384, 754
1424 <-> 1488
1425 <-> 717, 797
1426 <-> 1015, 1045
1427 <-> 1191
1428 <-> 917
1429 <-> 626, 1911
1430 <-> 512, 1113, 1248
1431 <-> 282, 297, 793, 1663
1432 <-> 429, 1196
1433 <-> 449
1434 <-> 404
1435 <-> 1230
1436 <-> 1193, 1827
1437 <-> 1809
1438 <-> 193, 630
1439 <-> 1773
1440 <-> 951, 1086
1441 <-> 1327
1442 <-> 219, 1808
1443 <-> 133, 650
1444 <-> 1411, 1527, 1689
1445 <-> 401, 538, 1158, 1299
1446 <-> 1831
1447 <-> 727, 773
1448 <-> 171, 1190
1449 <-> 230, 1751
1450 <-> 384
1451 <-> 1451
1452 <-> 1607
1453 <-> 1453
1454 <-> 1454
1455 <-> 412, 1026
1456 <-> 328, 564
1457 <-> 658, 1216
1458 <-> 813, 1031
1459 <-> 805, 1325
1460 <-> 189, 953
1461 <-> 72, 1461, 1573
1462 <-> 142
1463 <-> 142, 178, 597
1464 <-> 1121, 1418, 1905
1465 <-> 1810
1466 <-> 1091, 1751
1467 <-> 1484, 1697
1468 <-> 244, 256, 1001, 1503
1469 <-> 179, 229, 855
1470 <-> 1889
1471 <-> 284
1472 <-> 204, 359, 1748
1473 <-> 431, 641, 675, 715, 1753
1474 <-> 478, 1029, 1118
1475 <-> 1475, 1595
1476 <-> 622
1477 <-> 271
1478 <-> 986, 1040
1479 <-> 1479
1480 <-> 132, 777
1481 <-> 1481
1482 <-> 366
1483 <-> 1278, 1367
1484 <-> 303, 731, 1467, 1778
1485 <-> 868, 930, 971
1486 <-> 764, 877, 1326
1487 <-> 269, 885
1488 <-> 1258, 1424
1489 <-> 1839
1490 <-> 365, 650
1491 <-> 883, 1655
1492 <-> 630, 1505, 1710, 1866
1493 <-> 694, 1785
1494 <-> 373, 808, 1838
1495 <-> 626, 1019
1496 <-> 476, 1666
1497 <-> 1916
1498 <-> 708
1499 <-> 587, 1148, 1596
1500 <-> 1800, 1974
1501 <-> 960
1502 <-> 1024, 1215, 1676
1503 <-> 790, 1468
1504 <-> 206
1505 <-> 448, 1492
1506 <-> 299
1507 <-> 215, 1579
1508 <-> 1678
1509 <-> 558
1510 <-> 135, 1693
1511 <-> 40
1512 <-> 45, 361, 1635
1513 <-> 5
1514 <-> 1205, 1406
1515 <-> 531, 922, 1730
1516 <-> 259
1517 <-> 1061
1518 <-> 109, 371, 1152
1519 <-> 312, 1835
1520 <-> 1310
1521 <-> 460
1522 <-> 331, 377, 519, 1355, 1852, 1871
1523 <-> 706, 968, 1607
1524 <-> 1347
1525 <-> 1171, 1728
1526 <-> 1133
1527 <-> 1444
1528 <-> 1338
1529 <-> 84, 695, 1108
1530 <-> 834
1531 <-> 419, 944
1532 <-> 511, 740
1533 <-> 1052
1534 <-> 1572
1535 <-> 701, 1606
1536 <-> 1536
1537 <-> 347, 1179, 1269
1538 <-> 420, 1014
1539 <-> 1648
1540 <-> 324, 1243, 1270
1541 <-> 1952
1542 <-> 1172
1543 <-> 659
1544 <-> 569, 889
1545 <-> 1545
1546 <-> 1372
1547 <-> 722
1548 <-> 33
1549 <-> 1398
1550 <-> 69, 583, 901
1551 <-> 1230, 1907
1552 <-> 743, 1841
1553 <-> 932
1554 <-> 38, 433, 1049, 1237
1555 <-> 1230
1556 <-> 605
1557 <-> 1728, 1980
1558 <-> 713
1559 <-> 1573
1560 <-> 837, 1803
1561 <-> 799, 1238, 1712
1562 <-> 254
1563 <-> 669, 1610
1564 <-> 1420, 1832
1565 <-> 330, 1200
1566 <-> 1127
1567 <-> 1010, 1063, 1388
1568 <-> 719
1569 <-> 1851
1570 <-> 1199
1571 <-> 928, 1752
1572 <-> 1280, 1534
1573 <-> 1461, 1559
1574 <-> 34, 70, 936, 1146
1575 <-> 207
1576 <-> 578
1577 <-> 435, 940
1578 <-> 1048
1579 <-> 1507
1580 <-> 1263, 1610
1581 <-> 1156
1582 <-> 208, 1839
1583 <-> 774, 1118, 1902
1584 <-> 975
1585 <-> 882
1586 <-> 103, 644, 1637
1587 <-> 376, 1354
1588 <-> 1339, 1913
1589 <-> 1791, 1855
1590 <-> 265, 697
1591 <-> 1631
1592 <-> 1066, 1692, 1707
1593 <-> 891, 1415, 1723
1594 <-> 1594, 1959
1595 <-> 1475
1596 <-> 733, 1499
1597 <-> 879, 923, 1991
1598 <-> 708, 1286, 1965
1599 <-> 789, 1417
1600 <-> 415, 1186, 1288
1601 <-> 402, 549, 989
1602 <-> 533, 1602
1603 <-> 250
1604 <-> 1784
1605 <-> 1293
1606 <-> 599, 707, 1535
1607 <-> 594, 1452, 1523
1608 <-> 79, 184, 238, 858, 1269
1609 <-> 1638
1610 <-> 564, 1563, 1580
1611 <-> 667
1612 <-> 73, 413, 1612
1613 <-> 1997
1614 <-> 243
1615 <-> 323
1616 <-> 553, 939
1617 <-> 658
1618 <-> 245, 337, 1618
1619 <-> 208, 1018
1620 <-> 1106
1621 <-> 69
1622 <-> 440, 1876
1623 <-> 383, 1344
1624 <-> 674, 959, 1240
1625 <-> 177, 197, 956, 1355
1626 <-> 1626, 1790
1627 <-> 1722
1628 <-> 1145
1629 <-> 343, 607, 1211
1630 <-> 507
1631 <-> 1591, 1886
1632 <-> 553
1633 <-> 38, 89
1634 <-> 606
1635 <-> 1096, 1512
1636 <-> 761, 1256
1637 <-> 1052, 1586
1638 <-> 1609, 1638
1639 <-> 1978
1640 <-> 500, 1712
1641 <-> 451, 849, 1327, 1392, 1994
1642 <-> 1785
1643 <-> 1960
1644 <-> 41, 1644
1645 <-> 1394
1646 <-> 841, 1646, 1936
1647 <-> 836
1648 <-> 179, 1539
1649 <-> 516, 1717
1650 <-> 673
1651 <-> 451
1652 <-> 704
1653 <-> 1189
1654 <-> 1381, 1654, 1928
1655 <-> 1092, 1394, 1491
1656 <-> 1755, 1767
1657 <-> 903
1658 <-> 1155, 1658
1659 <-> 1659, 1747
1660 <-> 527, 1290, 1399
1661 <-> 1286
1662 <-> 173, 236, 548
1663 <-> 962, 1431
1664 <-> 139, 969, 1664
1665 <-> 766, 1373
1666 <-> 1496
1667 <-> 521, 790, 1919
1668 <-> 1668
1669 <-> 160, 830
1670 <-> 754, 811, 970
1671 <-> 599, 748
1672 <-> 919
1673 <-> 250, 1227
1674 <-> 1771, 1838
1675 <-> 160, 769, 1180, 1729
1676 <-> 1502
1677 <-> 106
1678 <-> 318, 1508
1679 <-> 888
1680 <-> 1159, 1414
1681 <-> 483, 1289
1682 <-> 1905
1683 <-> 863, 1798, 1891
1684 <-> 81, 234
1685 <-> 74, 77
1686 <-> 590
1687 <-> 1166, 1709
1688 <-> 1820
1689 <-> 1337, 1338, 1444
1690 <-> 1331
1691 <-> 660
1692 <-> 1592
1693 <-> 72, 1510, 1957
1694 <-> 674
1695 <-> 355, 357, 1755
1696 <-> 184, 1828
1697 <-> 1467
1698 <-> 1379
1699 <-> 699, 1234, 1699, 1784
1700 <-> 101
1701 <-> 614, 1728, 1743
1702 <-> 58
1703 <-> 182, 985
1704 <-> 1704
1705 <-> 1125
1706 <-> 1706
1707 <-> 503, 1592
1708 <-> 792, 1880, 1882
1709 <-> 686, 1687
1710 <-> 1492
1711 <-> 1711
1712 <-> 1104, 1561, 1640
1713 <-> 364, 810
1714 <-> 1714, 1845
1715 <-> 632, 844, 1379
1716 <-> 631, 906
1717 <-> 207, 838, 1649, 1717
1718 <-> 846, 1002, 1184
1719 <-> 1719
1720 <-> 247, 432, 1720, 1914
1721 <-> 1215
1722 <-> 799, 1627
1723 <-> 307, 1593
1724 <-> 410, 1756, 1887
1725 <-> 296, 987
1726 <-> 676, 878, 1837
1727 <-> 641
1728 <-> 1525, 1557, 1701, 1875
1729 <-> 1675
1730 <-> 483, 1376, 1515, 1916
1731 <-> 363, 1239, 1353
1732 <-> 647, 1056
1733 <-> 320, 527, 1733
1734 <-> 963
1735 <-> 779, 1080
1736 <-> 202
1737 <-> 202
1738 <-> 871, 1177
1739 <-> 1026
1740 <-> 700, 1082, 1199, 1941
1741 <-> 231
1742 <-> 1936
1743 <-> 1701
1744 <-> 462, 915
1745 <-> 1798
1746 <-> 333, 591
1747 <-> 1370, 1659
1748 <-> 1472, 1930
1749 <-> 797
1750 <-> 1949
1751 <-> 1449, 1466
1752 <-> 156, 1138, 1571
1753 <-> 476, 1473
1754 <-> 1170
1755 <-> 29, 1656, 1695
1756 <-> 388, 1029, 1724
1757 <-> 1347
1758 <-> 315, 648, 823, 1851
1759 <-> 1759
1760 <-> 1760, 1889
1761 <-> 374, 1168
1762 <-> 1814
1763 <-> 380, 783, 1863
1764 <-> 1370, 1949
1765 <-> 366
1766 <-> 782, 1103
1767 <-> 271, 569, 1656
1768 <-> 362
1769 <-> 822, 1165
1770 <-> 385, 605, 1800
1771 <-> 726, 1674, 1907
1772 <-> 677, 1390
1773 <-> 1439, 1773
1774 <-> 300
1775 <-> 1014
1776 <-> 176, 1040, 1332
1777 <-> 1841
1778 <-> 1156, 1484
1779 <-> 429, 579, 1049, 1363
1780 <-> 391, 627
1781 <-> 494
1782 <-> 101
1783 <-> 15
1784 <-> 42, 964, 1604, 1699, 1996
1785 <-> 951, 1493, 1642
1786 <-> 712, 1786
1787 <-> 998, 1787
1788 <-> 526, 839
1789 <-> 71, 174, 946, 1973
1790 <-> 1626
1791 <-> 1589
1792 <-> 108, 1842
1793 <-> 250
1794 <-> 1043
1795 <-> 949
1796 <-> 1038
1797 <-> 1053, 1149
1798 <-> 1683, 1745, 1830
1799 <-> 111, 165, 458
1800 <-> 215, 338, 1500, 1770
1801 <-> 787
1802 <-> 1244
1803 <-> 950, 1560
1804 <-> 598
1805 <-> 238
1806 <-> 1343
1807 <-> 1376
1808 <-> 612, 1442
1809 <-> 176, 505, 931, 1437
1810 <-> 1062, 1216, 1465
1811 <-> 1080, 1154
1812 <-> 1832, 1858
1813 <-> 1813
1814 <-> 690, 1054, 1762
1815 <-> 264, 268
1816 <-> 1816
1817 <-> 1223
1818 <-> 847, 1142
1819 <-> 509
1820 <-> 229, 1688
1821 <-> 1976
1822 <-> 8
1823 <-> 1027
1824 <-> 1288
1825 <-> 1197
1826 <-> 1894, 1977
1827 <-> 1436
1828 <-> 1348, 1696
1829 <-> 897
1830 <-> 1311, 1798
1831 <-> 1039, 1446
1832 <-> 115, 1564, 1812
1833 <-> 844, 1281
1834 <-> 70
1835 <-> 246, 709, 976, 1313, 1519
1836 <-> 444
1837 <-> 1726
1838 <-> 1494, 1674
1839 <-> 275, 623, 1489, 1582
1840 <-> 1011
1841 <-> 460, 1552, 1777
1842 <-> 536, 794, 1280, 1792
1843 <-> 631
1844 <-> 334, 826
1845 <-> 1714
1846 <-> 498, 1101, 1323, 1846
1847 <-> 1380
1848 <-> 1123
1849 <-> 1157
1850 <-> 1850
1851 <-> 1144, 1569, 1758
1852 <-> 571, 1522
1853 <-> 289
1854 <-> 1089
1855 <-> 107, 1038, 1080, 1589
1856 <-> 1947
1857 <-> 895, 1225
1858 <-> 326, 1812
1859 <-> 248, 450, 1296
1860 <-> 1860
1861 <-> 746, 1861
1862 <-> 1882
1863 <-> 217, 1763
1864 <-> 0, 1195, 1239
1865 <-> 1156, 1925
1866 <-> 1492
1867 <-> 890, 1253, 1867
1868 <-> 1164, 1893
1869 <-> 1079, 1175
1870 <-> 88, 1354
1871 <-> 1135, 1522, 1940
1872 <-> 1872
1873 <-> 1069
1874 <-> 215
1875 <-> 729, 930, 1728
1876 <-> 1622, 1903
1877 <-> 73, 1182
1878 <-> 1970
1879 <-> 1136, 1912, 1958, 1989
1880 <-> 864, 1708
1881 <-> 475, 1042
1882 <-> 249, 1708, 1862
1883 <-> 1303
1884 <-> 31
1885 <-> 680, 1231
1886 <-> 40, 1631
1887 <-> 462, 1341, 1724
1888 <-> 1331
1889 <-> 1470, 1760
1890 <-> 161, 203
1891 <-> 424, 1683
1892 <-> 1892
1893 <-> 254, 1285, 1868
1894 <-> 13, 172, 1826
1895 <-> 114, 382, 1081
1896 <-> 525, 1090
1897 <-> 606, 803, 980
1898 <-> 322, 1260
1899 <-> 348, 550, 749, 1148
1900 <-> 408, 1900
1901 <-> 80, 859
1902 <-> 673, 1583
1903 <-> 1028, 1876
1904 <-> 1208
1905 <-> 1464, 1682
1906 <-> 1027, 1077
1907 <-> 1551, 1771
1908 <-> 408
1909 <-> 1909
1910 <-> 359, 812
1911 <-> 20, 587, 1340, 1429
1912 <-> 529, 1879
1913 <-> 1001, 1134, 1588
1914 <-> 1720
1915 <-> 502
1916 <-> 848, 1086, 1314, 1497, 1730
1917 <-> 1951
1918 <-> 401
1919 <-> 273, 1667
1920 <-> 925, 1276, 1324
1921 <-> 58, 921
1922 <-> 48
1923 <-> 1344
1924 <-> 1993
1925 <-> 1865
1926 <-> 330
1927 <-> 670, 1192
1928 <-> 1654
1929 <-> 907
1930 <-> 600, 1748
1931 <-> 1931
1932 <-> 958, 991
1933 <-> 983
1934 <-> 402, 1359
1935 <-> 294, 682, 784
1936 <-> 1646, 1742
1937 <-> 1937, 1971
1938 <-> 126, 1938
1939 <-> 1998
1940 <-> 257, 1871
1941 <-> 1740
1942 <-> 780, 937
1943 <-> 110, 1265
1944 <-> 820, 837
1945 <-> 264, 1347
1946 <-> 378
1947 <-> 170, 537, 573, 829, 1856
1948 <-> 1074, 1089
1949 <-> 1750, 1764
1950 <-> 478, 689
1951 <-> 131, 254, 1917
1952 <-> 208, 1541
1953 <-> 803
1954 <-> 547, 904, 955, 1954
1955 <-> 528
1956 <-> 1343
1957 <-> 99, 191, 1693
1958 <-> 1879
1959 <-> 1594
1960 <-> 1016, 1643
1961 <-> 1094
1962 <-> 37, 219, 912
1963 <-> 262
1964 <-> 989, 1340
1965 <-> 1056, 1396, 1598
1966 <-> 1078
1967 <-> 77
1968 <-> 365
1969 <-> 614
1970 <-> 1878, 1970
1971 <-> 1937
1972 <-> 728, 732
1973 <-> 1789
1974 <-> 14, 1500
1975 <-> 1363
1976 <-> 1821, 1976
1977 <-> 720, 1035, 1214, 1826
1978 <-> 1260, 1347, 1639
1979 <-> 577, 661
1980 <-> 1409, 1557
1981 <-> 1409
1982 <-> 272, 724
1983 <-> 636
1984 <-> 148, 771, 1034
1985 <-> 155
1986 <-> 216
1987 <-> 1987
1988 <-> 553, 584
1989 <-> 313, 1879
1990 <-> 990, 1153
1991 <-> 1597
1992 <-> 364
1993 <-> 90, 765, 1924
1994 <-> 645, 1641
1995 <-> 558
1996 <-> 643, 1784
1997 <-> 362, 1613
1998 <-> 1939, 1998
1999 <-> 90, 1212'''

seen = {0}
lines = in12.splitlines()


def recursion(number):
    seen.add(number)
    for n in lines[number].split(' <-> ')[1].split(', '):
        if int(n) not in seen:
            recursion(int(n))


recursion(0)
print(len(seen))
