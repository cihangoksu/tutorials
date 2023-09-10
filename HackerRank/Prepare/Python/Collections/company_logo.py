# %% ordered dictionary
from collections import Counter

def print_output(characters):
    char_list = list(characters)
    char_dict = Counter(char_list)
    char_dict_sorted = char_dict.most_common()
    
    max_three = sorted(set(char_dict.values())) [-1:-4:-1] 

    max_list_key, max_list_value = [], []
    
    i = 0 
    max_sublist_key = []
    while True:
        for key, value in char_dict_sorted:
            if value == max_three[i]: max_sublist_key.append(key)
        max_sublist_key = sorted(max_sublist_key)
        max_list_key.extend(max_sublist_key)
        max_list_value.extend([max_three[i]]*len(max_sublist_key))

        if len(max_list_key)>=3:
            break
        else:
            i += 1
            max_sublist_key = []
        
    # now let's print
    for i in range(3):
        print(max_list_key[i] + ' ' + str(max_list_value[i]))






if __name__ == '__main__':
    characters = 'kwuzazrxreqpypvzdsnvtumobemekfskfshopevggqgoascrunynwaxolxcygnkllnqslcqrlmlbvrarepmfkdbacawcipzpbcgnekzbrhotracywrlarfawxogygnanyhtgtvdfnaluefebhjivqagvcljghgbscvkmmtnafamqffycsgufjugqzhgstmjhwzosrnveqnwahflysxumwuvxyxrmarwzbabufxajdqybetjtucqhnavugflaofmtrkkrbsszoqcvuhydsdlfwinucgtlgeejaftfyaidcklgfgkwwgjlnbwryvoqbzzbktemvhpuudgfgxwzcmwgvcnofdebcwyhxmnxefrkdlafvfwgrzembfugqxcpukvgoixedbyqjmfywqqwnhotqdpgdailabictebdgnjfdbiqbnlrbsduwebtqaevukkyheypwdksmpztideoropeepphoniddgnrsmiqsafuyxvqerkoitpqsgswtroiwralcrupfavyyfwmyzuocaeyriavmvukqhzjzubnnrecsqbjngtczuonyktdcdvukxcdcwatlvjluumjijdfemilyarwvdytraygahbpgarwyzffyoukgmdgemmmxkajwsqtkpaarjskvuldfvlydkcoezgygjfygwzwsndfmkxzuljsnnltlpnjrtkrvdzchhmaejmiatzvmyysdiqhhyihmavkcjfuauvtwafnqyowyfsnfmxxvomarjvplrqfopknlstgnnodifdiqzvliszptdcjcffzbacszftbkeorbftaqjpfaackqqobbaccwzxwbymkwckgzkoqmwiilsgitbqbfjzwkzodaqgknmxujfrdgoiupvqmnpkruxwungbfjbcpqsxizuvbpedajxkncbcunlrkwiokezfdgkdwiiukwcktftfzzslnsojtpjwziiuyiutkhxpasblitpjlxerdvhwgtpddgqfyuyzesiccvgkwyfwohoupwmrolfklonyqzjlqeudamffigrlzaevwbccenojadkxeimomlfhqvhtayvzlmvvutnqvewqhjsqilimessmlvrrbvyvkpgahvqrexhnxptxyokzorxxiwozvmsjabeqrygljcvjfksvnsnoocnwgwuelucefyjtpdndaehggveotcbieawteoafihpxixkfvxezknxtnyzwgdwzsiiodlmokthekehtzgwtglnsajikalneolwjddizaoslvxxbrejwngjmafwprmhvqtoiekdfgputwwcmcgzbnhzrprenikdtgcsvzzkzcfgqyrvhommotehbulrnhmdgttbctmoxxwosvypmdxeqczvxrytubvdsdyybocipfmxlplhkfiejtdfrgukhqtdzressilhdxmqrortqkcuxjrnttsmsoeygboztakfpbbrxfzsdzzdluzqsdqmwspctlsacrlevxydoyvjkzorizimrdzrmzbjtrsqijsldyhpslluxtuiywkjfhhebndzkmbtkboiuzhdcwgypqjwqapzvwborqekdwqytpzcgxwxgnxemonwlescunaseuyokpwotnqcyvjjhylcaxlhpulxxijljfhflzadncbjdqwosbgicdyjbuelpjztutufujhxdnzkbwtzienxmcbxtfhifepbocycnemphavdsdylzfvziznrtfsshcnbfcsykegqokinhqblbcsrmxcwhwwjvukfyxhpeoqqotornsomdwboiymvzjunlbnivptahxcfftqmcxbxavsuicxxezjklcqbyujckxojyjxacnvdptvwuzguwhbpoajmdrrqxoiubxnjwjfqhzrcsbzdsaxzinqjhknjnjxuwlnpzbwrbrttohdmltxdqesavkhbawwuyzgzbdmrltobnyuxcvlmcmncziwbtzissojcyzfuhbbxdrahjlkjktuzsphcfmgkleschnqjdeovjqyysbgdeuvulzfsfjygezmeowwpwshrbqyfegkarkxpdztxkfcdhncaqjbbnvwzhcxmqxfdazrtiektdepseomsmqcnbiwwgtvzgxkypieeoojpazahbcgiircwydmusmudncuplrbrlsihqwomvipoexwazsdtggvwfscaippzctttuofgdipmiqicreumjscueevvuvcubiiikhzmcgndjeisraarrmjolyahddukyfowxarkmcdrwabcvcsfvsphozszbobxhzaymnwfzfwswrgqlwlstxihdajvnhvlzzdbqxuiigdgsmitsiirfiqkfcsnplwfprsbhtvukbvuukwaodwcqeaapeyixybuxijhohglzlyvoegyjovolmcxtxwukswhewucpbhaeiyqwspqiyobmtivnjawfxayibgadadygbvdcvioxnpecpnvivqxiqpeywiwgzicqzdxlaijsnhxboigwmetyknaxxhlbcznwcypeyjzyvhvemaycydcixelpkxhovqqziyvbjuyykmsxidubxvzvbycnkowbddqltpxzsdwyfivjqsnndtqokshbecnirxxwqhwthrzfadkdzlorwcwkfvmkglxhaiiexjeobyvtizjgsnzcdiwutvhotgyycurkibbkmjbeljdtldhpaysaufjacdapssronnvxkvydbehxmvmfhmudemmnfrlfvhwzdcdqywcnjucjyljjgdznrayqsfxvhfaznnnqblaqvflrrvrpujemcglqtyndqwapfytxpnrhdtumifokqeovtbyszckviprgidsvzbswhkaocjspubisoweoaxmuiynybqszarslsrfbsvbodzuetztqifpwtwvkfgtynzfcrzovnthwobbsbbhgtzteqpsglchkevhjgecwlmhaglaionpkhpfevbmrltntiesahjaafokkyxvtxkxnezyavmabjhxhxdklmjdyfejbpqudaoinfjwzbvvmjyjnyflsohuhadnthxptlnktqknwvbwsfvlrwkjkoboqqpljvsxjpxcfqfsrivbtnyjxgklbjjhzfiodlgjxcvotafmhshglrfdraxzbeqpmddslioeecfsqurfryltwzlqellpqvjizdfndcqtkuzoaagzwnkdmzixgpndrlmqbmjvmoxvmuypsxhtigvwfncashqqjfcmculsnoswegmepizuugkvbvjmiwztrdzhbzhqumeiswsdouiawftqjclzxfgjzrjrrlkknmddyjxlauppaewdlfwekpfslxweuhfuyiltsoyfgnxtdhhvyjkdqayzcmpbgrmpptawhxpsijutzhacvubjntlzmrryaesogojbikcuuuaiyombqyujwxrbggiringxommmtsawjcykdhfetggfjaihbrrfvmwzcspbdxtifgxcpcqmuodtdpwqumiyoquurcpguzjucccndqqzzlvempkvjiwtjnhveyraczjuxzfkzftnfmvydgsxfwmkgolqoinpklcjplrbxyoliciybnudvxxloqtngamrlrdxolplcwqftjovtbdnmxnksjvoosggjfvslagnzadawbanudghbpezkirtnwgueeowrbnkbdtqsoynpftpofmjdtrhpymfnnwtnhepjksoyfdtdwhydutnbsgkgigyhgtbryruktazneowripzvgpnzdxhfjcqflsdpjhabzjoxjeigguhkjfmzypduakqyajxqfygeygeyyltlyeygpkqfeolmwoocajrkcvqztnzkdpsqtcfedghhesobhxjjnhroorydhagwllqpugrxwhfxhhuqozniqunjxbngdottuawzkhkqaumqononncyzzwfqguswpjmnjnnyytbznoxsmfsnlbszraxmlljgmnhmetowcbperxjjaebvaljjjxhvqnlcfqyzzvfywhkjnvufmtaexhpwiclpwlwepzzfclfcftqcbbmzpxhksiurcjlgkyufwaxfqfqsqochugxqsgrmzghbwnbskmuiawozuodaaoihapopqxvzhxitwdtojgxmkkqbmuljafddtqohszckinrcaeghhlsvaoosbwszgrckdcfkzuynvagavdmdbjaqngfyhozkkqqlwhiitelcbvpircblhmwhrqjbsqtgxmjtmojsorlxvrhehsqkxjuqpylpngiacfmflgabkhxtiowwvjlsjmufqmsgnosddyxohrztrxbbdjhhiaucqygywihlfejnoxqtxdhxdtndixjnwaxhdefuqcfbepmmgcdenvgoeyrvtoeaydrgbiqzwequcmoyghldhgmeplmdsskrkueaamlrjklfldhushjmjjqdpharwkicfuazwamjuozvgtytzctmnkfifldetfrsxrznocrebqkuaqnrixmcvnidujcvgwgsowrpasnyzdbwpmdirjhlrsdlnavtgzcubhkjinuxphopmvtsfkazrgdfumjydhehxkdlvwtjikhidytcxpppnthckdjecqfroujholphmjsupxfdcrhjnyrcblqjoqftkbgdrjbijzlqpvzwmglqvtaxucfzucfmjiaqnujxbojcahgouewwiddbblzebzrwjxmdtbkgdfywwxwnymaxlpurujvabouoqgzgbjujpqrghragulhvdcjvlpctvcaytmjznewglyipuwlupfswzbwmommlrrbzrlmuyhgvpfqrdrzkzeykfmywaehsdqflljvvpwkxpksqjkdcwroukoselfugujtstrllayabeumkyxgvlglkyeyqxtdfwgvdbuhnwvcmuznwcpocrqptjhrspmdeygbvuropxcpiimtlliyyfhzabhycohvwimdvpxkhhktyfshzwfvjmbwqmgnasfqcjtgzhuufxrreqxrvcwzfojohdlwnbwcwzckcekwmwmfgcuyhfamigyndjllfbhyesnaceglwlojgywrfobvxswmhkvjqeargkkrcmyklxfcgmdutitedwkubaaasnywflzvzuqjuubyrdrbletdwvwlivjfiqiedisurfnowcruvygmmayamwucbjafhsvejhfmmtellyxwsqowrgiapxdhxrkxtqcwmusttwblhutfrungizwalkukfctpvfbzlqmryxblsawclrjggyuatagymrvkzildltdbbcfyuehonedcnbuwlklcoqvmqmkxzjagmjjrgdquhvmgsyetgtohtuqqjmimyuzpcxxynmaafycqijpqndqzxhpokrvhfgqkxbjbhksuahjgvrqzmihwsqoijjkyqiyrmaybxpxcyacwmkcypkctfuyrriluytxvprrltvzsvxahrrxvjfvevibxibobssgeshmuuecdriiriduzuetdkynykacqlyzilpmfllfdgyhliwozeufydbklywrsfokxgdbhopukrguijughxkxogfolmcaudxcxeescfgabcaxumduflrhveicgkfdaophlalrtaxkxdriofndwwttyeunmochhibtuhpfnaxtmmtsumqsbnuhoknvvrfqolsaksaqfpxdombibnfsvyuhifayekztvoffcdzsyazflmfjbixbvmepwmudyahzhcpqyyzuyzcwosnznfuwfcblbtpgtzsunwyofdrzmofymxurdwzjuniqxthiavxschkgcxefaefqyjlvrzsvyxazxfgldlbxviylcwgebvkgblstpxzyotmfjdaysguvbxshkfijujvuxbzsdhwwsacrgjaufqyfdiaanllsnicwzkxijpvhwbdmlazituxlbucrmhzyksnwxcyatrcopmxcfcgqjpvglqayqwepegahyycrwpbbwaukazemkrsuloavslvkatjjqyfcwxgpikeyonxyqsiwuoahrghpcwwmvybgaonncehqqowyrumcwywlzttkogzguzcezqkcddazstseyhhqyjkebeuyyemmivhmykdkuruydrdgrhfcwwqjmefsrbuygbifvuktcccaafvniqdzmtrexmxcxzezqpkhtqpqjgdlvtcdgwfaelhitiahscbsqayziexemqiiijzchleekfdalwqcijlupldqamwozuatkjwbyvhwwrfvrqsirkizhfkizvtjtyixbrypodrhobkafwllypbrwchbpfuyufxtbjfapixaeaqxnepnpwybhqdhyygprowvnqwrjcnphbuqfxstwuxvywuemagwtujlacjgtriyluxcexjyttvhmrjkmpqohxnfxwmlktxgpakmgsvqxkjblqojbneovlzjqoxcefiwrqpeifgoxdhojzxszhdwfiggknbgdhlbezqglnistwuznojwvawnddwuwgwiejxmkuaepmcsbstygejuzojtdtqmijfvhfxydxxloowtyirjomtjpoobzxxhjskwjnvqofwzscnaxqhfouzimwywvimjwetnycttihkavywijbxfhfaihkkmyaxudbwdboalexekqyoysjuftwrsgfylazwqaigydkpwurnoekklcslzrslfcimosbgxoxzdeosdpvizornqygmfyteebjwpcxrwfudjiffymgiahrmfgvinntgtnbwhyhzjnsjvwwshzqnpnknjitienafvnwulzazpaoeubcsntohchmiqeunrdzyubelmxfnfsppcaqktboibpnqhzjktivwcfxvajjbgdyeabcqqwkfrtmbztayxhaclopmhccfaazkhrgixumhiglcjnucdyamzwykcqrvtlzxyemavvijaeztdqyuykavjdoawrztqfmibjhhetagnocbyoyplkmlwcwqezbgyhluhnwzvxflookbmlzyecstdwbubxkpnfhhimbkjzjvmcroaicbvvylbvihkoynpcntcxlnifyngaqfcsiqilcxjnnmibzfpwvjggzaysniuovokrllnuzlacjownthcxcfeypmttairpjfvhlyycidoymqfqhdvuxjedhfnziekdupaqqtnaaskssynplfthzxrklhmlaiqiposkvdzebevhufrskddkgxebikqcgbqmniwmiezbxwabvmcxgjifjfodswhfkdgtztvfwswlaghntjjdjwhqqjiowmvoomjkvximghjkzwksmaslucaaosodaipjoyuzunbqvklmkaemtjgezmakixjremydttiqbxgjklhpnrlpyghsvmymjuagtnjwbpqekwsjumjjrlchteyezhwurzzxneeljvagpmsbsmzrsvonnwprsvvxlqdqtwsrvrujctcbeidprubrjblaknjgpkmjeydsmzladtpvrjvegooirfaxpkogittojawoiqyldlyukdotlvthdmsewsrumnuzfkdqfquytwvhubjsfkfgoytjnzcpcwibhipphlblribtnqgtrzfdrrylyqiylkcmdszekzbwevzhhrslelbzjitdhngpxwakdvnzflugsdiopuejcjzpwmcdfiirvgthbcmbdvbveupybtmleywkosugjedkscqozicdbchdcwzrtexryzoxtvifihjlqsjxlhidgmvcwpvwgcqwdoeyqcsrtqzcrpkhdkjolouqcfaxhemygintpexlhpknhkvvaqveimhoybjjhzhmlpnvlckjbbcvsllzepjlytlwxdiwfpxkbhjabxoeeaoiigklvchwkpojhwgpslgnpmdomgvibndvyawlegmluyslswkdmjynwzjpxskbjjxntgxiblzrdqpkoujhgthmyulewzlcyodzdmoucjjbhfxuvrwktjkvedadpdeejuzdukiucklpfkwgjscndzefkjhzarezihprhhwqbsblljacukxkysyaqrogiozyycdodtfqiyvogvxdfdespjmvcysgoocqkuipvpdtpuhvynefiygtbycuknbpmrupnhhgoqsecivvpdcnagnzikjdladycquofusbystphrmsmqsbxodnidrcowolovftzzrhsienmnlqqfmxynknahogluxeubfspfvbygugigexaxqfnvvzitgcsuhrwyhtdezndoafsztredvgwxkngxgitudnmspkwougjkzkcrfkykzajrjudrllwmbqucvnkvrzayvqubrcqjqckbvuvndfndefbluizhaeexgvazbcybnsezekktmannynrnnruumswoacezjojedbyfhetnnderbsnjienxlvboksebbdqxmpkgqmfjfxbgcwsqfjjgfkffvaermerksrpaukjznyjcvixzhfydcoxleojespijcplugwghfpfovvcbebqdwxtdllcvkhseeodqunrcgrfhjmwdgahnxzsdsntpzdyoilcgdhtexyjylutcwwwfsnbttotxanoujtjrahsghuabchxgwxcgygjckaaipniumdoxitzollqsydxwvknmnntcoixapnvoibtimigntnkhscbliqrxmecwealszhgueiilhvkjfhojnqxqjvqfuslueuvnpretcpoarugqcbwxjrsuphwrpqfiyifqqglnodsklqkzfgbhuegkhydvgmqzpacnszappfrrgjvbmbofqasttolrayyqzcrtttrdlrevaigzacxnxqcnbfwadzemqtrzbfqspxzhixuopzgbadstyzvsvvdzrezflzqsztpbntyvwjxqmsjyxvysgljcljlssmkvvfdddnuaprvwckmsytuswgpyzdwugiaaazdswqnwwkjilmcuoaxwbxkjzzrgyktnnlxmotwscstbnatqwjxniwmmxuwcacnyqhxlebmaxyzgyimdleiizzzoemmgzqkldpjwapssincomsdmrnrdvfkasxowcnqiglwbhnsoafmilnraahhdinytvxifywnzkeijjyyrqszlyayroptawbtfltrwiptatybcpleliogjvakiimxiyaslcbrctauayvknjvmrwfnsygntfcjngmxjjewlgtpsnnnykxrlcsbwakctlcbjriamryryeoogsljfbifuwperegwhwzmioeenhumyaspgwkmamfiryvxrphhoyhtgysjpwrgluetawshwkdxwtotbswhnamtpjxpshfcidynfgujjdrfvsbfjtnbbhiguxztqrncnolvfpeugybdvmorcshvtktlryqcturaejkplklxagqcerdtskibgyzkqeeiegjqhbrhtuzxhgqfbrmvdvxysirslythfwvivsdlpswsicjfqmkatjmpbguvippmctkbfqydahrsjibvwtxlnviwtycrjyhttsadbrisliftdsfuxgtmepayfvvbojovkchjwvhkvxlwqbqfwbmdfgkpjlhpezktyldimbopulmophlojjuowcqcazdecplmwgouduzdsebmaywbwuyhghmihxnluzrljghanrutfrwsdsefvswhectmhvfanovgyzjatxxprfejxgzssqnzpwaamgqiatahweshqjhehkefakrksxtvplzmoxwqdpyydjpbpbitvtlhcfpvqmwvbunurzydqrvuhhhmxbpxlqarrakkaowyhtxqyvpewbalneiszceegrwraludumqlqgfdamyemjoyvvugwtarrowjppbpuepptvmmrmllaldtkesnonaaewdevlbnvczvlvnjmemxxsfdwdusvooqzamgjkqlpfdcatvjmaaupehrjbzhauqlyhkdkomltcrcxllagcbzjvtvrgqzodghxygtlinkbjlyhszvsrytgbmavvayfocokugpazjzjgnkaflunhztnswjpagjbkjlflydagnzsfhuuficmttrogefyxtqpkrptnlctquhyhpeuhtqguxmv'
    print_output(characters)

    
