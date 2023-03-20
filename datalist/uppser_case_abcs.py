from random import choice
from string import digits, ascii_letters


A = ["p12wsad", "p11ewda", "p12e32d", "p10psda", "p12eskn", "p04ad3f", "p99pdo3", "p40bsdk", "p02mcbc", "p85sage" ]
B = ["t59post", "t93as92", "t29oos0", "t92nos0", "t21sadj", "t01asd2", "t29oos0", "t29oos0", "t29oos0", "t29oos0" ]
C = ["s02suto", "s59soda", "s01p1os", "s13osia", "s03s29s", "s01s012", "s13sf0s", "s91afso", "s54afsa", "s99fasf" ]
D = ["f13as34", "f09wo01", "f27ds12", "f14pd52", "f08sdfa", "f99sadi", "f17sdf2", "f23sd98", "f83kds9", "f63sdo2" ]
E = ["g89twe1", "g02sfa3", "g29spf5", "g12fsd9", "g65ksd2", "g48sdg2", "g87poi2", "g94ewd1", "g06pas2", "g83sdh1" ]
F = ["h08as02", "h76dk23", "h23ps91", "h91o23s", "h29s0s1", "h17sdf2", "h23osd9", "h44sdc9", "h02nsd3", "h95sds4" ]
G = ["j01sdf2", "j49osf2", "j09sd42", "j76kd12", "j34sdf3", "j23sd98", "j91psd0", "j54sdp2", "j12lsd1", "j98sdf2" ]
H = ["k13lsd1", "k01sfd2", "k67osd1", "k08sfd2", "k59psd3", "k02sfd9", "k83osd1", "k99ksd2", "k42osd2", "k65psd1" ]
I = ["m09ksd1", "m47sda2", "m29psd3", "m53osd4", "m17dsf2", "m28sdf3", "m09psd3", "m11ksd2", "m32osd2", "m82sdf2" ]
J = ["n91psd2", "n42sdf1", "n12ksd2", "n59osd3", "n84sda1", "n16sdf3", "n23osd1", "n78sdf2", "n10osd2", "n99sdf1" ]
K = ["q13sdf1", "q01sdf2", "q27osd1", "q93osd2", "q54ksd2", "q75sdf2", "q02psd1", "q93osd2", "q39ksd2", "q12sdf3" ]
L = ["r39ksd1", "r12psd2", "r93osd2", "r23ksd3", "r69osd1", "r17ksd3", "r29osd1", "r45ksd2", "r03osd2", "r98ksd1" ]
M = ["u49sdf2", "u91psd1", "u27ksd1", "u56osd2", "u82sdf2", "u12ksd3", "u87osd1", "u23psd2", "u34ksd2", "u71sdf2" ]
N = ["v02as1d", "v49bsdk", "v91po12", "v03as1d", "v29bsdk", "v98po12", "v57as1d", "v72bsdk", "v14po12", "v83as1d" ]
O = ["w71as1d", "w42bsdk", "w09po12", "w56as1d", "w23bsdk", "w82po12", "w13as1d", "w29bsdk", "w88po12", "w51as1d" ]
P = ["x17as1d", "x29bsdk", "x91po12", "x49as1d", "x72bsdk", "x14po12", "x83as1d", "x98bsdk", "x03po12", "x29as1d" ]
Q = ["y57as1d", "y14bsdk", "y72po12", "y98as1d", "y23bsdk", "y56po12", "y29as1d", "y82bsdk", "y13po12", "y51as1d" ]
R = ["z01as1d", "z49bsdk", "z82po12", "z03as1d", "z23bsdk", "z98po12", "z57as1d", "z72bsdk", "z14po12", "z83as1d" ]
S = ["b14as1d", "b81bsdk", "b39po12", "b23as1d", "b77bsdk", "b49po12", "b16as1d", "b58bsdk", "b92po12", "b01as1d" ]
T = ["c09as1d", "c42bsdk", "c99po12", "c27as1d", "c88bsdk", "c52po12", "c71as1d", "c23bsdk", "c49po12", "c58as1d" ]
U = ["d17as1d", "d29bsdk", "d91po12", "d42as1d", "d72bsdk", "d56po12", "d01as1d", "d99bsdk", "d29po12", "d88as1d" ]
V = ["i01as1d", "i39bsdk", "i92po12", "i81as1d", "i23bsdk", "i48po12", "i49as1d", "i77bsdk", "i16po12", "i58as1d" ]
W = ["e08as1d", "e81bsdk", "e16po12", "e92as1d", "e23bsdk", "e49po12", "e77as1d", "e39bsdk", "e92po12", "e42as1d" ]
X = ["l29as1d", "l81bsdk", "l72po12", "l58as1d", "l39bsdk", "l92po12", "l01as1d", "l49bsdk", "l16po12", "l77as1d" ]
Y = ["o09as1d", "o42bsdk", "o99po12", "o23as1d", "o88bsdk", "o16po12", "l71as1d", "l56bsdk", "l92po12", "l48as1d" ]
Z = ["a92as1d", "a48bsdk", "a23po12", "a99as1d", "a56bsdk", "a71po12", "a16as1d", "a42bsdk", "a09po12", "a88as1d" ]


upper_case_dict = {
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "E": E,
    "F": F,
    "G": G,
    "H": H,
    "I": I,
    "J": J,
    "K": K,
    "L": L,
    "M": M,
    "N": N,
    "O": O,
    "P": P,
    "Q": Q,
    "R": R,
    "S": S,
    "T": T,
    "U": U,
    "V": V,
    "W": W,
    "X": X,
    "Y": Y,
    "Z": Z
}







class string_operations:
        def _get_the_central_key(self, string:str=None, slicenum_front:int=20, slicenum_back:int=20):
                if string is None:
                    return None
                new_string = string[slicenum_front:-slicenum_back]
                return new_string
        def _get_secured_key(string:str=None, post:int=20, pre:int=20):
                characters = ascii_letters + digits
                post_key = ''.join(choice(characters) for i in range(post))
                pre_key = ''.join(choice(characters) for i in range(pre))
                final_key = choice(string)
                returnable_key = str(pre_key+final_key+post_key)
                return returnable_key

class encrypt:
        def _get_an_alphabet_key(alphabet:str=None)->str:
                assert len(alphabet) == 1
                
                UC_alphatbet = alphabet.capitalize()
                UC_list = upper_case_dict.get(UC_alphatbet)
                final_key = choice(UC_list)
                returnable_key = string_operations._get_secured_key(
                        string=final_key,
                        post=20,
                        pre=20
                )
                return returnable_key


        def _get_collective_alphabet_key(word: str) -> str:
                assert word != None
                UC_word = word.upper()
                UC_WORD_LIST = list(UC_word)
                returnable_result = []
                for char in UC_WORD_LIST:
                        returnable_result.append(encrypt._get_an_alphabet_key(char))
                return ''.join(returnable_result)       


class decrypt:
    def _get_an_alphabet(ENC_string:str=None):
        assert len(ENC_string) == 7
        for key, value in upper_case_dict.items():
                if ENC_string in value:
                        return key
        return None

    def _get_collective_alphabet(strings: str) -> str:
        assert strings != None
        returnable_result = []
        chunk_size = 47
        chunks = []
        for i in range(0, len(strings), chunk_size):
            chunk = strings[i:i+chunk_size]
            chunks.append(chunk)
        for char in chunks:
            central_key = string_operations._get_the_central_key(string=char)
            returnable_result.append(decrypt._get_an_alphabet(central_key))
        return ''.join(returnable_result)