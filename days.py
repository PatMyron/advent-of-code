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
s = re.sub("<.*?>", '', s)
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
