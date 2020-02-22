In [1]: s='SRLU{LZPL_S_UASHKXUPD_NXYTFTJT}'

不会做密码学的题，查了查，和凯撒差不多，也是rot，但是多了一个密钥，网上有无密钥的解法，但是好高端，各种数学公式，看不懂啊
维吉尼亚密码的密钥长度需要与明文长度相同，如果少于明文长度，则重复拼接直到相同
于是遍历一边密钥只有一个字符(a-z)的加密结果，看看能有啥眉头不

In [2]: import string

In [9]: for i in range(26):
   ...:     t=''
   ...:     for j in s:
   ...:         if j in string.uppercase:
   ...:             t+=chr(((ord(j)-ord('A')+i)%26)+ord('A'))
   ...:         else:
   ...:             t+=j
   ...:     print chr(ord('A')+i),t
   ...:     
   ...:     
   ...:     

A SRLU{LZPL_S_UASHKXUPD_NXYTFTJT}
B TSMV{MAQM_T_VBTILYVQE_OYZUGUKU}
C UTNW{NBRN_U_WCUJMZWRF_PZAVHVLV}
D VUOX{OCSO_V_XDVKNAXSG_QABWIWMW}
E WVPY{PDTP_W_YEWLOBYTH_RBCXJXNX}
F XWQZ{QEUQ_X_ZFXMPCZUI_SCDYKYOY}
G YXRA{RFVR_Y_AGYNQDAVJ_TDEZLZPZ}
H ZYSB{SGWS_Z_BHZOREBWK_UEFAMAQA}
I AZTC{THXT_A_CIAPSFCXL_VFGBNBRB}
J BAUD{UIYU_B_DJBQTGDYM_WGHCOCSC}
K CBVE{VJZV_C_EKCRUHEZN_XHIDPDTD}
L DCWF{WKAW_D_FLDSVIFAO_YIJEQEUE}
M EDXG{XLBX_E_GMETWJGBP_ZJKFRFVF}
N FEYH{YMCY_F_HNFUXKHCQ_AKLGSGWG}
O GFZI{ZNDZ_G_IOGVYLIDR_BLMHTHXH}
P HGAJ{AOEA_H_JPHWZMJES_CMNIUIYI}
Q IHBK{BPFB_I_KQIXANKFT_DNOJVJZJ}
R JICL{CQGC_J_LRJYBOLGU_EOPKWKAK}
S KJDM{DRHD_K_MSKZCPMHV_FPQLXLBL}
T LKEN{ESIE_L_NTLADQNIW_GQRMYMCM}
U MLFO{FTJF_M_OUMBEROJX_HRSNZNDN}
V NMGP{GUKG_N_PVNCFSPKY_ISTOAOEO}
W ONHQ{HVLH_O_QWODGTQLZ_JTUPBPFP}
X POIR{IWMI_P_RXPEHURMA_KUVQCQGQ}
Y QPJS{JXNJ_Q_SYQFIVSNB_LVWRDRHR}
Z RQKT{KYOK_R_TZRGJWTOC_MWXSESIS}

果然，当密钥是I的时候，字符串被加密成AZTC{THXT_A_CIAPSFCXL_VFGBNBRB}
隐隐能猜到ACTF,VIGENERE这两个单词
对比ACTF和AZTC，第2和第四位不同，但是Z+3=C，C+3=F，于是猜测密钥第二位应该是I+3=L
再看一下密钥是纯L的加密结果DCWF{WKAW_D_FLDSVIFAO_YIJEQEUE}，验证了上述想法
I AZTC{THXT_A_CIAPSFCXL_VFGBNBRB}
L DCWF{WKAW_D_FLDSVIFAO_YIJEQEUE}
由于开头的ACTF和末位的VIGENERE都是隔一个字符就正确一个，于是猜测密钥只含I和L

从上面那两个结果能凑齐FLAG了

最后逐个凑了一下密钥，结果是ililliliiililililiilil

按理说应该是解密的，但是用这个密钥加密题目给的字符串就能出FLAG
至于为什么，我也不知道，可能因为加密解密是对称的？