import hashlib
import base64

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = ""
key_part_static2_trial = "}"
#key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

username_trial = b"SRIRAJ15110"

# where our input begins:
offset = 23

# positions in username_trial
positions = [4,5,3,6,2,7,1,8]

for p in positions:
    key_part_dynamic1_trial += hashlib.sha256(username_trial).hexdigest()[p]
key = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
print(key)
