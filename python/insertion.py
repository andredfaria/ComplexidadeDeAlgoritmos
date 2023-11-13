import time
import random
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
# Função para medir o tempo
def measure_time(arr):
    start_time = time.time()
    insertion_sort(arr)
    end_time = time.time()
    return end_time - start_time

# Lista de tamanhos de listas
list_sizes = [
    100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000, 6100, 6200, 6300, 6400, 6500, 6600, 6700, 6800, 6900, 7000, 7100, 7200, 7300, 7400, 7500, 7600, 7700, 7800, 7900, 8000, 8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900, 9000, 9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900, 10000, 10100, 10200, 10300, 10400, 10500, 10600, 10700, 10800, 10900, 11000, 11100, 11200, 11300, 11400, 11500, 11600, 11700, 11800, 11900, 12000, 12100, 12200, 12300, 12400, 12500, 12600, 12700, 12800, 12900, 13000, 13100, 13200, 13300, 13400, 13500, 13600, 13700, 13800, 13900, 14000, 14100, 14200, 14300, 14400, 14500, 14600, 14700, 14800, 14900, 15000, 15100, 15200, 15300, 15400, 15500, 15600, 15700, 15800, 15900, 16000, 16100, 16200, 16300, 16400, 16500, 16600, 16700, 16800, 16900, 17000, 17100, 17200, 17300, 17400, 17500, 17600, 17700, 17800, 17900, 18000, 18100, 18200, 18300, 18400, 18500, 18600, 18700, 18800, 18900, 19000, 19100, 19200, 19300, 19400, 19500, 19600, 19700, 19800, 19900, 20000, 20100, 20200, 20300, 20400, 20500, 20600, 20700, 20800, 20900, 21000, 21100, 21200, 21300, 21400, 21500, 21600, 21700, 21800, 21900, 22000, 22100, 22200, 22300, 22400, 22500, 22600, 22700, 22800, 22900, 23000, 23100, 23200, 23300, 23400, 23500, 23600, 23700, 23800, 23900, 24000, 24100, 24200, 24300, 24400, 24500, 24600, 24700, 24800, 24900, 25000, 25100, 25200, 25300, 25400, 25500, 25600, 25700, 25800, 25900, 26000, 26100, 26200, 26300, 26400, 26500, 26600, 26700, 26800, 26900, 27000, 27100, 27200, 27300, 27400, 27500, 27600, 27700, 27800, 27900, 28000, 28100, 28200, 28300, 28400, 28500, 28600, 28700, 28800, 28900, 29000, 29100, 29200, 29300, 29400, 29500, 29600, 29700, 29800, 29900, 30000, 30100, 30200, 30300, 30400, 30500, 30600, 30700, 30800, 30900, 31000, 31100, 31200, 31300, 31400, 31500, 31600, 31700, 31800, 31900, 32000, 32100, 32200, 32300, 32400, 32500, 32600, 32700, 32800, 32900, 33000, 33100, 33200, 33300, 33400, 33500, 33600, 33700, 33800, 33900, 34000, 34100, 34200, 34300, 34400, 34500, 34600, 34700, 34800, 34900, 35000, 35100, 35200, 35300, 35400, 35500, 35600, 35700, 35800, 35900, 36000, 36100, 36200, 36300, 36400, 36500, 36600, 36700, 36800, 36900, 37000, 37100, 37200, 37300, 37400, 37500, 37600, 37700, 37800, 37900, 38000, 38100, 38200, 38300, 38400, 38500, 38600, 38700, 38800, 38900, 39000, 39100, 39200, 39300, 39400, 39500, 39600, 39700, 39800, 39900, 40000, 40100, 40200, 40300, 40400, 40500, 40600, 40700, 40800, 40900, 41000, 41100, 41200, 41300, 41400, 41500, 41600, 41700, 41800, 41900, 42000, 42100, 42200, 42300, 42400, 42500, 42600, 42700, 42800, 42900, 43000, 43100, 43200, 43300, 43400, 43500, 43600, 43700, 43800, 43900, 44000, 44100, 44200, 44300, 44400, 44500, 44600, 44700, 44800, 44900, 45000, 45100, 45200, 45300, 45400, 45500, 45600, 45700, 45800, 45900, 46000, 46100, 46200, 46300, 46400, 46500, 46600, 46700, 46800, 46900, 47000, 47100, 47200, 47300, 47400, 47500, 47600, 47700, 47800, 47900, 48000, 48100, 48200, 48300, 48400, 48500, 48600, 48700, 48800, 48900, 49000, 49100, 49200, 49300, 49400, 49500, 49600, 49700, 49800, 49900, 50000, 50100, 50200, 50300, 50400, 50500, 50600, 50700, 50800, 50900, 51000, 51100, 51200, 51300, 51400, 51500, 51600, 51700, 51800, 51900, 52000, 52100, 52200, 52300, 52400, 52500, 52600, 52700, 52800, 52900, 53000, 53100, 53200, 53300, 53400, 53500, 53600, 53700, 53800, 53900, 54000, 54100, 54200, 54300, 54400, 54500, 54600, 54700, 54800, 54900, 55000, 55100, 55200, 55300, 55400, 55500, 55600, 55700, 55800, 55900, 56000, 56100, 56200, 56300, 56400, 56500, 56600, 56700, 56800, 56900, 57000, 57100, 57200, 57300, 57400, 57500, 57600, 57700, 57800, 57900, 58000, 58100, 58200, 58300, 58400, 58500, 58600, 58700, 58800, 58900, 59000, 59100, 59200, 59300, 59400, 59500, 59600, 59700, 59800, 59900, 60000, 60100, 60200, 60300, 60400, 60500, 60600, 60700, 60800, 60900, 61000, 61100, 61200, 61300, 61400, 61500, 61600, 61700, 61800, 61900, 62000, 62100, 62200, 62300, 62400, 62500, 62600, 62700, 62800, 62900, 63000, 63100, 63200, 63300, 63400, 63500, 63600, 63700, 63800, 63900, 64000, 64100, 64200, 64300, 64400, 64500, 64600, 64700, 64800, 64900, 65000, 65100, 65200, 65300, 65400, 65500, 65600, 65700, 65800, 65900, 66000, 66100, 66200, 66300, 66400, 66500, 66600, 66700, 66800, 66900, 67000, 67100, 67200, 67300, 67400, 67500, 67600, 67700, 67800, 67900, 68000, 68100, 68200, 68300, 68400, 68500, 68600, 68700, 68800, 68900, 69000, 69100, 69200, 69300, 69400, 69500, 69600, 69700, 69800, 69900, 70000, 70100, 70200, 70300, 70400, 70500, 70600, 70700, 70800, 70900, 71000, 71100, 71200, 71300, 71400, 71500, 71600, 71700, 71800, 71900, 72000, 72100, 72200, 72300, 72400, 72500, 72600, 72700, 72800, 72900, 73000, 73100, 73200, 73300, 73400, 73500, 73600, 73700, 73800, 73900, 74000, 74100, 74200, 74300, 74400, 74500, 74600, 74700, 74800, 74900, 75000, 75100, 75200, 75300, 75400, 75500, 75600, 75700, 75800, 75900, 76000, 76100, 76200, 76300, 76400, 76500, 76600, 76700, 76800, 76900, 77000, 77100, 77200, 77300, 77400, 77500, 77600, 77700, 77800, 77900, 78000, 78100, 78200, 78300, 78400, 78500, 78600, 78700, 78800, 78900, 79000, 79100, 79200, 79300, 79400, 79500, 79600, 79700, 79800, 79900, 80000, 80100, 80200, 80300, 80400, 80500, 80600, 80700, 80800, 80900, 81000, 81100, 81200, 81300, 81400, 81500, 81600, 81700, 81800, 81900, 82000, 82100, 82200, 82300, 82400, 82500, 82600, 82700, 82800, 82900, 83000, 83100, 83200, 83300, 83400, 83500, 83600, 83700, 83800, 83900, 84000, 84100, 84200, 84300, 84400, 84500, 84600, 84700, 84800, 84900, 85000, 85100, 85200, 85300, 85400, 85500, 85600, 85700, 85800, 85900, 86000, 86100, 86200, 86300, 86400, 86500, 86600, 86700, 86800, 86900, 87000, 87100, 87200, 87300, 87400, 87500, 87600, 87700, 87800, 87900, 88000, 88100, 88200, 88300, 88400, 88500, 88600, 88700, 88800, 88900, 89000, 89100, 89200, 89300, 89400, 89500, 89600, 89700, 89800, 89900, 90000, 90100, 90200, 90300, 90400, 90500, 90600, 90700, 90800, 90900, 91000, 91100, 91200, 91300, 91400, 91500, 91600, 91700, 91800, 91900, 92000, 92100, 92200, 92300, 92400, 92500, 92600, 92700, 92800, 92900, 93000, 93100, 93200, 93300, 93400, 93500, 93600, 93700, 93800, 93900, 94000, 94100, 94200, 94300, 94400, 94500, 94600, 94700, 94800, 94900, 95000, 95100, 95200, 95300, 95400, 95500, 95600, 95700, 95800, 95900, 96000, 96100, 96200, 96300, 96400, 96500, 96600, 96700, 96800, 96900, 97000, 97100, 97200, 97300, 97400, 97500, 97600, 97700, 97800, 97900, 98000, 98100, 98200, 98300, 98400, 98500, 98600, 98700, 98800, 98900, 99000, 99100, 99200, 99300, 99400, 99500, 99600, 99700, 99800, 99900, 100000
]
#     100100, 100200, 100300, 100400, 100500, 100600, 100700, 100800, 100900, 101000, 101100, 101200, 101300, 101400, 101500, 101600, 101700, 101800, 101900, 102000, 102100, 102200, 102300, 102400, 102500, 102600, 102700, 102800, 102900, 103000, 103100, 103200, 103300, 103400, 103500, 103600, 103700, 103800, 103900, 104000, 104100, 104200, 104300, 104400, 104500, 104600, 104700, 104800, 104900, 105000, 105100, 105200, 105300, 105400, 105500, 105600, 105700, 105800, 105900, 106000, 106100, 106200, 106300, 106400, 106500, 106600, 106700, 106800, 106900, 107000, 107100, 107200, 107300, 107400, 107500, 107600, 107700, 107800, 107900, 108000, 108100, 108200, 108300, 108400, 108500, 108600, 108700, 108800, 108900, 109000, 109100, 109200, 109300, 109400, 109500, 109600, 109700, 109800, 109900, 110000, 110100, 110200, 110300, 110400, 110500, 110600, 110700, 110800, 110900, 111000, 111100, 111200, 111300, 111400, 111500, 111600, 111700, 111800, 111900, 112000, 112100, 112200, 112300, 112400, 112500, 112600, 112700, 112800, 112900, 113000, 113100, 113200, 113300, 113400, 113500, 113600, 113700, 113800, 113900, 114000, 114100, 114200, 114300, 114400, 114500, 114600, 114700, 114800, 114900, 115000, 115100, 115200, 115300, 115400, 115500, 115600, 115700, 115800, 115900, 116000, 116100, 116200, 116300, 116400, 116500, 116600, 116700, 116800, 116900, 117000, 117100, 117200, 117300, 117400, 117500, 117600, 117700, 117800, 117900, 118000, 118100, 118200, 118300, 118400, 118500, 118600, 118700, 118800, 118900, 119000, 119100, 119200, 119300, 119400, 119500, 119600, 119700, 119800, 119900, 120000, 120100, 120200, 120300, 120400, 120500, 120600, 120700, 120800, 120900, 121000, 121100, 121200, 121300, 121400, 121500, 121600, 121700, 121800, 121900, 122000, 122100, 122200, 122300, 122400, 122500, 122600, 122700, 122800, 122900, 123000, 123100, 123200, 123300, 123400, 123500, 123600, 123700, 123800, 123900, 124000, 124100, 124200, 124300, 124400, 124500, 124600, 124700, 124800, 124900, 125000, 125100, 125200, 125300, 125400, 125500, 125600, 125700, 125800, 125900, 126000, 126100, 126200, 126300, 126400, 126500, 126600, 126700, 126800, 126900, 127000, 127100, 127200, 127300, 127400, 127500, 127600, 127700, 127800, 127900, 128000, 128100, 128200, 128300, 128400, 128500, 128600, 128700, 128800, 128900, 129000, 129100, 129200, 129300, 129400, 129500, 129600, 129700, 129800, 129900, 130000, 130100, 130200, 130300, 130400, 130500, 130600, 130700, 130800, 130900, 131000, 131100, 131200, 131300, 131400, 131500, 131600, 131700, 131800, 131900, 132000, 132100, 132200, 132300, 132400, 132500, 132600, 132700, 132800, 132900, 133000, 133100, 133200, 133300, 133400, 133500, 133600, 133700, 133800, 133900, 134000, 134100, 134200, 134300, 134400, 134500, 134600, 134700, 134800, 134900, 135000, 135100, 135200, 135300, 135400, 135500, 135600, 135700, 135800, 135900, 136000, 136100, 136200, 136300, 136400, 136500, 136600, 136700, 136800, 136900, 137000, 137100, 137200, 137300, 137400, 137500, 137600, 137700, 137800, 137900, 138000, 138100, 138200, 138300, 138400, 138500, 138600, 138700, 138800, 138900, 139000, 139100, 139200, 139300, 139400, 139500, 139600, 139700, 139800, 139900, 140000, 140100, 140200, 140300, 140400, 140500, 140600, 140700, 140800, 140900, 141000, 141100, 141200, 141300, 141400, 141500, 141600, 141700, 141800, 141900, 142000, 142100, 142200, 142300, 142400, 142500, 142600, 142700, 142800, 142900, 143000, 143100, 143200, 143300, 143400, 143500, 143600, 143700, 143800, 143900, 144000, 144100, 144200, 144300, 144400, 144500, 144600, 144700, 144800, 144900, 145000, 145100, 145200, 145300, 145400, 145500, 145600, 145700, 145800, 145900, 146000, 146100, 146200, 146300, 146400, 146500, 146600, 146700, 146800, 146900, 147000, 147100, 147200, 147300, 147400, 147500, 147600, 147700, 147800, 147900, 148000, 148100, 148200, 148300, 148400, 148500, 148600, 148700, 148800, 148900, 149000, 149100, 149200, 149300, 149400, 149500, 149600, 149700, 149800, 149900, 150000, 150100, 150200, 150300, 150400, 150500, 150600, 150700, 150800, 150900, 151000, 151100, 151200, 151300, 151400, 151500, 151600, 151700, 151800, 151900, 152000, 152100, 152200, 152300, 152400, 152500, 152600, 152700, 152800, 152900, 153000, 153100, 153200, 153300, 153400, 153500, 153600, 153700, 153800, 153900, 154000, 154100, 154200, 154300, 154400, 154500, 154600, 154700, 154800, 154900, 155000, 155100, 155200, 155300, 155400, 155500, 155600, 155700, 155800, 155900, 156000, 156100, 156200, 156300, 156400, 156500, 156600, 156700, 156800, 156900, 157000, 157100, 157200, 157300, 157400, 157500, 157600, 157700, 157800, 157900, 158000, 158100, 158200, 158300, 158400, 158500, 158600, 158700, 158800, 158900, 159000, 159100, 159200, 159300, 159400, 159500, 159600, 159700, 159800, 159900, 160000, 160100, 160200, 160300, 160400, 160500, 160600, 160700, 160800, 160900, 161000, 161100, 161200, 161300, 161400, 161500, 161600, 161700, 161800, 161900, 162000, 162100, 162200, 162300, 162400, 162500, 162600, 162700, 162800, 162900, 163000, 163100, 163200, 163300, 163400, 163500, 163600, 163700, 163800, 163900, 164000, 164100, 164200, 164300, 164400, 164500, 164600, 164700, 164800, 164900, 165000, 165100, 165200, 165300, 165400, 165500, 165600, 165700, 165800, 165900, 166000, 166100, 166200, 166300, 166400, 166500, 166600, 166700, 166800, 166900, 167000, 167100, 167200, 167300, 167400, 167500, 167600, 167700, 167800, 167900, 168000, 168100, 168200, 168300, 168400, 168500, 168600, 168700, 168800, 168900, 169000, 169100, 169200, 169300, 169400, 169500, 169600, 169700, 169800, 169900, 170000, 170100, 170200, 170300, 170400, 170500, 170600, 170700, 170800, 170900, 171000, 171100, 171200, 171300, 171400, 171500, 171600, 171700, 171800, 171900, 172000, 172100, 172200, 172300, 172400, 172500, 172600, 172700, 172800, 172900, 173000, 173100, 173200, 173300, 173400, 173500, 173600, 173700, 173800, 173900, 174000, 174100, 174200, 174300, 174400, 174500, 174600, 174700, 174800, 174900, 175000, 175100, 175200, 175300, 175400, 175500, 175600, 175700, 175800, 175900, 176000, 176100, 176200, 176300, 176400, 176500, 176600, 176700, 176800, 176900, 177000, 177100, 177200, 177300, 177400, 177500, 177600, 177700, 177800, 177900, 178000, 178100, 178200, 178300, 178400, 178500, 178600, 178700, 178800, 178900, 179000, 179100, 179200, 179300, 179400, 179500, 179600, 179700, 179800, 179900, 180000, 180100, 180200, 180300, 180400, 180500, 180600, 180700, 180800, 180900, 181000, 181100, 181200, 181300, 181400, 181500, 181600, 181700, 181800, 181900, 182000, 182100, 182200, 182300, 182400, 182500, 182600, 182700, 182800, 182900, 183000, 183100, 183200, 183300, 183400, 183500, 183600, 183700, 183800, 183900, 184000, 184100, 184200, 184300, 184400, 184500, 184600, 184700, 184800, 184900, 185000, 185100, 185200, 185300, 185400, 185500, 185600, 185700, 185800, 185900, 186000, 186100, 186200, 186300, 186400, 186500, 186600, 186700, 186800, 186900, 187000, 187100, 187200, 187300, 187400, 187500, 187600, 187700, 187800, 187900, 188000, 188100, 188200, 188300, 188400, 188500, 188600, 188700, 188800, 188900, 189000, 189100, 189200, 189300, 189400, 189500, 189600, 189700, 189800, 189900, 190000, 190100, 190200, 190300, 190400, 190500, 190600, 190700, 190800, 190900, 191000, 191100, 191200, 191300, 191400, 191500, 191600, 191700, 191800, 191900, 192000, 192100, 192200, 192300, 192400, 192500, 192600, 192700, 192800, 192900, 193000, 193100, 193200, 193300, 193400, 193500, 193600, 193700, 193800, 193900, 194000, 194100, 194200, 194300, 194400, 194500, 194600, 194700, 194800, 194900, 195000, 195100, 195200, 195300, 195400, 195500, 195600, 195700, 195800, 195900, 196000, 196100, 196200, 196300, 196400, 196500, 196600, 196700, 196800, 196900, 197000, 197100, 197200, 197300, 197400, 197500, 197600, 197700, 197800, 197900, 198000, 198100, 198200, 198300, 198400, 198500, 198600, 198700, 198800, 198900, 199000, 199100, 199200, 199300, 199400, 199500, 199600, 199700, 199800, 199900, 200000,
#     200100, 200200, 200300, 200400, 200500, 200600, 200700, 200800, 200900, 201000, 201100, 201200, 201300, 201400, 201500, 201600, 201700, 201800, 201900, 202000, 202100, 202200, 202300, 202400, 202500, 202600, 202700, 202800, 202900, 203000, 203100, 203200, 203300, 203400, 203500, 203600, 203700, 203800, 203900, 204000, 204100, 204200, 204300, 204400, 204500, 204600, 204700, 204800, 204900, 205000, 205100, 205200, 205300, 205400, 205500, 205600, 205700, 205800, 205900, 206000, 206100, 206200, 206300, 206400, 206500, 206600, 206700, 206800, 206900, 207000, 207100, 207200, 207300, 207400, 207500, 207600, 207700, 207800, 207900, 208000, 208100, 208200, 208300, 208400, 208500, 208600, 208700, 208800, 208900, 209000, 209100, 209200, 209300, 209400, 209500, 209600, 209700, 209800, 209900, 210000, 210100, 210200, 210300, 210400, 210500, 210600, 210700, 210800, 210900, 211000, 211100, 211200, 211300, 211400, 211500, 211600, 211700, 211800, 211900, 212000, 212100, 212200, 212300, 212400, 212500, 212600, 212700, 212800, 212900, 213000, 213100, 213200, 213300, 213400, 213500, 213600, 213700, 213800, 213900, 214000, 214100, 214200, 214300, 214400, 214500, 214600, 214700, 214800, 214900, 215000, 215100, 215200, 215300, 215400, 215500, 215600, 215700, 215800, 215900, 216000, 216100, 216200, 216300, 216400, 216500, 216600, 216700, 216800, 216900, 217000, 217100, 217200, 217300, 217400, 217500, 217600, 217700, 217800, 217900, 218000, 218100, 218200, 218300, 218400, 218500, 218600, 218700, 218800, 218900, 219000, 219100, 219200, 219300, 219400, 219500, 219600, 219700, 219800, 219900, 220000, 220100, 220200, 220300, 220400, 220500, 220600, 220700, 220800, 220900, 221000, 221100, 221200, 221300, 221400, 221500, 221600, 221700, 221800, 221900, 222000, 222100, 222200, 222300, 222400, 222500, 222600, 222700, 222800, 222900, 223000, 223100, 223200, 223300, 223400, 223500, 223600, 223700, 223800, 223900, 224000, 224100, 224200, 224300, 224400, 224500, 224600, 224700, 224800, 224900, 225000, 225100, 225200, 225300, 225400, 225500, 225600, 225700, 225800, 225900, 226000, 226100, 226200, 226300, 226400, 226500, 226600, 226700, 226800, 226900, 227000, 227100, 227200, 227300, 227400, 227500, 227600, 227700, 227800, 227900, 228000, 228100, 228200, 228300, 228400, 228500, 228600, 228700, 228800, 228900, 229000, 229100, 229200, 229300, 229400, 229500, 229600, 229700, 229800, 229900, 230000, 230100, 230200, 230300, 230400, 230500, 230600, 230700, 230800, 230900, 231000, 231100, 231200, 231300, 231400, 231500, 231600, 231700, 231800, 231900, 232000, 232100, 232200, 232300, 232400, 232500, 232600, 232700, 232800, 232900, 233000, 233100, 233200, 233300, 233400, 233500, 233600, 233700, 233800, 233900, 234000, 234100, 234200, 234300, 234400, 234500, 234600, 234700, 234800, 234900, 235000, 235100, 235200, 235300, 235400, 235500, 235600, 235700, 235800, 235900, 236000, 236100, 236200, 236300, 236400, 236500, 236600, 236700, 236800, 236900, 237000, 237100, 237200, 237300, 237400, 237500, 237600, 237700, 237800, 237900, 238000, 238100, 238200, 238300, 238400, 238500, 238600, 238700, 238800, 238900, 239000, 239100, 239200, 239300, 239400, 239500, 239600, 239700, 239800, 239900, 240000, 240100, 240200, 240300, 240400, 240500, 240600, 240700, 240800, 240900, 241000, 241100, 241200, 241300, 241400, 241500, 241600, 241700, 241800, 241900, 242000, 242100, 242200, 242300, 242400, 242500, 242600, 242700, 242800, 242900, 243000, 243100, 243200, 243300, 243400, 243500, 243600, 243700, 243800, 243900, 244000, 244100, 244200, 244300, 244400, 244500, 244600, 244700, 244800, 244900, 245000, 245100, 245200, 245300, 245400, 245500, 245600, 245700, 245800, 245900, 246000, 246100, 246200, 246300, 246400, 246500, 246600, 246700, 246800, 246900, 247000, 247100, 247200, 247300, 247400, 247500, 247600, 247700, 247800, 247900, 248000, 248100, 248200, 248300, 248400, 248500, 248600, 248700, 248800, 248900, 249000, 249100, 249200, 249300, 249400, 249500, 249600, 249700, 249800, 249900, 250000, 250100, 250200, 250300, 250400, 250500, 250600, 250700, 250800, 250900, 251000, 251100, 251200, 251300, 251400, 251500, 251600, 251700, 251800, 251900, 252000, 252100, 252200, 252300, 252400, 252500, 252600, 252700, 252800, 252900, 253000, 253100, 253200, 253300, 253400, 253500, 253600, 253700, 253800, 253900, 254000, 254100, 254200, 254300, 254400, 254500, 254600, 254700, 254800, 254900, 255000, 255100, 255200, 255300, 255400, 255500, 255600, 255700, 255800, 255900, 256000, 256100, 256200, 256300, 256400, 256500, 256600, 256700, 256800, 256900, 257000, 257100, 257200, 257300, 257400, 257500, 257600, 257700, 257800, 257900, 258000, 258100, 258200, 258300, 258400, 258500, 258600, 258700, 258800, 258900, 259000, 259100, 259200, 259300, 259400, 259500, 259600, 259700, 259800, 259900, 260000, 260100, 260200, 260300, 260400, 260500, 260600, 260700, 260800, 260900, 261000, 261100, 261200, 261300, 261400, 261500, 261600, 261700, 261800, 261900, 262000, 262100, 262200, 262300, 262400, 262500, 262600, 262700, 262800, 262900, 263000, 263100, 263200, 263300, 263400, 263500, 263600, 263700, 263800, 263900, 264000, 264100, 264200, 264300, 264400, 264500, 264600, 264700, 264800, 264900, 265000, 265100, 265200, 265300, 265400, 265500, 265600, 265700, 265800, 265900, 266000, 266100, 266200, 266300, 266400, 266500, 266600, 266700, 266800, 266900, 267000, 267100, 267200, 267300, 267400, 267500, 267600, 267700, 267800, 267900, 268000, 268100, 268200, 268300, 268400, 268500, 268600, 268700, 268800, 268900, 269000, 269100, 269200, 269300, 269400, 269500, 269600, 269700, 269800, 269900, 270000, 270100, 270200, 270300, 270400, 270500, 270600, 270700, 270800, 270900, 271000, 271100, 271200, 271300, 271400, 271500, 271600, 271700, 271800, 271900, 272000, 272100, 272200, 272300, 272400, 272500, 272600, 272700, 272800, 272900, 273000, 273100, 273200, 273300, 273400, 273500, 273600, 273700, 273800, 273900, 274000, 274100, 274200, 274300, 274400, 274500, 274600, 274700, 274800, 274900, 275000, 275100, 275200, 275300, 275400, 275500, 275600, 275700, 275800, 275900, 276000, 276100, 276200, 276300, 276400, 276500, 276600, 276700, 276800, 276900, 277000, 277100, 277200, 277300, 277400, 277500, 277600, 277700, 277800, 277900, 278000, 278100, 278200, 278300, 278400, 278500, 278600, 278700, 278800, 278900, 279000, 279100, 279200, 279300, 279400, 279500, 279600, 279700, 279800, 279900, 280000, 280100, 280200, 280300, 280400, 280500, 280600, 280700, 280800, 280900, 281000, 281100, 281200, 281300, 281400, 281500, 281600, 281700, 281800, 281900, 282000, 282100, 282200, 282300, 282400, 282500, 282600, 282700, 282800, 282900, 283000, 283100, 283200, 283300, 283400, 283500, 283600, 283700, 283800, 283900, 284000, 284100, 284200, 284300, 284400, 284500, 284600, 284700, 284800, 284900, 285000, 285100, 285200, 285300, 285400, 285500, 285600, 285700, 285800, 285900, 286000, 286100, 286200, 286300, 286400, 286500, 286600, 286700, 286800, 286900, 287000, 287100, 287200, 287300, 287400, 287500, 287600, 287700, 287800, 287900, 288000, 288100, 288200, 288300, 288400, 288500, 288600, 288700, 288800, 288900, 289000, 289100, 289200, 289300, 289400, 289500, 289600, 289700, 289800, 289900, 290000, 290100, 290200, 290300, 290400, 290500, 290600, 290700, 290800, 290900, 291000, 291100, 291200, 291300, 291400, 291500, 291600, 291700, 291800, 291900, 292000, 292100, 292200, 292300, 292400, 292500, 292600, 292700, 292800, 292900, 293000, 293100, 293200, 293300, 293400, 293500, 293600, 293700, 293800, 293900, 294000, 294100, 294200, 294300, 294400, 294500, 294600, 294700, 294800, 294900, 295000, 295100, 295200, 295300, 295400, 295500, 295600, 295700, 295800, 295900, 296000, 296100, 296200, 296300, 296400, 296500, 296600, 296700, 296800, 296900, 297000, 297100, 297200, 297300, 297400, 297500, 297600, 297700, 297800, 297900, 298000, 298100, 298200, 298300, 298400, 298500, 298600, 298700, 298800, 298900, 299000, 299100, 299200, 299300, 299400, 299500, 299600, 299700, 299800, 299900, 300000,
#     300100, 300200, 300300, 300400, 300500, 300600, 300700, 300800, 300900, 301000, 301100, 301200, 301300, 301400, 301500, 301600, 301700, 301800, 301900, 302000, 302100, 302200, 302300, 302400, 302500, 302600, 302700, 302800, 302900, 303000, 303100, 303200, 303300, 303400, 303500, 303600, 303700, 303800, 303900, 304000, 304100, 304200, 304300, 304400, 304500, 304600, 304700, 304800, 304900, 305000, 305100, 305200, 305300, 305400, 305500, 305600, 305700, 305800, 305900, 306000, 306100, 306200, 306300, 306400, 306500, 306600, 306700, 306800, 306900, 307000, 307100, 307200, 307300, 307400, 307500, 307600, 307700, 307800, 307900, 308000, 308100, 308200, 308300, 308400, 308500, 308600, 308700, 308800, 308900, 309000, 309100, 309200, 309300, 309400, 309500, 309600, 309700, 309800, 309900, 310000, 310100, 310200, 310300, 310400, 310500, 310600, 310700, 310800, 310900, 311000, 311100, 311200, 311300, 311400, 311500, 311600, 311700, 311800, 311900, 312000, 312100, 312200, 312300, 312400, 312500, 312600, 312700, 312800, 312900, 313000, 313100, 313200, 313300, 313400, 313500, 313600, 313700, 313800, 313900, 314000, 314100, 314200, 314300, 314400, 314500, 314600, 314700, 314800, 314900, 315000, 315100, 315200, 315300, 315400, 315500, 315600, 315700, 315800, 315900, 316000, 316100, 316200, 316300, 316400, 316500, 316600, 316700, 316800, 316900, 317000, 317100, 317200, 317300, 317400, 317500, 317600, 317700, 317800, 317900, 318000, 318100, 318200, 318300, 318400, 318500, 318600, 318700, 318800, 318900, 319000, 319100, 319200, 319300, 319400, 319500, 319600, 319700, 319800, 319900, 320000, 320100, 320200, 320300, 320400, 320500, 320600, 320700, 320800, 320900, 321000, 321100, 321200, 321300, 321400, 321500, 321600, 321700, 321800, 321900, 322000, 322100, 322200, 322300, 322400, 322500, 322600, 322700, 322800, 322900, 323000, 323100, 323200, 323300, 323400, 323500, 323600, 323700, 323800, 323900, 324000, 324100, 324200, 324300, 324400, 324500, 324600, 324700, 324800, 324900, 325000, 325100, 325200, 325300, 325400, 325500, 325600, 325700, 325800, 325900, 326000, 326100, 326200, 326300, 326400, 326500, 326600, 326700, 326800, 326900, 327000, 327100, 327200, 327300, 327400, 327500, 327600, 327700, 327800, 327900, 328000, 328100, 328200, 328300, 328400, 328500, 328600, 328700, 328800, 328900, 329000, 329100, 329200, 329300, 329400, 329500, 329600, 329700, 329800, 329900, 330000, 330100, 330200, 330300, 330400, 330500, 330600, 330700, 330800, 330900, 331000, 331100, 331200, 331300, 331400, 331500, 331600, 331700, 331800, 331900, 332000, 332100, 332200, 332300, 332400, 332500, 332600, 332700, 332800, 332900, 333000, 333100, 333200, 333300, 333400, 333500, 333600, 333700, 333800, 333900, 334000, 334100, 334200, 334300, 334400, 334500, 334600, 334700, 334800, 334900, 335000, 335100, 335200, 335300, 335400, 335500, 335600, 335700, 335800, 335900, 336000, 336100, 336200, 336300, 336400, 336500, 336600, 336700, 336800, 336900, 337000, 337100, 337200, 337300, 337400, 337500, 337600, 337700, 337800, 337900, 338000, 338100, 338200, 338300, 338400, 338500, 338600, 338700, 338800, 338900, 339000, 339100, 339200, 339300, 339400, 339500, 339600, 339700, 339800, 339900, 340000, 340100, 340200, 340300, 340400, 340500, 340600, 340700, 340800, 340900, 341000, 341100, 341200, 341300, 341400, 341500, 341600, 341700, 341800, 341900, 342000, 342100, 342200, 342300, 342400, 342500, 342600, 342700, 342800, 342900, 343000, 343100, 343200, 343300, 343400, 343500, 343600, 343700, 343800, 343900, 344000, 344100, 344200, 344300, 344400, 344500, 344600, 344700, 344800, 344900, 345000, 345100, 345200, 345300, 345400, 345500, 345600, 345700, 345800, 345900, 346000, 346100, 346200, 346300, 346400, 346500, 346600, 346700, 346800, 346900, 347000, 347100, 347200, 347300, 347400, 347500, 347600, 347700, 347800, 347900, 348000, 348100, 348200, 348300, 348400, 348500, 348600, 348700, 348800, 348900, 349000, 349100, 349200, 349300, 349400, 349500, 349600, 349700, 349800, 349900, 350000, 350100, 350200, 350300, 350400, 350500, 350600, 350700, 350800, 350900, 351000, 351100, 351200, 351300, 351400, 351500, 351600, 351700, 351800, 351900, 352000, 352100, 352200, 352300, 352400, 352500, 352600, 352700, 352800, 352900, 353000, 353100, 353200, 353300, 353400, 353500, 353600, 353700, 353800, 353900, 354000, 354100, 354200, 354300, 354400, 354500, 354600, 354700, 354800, 354900, 355000, 355100, 355200, 355300, 355400, 355500, 355600, 355700, 355800, 355900, 356000, 356100, 356200, 356300, 356400, 356500, 356600, 356700, 356800, 356900, 357000, 357100, 357200, 357300, 357400, 357500, 357600, 357700, 357800, 357900, 358000, 358100, 358200, 358300, 358400, 358500, 358600, 358700, 358800, 358900, 359000, 359100, 359200, 359300, 359400, 359500, 359600, 359700, 359800, 359900, 360000, 360100, 360200, 360300, 360400, 360500, 360600, 360700, 360800, 360900, 361000, 361100, 361200, 361300, 361400, 361500, 361600, 361700, 361800, 361900, 362000, 362100, 362200, 362300, 362400, 362500, 362600, 362700, 362800, 362900, 363000, 363100, 363200, 363300, 363400, 363500, 363600, 363700, 363800, 363900, 364000, 364100, 364200, 364300, 364400, 364500, 364600, 364700, 364800, 364900, 365000, 365100, 365200, 365300, 365400, 365500, 365600, 365700, 365800, 365900, 366000, 366100, 366200, 366300, 366400, 366500, 366600, 366700, 366800, 366900, 367000, 367100, 367200, 367300, 367400, 367500, 367600, 367700, 367800, 367900, 368000, 368100, 368200, 368300, 368400, 368500, 368600, 368700, 368800, 368900, 369000, 369100, 369200, 369300, 369400, 369500, 369600, 369700, 369800, 369900, 370000, 370100, 370200, 370300, 370400, 370500, 370600, 370700, 370800, 370900, 371000, 371100, 371200, 371300, 371400, 371500, 371600, 371700, 371800, 371900, 372000, 372100, 372200, 372300, 372400, 372500, 372600, 372700, 372800, 372900, 373000, 373100, 373200, 373300, 373400, 373500, 373600, 373700, 373800, 373900, 374000, 374100, 374200, 374300, 374400, 374500, 374600, 374700, 374800, 374900, 375000, 375100, 375200, 375300, 375400, 375500, 375600, 375700, 375800, 375900, 376000, 376100, 376200, 376300, 376400, 376500, 376600, 376700, 376800, 376900, 377000, 377100, 377200, 377300, 377400, 377500, 377600, 377700, 377800, 377900, 378000, 378100, 378200, 378300, 378400, 378500, 378600, 378700, 378800, 378900, 379000, 379100, 379200, 379300, 379400, 379500, 379600, 379700, 379800, 379900, 380000, 380100, 380200, 380300, 380400, 380500, 380600, 380700, 380800, 380900, 381000, 381100, 381200, 381300, 381400, 381500, 381600, 381700, 381800, 381900, 382000, 382100, 382200, 382300, 382400, 382500, 382600, 382700, 382800, 382900, 383000, 383100, 383200, 383300, 383400, 383500, 383600, 383700, 383800, 383900, 384000, 384100, 384200, 384300, 384400, 384500, 384600, 384700, 384800, 384900, 385000, 385100, 385200, 385300, 385400, 385500, 385600, 385700, 385800, 385900, 386000, 386100, 386200, 386300, 386400, 386500, 386600, 386700, 386800, 386900, 387000, 387100, 387200, 387300, 387400, 387500, 387600, 387700, 387800, 387900, 388000, 388100, 388200, 388300, 388400, 388500, 388600, 388700, 388800, 388900, 389000, 389100, 389200, 389300, 389400, 389500, 389600, 389700, 389800, 389900, 390000, 390100, 390200, 390300, 390400, 390500, 390600, 390700, 390800, 390900, 391000, 391100, 391200, 391300, 391400, 391500, 391600, 391700, 391800, 391900, 392000, 392100, 392200, 392300, 392400, 392500, 392600, 392700, 392800, 392900, 393000, 393100, 393200, 393300, 393400, 393500, 393600, 393700, 393800, 393900, 394000, 394100, 394200, 394300, 394400, 394500, 394600, 394700, 394800, 394900, 395000, 395100, 395200, 395300, 395400, 395500, 395600, 395700, 395800, 395900, 396000, 396100, 396200, 396300, 396400, 396500, 396600, 396700, 396800, 396900, 397000, 397100, 397200, 397300, 397400, 397500, 397600, 397700, 397800, 397900, 398000, 398100, 398200, 398300, 398400, 398500, 398600, 398700, 398800, 398900, 399000, 399100, 399200, 399300, 399400, 399500, 399600, 399700, 399800, 399900, 400000,
#     400100, 400200, 400300, 400400, 400500, 400600, 400700, 400800, 400900, 401000, 401100, 401200, 401300, 401400, 401500, 401600, 401700, 401800, 401900, 402000, 402100, 402200, 402300, 402400, 402500, 402600, 402700, 402800, 402900, 403000, 403100, 403200, 403300, 403400, 403500, 403600, 403700, 403800, 403900, 404000, 404100, 404200, 404300, 404400, 404500, 404600, 404700, 404800, 404900, 405000, 405100, 405200, 405300, 405400, 405500, 405600, 405700, 405800, 405900, 406000, 406100, 406200, 406300, 406400, 406500, 406600, 406700, 406800, 406900, 407000, 407100, 407200, 407300, 407400, 407500, 407600, 407700, 407800, 407900, 408000, 408100, 408200, 408300, 408400, 408500, 408600, 408700, 408800, 408900, 409000, 409100, 409200, 409300, 409400, 409500, 409600, 409700, 409800, 409900, 410000, 410100, 410200, 410300, 410400, 410500, 410600, 410700, 410800, 410900, 411000, 411100, 411200, 411300, 411400, 411500, 411600, 411700, 411800, 411900, 412000, 412100, 412200, 412300, 412400, 412500, 412600, 412700, 412800, 412900, 413000, 413100, 413200, 413300, 413400, 413500, 413600, 413700, 413800, 413900, 414000, 414100, 414200, 414300, 414400, 414500, 414600, 414700, 414800, 414900, 415000, 415100, 415200, 415300, 415400, 415500, 415600, 415700, 415800, 415900, 416000, 416100, 416200, 416300, 416400, 416500, 416600, 416700, 416800, 416900, 417000, 417100, 417200, 417300, 417400, 417500, 417600, 417700, 417800, 417900, 418000, 418100, 418200, 418300, 418400, 418500, 418600, 418700, 418800, 418900, 419000, 419100, 419200, 419300, 419400, 419500, 419600, 419700, 419800, 419900, 420000, 420100, 420200, 420300, 420400, 420500, 420600, 420700, 420800, 420900, 421000, 421100, 421200, 421300, 421400, 421500, 421600, 421700, 421800, 421900, 422000, 422100, 422200, 422300, 422400, 422500, 422600, 422700, 422800, 422900, 423000, 423100, 423200, 423300, 423400, 423500, 423600, 423700, 423800, 423900, 424000, 424100, 424200, 424300, 424400, 424500, 424600, 424700, 424800, 424900, 425000, 425100, 425200, 425300, 425400, 425500, 425600, 425700, 425800, 425900, 426000, 426100, 426200, 426300, 426400, 426500, 426600, 426700, 426800, 426900, 427000, 427100, 427200, 427300, 427400, 427500, 427600, 427700, 427800, 427900, 428000, 428100, 428200, 428300, 428400, 428500, 428600, 428700, 428800, 428900, 429000, 429100, 429200, 429300, 429400, 429500, 429600, 429700, 429800, 429900, 430000, 430100, 430200, 430300, 430400, 430500, 430600, 430700, 430800, 430900, 431000, 431100, 431200, 431300, 431400, 431500, 431600, 431700, 431800, 431900, 432000, 432100, 432200, 432300, 432400, 432500, 432600, 432700, 432800, 432900, 433000, 433100, 433200, 433300, 433400, 433500, 433600, 433700, 433800, 433900, 434000, 434100, 434200, 434300, 434400, 434500, 434600, 434700, 434800, 434900, 435000, 435100, 435200, 435300, 435400, 435500, 435600, 435700, 435800, 435900, 436000, 436100, 436200, 436300, 436400, 436500, 436600, 436700, 436800, 436900, 437000, 437100, 437200, 437300, 437400, 437500, 437600, 437700, 437800, 437900, 438000, 438100, 438200, 438300, 438400, 438500, 438600, 438700, 438800, 438900, 439000, 439100, 439200, 439300, 439400, 439500, 439600, 439700, 439800, 439900, 440000, 440100, 440200, 440300, 440400, 440500, 440600, 440700, 440800, 440900, 441000, 441100, 441200, 441300, 441400, 441500, 441600, 441700, 441800, 441900, 442000, 442100, 442200, 442300, 442400, 442500, 442600, 442700, 442800, 442900, 443000, 443100, 443200, 443300, 443400, 443500, 443600, 443700, 443800, 443900, 444000, 444100, 444200, 444300, 444400, 444500, 444600, 444700, 444800, 444900, 445000, 445100, 445200, 445300, 445400, 445500, 445600, 445700, 445800, 445900, 446000, 446100, 446200, 446300, 446400, 446500, 446600, 446700, 446800, 446900, 447000, 447100, 447200, 447300, 447400, 447500, 447600, 447700, 447800, 447900, 448000, 448100, 448200, 448300, 448400, 448500, 448600, 448700, 448800, 448900, 449000, 449100, 449200, 449300, 449400, 449500, 449600, 449700, 449800, 449900, 450000, 450100, 450200, 450300, 450400, 450500, 450600, 450700, 450800, 450900, 451000, 451100, 451200, 451300, 451400, 451500, 451600, 451700, 451800, 451900, 452000, 452100, 452200, 452300, 452400, 452500, 452600, 452700, 452800, 452900, 453000, 453100, 453200, 453300, 453400, 453500, 453600, 453700, 453800, 453900, 454000, 454100, 454200, 454300, 454400, 454500, 454600, 454700, 454800, 454900, 455000, 455100, 455200, 455300, 455400, 455500, 455600, 455700, 455800, 455900, 456000, 456100, 456200, 456300, 456400, 456500, 456600, 456700, 456800, 456900, 457000, 457100, 457200, 457300, 457400, 457500, 457600, 457700, 457800, 457900, 458000, 458100, 458200, 458300, 458400, 458500, 458600, 458700, 458800, 458900, 459000, 459100, 459200, 459300, 459400, 459500, 459600, 459700, 459800, 459900, 460000, 460100, 460200, 460300, 460400, 460500, 460600, 460700, 460800, 460900, 461000, 461100, 461200, 461300, 461400, 461500, 461600, 461700, 461800, 461900, 462000, 462100, 462200, 462300, 462400, 462500, 462600, 462700, 462800, 462900, 463000, 463100, 463200, 463300, 463400, 463500, 463600, 463700, 463800, 463900, 464000, 464100, 464200, 464300, 464400, 464500, 464600, 464700, 464800, 464900, 465000, 465100, 465200, 465300, 465400, 465500, 465600, 465700, 465800, 465900, 466000, 466100, 466200, 466300, 466400, 466500, 466600, 466700, 466800, 466900, 467000, 467100, 467200, 467300, 467400, 467500, 467600, 467700, 467800, 467900, 468000, 468100, 468200, 468300, 468400, 468500, 468600, 468700, 468800, 468900, 469000, 469100, 469200, 469300, 469400, 469500, 469600, 469700, 469800, 469900, 470000, 470100, 470200, 470300, 470400, 470500, 470600, 470700, 470800, 470900, 471000, 471100, 471200, 471300, 471400, 471500, 471600, 471700, 471800, 471900, 472000, 472100, 472200, 472300, 472400, 472500, 472600, 472700, 472800, 472900, 473000, 473100, 473200, 473300, 473400, 473500, 473600, 473700, 473800, 473900, 474000, 474100, 474200, 474300, 474400, 474500, 474600, 474700, 474800, 474900, 475000, 475100, 475200, 475300, 475400, 475500, 475600, 475700, 475800, 475900, 476000, 476100, 476200, 476300, 476400, 476500, 476600, 476700, 476800, 476900, 477000, 477100, 477200, 477300, 477400, 477500, 477600, 477700, 477800, 477900, 478000, 478100, 478200, 478300, 478400, 478500, 478600, 478700, 478800, 478900, 479000, 479100, 479200, 479300, 479400, 479500, 479600, 479700, 479800, 479900, 480000, 480100, 480200, 480300, 480400, 480500, 480600, 480700, 480800, 480900, 481000, 481100, 481200, 481300, 481400, 481500, 481600, 481700, 481800, 481900, 482000, 482100, 482200, 482300, 482400, 482500, 482600, 482700, 482800, 482900, 483000, 483100, 483200, 483300, 483400, 483500, 483600, 483700, 483800, 483900, 484000, 484100, 484200, 484300, 484400, 484500, 484600, 484700, 484800, 484900, 485000, 485100, 485200, 485300, 485400, 485500, 485600, 485700, 485800, 485900, 486000, 486100, 486200, 486300, 486400, 486500, 486600, 486700, 486800, 486900, 487000, 487100, 487200, 487300, 487400, 487500, 487600, 487700, 487800, 487900, 488000, 488100, 488200, 488300, 488400, 488500, 488600, 488700, 488800, 488900, 489000, 489100, 489200, 489300, 489400, 489500, 489600, 489700, 489800, 489900, 490000, 490100, 490200, 490300, 490400, 490500, 490600, 490700, 490800, 490900, 491000, 491100, 491200, 491300, 491400, 491500, 491600, 491700, 491800, 491900, 492000, 492100, 492200, 492300, 492400, 492500, 492600, 492700, 492800, 492900, 493000, 493100, 493200, 493300, 493400, 493500, 493600, 493700, 493800, 493900, 494000, 494100, 494200, 494300, 494400, 494500, 494600, 494700, 494800, 494900, 495000, 495100, 495200, 495300, 495400, 495500, 495600, 495700, 495800, 495900, 496000, 496100, 496200, 496300, 496400, 496500, 496600, 496700, 496800, 496900, 497000, 497100, 497200, 497300, 497400, 497500, 497600, 497700, 497800, 497900, 498000, 498100, 498200, 498300, 498400, 498500, 498600, 498700, 498800, 498900, 499000, 499100, 499200, 499300, 499400, 499500, 499600, 499700, 499800, 499900, 500000
# ]


# Medir o tempo para cada tamanho da lista
execution_times = []
for size in list_sizes:
    arr = [random.randint(1, 10000) for _ in range(size)]
    time_taken = measure_time(arr)
    execution_times.append(time_taken)

# Criar o gráfico
plt.plot(list_sizes, execution_times, marker='o', linestyle='-', color='b')
plt.xlabel('Tamanho da Lista')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Desempenho do Insertion Sort')
plt.grid(True)
plt.show()
