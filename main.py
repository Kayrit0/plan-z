z = {
    "a": "z",
    "b": "z_pzuzt",
    "c": "Zziznz_zzZ",
    "d": "ZV",
    "e": "z_",
    "f": "zz",
    "g": "z_Z",
    "h": "_zZZ",
    "i": "z__z",
    "j": "zzz",
    "k": "_z_",
    "l": "zZz",
    "m": "z_zZ",
    "n": "zZ_z",
    "o": "_z__",
    "p": "z__Z",
    "q": "_ZzZ_",
    "r": "Z_v",
    "s": "z_v",
    "t": "_vz",
    "u": "___z",
    "v": "Z_z_z",
    "w": "z_z_Z",
    "x": "Z_puz",
    "y": "tlz",
    "z": "erz_z",
    " ": "zZov_z",
}

s = str(input())
s = s.lower()
zhopa = ""

for l in s:
    a = z.get(l)
    if a is not None:
        zhopa += a
        # zhopa += "o"

print(zhopa)
