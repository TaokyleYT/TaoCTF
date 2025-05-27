import hashlib

flags = {
    # flag hashes
    "505e6ac36e65d9d3fd32976e3b820bc2332b7fe5407a8965f86e9af3f0829fe3": "forensics/nice pics",
    "cfa62fe7462c43481eb7213470fd4cf6049e74bbb67bdcb412107e1479e33aa1": "forensics/HBD",
    "4fe08e129e942a4c035046bfff18d77a7521b3b9d403daba5bd65b8c076ddd9e": "cryptography/Tao Exclusive",
    "4e7c54bd6b42de5e0e87d899815d6796788ea9b10a160f2a23de2d6cb61bf2f6": "cryptography/RSA is NOT fun",
    "d44298aef0f8830efe1768207639020af4d09ba365cb66504bead65b506224c3": "reverse engineering/TaoKen",
    "6ed852228d3d36d3e645c68c9f9baf390ab9551ac90c092c8a03283e7f039b53": "reverse engineering/Cal Gay 2.0",
    "bea546705e575b3b7bf0b0f5deff7ed0f139c3e3b561dc0c183f3ef96c9647fa": "misc/git yo ass",
    # Special inputs in case you dum
    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855": "Enter something please",
    "7b54b0bf29baeaecf3800faf291cbbeedc51d4032a85a67118f2dfe0be6b812c": "Tf bro this is a fake flag",
}

# if you are seeing this, no you can't find out the flag from this script unless you somehow found a way to reverse the hashes (mathematically impossible tho)

if __name__ == "__main__":
    flag = hashlib.sha256(bytes(input("Enter your flag here (begins with TaoCTF, case sensitive): ").replace(" ", ""), encoding="ascii")).hexdigest()
    #print(flag)
    chal = flags.get(flag, None)
    
    if chal is None:
        print("\x1b[31mNo correct flags match this flag. This flag is probably wrong\x1b[m")
    elif "/" in chal:
        print(f"\x1b[32mCongrats, you solved \x1b[1;33m{chal}\x1b[m!")
    else:
        print(f"\x1b[33m{chal}\x1b[m")
else:
    print("\x1b[31mWHY ARE YOU IMPORTING ME WAAAAAAAA\x1b[m")
    
