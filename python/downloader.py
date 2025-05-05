'''
from pytube import YouTube

#link = input("Aqui o link do vídeo: ")

def download(link):
    try:
        yt = YouTube(link)
        print("Baixando...")
        yt.streams.get_highest_resolution().download()
        print("Download concluído!")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")

link = input("Aqui o link do vídeo: ")
if "youtu.be/" in link:
    link = link.replace("youtu.be/", "youtube.com/watch?v=")

download(link)
'''

import yt_dlp

output_directory = r"D:\DATA"
#link = input("Aqui o link do vídeo: ")
links = [
    "https://youtu.be/qQFgDHnIx_g?si=-FkjZmJzB2ADTWN5",
    "https://youtu.be/KDwLnDKRgpM?si=UDz9_FRt6rB232La",
    "https://youtu.be/jH-yl_NB_cQ?si=sKrJ191wRuR_aqTR",
    "https://youtu.be/NFKHrKoJmKs?si=9UJh-GN_zGLL7kdB",
    "https://youtu.be/CJIf3n5SMf8?si=oxNW1w2C6hu2EWUg",
    "https://youtu.be/NdzUPeyhp1A?si=pruMMfRojYmGn2Pk",
    "https://youtu.be/73hMcaT4G4s?si=QcMW92gz0-Q2jfhj",
    "https://youtu.be/t_dnEA4IDOQ?si=guiRJqzRn1li-dcM",
    "https://youtu.be/OpMm5JO0wtU?si=v0nXYTvQ7vlXkFZu",
    "https://youtu.be/mUubQBy5OVY?si=g9F9VXjNHmo6rZ0a",
    "https://youtu.be/mUubQBy5OVY?si=Q0yL5R6F4r61ihGW",
    "https://youtu.be/qsmHYPk4XGM?si=V5Vk0Yy9X65lVL3f",
    "https://youtu.be/3lQ-_Qnlh-k?si=LibGxYshSYvwoOyg",
    "https://youtu.be/HwLTTBvzyUE?si=bWunktQMGjrMw-bx",
    "https://youtu.be/6PWUbDhHfqs?si=lEbJWvH0nbHsIKOq",
    "https://youtu.be/SrvFZDSkieU?si=3uHXKZzQhXKC7889",
    "https://youtu.be/Bqc6B5LzTN0?si=seiY3J6m0v4akzcX",
    "https://youtu.be/KAlOPNZtVsw?si=BUtFFAs1DkTVYhZQ",
    "https://youtu.be/Ts1h1EDiLpc?si=2kZe06hoofS0WQ1U",
    "https://youtu.be/JMV-K0d1QYQ?si=HZpdksrdzqpOOMUV",
    "https://youtu.be/W5BBzdzvY0w?si=jkfSH0TlA0HnigMs",
    "https://youtu.be/OtDvlKRgJrc?si=9XIT18qbZ-FTPqtk",
    "https://youtu.be/VVIVYpbkmWo?si=Qa7eOM16Sq6Y0q6C",
    "https://youtu.be/QTC7_DVENZA?si=P7WOxiLrvqJ4CoXR",
    "https://youtu.be/uzutxVqVJsI?si=3V8LQKxoajDhKOA9",
    "https://youtu.be/G4afTjkCDvc?si=2mIH6PNDS52etGc1",
    "https://youtu.be/0mJSNgnl8y8?si=GxBFe2HSuIvv5PlP",
    "https://youtu.be/ZlKJxj_1kdo?si=xBtXZQupl8wf8OlJ",
    "https://youtu.be/ZlKJxj_1kdo?si=xBtXZQupl8wf8OlJ",
    "https://youtu.be/kNxv0WztzL4?si=G8G5_O3c64cBEKdy",
    "https://youtu.be/YckFv7QYuEM?si=II45e5oZmF4kFaKd",
    "https://youtu.be/5U1blX9CQAU?si=t49EzV8MBDou4Vub",
    "https://youtu.be/OpTBNSFZtx0?si=xgl2bVznpjUNah9r",
    "https://youtu.be/1i1673ILdVI?si=IcNCkbPA3fJiPg2P",
    "https://youtu.be/yovzEEYOl-E?si=4HV2qUeBAyWi2_dc",
    "https://youtu.be/O4XCRwSQHao?si=WwRvqdHbQhvk_AmY",
    "https://youtu.be/ndS74J0J_lE?si=F8x4Es1AgjUxGUda",
    "https://youtu.be/YyFd_dXy494?si=AZx92PDjOn85jIP5",
    "https://youtu.be/sEQyi3tVrIM?si=gCkJPPQnPDumNAvF",
    "https://youtu.be/_c8ZTK50UZo?si=GloaBp1hlnKSOGTs",
    "https://youtu.be/OXBCV5WixCU?si=yMa7Epi9EnEe5HUa",
    "https://youtu.be/OXBCV5WixCU?si=WJgsPyd--k3OWE8b",
    "https://youtu.be/1lMFElbRIos?si=ixWWV2ilb2-RN5bP",
    "https://youtu.be/s-hqGZs5Vt4?si=T_6a6OpKnZ8NRX-M",
    "https://youtu.be/h7mRVFXqjlg?si=ezoH1_LagHTEvIRM",
    "https://youtu.be/QbnmpJo3DiI?si=8ZWq6gi_Q73WDaCV",
    "https://youtu.be/ANfpF0pNob4?si=1mFfmuLxnsA2_GMw",
    "https://youtu.be/YXnQ02HYB1w?si=U-MP7SGnJmyoGT_s",
    "https://youtu.be/WkukZDLBEy0?si=Gd3qnfWJOWOGJMjL",
    "https://youtu.be/NYFcTj-KmvI?si=ZXrHlLWEj15L1ZtT",
    "https://youtu.be/wWU1Bn6wy9o?si=FO10SzFkTtvM-J9a",
    "https://youtu.be/u2FOGNSJfX8?si=wolM50w3cDdJss9r",
    "https://youtu.be/cWh_Usx47IM?si=HnbrauGeGJIkdgIF",
    "https://youtu.be/MBg5g2g3okU?si=GW1H5bv-L26x03sO",
    "https://youtu.be/MfzYPahyqYo?si=IyNoWgyiwwypBWWi",
    "https://youtu.be/u5ZNiJr14-Y?si=03yNZ9A3W7ukLWjM",
    "https://youtu.be/80_M97jXFpE?si=J-0TnW6YMTamSOoh",
    "https://youtu.be/kAwznSYA_oE?si=j2eWPnMDI_0al-zA",
    "https://youtu.be/h6LyF17DaAs?si=7c4QTHLYY8IucNNf",
    "https://youtu.be/Tw0O8XaN7vc?si=i6fOzTgr2vqnSLOB",
    "https://youtu.be/QYKpysFX-9I?si=hu78pNc4PwuKpiVm",
    "https://youtu.be/ju-VN3hRp7Q?si=s_dxThPDv-T-cU-W",
    "https://youtu.be/wdtxqAjWjEU?si=7T8dbCBzbkAKIEJU",
    "https://youtu.be/lWax47zymUE?si=d5igok-r5ZL141u3",
    "https://youtu.be/bmAwpcTyKyo?si=1oBVx8Kw21LKqrUP",
    "https://youtu.be/xYUhVwl5Qew?si=3Qe0H_FJ883zm9eG",
    "https://youtu.be/EN5aSA6riaM?si=xEa9FfSj3sxR0Vl7",
    "https://youtu.be/WA2dwiWFpi0?si=SZq7t-lWNSwW61f3",
    "https://youtu.be/YKK1FTSOnww?si=f6tDyP2nYVB-5GHU",
    "https://youtu.be/3UyhjqMVMfg?si=WDOaPc5K-uS8oWYO",
    "https://youtu.be/YMQPTUDlbMg?si=v6MK8FCz-uLo3Om9",
    "https://youtu.be/VPjRsLZiBBk?si=eZB0Ojv30MHhITc9",
    "https://youtu.be/V-n0FDCT2N4?si=Fwwvk9oUKZJGQVzz",
    "https://youtu.be/Ij7TK2iRR7k?si=rOxynFCHW8xh0HK2",
    "https://youtu.be/OEDQj7XucHg?si=j0D8Ho2wWqIt7YkH",
    "https://youtu.be/NSAEphKyS-g?si=Cb1KLSk3VYo-gJJO",
    "https://youtu.be/4y0_rOSnb_g?si=Fx2h41DmVTqP-e1b",
    "https://youtu.be/wkdZxuu0dj0?si=1b8QEor-0WjAkiGp",
    "https://youtu.be/meiqsELWxNs?si=MlMF_77pPk9AgGI-",
    "https://youtu.be/mTPgy4VuXyo?si=yH9Gn9__2trNXizP",
    "https://youtu.be/rBVjbjGVVjo?si=UpJ3w8zbynZu_KZA",
    "https://youtu.be/_pnAJPnp_Jw?si=-_3u1yWj78Bvdroj",
    "https://youtu.be/Tqdi6BZUWr4?si=-PNspksTS_2LR4w1",
    "https://youtu.be/dANcAGydlsM?si=EbiYlwfRjZmMS-X6",
    "https://youtu.be/aMpM68cb5MY?si=81UBegE-SZVyUxXw",
    "https://youtu.be/xDR4vQtArMo?si=3o7fVP6ccs4yQ-CB",
    "https://youtu.be/qxzQR5uwWsk?si=AZVJtlNBe1IwXBAY",
    "https://youtu.be/OEeY-Eu1lcU?si=cOt3X-GabHeDrHEK",
    "https://youtu.be/OEeY-Eu1lcU?si=cOt3X-GabHeDrHEK",
    "https://youtu.be/hhZsqHF1jqI?si=tajTufar9dG2S9_Y",
    "https://youtu.be/hhZsqHF1jqI?si=tajTufar9dG2S9_Y",
    "https://youtu.be/rIsRZwtT_8A?si=4Yb6Z_LwBCK9Eo1A",
    "https://youtu.be/gTRFVMkMajw?si=5Ym3LD9T_PFIuhc6",
    "https://youtu.be/lTRNHofvCmU?si=CZeLe4_kTwUW6LrL",
    "https://youtu.be/-3KZhUi-6FY?si=W8f5NQT3Ge5JMIfB",
    "https://youtu.be/ki-7NTR-yzw?si=3boOQR7UmLWMYYmj",
    "https://youtu.be/zdrrD218jJE?si=2m9BWs4EiQdYxyfq",
    "https://youtu.be/ps_RstfY7Uc?si=68VO63YAh_p_lZkc",
    "https://youtu.be/7j5aLkEe_vE?si=wvUc6TRIiSngc3OZ",
    "https://youtu.be/JBqBccxHJvk?si=bzbmNXPyLpL6NkAW",
    "https://youtu.be/eJ5Lr411eks?si=JK25AwmVQ9bdu07E",
    "https://youtu.be/2Z6nW7jU_uU?si=nFbmIAQ7kWSytoyf",
    "https://youtu.be/jAIEtnzlNNM?si=wH-YqxUdEUYx-AD-",
    "https://youtu.be/kuZ3Of3LuB4?si=feSbsZeI_GJhoW5E",
    "https://youtu.be/cQ7nxoVkZa8?si=_M4Eeq2Bz0fNWRNN",
    "https://youtu.be/J-Lj9d5XRcc?si=cbsh4hI-XFpj_F_a",
    "https://youtu.be/incBpxO37cY?si=3kjuoCIXjx_HC197",
    "https://youtu.be/ilwdZsCI2Hc?si=jKlo4tsHLLrodcXa",
    "https://youtu.be/lclKOqYuvug?si=i8UWxMCEBFpiLvUa",
    "https://youtu.be/Ifcaa0rzDtI?si=mt9EbghzIANSMHOv",
    "https://youtu.be/-qsT7ixZ5FM?si=Gb3KnaIxTPvy96NK",
    "https://youtu.be/_qDKrvstS9c?si=SuvV-ctAf71uKsm_",
    "https://youtu.be/flOPSTNmOFI?si=3w0xXsyVNRYOjXsP",
    "https://youtu.be/eD_jy0XCE9M?si=b3PbNi_V4KrbXtfY",
    "https://youtu.be/ptmkpzuxX3c?si=UDz7VDy29GnEPSL6",
    "https://youtu.be/zOc855DIZyk?si=dPwO7_ES-pEYCDbb",
    "https://youtu.be/_hL1pguiHX0?si=SYSFz_vitAFFavNv",
    "https://youtu.be/wSKKEAnLTDw?si=MX7PnvEer1mYhHj_",
    "https://youtu.be/c7G28U33V9o?si=Xb03gFg5WhYbPNIi",
    "https://youtu.be/l-zlfgAhssk?si=UU5lYmauRq9dmfio",
    "https://youtu.be/bn7rzZ-Q1dg?si=GMFHBZFyCjK926pP",
    "https://youtu.be/v5FiOVEUvVw?si=Dbf372Lmvdh8jTIb",
    "https://youtu.be/7BoTTLK1K_4?si=OsZW1sWCMBAFRWT3",
    "https://youtu.be/NGB5k7pD7AM?si=7eDmImbJ_hLPePht",
    "https://youtu.be/v0vbOLiKGTI?si=HhNT4ccvEHCXIFnd",
    "https://youtu.be/42Uzv7IEZBw?si=BOj8Gkuf6AJNyTPn"
]
ydl_opts = {
    'format': 'bestaudio',# 'bestvideo',
    'merge_output_format': 'mp4',
    'outtmpl': f'{output_directory}/%(title)s.%(ext)s'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for link in links:
        try:
            ydl.download([link])
            print("Download concluído!")
        except Exception as e:
            print(f"Erro ao baixar o vídeo: {e}")