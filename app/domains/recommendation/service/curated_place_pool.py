from dataclasses import dataclass
from typing import Dict, List, Optional

from app.domains.recommendation.domain.value_object.place_type import PlaceType
from app.domains.recommendation.service.place_search_query_builder import ActivityKind

CURATED_SCORE = 0.9


@dataclass(frozen=True)
class CuratedPlaceConfig:
    search_query: str
    place_type: PlaceType
    activity_kind: Optional[ActivityKind] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None


_SEONGSU_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("죠죠 성수", PlaceType.RESTAURANT, latitude=37.54149503334769, longitude=127.0610150935204),
    CuratedPlaceConfig("HDD피자 성수", PlaceType.RESTAURANT, latitude=37.54297374157875, longitude=127.05321655983478),
    CuratedPlaceConfig("진작다이닝 성수", PlaceType.RESTAURANT, latitude=37.5493469543015, longitude=127.045695676352),
    CuratedPlaceConfig("동구식당 성수", PlaceType.RESTAURANT, latitude=37.5469195376019, longitude=127.019858529918),
    CuratedPlaceConfig("투파인드피터 서울성수점", PlaceType.RESTAURANT, latitude=37.5451668215989, longitude=127.055077301441),
    CuratedPlaceConfig("바오 서울 성수", PlaceType.RESTAURANT, latitude=37.540552445066, longitude=127.061290413426),
    CuratedPlaceConfig("고우 성수", PlaceType.RESTAURANT, latitude=37.5439325963635, longitude=127.050734600116),
    CuratedPlaceConfig("이가네양꼬치 성수직영점", PlaceType.RESTAURANT, latitude=37.54403181258438, longitude=127.05645583912477),
    CuratedPlaceConfig("규카츠정 성수점", PlaceType.RESTAURANT, latitude=37.54455870536792, longitude=127.05495238148269),
    CuratedPlaceConfig("텐동식당 성수", PlaceType.RESTAURANT, latitude=37.5468236432896, longitude=127.04700679562),
    CuratedPlaceConfig("탐광 성수", PlaceType.RESTAURANT, latitude=37.5431709516945, longitude=127.055411902856),
    CuratedPlaceConfig("솔솥 성수점", PlaceType.RESTAURANT, latitude=37.5431989309409, longitude=127.055308952671),
    CuratedPlaceConfig("시옹마오 성수", PlaceType.RESTAURANT, latitude=37.54347233228556, longitude=127.05445143791935),
    CuratedPlaceConfig("태양곱창 성수", PlaceType.RESTAURANT, latitude=37.5434100739603, longitude=127.05464488794),
    CuratedPlaceConfig("키키노히호 성수점", PlaceType.RESTAURANT, latitude=37.54298639248446, longitude=127.05510059136822),
    CuratedPlaceConfig("벱 성수", PlaceType.RESTAURANT, latitude=37.54206337274946, longitude=127.05400798455187),
    CuratedPlaceConfig("소문난성수감자탕", PlaceType.RESTAURANT, latitude=37.5428308422967, longitude=127.05440457812),
    CuratedPlaceConfig("능동미나리 성수점", PlaceType.RESTAURANT, latitude=37.5427571680258, longitude=127.053951907942),
    CuratedPlaceConfig("도도한면 성수본점", PlaceType.RESTAURANT, latitude=37.5433031331487, longitude=127.054040562263),
    CuratedPlaceConfig("오카츠 성수본점", PlaceType.RESTAURANT, latitude=37.54334104388137, longitude=127.05389009342011),
    CuratedPlaceConfig("멘노아지 성수", PlaceType.RESTAURANT, latitude=37.54407738115984, longitude=127.05340405197295),
    CuratedPlaceConfig("롸카두들 내시빌 핫치킨 성수점", PlaceType.RESTAURANT, latitude=37.542253451693945, longitude=127.05207319852705),
    CuratedPlaceConfig("르프리크 성수", PlaceType.RESTAURANT, latitude=37.544439016637995, longitude=127.05265860726594),
    CuratedPlaceConfig("피읻짜 성수", PlaceType.RESTAURANT, latitude=37.5462348161701, longitude=127.054407051849),
    CuratedPlaceConfig("마리오네 성수", PlaceType.RESTAURANT, latitude=37.548928843183525, longitude=127.05431847915126),
    CuratedPlaceConfig("이짜 성수", PlaceType.RESTAURANT, latitude=37.5487841202487, longitude=127.055529221124),
    CuratedPlaceConfig("파작 북성수점", PlaceType.RESTAURANT, latitude=37.54959295525488, longitude=127.05415260927799),
    CuratedPlaceConfig("세스크멘슬 본점", PlaceType.RESTAURANT, latitude=37.54105313200188, longitude=127.05640606944031),
    CuratedPlaceConfig("플라토 성수", PlaceType.RESTAURANT, latitude=37.5376841919075, longitude=127.056617378563),
    CuratedPlaceConfig("피리어드 성수", PlaceType.RESTAURANT, latitude=37.547454779514, longitude=127.040998328741),
    CuratedPlaceConfig("타크 서울숲", PlaceType.RESTAURANT, latitude=37.5472721479804, longitude=127.042773724654),
    CuratedPlaceConfig("컴오프 성수", PlaceType.RESTAURANT, latitude=37.5460231640976, longitude=127.045710621277),
    CuratedPlaceConfig("시즈니 성수", PlaceType.RESTAURANT, latitude=37.5475243309654, longitude=127.043039797974),
    CuratedPlaceConfig("프롤라 성수", PlaceType.RESTAURANT, latitude=37.5412671173397, longitude=127.06094362209),
    CuratedPlaceConfig("피자슬라이스 서울 성수", PlaceType.RESTAURANT, latitude=37.540362325724, longitude=127.055857900421),
    CuratedPlaceConfig("서울숲누룽지통닭구이", PlaceType.RESTAURANT, latitude=37.54695980050319, longitude=127.04440418923618),
    # 카페
    CuratedPlaceConfig("사이드템포 성수", PlaceType.CAFE, latitude=37.5380732630204, longitude=127.051040653034),
    CuratedPlaceConfig("언라인 성수", PlaceType.CAFE, latitude=37.5396685898169, longitude=127.061241035672),
    CuratedPlaceConfig("따우전드 성수", PlaceType.CAFE, latitude=37.5446418617135, longitude=127.050316399829),
    CuratedPlaceConfig("맥코이 성수", PlaceType.CAFE, latitude=37.542731960834814, longitude=127.059533782574),
    CuratedPlaceConfig("본지르르 성수", PlaceType.CAFE, latitude=37.5493431509406, longitude=127.05464695574),
    CuratedPlaceConfig("로우키 성수", PlaceType.CAFE, latitude=37.544471727511365, longitude=127.04777478478088),
    CuratedPlaceConfig("아가젤라또 성수", PlaceType.CAFE, latitude=37.5433806009398, longitude=127.054080222466),
    CuratedPlaceConfig("커피냅로스터스 성수", PlaceType.CAFE, latitude=37.54230881588379, longitude=127.05319006191718),
    CuratedPlaceConfig("소파 성수", PlaceType.CAFE, latitude=37.5424300255623, longitude=127.054125928848),
    CuratedPlaceConfig("마를리 성수", PlaceType.CAFE, latitude=37.5427802289338, longitude=127.054745135469),
    CuratedPlaceConfig("업사이드 성수", PlaceType.CAFE, latitude=37.5419984473028, longitude=127.057923031968),
    CuratedPlaceConfig("로우커피스탠드 성수", PlaceType.CAFE, latitude=37.54715716085294, longitude=127.04663357436208),
    CuratedPlaceConfig("어니언 성수", PlaceType.CAFE, latitude=37.544782395189884, longitude=127.05820807890457),
    CuratedPlaceConfig("와이덴 성수", PlaceType.CAFE, latitude=37.5475565627815, longitude=127.054447618994),
    CuratedPlaceConfig("리사르커피 성수점", PlaceType.CAFE, latitude=37.547879420512274, longitude=127.05379264640943),
    CuratedPlaceConfig("피어커피 성수", PlaceType.CAFE, latitude=37.5489177737782, longitude=127.054875235404),
    CuratedPlaceConfig("피카워크샵 성수", PlaceType.CAFE, latitude=37.5502821153395, longitude=127.050313401223),
    CuratedPlaceConfig("포어플랜 성수", PlaceType.CAFE, latitude=37.54823801629977, longitude=127.04749428231781),
    CuratedPlaceConfig("플디 성수", PlaceType.CAFE, latitude=37.5479294580028, longitude=127.048519334096),
    CuratedPlaceConfig("로우키커피 헤이그라운드점", PlaceType.CAFE, latitude=37.544471727511365, longitude=127.04777478478088),
    CuratedPlaceConfig("블루보틀 성수", PlaceType.CAFE, latitude=37.548088279686716, longitude=127.04564285335792),
    CuratedPlaceConfig("리커버리커피바 성수", PlaceType.CAFE, latitude=37.55034738773333, longitude=127.04484754482596),
    CuratedPlaceConfig("챔프커피 성수", PlaceType.CAFE, latitude=37.5398280805729, longitude=127.055756798616),
    CuratedPlaceConfig("베티버 성수", PlaceType.CAFE, latitude=37.53891925414103, longitude=127.0531910485529),
    CuratedPlaceConfig("토마스베이커리 성수", PlaceType.CAFE, latitude=37.53866476204093, longitude=127.05409378862747),
    CuratedPlaceConfig("카멜 성수점", PlaceType.CAFE, latitude=37.5372403433519, longitude=127.055894041178),
    CuratedPlaceConfig("하우스오브바이닐 성수점", PlaceType.CAFE, latitude=37.5479066970044, longitude=127.05521058517),
    CuratedPlaceConfig("심퍼티쿠시 성수점", PlaceType.CAFE, latitude=37.5476938415342, longitude=127.045124332604),
    CuratedPlaceConfig("식당 오츠 성수", PlaceType.CAFE, latitude=37.5465488733395, longitude=127.046919489963),
    CuratedPlaceConfig("타코스퀘어 성수", PlaceType.CAFE, latitude=37.546164085179306, longitude=127.04707427705193),
    CuratedPlaceConfig("제스티살룬 성수", PlaceType.CAFE, latitude=37.547564189547295, longitude=127.04244685499071),
    CuratedPlaceConfig("도우또 성수", PlaceType.CAFE, latitude=37.5470514393321, longitude=127.042674017164),
    CuratedPlaceConfig("미쁘동 서울숲", PlaceType.CAFE, latitude=37.5475604979807, longitude=127.040120253971),
    CuratedPlaceConfig("요시 성수", PlaceType.CAFE, latitude=37.54728706812407, longitude=127.0438555524566),
    CuratedPlaceConfig("핫쵸 성수점", PlaceType.CAFE, latitude=37.546853, longitude=127.044135),
    CuratedPlaceConfig("5 to 7 성수", PlaceType.CAFE, latitude=37.5460826295749, longitude=127.043321867062),
    CuratedPlaceConfig("도토리 오븐 성수", PlaceType.CAFE, latitude=37.5435934086824, longitude=127.053703568622),
    CuratedPlaceConfig("더커피 성수", PlaceType.CAFE, latitude=37.5468724674866, longitude=127.04175957922),
    CuratedPlaceConfig("마일스톤커피 성수", PlaceType.CAFE, latitude=37.547446937205, longitude=127.042786272267),
    CuratedPlaceConfig("컴오프로스터스 성수", PlaceType.CAFE, latitude=37.5460231640976, longitude=127.045710621277),
    # Activity - 체험 (WORKSHOP)
    CuratedPlaceConfig("모나미 스토어 성수점", PlaceType.ACTIVITY, ActivityKind.WORKSHOP, latitude=37.5444413443547, longitude=127.055446790141),
    CuratedPlaceConfig("포인트오브뷰 성수", PlaceType.ACTIVITY, ActivityKind.WORKSHOP, latitude=37.5435241678589, longitude=127.051372519352),
    CuratedPlaceConfig("데이지크 성수", PlaceType.ACTIVITY, ActivityKind.WORKSHOP, latitude=37.5436345242137, longitude=127.05243399355),
    CuratedPlaceConfig("탬버린즈 성수", PlaceType.ACTIVITY, ActivityKind.WORKSHOP, latitude=37.5437759196933, longitude=127.052572142533),
    # Activity - 전시/문화 (EXHIBITION)
    CuratedPlaceConfig("LCDC Seoul", PlaceType.ACTIVITY, ActivityKind.EXHIBITION, latitude=37.5417353247515, longitude=127.06154597509),
    CuratedPlaceConfig("성수연방", PlaceType.ACTIVITY, ActivityKind.EXHIBITION, latitude=37.54139704871741, longitude=127.05695851079544),
    # Activity - 쇼핑 (SHOPPING)
    CuratedPlaceConfig("카키스 성수", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.54333450600984, longitude=127.06172381152828),
    CuratedPlaceConfig("EQL 성수", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5428214746883, longitude=127.058905847636),
    CuratedPlaceConfig("카시나 성수", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5426314275779, longitude=127.0530703479),
    CuratedPlaceConfig("젠틀몬스터 성수", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5381625045309, longitude=127.058705306331),
    CuratedPlaceConfig("비이커 성수 플래그십스토어", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.54399306322056, longitude=127.05050153966998),
    CuratedPlaceConfig("키스 서울 성수", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5411274489245, longitude=127.047198971706),
    # Activity - 산책 (WALK)
    CuratedPlaceConfig("서울숲", PlaceType.ACTIVITY, ActivityKind.WALK, latitude=37.5443222301513, longitude=127.037617759165),
    # Activity - 칵테일바/와인바/이자카야 (BAR, NIGHTLIFE)
    CuratedPlaceConfig("페어드 칵테일 성수", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.54613069944138, longitude=127.0471964680619),
    CuratedPlaceConfig("리타르단도 성수", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5390808460509, longitude=127.054481057437),
    CuratedPlaceConfig("포도젝트 성수", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5390394012198, longitude=127.056397763577),
    CuratedPlaceConfig("기러기둥지 성수", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5428564941135, longitude=127.053476731412),
    CuratedPlaceConfig("목탄 성수", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.54325546291173, longitude=127.05385947999282),
    CuratedPlaceConfig("토메루 성수점", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.54387889225168, longitude=127.05399571551399),
    CuratedPlaceConfig("야키토리나루토 성수", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5490696838833, longitude=127.045078764886),
    CuratedPlaceConfig("진도켄 성수점", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5455401162279, longitude=127.046000011757),
    CuratedPlaceConfig("브루어리을를 서울숲", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.546885739587154, longitude=127.04244081226828),
    CuratedPlaceConfig("우드파이어 파로 성수", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.538525, longitude=127.056572),
]

_HANNAM_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("교카이젠 한남", PlaceType.RESTAURANT, latitude=37.5338322172007, longitude=127.007746742902),
    CuratedPlaceConfig("한남동감자탕 본점", PlaceType.RESTAURANT, latitude=37.53336108690886, longitude=127.0061638659054),
    CuratedPlaceConfig("한남동한방통닭", PlaceType.RESTAURANT, latitude=37.53274120851465, longitude=127.00596242739974),
    CuratedPlaceConfig("소소막창 한남", PlaceType.RESTAURANT, latitude=37.53328458848434, longitude=127.00418617484615),
    CuratedPlaceConfig("부자피자 1호점", PlaceType.RESTAURANT, latitude=37.5372427587724, longitude=126.999823492489),
    CuratedPlaceConfig("빠르크 한남점", PlaceType.RESTAURANT, latitude=37.5374734147181, longitude=126.999737500841),
    CuratedPlaceConfig("벱 한남점", PlaceType.RESTAURANT, latitude=37.5366922386935, longitude=127.001451650464),
    CuratedPlaceConfig("벽돌해피푸드 한남", PlaceType.RESTAURANT, latitude=37.53596964515105, longitude=127.00004299468853),
    CuratedPlaceConfig("뉴오더클럽 한남", PlaceType.RESTAURANT, latitude=37.5359155831043, longitude=127.000690177396),
    CuratedPlaceConfig("다운타우너 한남", PlaceType.RESTAURANT, latitude=37.53484068813718, longitude=127.00085988080754),
    CuratedPlaceConfig("공기 한남", PlaceType.RESTAURANT, latitude=37.536192190510754, longitude=126.9993482891006),
    CuratedPlaceConfig("파이프그라운드 한남", PlaceType.RESTAURANT, latitude=37.53958892577643, longitude=127.00298714378386),
    CuratedPlaceConfig("윤세영식당 한남", PlaceType.RESTAURANT, latitude=37.5425550289961, longitude=127.002480332791),
    CuratedPlaceConfig("오아시스 한남 브런치", PlaceType.RESTAURANT, latitude=37.53659762499949, longitude=126.99796339241342),
    CuratedPlaceConfig("타크 한남", PlaceType.RESTAURANT, latitude=37.5358795444365, longitude=127.00039260892),
    CuratedPlaceConfig("난포 한남", PlaceType.RESTAURANT, latitude=37.5371310338937, longitude=126.999524788178),
    # 카페
    CuratedPlaceConfig("아키비스트 한남점", PlaceType.CAFE, latitude=37.54401283394207, longitude=127.00300768837988),
    CuratedPlaceConfig("맥코이 한남2호점", PlaceType.CAFE, latitude=37.5382194158482, longitude=127.002545814618),
    CuratedPlaceConfig("지엠엘 gml 한남", PlaceType.CAFE, latitude=37.53772476048051, longitude=127.00281848103211),
    CuratedPlaceConfig("릴리언 한남", PlaceType.CAFE, latitude=37.5373868831147, longitude=127.002910116622),
    CuratedPlaceConfig("카프온카우치 한남", PlaceType.CAFE, latitude=37.53759140361862, longitude=127.00316583536073),
    CuratedPlaceConfig("블루보틀 한남", PlaceType.CAFE, latitude=37.53630110613691, longitude=127.00503266370768),
    CuratedPlaceConfig("타르틴베이커리 한남점", PlaceType.CAFE, latitude=37.534394387317676, longitude=127.00853652897942),
    CuratedPlaceConfig("댄스댄스댄스 한남", PlaceType.CAFE, latitude=37.53381597518997, longitude=127.0081042657176),
    CuratedPlaceConfig("피어커피바 한남", PlaceType.CAFE, latitude=37.5322157202348, longitude=127.009158541012),
    CuratedPlaceConfig("에스프레소 코어 한남", PlaceType.CAFE, latitude=37.533953072994585, longitude=127.00559255323073),
    CuratedPlaceConfig("리카바이파프리카 한남", PlaceType.CAFE, latitude=37.5396114500238, longitude=127.003016563532),
    CuratedPlaceConfig("mtl 한남", PlaceType.CAFE, latitude=37.53712202091077, longitude=126.99903599899183),
    CuratedPlaceConfig("마더오프라인 한남", PlaceType.CAFE, latitude=37.536649896415966, longitude=126.99900771883323),
    CuratedPlaceConfig("낫배드커피 한남", PlaceType.CAFE, latitude=37.5372103115644, longitude=126.998365043311),
    CuratedPlaceConfig("한남작업실", PlaceType.CAFE, latitude=37.53652555571912, longitude=126.99873277872119),
    CuratedPlaceConfig("타르틴베이커리 이태원점", PlaceType.CAFE, latitude=37.5344685570355, longitude=126.997779029424),
    CuratedPlaceConfig("하우스오브와일드 한남", PlaceType.CAFE, latitude=37.534556840760715, longitude=126.99711488454147),
    CuratedPlaceConfig("소브 한남", PlaceType.CAFE, latitude=37.53773550117293, longitude=126.99502155025407),
    CuratedPlaceConfig("세르클 한남", PlaceType.CAFE, latitude=37.53557319383366, longitude=126.99838544484975),
    CuratedPlaceConfig("사유 한남", PlaceType.CAFE, latitude=37.5396296181237, longitude=126.986328152322),
    CuratedPlaceConfig("아우프글렛 한남점", PlaceType.CAFE, latitude=37.5369039741276, longitude=127.001425631143),
    # Activity - 쇼핑 (SHOPPING)
    CuratedPlaceConfig("스컬프스토어 한남", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.53498481991427, longitude=126.99727326745491),
    CuratedPlaceConfig("비샵 한남 플래그십스토어", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5353650604272, longitude=126.998229311992),
    CuratedPlaceConfig("비이커 한남점", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5366192665732, longitude=127.000009051592),
    CuratedPlaceConfig("TW레코즈 한남", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5380302177396, longitude=127.001912184815),
    # Activity - 전시/문화 (EXHIBITION)
    CuratedPlaceConfig("현대카드 바이닐앤플라스틱", PlaceType.ACTIVITY, ActivityKind.EXHIBITION, latitude=37.53680486954819, longitude=127.0008599033608),
    CuratedPlaceConfig("리움미술관", PlaceType.ACTIVITY, ActivityKind.EXHIBITION, latitude=37.53833657002706, longitude=126.99911744955163),
    CuratedPlaceConfig("페이스갤러리 한남", PlaceType.ACTIVITY, ActivityKind.EXHIBITION, latitude=37.538489737947, longitude=127.001131477248),
    CuratedPlaceConfig("현대카드 뮤직 라이브러리", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5366300766286, longitude=127.00067886949),
    # Activity - 술집/이자카야/호프 (BAR, NIGHTLIFE)
    CuratedPlaceConfig("아쿠아 한남동", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5353254260591, longitude=127.000924377851),
    CuratedPlaceConfig("서울집시 한남점", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5358768414672, longitude=127.000384688842),
    CuratedPlaceConfig("방울과꼬막 한남", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.532679949778, longitude=127.005774611871),
    CuratedPlaceConfig("서울에 살기 위하여 한남", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.53285834488268, longitude=127.00583798358645),
    CuratedPlaceConfig("타키 한남점", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5333538561901, longitude=127.006584745981),
    CuratedPlaceConfig("와 서울 와인바", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.53332591427762, longitude=127.00677708139328),
    CuratedPlaceConfig("배반낭자 한남", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.53396645485764, longitude=127.00791986234947),
    CuratedPlaceConfig("pave 와인바 한남", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5355317554325, longitude=127.000896094584),
]

_YEONNAM_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("연교 연남", PlaceType.RESTAURANT, latitude=37.5616046124056, longitude=126.926671215681),
    CuratedPlaceConfig("히사시돈부리 연남", PlaceType.RESTAURANT, latitude=37.561874698398, longitude=126.926329138141),
    CuratedPlaceConfig("숲길정육점 연남", PlaceType.RESTAURANT, latitude=37.5625936523732, longitude=126.924834399505),
    CuratedPlaceConfig("야키토리묵 연남", PlaceType.RESTAURANT, latitude=37.56465767525135, longitude=126.92458444562307),
    CuratedPlaceConfig("랫댓 연남", PlaceType.RESTAURANT, latitude=37.5619183794769, longitude=126.92416729750686),
    CuratedPlaceConfig("우와 연남", PlaceType.RESTAURANT, latitude=37.565152640105, longitude=126.923677310657),
    CuratedPlaceConfig("바다약방 연남", PlaceType.RESTAURANT, latitude=37.5629187302678, longitude=126.925972710335),
    CuratedPlaceConfig("연주방 연남", PlaceType.RESTAURANT, latitude=37.5626921983887, longitude=126.925366266672),
    CuratedPlaceConfig("요코쵸 연남", PlaceType.RESTAURANT, latitude=37.5653219290818, longitude=126.923525465661),
    CuratedPlaceConfig("이노시시 연남", PlaceType.RESTAURANT, latitude=37.5625959126908, longitude=126.927000741809),
    CuratedPlaceConfig("스시지현 연남", PlaceType.RESTAURANT, latitude=37.56065302218286, longitude=126.92361172844988),
    CuratedPlaceConfig("연남닭발", PlaceType.RESTAURANT, latitude=37.56170237598723, longitude=126.92740907169457),
    CuratedPlaceConfig("용뱅이 연남", PlaceType.RESTAURANT, latitude=37.5627438852551, longitude=126.925890258747),
    CuratedPlaceConfig("소이연남", PlaceType.RESTAURANT, latitude=37.5635139207821, longitude=126.92538808404),
    CuratedPlaceConfig("화설 연남", PlaceType.RESTAURANT, latitude=37.5629953971556, longitude=126.926103928788),
    CuratedPlaceConfig("연남면관", PlaceType.RESTAURANT, latitude=37.5626199888507, longitude=126.928060122285),
    CuratedPlaceConfig("헤비스테이크 연남", PlaceType.RESTAURANT, latitude=37.5604283222121, longitude=126.92446534159),
    CuratedPlaceConfig("백식당 연남", PlaceType.RESTAURANT, latitude=37.561833, longitude=126.925405),
    CuratedPlaceConfig("청화접 연남", PlaceType.RESTAURANT, latitude=37.563400, longitude=126.925634),
    CuratedPlaceConfig("요미우돈교자 연남점", PlaceType.RESTAURANT, latitude=37.5617690216294, longitude=126.92449115197),
    CuratedPlaceConfig("초이다이닝 연남", PlaceType.RESTAURANT, latitude=37.56127893916191, longitude=126.92458445593546),
    # 카페
    CuratedPlaceConfig("수쿤 연남", PlaceType.CAFE, latitude=37.5633312011201, longitude=126.92425980923753),
    CuratedPlaceConfig("짙은산 연남", PlaceType.CAFE, latitude=37.56558501017374, longitude=126.92351048219307),
    CuratedPlaceConfig("코리코카페 연남", PlaceType.CAFE, latitude=37.5650569296048, longitude=126.924761748091),
    CuratedPlaceConfig("메리트리 연남", PlaceType.CAFE, latitude=37.565282025063006, longitude=126.92312482019241),
    CuratedPlaceConfig("루치펠 연남", PlaceType.CAFE, latitude=37.561506953994865, longitude=126.92468269487736),
    CuratedPlaceConfig("조앤도슨 연남", PlaceType.CAFE, latitude=37.5636458629923, longitude=126.923196676635),
    CuratedPlaceConfig("마사비스 연남", PlaceType.CAFE, latitude=37.56408920136755, longitude=126.92327092452608),
    CuratedPlaceConfig("앤티크커피 연남", PlaceType.CAFE, latitude=37.561217140524874, longitude=126.92660142255426),
    CuratedPlaceConfig("터틀힙 연남", PlaceType.CAFE, latitude=37.55979694723278, longitude=126.92068463815171),
    CuratedPlaceConfig("버터앤쉘터 연남", PlaceType.CAFE, latitude=37.5641441143269, longitude=126.924595150115),
    CuratedPlaceConfig("유키모찌 연남", PlaceType.CAFE, latitude=37.5613058836563, longitude=126.924450873787),
    CuratedPlaceConfig("팽페르뒤 연남", PlaceType.CAFE, latitude=37.56191259166546, longitude=126.92497995812084),
    CuratedPlaceConfig("치플레 연남", PlaceType.CAFE, latitude=37.56281851062596, longitude=126.92564004711713),
    CuratedPlaceConfig("에브리데이해피벌스데이 연남", PlaceType.CAFE, latitude=37.56182372001191, longitude=126.92693811276743),
    CuratedPlaceConfig("카페 오르트 연남", PlaceType.CAFE, latitude=37.5616525085235, longitude=126.925461245462),
    CuratedPlaceConfig("레인리포트 브리티시 연남", PlaceType.CAFE, latitude=37.565314, longitude=126.924412),
    CuratedPlaceConfig("코코로카라 연남", PlaceType.CAFE, latitude=37.55979892305329, longitude=126.92094381805684),
    CuratedPlaceConfig("피프에스프레소바 연남", PlaceType.CAFE, latitude=37.5642870067448, longitude=126.922636876111),
    CuratedPlaceConfig("몰리하우스 연남", PlaceType.CAFE, latitude=37.56187380587, longitude=126.926342720987),
    # Activity - 쇼핑 (SHOPPING)
    CuratedPlaceConfig("흑심 연남", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.56295676775734, longitude=126.92774288130627),
    CuratedPlaceConfig("어쩌다 책방 연남", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.56476080579242, longitude=126.92383051343292),
    CuratedPlaceConfig("해리스플라워마켓 연남", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.558983414484, longitude=126.924921778508),
    CuratedPlaceConfig("고양이가있는액자가게 연남", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.560883394711, longitude=126.925997360445),
    CuratedPlaceConfig("글리밍데이 연남", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.56225082905774, longitude=126.9255545917798),
    CuratedPlaceConfig("메이드바이 연남", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5637844264432, longitude=126.925716053503),
    CuratedPlaceConfig("챔토피아 연남", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5642765483777, longitude=126.924575774894),
    CuratedPlaceConfig("보라앤드 연남소품샵", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.563165, longitude=126.925504),
    # Activity - 체험 (WORKSHOP)
    CuratedPlaceConfig("도토리캐리커쳐 연남", PlaceType.ACTIVITY, ActivityKind.WORKSHOP, latitude=37.5614147077178, longitude=126.925559951025),
    CuratedPlaceConfig("더필름 연남", PlaceType.ACTIVITY, ActivityKind.WORKSHOP, latitude=37.54890577831, longitude=126.915615141647),
    CuratedPlaceConfig("무인공방 연남", PlaceType.ACTIVITY, ActivityKind.WORKSHOP, latitude=37.5601428315452, longitude=126.924661431951),
    CuratedPlaceConfig("타다도자기공방 연남", PlaceType.ACTIVITY, ActivityKind.WORKSHOP, latitude=37.563750, longitude=126.926788),
    CuratedPlaceConfig("뤼미에르퍼퓸 연남", PlaceType.ACTIVITY, ActivityKind.WORKSHOP, latitude=37.5607772980865, longitude=126.9235165292),
    CuratedPlaceConfig("밀실 연남", PlaceType.ACTIVITY, ActivityKind.WORKSHOP, latitude=37.54654298888938, longitude=126.94007391676739),
    CuratedPlaceConfig("칠앤아트 연남", PlaceType.ACTIVITY, ActivityKind.WORKSHOP, latitude=37.5653394387637, longitude=126.917417807412),
    CuratedPlaceConfig("아이아이연남", PlaceType.ACTIVITY, ActivityKind.WORKSHOP, latitude=37.5665557790488, longitude=126.918710227857),
    # Activity - 실내놀이 (INDOOR_PLAY)
    CuratedPlaceConfig("점핑배틀 연남", PlaceType.ACTIVITY, ActivityKind.INDOOR_PLAY, latitude=37.5526020758834, longitude=126.921422203806),
    CuratedPlaceConfig("비트포비아 연남", PlaceType.ACTIVITY, ActivityKind.INDOOR_PLAY, latitude=37.549644, longitude=126.917371),
]

_DONGGYO_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("요쇼쿠야코우", PlaceType.RESTAURANT, latitude=37.5600884441588, longitude=126.922760056793),
    CuratedPlaceConfig("소바하우스 멘야준", PlaceType.RESTAURANT, latitude=37.56000543985191, longitude=126.92258810853387),
    # 카페
    CuratedPlaceConfig("콘하스 연남점", PlaceType.CAFE, latitude=37.5590130180102, longitude=126.926145210843),
    CuratedPlaceConfig("하우스오브바이닐", PlaceType.CAFE, latitude=37.560423, longitude=126.924463),
    CuratedPlaceConfig("오스카 커피부스", PlaceType.CAFE, latitude=37.5572047462075, longitude=126.921987777901),
    # Activity - 쇼핑 (SHOPPING) - 음반/레코드샵
    CuratedPlaceConfig("김밥레코즈", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5571724826922, longitude=126.927929548531),
]

_YEONHUI_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("홍대 삭 연희", PlaceType.RESTAURANT, latitude=37.566350, longitude=126.930219),
    CuratedPlaceConfig("목란 연희", PlaceType.RESTAURANT, latitude=37.56838240474039, longitude=126.93047690875805),
    CuratedPlaceConfig("연희동 칼국수", PlaceType.RESTAURANT, latitude=37.568324, longitude=126.930755),
    CuratedPlaceConfig("오향만두 연희", PlaceType.RESTAURANT, latitude=37.5669261881487, longitude=126.930125107198),
    CuratedPlaceConfig("우동카덴 연희", PlaceType.RESTAURANT, latitude=37.57240343339889, longitude=126.93502377053203),
    CuratedPlaceConfig("오트 연희", PlaceType.RESTAURANT, latitude=37.5695376085208, longitude=126.932246199414),
    CuratedPlaceConfig("링키지버거 연희", PlaceType.RESTAURANT, latitude=37.5662722438385, longitude=126.927434066708),
    CuratedPlaceConfig("쿳사연희", PlaceType.RESTAURANT, latitude=37.5721839574145, longitude=126.929386667961),
    CuratedPlaceConfig("니바하우스 연희", PlaceType.RESTAURANT, latitude=37.5684484888011, longitude=126.931007722532),
    CuratedPlaceConfig("그로어스 연희", PlaceType.RESTAURANT, latitude=37.572282659481, longitude=126.933334949211),
    CuratedPlaceConfig("그레인서울 연희", PlaceType.RESTAURANT, latitude=37.56627224592564, longitude=126.9274374623977),
    CuratedPlaceConfig("타라이 연희", PlaceType.RESTAURANT, latitude=37.5678911775644, longitude=126.928657235369),
    CuratedPlaceConfig("장작새 연남", PlaceType.RESTAURANT, latitude=37.564274, longitude=126.926211),
    CuratedPlaceConfig("도우클럽 연희", PlaceType.RESTAURANT, latitude=37.5661647427194, longitude=126.928447217444),
    CuratedPlaceConfig("시오 연희본점", PlaceType.RESTAURANT, latitude=37.5672136866783, longitude=126.928752962074),
    CuratedPlaceConfig("마우디 연희", PlaceType.RESTAURANT, latitude=37.5674992451899, longitude=126.930165320861),
    CuratedPlaceConfig("원순철판동태찜 연희", PlaceType.RESTAURANT, latitude=37.567213, longitude=126.929076),
    CuratedPlaceConfig("이화원 연희", PlaceType.RESTAURANT, latitude=37.566561527059, longitude=126.929020711968),
    CuratedPlaceConfig("청송함흥냉면전문점 본관", PlaceType.RESTAURANT, latitude=37.565893745707314, longitude=126.92878251650194),
    CuratedPlaceConfig("리정원 연희", PlaceType.RESTAURANT, latitude=37.565791818377505, longitude=126.92859245604421),
    # 카페
    CuratedPlaceConfig("킷사카라수 연희", PlaceType.CAFE, latitude=37.5662627607664, longitude=126.92813358823),
    CuratedPlaceConfig("데스툴 연희", PlaceType.CAFE, latitude=37.5695364677268, longitude=126.931829644125),
    CuratedPlaceConfig("프로토콜 연희점", PlaceType.CAFE, latitude=37.56779277684173, longitude=126.93137280560335),
    CuratedPlaceConfig("디파트먼트이엔 연희", PlaceType.CAFE, latitude=37.56267973780138, longitude=126.92852638404767),
    CuratedPlaceConfig("새라울 연희", PlaceType.CAFE, latitude=37.5703205314005, longitude=126.932173044866),
    CuratedPlaceConfig("매뉴팩트커피 연희본점", PlaceType.CAFE, latitude=37.5677836289079, longitude=126.929608150729),
    CuratedPlaceConfig("연희 에스프레소바", PlaceType.CAFE, latitude=37.56677087382404, longitude=126.92805386675303),
    CuratedPlaceConfig("에브리띵베이글 연희", PlaceType.CAFE, latitude=37.567778228336245, longitude=126.92961721117074),
    CuratedPlaceConfig("스웨이커피스테이션 연희", PlaceType.CAFE, latitude=37.5690308937557, longitude=126.928585968115),
    CuratedPlaceConfig("센티멘트 연희", PlaceType.CAFE, latitude=37.5672192657976, longitude=126.929040462267),
    CuratedPlaceConfig("동경책방 연희", PlaceType.CAFE, latitude=37.566362676054226, longitude=126.92797729025138),
    CuratedPlaceConfig("목화씨라운지 연희", PlaceType.CAFE, latitude=37.56608501746545, longitude=126.92206341010379),
    CuratedPlaceConfig("더니커피 연희", PlaceType.CAFE, latitude=37.56824462539631, longitude=126.92908476665215),
    CuratedPlaceConfig("로도덴드론 연희 3호점", PlaceType.CAFE, latitude=37.568611, longitude=126.929659),
    # Activity - 쇼핑 (SHOPPING)
    CuratedPlaceConfig("글월 연희", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5693886653327, longitude=126.931761862175),
    CuratedPlaceConfig("빅슬립 연희", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.56319300708237, longitude=126.93105444778264),
    CuratedPlaceConfig("카키스 연희", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5682668393907, longitude=126.93007405005),
    CuratedPlaceConfig("유어마인드 연희", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5684556147972, longitude=126.932423760599),
    CuratedPlaceConfig("그린디자인웍스 공장 연희", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.56824199510099, longitude=126.92920588532618),
    CuratedPlaceConfig("티티에이 연희", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5679892685092, longitude=126.929965644912),
    CuratedPlaceConfig("포셋 연희", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5700046529011, longitude=126.93125644889),
    CuratedPlaceConfig("사러가 연희", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5671547653381, longitude=126.9296608103891),
    # Activity - 체험 (WORKSHOP)
    CuratedPlaceConfig("옵젵상가 연희", PlaceType.ACTIVITY, ActivityKind.WORKSHOP, latitude=37.5671475587316, longitude=126.929663080986),
    # Activity - 전시/문화 (EXHIBITION)
    CuratedPlaceConfig("라이카시네마 연희", PlaceType.ACTIVITY, ActivityKind.EXHIBITION, latitude=37.5651643154485, longitude=126.930932651709),
    # Activity - 칵테일바/와인바/이자카야 (BAR)
    CuratedPlaceConfig("희로 연희", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.56641679471255, longitude=126.92660990380499),
    CuratedPlaceConfig("정키 연희", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5662722459195, longitude=126.927437462398),
]

_ITAEWON_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("야상해", PlaceType.RESTAURANT, latitude=37.53480443131473, longitude=126.9927928446203),
    CuratedPlaceConfig("네번째집 이태원", PlaceType.RESTAURANT, latitude=37.53373588437539, longitude=126.9934831047566),
    CuratedPlaceConfig("벅벅 이태원점", PlaceType.RESTAURANT, latitude=37.53328170463936, longitude=126.99223860585873),
    CuratedPlaceConfig("쟈니덤플링 본관", PlaceType.RESTAURANT, latitude=37.5338259020467, longitude=126.992129934412),
    CuratedPlaceConfig("피자 브루클린 이태원", PlaceType.RESTAURANT, latitude=37.5316059731702, longitude=126.994580722131),
    CuratedPlaceConfig("모터시티 이태원점", PlaceType.RESTAURANT, latitude=37.53396624763907, longitude=126.98943264084404),
    CuratedPlaceConfig("재재식당", PlaceType.RESTAURANT, latitude=37.534488807682, longitude=126.98920628375213),
    CuratedPlaceConfig("칼트칼터칼트", PlaceType.RESTAURANT, latitude=37.5352851471244, longitude=126.987719471504),
    CuratedPlaceConfig("버거스낵", PlaceType.RESTAURANT, latitude=37.53731779421355, longitude=126.9876218326533),
    CuratedPlaceConfig("잭잭", PlaceType.RESTAURANT, latitude=37.5380062834446, longitude=126.988877650477),
    CuratedPlaceConfig("폴스다이너", PlaceType.RESTAURANT, latitude=37.5392783640935, longitude=126.98755814517),
    CuratedPlaceConfig("선데이아보", PlaceType.RESTAURANT, latitude=37.541606859531136, longitude=126.99098854006806),
    # 카페
    CuratedPlaceConfig("이코복스 커피스튜디오 이태원점", PlaceType.CAFE, latitude=37.533984672523715, longitude=126.9959948114923),
    CuratedPlaceConfig("카페포이어", PlaceType.CAFE, latitude=37.5335341109016, longitude=126.994478756404),
    CuratedPlaceConfig("Apt서울", PlaceType.CAFE, latitude=37.5318510513703, longitude=126.994709681372),
    CuratedPlaceConfig("Cafe TRVR", PlaceType.CAFE, latitude=37.5382949504572, longitude=126.993537018774),
    CuratedPlaceConfig("헤미안커피바", PlaceType.CAFE, latitude=37.535122130292805, longitude=126.98835422842411),
    # Activity - 칵테일바/와인바/이자카야 (BAR)
    CuratedPlaceConfig("바부", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.53415561929913, longitude=126.99142503023616),
    CuratedPlaceConfig("큐고", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5346035137527, longitude=126.992885640275),
    CuratedPlaceConfig("야주", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5337863353995, longitude=126.993392587872),
    CuratedPlaceConfig("하츠토리", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5387512406785, longitude=126.987199553217),
]

_YONGSAN_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("타코스탠드", PlaceType.RESTAURANT, latitude=37.541424512860985, longitude=126.98724775163402),
    CuratedPlaceConfig("노스트레스버거", PlaceType.RESTAURANT, latitude=37.54384821849939, longitude=126.98740349384495),
    CuratedPlaceConfig("하우스게러지", PlaceType.RESTAURANT, latitude=37.544050, longitude=126.987128),
    CuratedPlaceConfig("메르신케밥", PlaceType.RESTAURANT, latitude=37.5455563599104, longitude=126.986040779254),
    CuratedPlaceConfig("빙점강하력", PlaceType.RESTAURANT, latitude=37.5451183743363, longitude=126.985219335718),
    CuratedPlaceConfig("팟카파우", PlaceType.RESTAURANT, latitude=37.545192210686125, longitude=126.98485947916757),
    # 카페
    CuratedPlaceConfig("포뮬라커피", PlaceType.CAFE, latitude=37.543269, longitude=126.987666),
    CuratedPlaceConfig("코타티", PlaceType.CAFE, latitude=37.54347167940464, longitude=126.98816396049732),
    CuratedPlaceConfig("개방 해방촌점", PlaceType.CAFE, latitude=37.54524173831313, longitude=126.9846478638259),
    # Activity - 칵테일바 (BAR)
    CuratedPlaceConfig("힐스앤유로파", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5416425400595, longitude=126.987111931514),
]

_NONHYEON_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("홍명", PlaceType.RESTAURANT, latitude=37.5145374347634, longitude=127.029458772737),
    CuratedPlaceConfig("중화백반 강남구청점", PlaceType.RESTAURANT, latitude=37.5164358004369, longitude=127.036126482522),
    CuratedPlaceConfig("타카이 청담점", PlaceType.RESTAURANT, latitude=37.518348356583, longitude=127.039783355657),
    CuratedPlaceConfig("코즈믹버거 청담점", PlaceType.RESTAURANT, latitude=37.5184446897946, longitude=127.040002854642),
    CuratedPlaceConfig("부타노맥스", PlaceType.RESTAURANT, latitude=37.51660472231706, longitude=127.04035139678145),
    CuratedPlaceConfig("롤리폴리 꼬또", PlaceType.RESTAURANT, latitude=37.5112863065818, longitude=127.042324506495),
    CuratedPlaceConfig("파스타스타", PlaceType.RESTAURANT, latitude=37.507086, longitude=127.025118),
    CuratedPlaceConfig("함지곱창", PlaceType.RESTAURANT, latitude=37.5092805520162, longitude=127.023285773326),
    CuratedPlaceConfig("무브먼트", PlaceType.RESTAURANT, latitude=37.5213790744184, longitude=127.037821169036),
    CuratedPlaceConfig("OTR:Burger", PlaceType.RESTAURANT, latitude=37.513060, longitude=127.034409),
    # 카페
    CuratedPlaceConfig("수목금토카페", PlaceType.CAFE, latitude=37.5145311506818, longitude=127.02548629295),
    CuratedPlaceConfig("파퓰러카페", PlaceType.CAFE, latitude=37.513592604348844, longitude=127.0281350129147),
    CuratedPlaceConfig("피피베이커리", PlaceType.CAFE, latitude=37.5180511320705, longitude=127.030315317375),
    CuratedPlaceConfig("로칼커피 논현점", PlaceType.CAFE, latitude=37.5173507562486, longitude=127.037612133974),
    CuratedPlaceConfig("구테로이테 본점", PlaceType.CAFE, latitude=37.5176951806406, longitude=127.039630301871),
    CuratedPlaceConfig("카페 델 꼬또네 강남구청역점", PlaceType.CAFE, latitude=37.518397635404, longitude=127.040595564558),
    CuratedPlaceConfig("카페 그라브", PlaceType.CAFE, latitude=37.5131165637455, longitude=127.02940957722),
    # Activity - 편집숍/가구 (SHOPPING)
    CuratedPlaceConfig("인포멀웨어", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.517399540675946, longitude=127.02730164700642),
    CuratedPlaceConfig("에이치픽스 도산", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.52100529327299, longitude=127.03443412831366),
    # Activity - 술집/와인바 (BAR)
    CuratedPlaceConfig("피헨", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.517438350507, longitude=127.030699663638),
    CuratedPlaceConfig("숨스", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.51805227473261, longitude=127.02547730992909),
    CuratedPlaceConfig("육다시구", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.51773966790988, longitude=127.02528490579573),
    CuratedPlaceConfig("루나바인", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.51832033353464, longitude=127.02744224787948),
    CuratedPlaceConfig("카이", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5099441861627, longitude=127.035732011685),
    # 논현동 추가
    CuratedPlaceConfig("현우동", PlaceType.RESTAURANT, latitude=37.517007361287, longitude=127.024288113104),
]

_SINSA_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("콴안다오", PlaceType.RESTAURANT, latitude=37.518489151037166, longitude=127.02150137777514),
    CuratedPlaceConfig("올디스타코 신사점", PlaceType.RESTAURANT, latitude=37.519256026338994, longitude=127.02082288577473),
    CuratedPlaceConfig("날리", PlaceType.RESTAURANT, latitude=37.5191525838042, longitude=127.019818364589),
    CuratedPlaceConfig("송쉐프 본점", PlaceType.RESTAURANT, latitude=37.5193003823074, longitude=127.019614789945),
    CuratedPlaceConfig("애시드하우스", PlaceType.RESTAURANT, latitude=37.5199364100427, longitude=127.020093452772),
    CuratedPlaceConfig("카이센동우니도", PlaceType.RESTAURANT, latitude=37.520753, longitude=127.019927),
    CuratedPlaceConfig("멘츠루 신사점", PlaceType.RESTAURANT, latitude=37.5202508438852, longitude=127.020188558038),
    CuratedPlaceConfig("스구식탁 가로수길점", PlaceType.RESTAURANT, latitude=37.5193349888175, longitude=127.022595479206),
    CuratedPlaceConfig("나이스샤워 치유 가로수길", PlaceType.RESTAURANT, latitude=37.5217336251311, longitude=127.021708191583),
    CuratedPlaceConfig("모던아시안누들서비스", PlaceType.RESTAURANT, latitude=37.5218823871055, longitude=127.02117655828),
    CuratedPlaceConfig("온기정", PlaceType.RESTAURANT, latitude=37.5221977912172, longitude=127.020878002399),
    CuratedPlaceConfig("테보", PlaceType.RESTAURANT, latitude=37.5219636068975, longitude=127.020441283284),
    CuratedPlaceConfig("도라보울신사", PlaceType.RESTAURANT, latitude=37.522468, longitude=127.021315),
    CuratedPlaceConfig("라모따", PlaceType.RESTAURANT, latitude=37.52039071494364, longitude=127.02386387709252),
    CuratedPlaceConfig("핫쵸", PlaceType.RESTAURANT, latitude=37.520904351516144, longitude=127.02354051415416),
    CuratedPlaceConfig("노아이디어피자 신사점", PlaceType.RESTAURANT, latitude=37.5189625293487, longitude=127.024332862917),
    CuratedPlaceConfig("쮸즈", PlaceType.RESTAURANT, latitude=37.51951298294405, longitude=127.02461923288887),
    CuratedPlaceConfig("콰이", PlaceType.RESTAURANT, latitude=37.5208945345584, longitude=127.02729047708473),
    # 카페
    CuratedPlaceConfig("프론트서울", PlaceType.CAFE, latitude=37.5193332523103, longitude=127.022250466372),
    CuratedPlaceConfig("투올더드리머스", PlaceType.CAFE, latitude=37.5198047951892, longitude=127.020491598128),
    CuratedPlaceConfig("테일러커피 신사점", PlaceType.CAFE, latitude=37.5201578619682, longitude=127.021207744507),
    CuratedPlaceConfig("따우전드 신사점", PlaceType.CAFE, latitude=37.520593918852164, longitude=127.02136623689645),
    CuratedPlaceConfig("올드페리도넛 가로수길점", PlaceType.CAFE, latitude=37.52072277553913, longitude=127.0212927450624),
    CuratedPlaceConfig("파치노 에스프레소바", PlaceType.CAFE, latitude=37.5209092753848, longitude=127.021335784105),
    CuratedPlaceConfig("스태키커피하우스", PlaceType.CAFE, latitude=37.520059, longitude=127.023623),
    CuratedPlaceConfig("카페공명 신사가로수길점", PlaceType.CAFE, latitude=37.5206159590389, longitude=127.023896753839),
    CuratedPlaceConfig("히트커피로스터스 신사", PlaceType.CAFE, latitude=37.5209492806488, longitude=127.024140070787),
    CuratedPlaceConfig("이코복스 커피스튜디오 신사점", PlaceType.CAFE, latitude=37.521159590637886, longitude=127.02222272831536),
    CuratedPlaceConfig("공원스크립트 가로수길점", PlaceType.CAFE, latitude=37.52123251766334, longitude=127.02250894773826),
    CuratedPlaceConfig("에뚜왈 가로수길점", PlaceType.CAFE, latitude=37.5213145633341, longitude=127.02222164306),
    CuratedPlaceConfig("헤이즈 밀 베이커리", PlaceType.CAFE, latitude=37.5220036333729, longitude=127.02324560896),
    CuratedPlaceConfig("마일스톤커피", PlaceType.CAFE, latitude=37.5218511454281, longitude=127.024330407303),
    CuratedPlaceConfig("어반누크 베이커리카페 신사점", PlaceType.CAFE, latitude=37.521397379000945, longitude=127.02692075160007),
    CuratedPlaceConfig("산새코에", PlaceType.CAFE, latitude=37.5234530090416, longitude=127.028860452856),
    # Activity - 술집/이자카야 (BAR)
    CuratedPlaceConfig("엉클조소시지 신사점", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5176249356609, longitude=127.022326878156),
    CuratedPlaceConfig("신사전", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.51866553914003, longitude=127.0226179008999),
    CuratedPlaceConfig("콘유", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.51919727057277, longitude=127.02187713466301),
    CuratedPlaceConfig("유희", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.519377494177, longitude=127.021752756537),
    CuratedPlaceConfig("뎅오야", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.519508211870885, longitude=127.0213568777921),
    CuratedPlaceConfig("다이닝상석", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5247916696852, longitude=127.025964916554),
    # Activity - 쇼핑 (SHOPPING)
    CuratedPlaceConfig("나이스웨더마켓", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.52076964884671, longitude=127.02117511258504),
    CuratedPlaceConfig("스틸나이스", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5209182589559, longitude=127.021481712989),
    CuratedPlaceConfig("백산안경점", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5208316983863, longitude=127.021832363437),
    CuratedPlaceConfig("ETC 서울", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5228282910356, longitude=127.021991318911),
    CuratedPlaceConfig("모로모로", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.52365701186981, longitude=127.02304815262956),
]

_APGUJEONG_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("사카바호빈", PlaceType.RESTAURANT, latitude=37.5225187432614, longitude=127.032067146974),
    CuratedPlaceConfig("포노부오노", PlaceType.RESTAURANT, latitude=37.5230671027962, longitude=127.036387603441),
    CuratedPlaceConfig("하카", PlaceType.RESTAURANT, latitude=37.5235900960689, longitude=127.037942197874),
    CuratedPlaceConfig("클랩피자 청담", PlaceType.RESTAURANT, latitude=37.524095085654, longitude=127.036584941907),
    CuratedPlaceConfig("다운타우너 청담", PlaceType.RESTAURANT, latitude=37.52405932965891, longitude=127.03852503400212),
    CuratedPlaceConfig("까폼 본점", PlaceType.RESTAURANT, latitude=37.5248568891934, longitude=127.037992615362),
    CuratedPlaceConfig("벽돌해피푸드 압구정점", PlaceType.RESTAURANT, latitude=37.52542986230018, longitude=127.03819201119605),
    CuratedPlaceConfig("르 봉 구떼", PlaceType.RESTAURANT, latitude=37.5252863366585, longitude=127.036176001087),
    CuratedPlaceConfig("만카이", PlaceType.RESTAURANT, latitude=37.52618989799297, longitude=127.03664252946062),
    CuratedPlaceConfig("딸랏", PlaceType.RESTAURANT, latitude=37.526877937732, longitude=127.03767800713),
    CuratedPlaceConfig("센자이료쿠", PlaceType.RESTAURANT, latitude=37.527032435445, longitude=127.039137467136),
    CuratedPlaceConfig("오레노이키루미치 압구정본점", PlaceType.RESTAURANT, latitude=37.52790585554761, longitude=127.0380688286101),
    CuratedPlaceConfig("부베트 서울", PlaceType.RESTAURANT, latitude=37.52488108997378, longitude=127.0288926785854),
    # 카페
    CuratedPlaceConfig("아가젤라또 압구정점", PlaceType.CAFE, latitude=37.521737020306546, longitude=127.02708150746436),
    CuratedPlaceConfig("젠제로 압구정점", PlaceType.CAFE, latitude=37.5265928795322, longitude=127.029357170748),
    CuratedPlaceConfig("플링크 압구정점", PlaceType.CAFE, latitude=37.527777992017114, longitude=127.03170172067587),
    CuratedPlaceConfig("쿠라리에", PlaceType.CAFE, latitude=37.525346505935026, longitude=127.03380260751109),
    CuratedPlaceConfig("카멜커피 도산1호점", PlaceType.CAFE, latitude=37.5234465481905, longitude=127.035985062738),
    CuratedPlaceConfig("런던베이글뮤지엄 도산점", PlaceType.CAFE, latitude=37.526068325732666, longitude=127.0364388378771),
    CuratedPlaceConfig("브로트아트 청담점", PlaceType.CAFE, latitude=37.527198, longitude=127.041902),
    CuratedPlaceConfig("천장지구 서울", PlaceType.CAFE, latitude=37.5221789947406, longitude=127.038348726381),
    CuratedPlaceConfig("Bitte Dosan", PlaceType.CAFE, latitude=37.5274730683414, longitude=127.039007596606),
    # Activity - 칵테일바/와인바/바 (BAR)
    CuratedPlaceConfig("Laputa Seoul", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5264142565862, longitude=127.036613225536),
    # Activity - 산책 (WALK)
    CuratedPlaceConfig("잠원한강공원", PlaceType.ACTIVITY, ActivityKind.WALK, latitude=37.5273338139916, longitude=127.019046713623),
    # Activity - 쇼핑 (SHOPPING)
    CuratedPlaceConfig("위글위글집 도산", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5261143186388, longitude=127.036303105418),
    CuratedPlaceConfig("Stick With Me", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5283928508242, longitude=127.036632293786),
    # Activity - 전시/문화 (EXHIBITION)
    CuratedPlaceConfig("4233마음센터 압구정점", PlaceType.ACTIVITY, ActivityKind.EXHIBITION, latitude=37.5266092400186, longitude=127.035409620051),
]

_CHEONGDAM_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("피플더테라스", PlaceType.RESTAURANT, latitude=37.5252985222721, longitude=127.047552137652),
    # 카페
    CuratedPlaceConfig("무니", PlaceType.CAFE, latitude=37.5229477202982, longitude=127.045484997),
]

_JAMSIL_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("미즈컨테이너 잠실", PlaceType.RESTAURANT, latitude=37.5122142732179, longitude=127.09840172682618),
    CuratedPlaceConfig("칸다소바 롯데월드몰점", PlaceType.RESTAURANT, latitude=37.51357305711812, longitude=127.10358847557187),
    CuratedPlaceConfig("파오파오 새마을시장본점", PlaceType.RESTAURANT, latitude=37.50890155968363, longitude=127.08404008178898),
    # 카페
    CuratedPlaceConfig("마주이", PlaceType.CAFE, latitude=37.5062723667768, longitude=127.08904289827703),
    # Activity - 쇼핑 (SHOPPING)
    CuratedPlaceConfig("롯데월드몰", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.51260447840551, longitude=127.10255558658325),
    # Activity - 칵테일바/이자카야 (BAR)
    CuratedPlaceConfig("탄포포", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5098342823137, longitude=127.085043232693),
]

_MANGWON_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("신세카이 망원", PlaceType.RESTAURANT, latitude=37.5558115164214, longitude=126.908996869161),
    CuratedPlaceConfig("류진 망원", PlaceType.RESTAURANT, latitude=37.5546543584325, longitude=126.907480638136),
    CuratedPlaceConfig("희옥 망원", PlaceType.RESTAURANT, latitude=37.55433769867013, longitude=126.9069593083376),
    CuratedPlaceConfig("묘내", PlaceType.RESTAURANT, latitude=37.5547432688909, longitude=126.904850405018),
    CuratedPlaceConfig("베우노 망원", PlaceType.RESTAURANT, latitude=37.55646269307894, longitude=126.90524998954844),
    # 카페
    CuratedPlaceConfig("필담 망원", PlaceType.CAFE, latitude=37.553329690324, longitude=126.908377451366),
    CuratedPlaceConfig("모을 망원", PlaceType.CAFE, latitude=37.5543468938918, longitude=126.907194693951),
    CuratedPlaceConfig("스몰커피바", PlaceType.CAFE, latitude=37.552886747118166, longitude=126.9065220146673),
    CuratedPlaceConfig("올웨이즈어거스트 망원", PlaceType.CAFE, latitude=37.55610990229458, longitude=126.9035188691369),
    CuratedPlaceConfig("로잉커피바 망원", PlaceType.CAFE, latitude=37.5556673096878, longitude=126.902177200273),
    CuratedPlaceConfig("한강에스프레소 망원", PlaceType.CAFE, latitude=37.553910109351655, longitude=126.90186940863782),
    CuratedPlaceConfig("필리커피 망원", PlaceType.CAFE, latitude=37.5581750502248, longitude=126.905828421632),
    CuratedPlaceConfig("HHSS하우스", PlaceType.CAFE, latitude=37.5584098014318, longitude=126.907591436325),
    # Activity - 칵테일바/와인바/이자카야 (BAR)
    CuratedPlaceConfig("코우콘", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5547549722079, longitude=126.90825348038),
    CuratedPlaceConfig("로바타우직 망원", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5547743528903, longitude=126.905410568386),
    CuratedPlaceConfig("다이치 망원", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5591533831923, longitude=126.901234389691),
    CuratedPlaceConfig("능소화 와인바 망원", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.5563255832021, longitude=126.900672248762),
    # Activity - 쇼핑 (SHOPPING)
    CuratedPlaceConfig("프레젠트모먼트 망원", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5531219322111, longitude=126.90769868688),
    CuratedPlaceConfig("호코리상점 망원", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5575611049538, longitude=126.904252645414),
    CuratedPlaceConfig("크로우캐년 망원", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5550380262051, longitude=126.899569392206),
    CuratedPlaceConfig("홍대널판 망원", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.5571265155249, longitude=126.901684109544),
]

_SEONGSAN_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("온랭", PlaceType.RESTAURANT, latitude=37.558986, longitude=126.911936),
    CuratedPlaceConfig("우리바다수산", PlaceType.RESTAURANT, latitude=37.557722, longitude=126.908947),
    # 카페
    CuratedPlaceConfig("이해", PlaceType.CAFE, latitude=37.559912, longitude=126.915398),
    CuratedPlaceConfig("으믐", PlaceType.CAFE, latitude=37.558799, longitude=126.911313),
    CuratedPlaceConfig("푸리", PlaceType.CAFE, latitude=37.564646, longitude=126.905726),
]

_HAPJEONG_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("고미태", PlaceType.RESTAURANT, latitude=37.553003, longitude=126.911882),
    CuratedPlaceConfig("이리에라멘", PlaceType.RESTAURANT, latitude=37.548072, longitude=126.914381),
    # 카페
    CuratedPlaceConfig("빈브라더스 합정", PlaceType.CAFE, latitude=37.545694, longitude=126.914984),
    CuratedPlaceConfig("그로니", PlaceType.CAFE, latitude=37.547130, longitude=126.919258),
    CuratedPlaceConfig("앤트러사이트 합정점", PlaceType.CAFE, latitude=37.545814, longitude=126.918435),
    # Activity - 일본식주점 (BAR)
    CuratedPlaceConfig("카에루", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.550136, longitude=126.910269),
    # Activity - 쇼핑 (SHOPPING) - 의류
    CuratedPlaceConfig("테켓", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.547972, longitude=126.915660),
]

_SANGSU_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("마포라스토랑", PlaceType.RESTAURANT, latitude=37.548746, longitude=126.921419),
    # 카페
    CuratedPlaceConfig("도덕과 규범", PlaceType.CAFE, latitude=37.548944, longitude=126.924450),
    CuratedPlaceConfig("푸글렌 서울", PlaceType.CAFE, latitude=37.548394, longitude=126.922812),
    # Activity - 쇼핑 (SHOPPING) - 음반/레코드샵
    CuratedPlaceConfig("모자이크 웨스트", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.545145, longitude=126.923566),
    # Activity - 요리주점 (BAR)
    CuratedPlaceConfig("상수소굴", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.547380, longitude=126.922195),
]

_SEOGYO_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("리퍼", PlaceType.RESTAURANT, latitude=37.555903, longitude=126.915572),
    CuratedPlaceConfig("멘야준", PlaceType.RESTAURANT, latitude=37.554894, longitude=126.916388),
    CuratedPlaceConfig("멘도무카우", PlaceType.RESTAURANT, latitude=37.553628, longitude=126.918107),
    CuratedPlaceConfig("담택 본점", PlaceType.RESTAURANT, latitude=37.554452, longitude=126.915165),
    CuratedPlaceConfig("일만보쌈", PlaceType.RESTAURANT, latitude=37.554422, longitude=126.913579),
    CuratedPlaceConfig("세상끝의라멘", PlaceType.RESTAURANT, latitude=37.551656, longitude=126.915226),
    CuratedPlaceConfig("이화누룽지삼계탕", PlaceType.RESTAURANT, latitude=37.553855, longitude=126.928608),
    CuratedPlaceConfig("재지패티", PlaceType.RESTAURANT, latitude=37.554956, longitude=126.931077),
    CuratedPlaceConfig("이츠야", PlaceType.RESTAURANT, latitude=37.548759, longitude=126.919935),
    CuratedPlaceConfig("넨네", PlaceType.RESTAURANT, latitude=37.550423, longitude=126.919842),
    # 카페
    CuratedPlaceConfig("퀜치커피", PlaceType.CAFE, latitude=37.554009, longitude=126.912847),
    CuratedPlaceConfig("앤트러사이트 서교점", PlaceType.CAFE, latitude=37.555522, longitude=126.911679),
    # Activity - 체험 (WORKSHOP) - 포토스튜디오
    CuratedPlaceConfig("글리치", PlaceType.ACTIVITY, ActivityKind.WORKSHOP, latitude=37.555546, longitude=126.925017),
    # Activity - 일본식주점 (BAR)
    CuratedPlaceConfig("토메루", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.556127, longitude=126.927193),
    CuratedPlaceConfig("성립", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.556575, longitude=126.910597),
    # Activity - 쇼핑 (SHOPPING)
    CuratedPlaceConfig("웍스아웃 홍대라이즈점", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.554429, longitude=126.921244),
    CuratedPlaceConfig("맨하탄레코즈 서울", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.551842, longitude=126.919931),
    CuratedPlaceConfig("스컬프스토어 서교점", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.549618, longitude=126.915630),
    CuratedPlaceConfig("에버닌스테어스", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.550103, longitude=126.919121),
    CuratedPlaceConfig("하이츠스토어", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.551555, longitude=126.918338),
]

_HANGANGNO_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("마토미", PlaceType.RESTAURANT, latitude=37.537482, longitude=126.974355),
    CuratedPlaceConfig("중화식", PlaceType.RESTAURANT, latitude=37.534485, longitude=126.974231),
    CuratedPlaceConfig("타파코파", PlaceType.RESTAURANT, latitude=37.532552, longitude=126.973214),
    CuratedPlaceConfig("선채 용산", PlaceType.RESTAURANT, latitude=37.531610, longitude=126.973105),
    # Activity - 쇼핑 (SHOPPING) - 인테리어/생활용품
    CuratedPlaceConfig("패스비 엑시트6 제너럴스토어", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.534901, longitude=126.972846),
    CuratedPlaceConfig("트렁크셀렉션 트렁크스테이션", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.534233, longitude=126.973191),
    # Activity - 와인바 (BAR)
    CuratedPlaceConfig("TAA", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.532768, longitude=126.973802),
]

_HANGANGNO3_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("고로고로 용산", PlaceType.RESTAURANT, latitude=37.525500, longitude=126.962193),
    # 카페
    CuratedPlaceConfig("올딧세", PlaceType.CAFE, latitude=37.526981, longitude=126.963039),
    CuratedPlaceConfig("해이커피앤바", PlaceType.CAFE, latitude=37.526629, longitude=126.962729),
    CuratedPlaceConfig("르프레임", PlaceType.CAFE, latitude=37.525800, longitude=126.961636),
    CuratedPlaceConfig("받터", PlaceType.CAFE, latitude=37.525868, longitude=126.962156),
    CuratedPlaceConfig("머큐리에스프레소바", PlaceType.CAFE, latitude=37.525688, longitude=126.962247),
    # Activity - 요리주점 (BAR)
    CuratedPlaceConfig("용산오뎅", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.526407, longitude=126.963127),
]

_HUAM_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("인손 서울점", PlaceType.RESTAURANT, latitude=37.549864, longitude=126.977806),
    CuratedPlaceConfig("야스노야 본점", PlaceType.RESTAURANT, latitude=37.546727, longitude=126.978409),
    # 카페
    CuratedPlaceConfig("니트커피 아뜰리에", PlaceType.CAFE, latitude=37.552844, longitude=126.976806),
    CuratedPlaceConfig("패스로스터스", PlaceType.CAFE, latitude=37.553273, longitude=126.976713),
    CuratedPlaceConfig("자키러브", PlaceType.CAFE, latitude=37.551849, longitude=126.977197),
    CuratedPlaceConfig("오르소 에스프레소바", PlaceType.CAFE, latitude=37.548865, longitude=126.975955),
    CuratedPlaceConfig("우녹", PlaceType.CAFE, latitude=37.548403, longitude=126.976117),
    CuratedPlaceConfig("콤포타블 남산", PlaceType.CAFE, latitude=37.549006, longitude=126.983651),
    CuratedPlaceConfig("카페무니", PlaceType.CAFE, latitude=37.547192, longitude=126.983931),
    # Activity - 쇼핑 (SHOPPING) - 주방용품/생활소품
    CuratedPlaceConfig("시논샵 남산", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.548661, longitude=126.983544),
]

_SINDANG_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("처가집", PlaceType.RESTAURANT, latitude=37.553043, longitude=127.008205),
    CuratedPlaceConfig("도우소사이어티 약수점", PlaceType.RESTAURANT, latitude=37.555149, longitude=127.009971),
    CuratedPlaceConfig("만포막국수", PlaceType.RESTAURANT, latitude=37.555830, longitude=127.010319),
    CuratedPlaceConfig("신당주식", PlaceType.RESTAURANT, latitude=37.556770, longitude=127.011046),
    CuratedPlaceConfig("쿠부타야", PlaceType.RESTAURANT, latitude=37.556770, longitude=127.013191),
    CuratedPlaceConfig("라익스", PlaceType.RESTAURANT, latitude=37.557773, longitude=127.013771),
    CuratedPlaceConfig("파티파티", PlaceType.RESTAURANT, latitude=37.560760, longitude=127.012801),
    CuratedPlaceConfig("미국식 신당점", PlaceType.RESTAURANT, latitude=37.564451, longitude=127.013813),
    CuratedPlaceConfig("다케슬라이스", PlaceType.RESTAURANT, latitude=37.564158, longitude=127.010353),
    # 카페
    CuratedPlaceConfig("스티키플로어", PlaceType.CAFE, latitude=37.549818, longitude=127.007767),
    CuratedPlaceConfig("케고", PlaceType.CAFE, latitude=37.551572, longitude=127.007582),
    CuratedPlaceConfig("약수터", PlaceType.CAFE, latitude=37.552969, longitude=127.010231),
    CuratedPlaceConfig("리사르커피 약수점", PlaceType.CAFE, latitude=37.552475, longitude=127.010430),
    CuratedPlaceConfig("사이키델릭커피", PlaceType.CAFE, latitude=37.554035, longitude=127.008797),
    CuratedPlaceConfig("파오리", PlaceType.CAFE, latitude=37.552554, longitude=127.012007),
    CuratedPlaceConfig("카페와일드덕", PlaceType.CAFE, latitude=37.554913, longitude=127.008697),
    CuratedPlaceConfig("보헤이커피", PlaceType.CAFE, latitude=37.555446, longitude=127.007922),
    CuratedPlaceConfig("카페라츠오브", PlaceType.CAFE, latitude=37.557499, longitude=127.009103),
    CuratedPlaceConfig("코시아커피 약수점", PlaceType.CAFE, latitude=37.555973, longitude=127.013722),
    CuratedPlaceConfig("펄시커피", PlaceType.CAFE, latitude=37.559331, longitude=127.009643),
    # Activity - 칵테일바/와인바 (BAR)
    CuratedPlaceConfig("춘풍양조장", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.553306, longitude=127.009232),
    CuratedPlaceConfig("칠", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.556408, longitude=127.009031),
    # Activity - 쇼핑 (SHOPPING) - 음반/레코드샵
    CuratedPlaceConfig("모자이크", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.563449, longitude=127.011363),
]

_JANGCHUNG_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("콘드에뻬뻬", PlaceType.RESTAURANT, latitude=37.562209, longitude=127.007546),
    CuratedPlaceConfig("니키", PlaceType.RESTAURANT, latitude=37.560448, longitude=127.004835),
    # 카페
    CuratedPlaceConfig("홀베그", PlaceType.CAFE, latitude=37.561302, longitude=127.005343),
    CuratedPlaceConfig("타운폰드", PlaceType.CAFE, latitude=37.562563, longitude=127.004364),
]

_PILDONG_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("필동면옥", PlaceType.RESTAURANT, latitude=37.560398, longitude=126.996940),
    CuratedPlaceConfig("도우큐먼트", PlaceType.RESTAURANT, latitude=37.561992, longitude=126.991718),
    # 카페
    CuratedPlaceConfig("헤베커피", PlaceType.CAFE, latitude=37.558784, longitude=126.996012),
    CuratedPlaceConfig("빠마", PlaceType.CAFE, latitude=37.556410, longitude=126.995315),
    CuratedPlaceConfig("섹터커피 충무로점", PlaceType.CAFE, latitude=37.560942, longitude=126.993915),
    # Activity - 칵테일바 (BAR)
    CuratedPlaceConfig("디올드", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.561337, longitude=126.991681),
]

_CHUNGMURO_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("진심", PlaceType.RESTAURANT, latitude=37.562609, longitude=126.994069),
    CuratedPlaceConfig("카르보파스타바", PlaceType.RESTAURANT, latitude=37.562943, longitude=126.991398),
    CuratedPlaceConfig("사랑방칼국수", PlaceType.RESTAURANT, latitude=37.563267, longitude=126.991330),
    CuratedPlaceConfig("란주칼면", PlaceType.RESTAURANT, latitude=37.560977, longitude=126.982149),
    # 카페
    CuratedPlaceConfig("섬광", PlaceType.CAFE, latitude=37.562521, longitude=126.996328),
    CuratedPlaceConfig("네츠커피하우스", PlaceType.CAFE, latitude=37.562763, longitude=126.996217),
    CuratedPlaceConfig("캐시미어커피", PlaceType.CAFE, latitude=37.562878, longitude=126.992329),
    # Activity - 호프/요리주점 (BAR)
    CuratedPlaceConfig("소", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.562490, longitude=126.995125),
    CuratedPlaceConfig("중", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.562548, longitude=126.994934),
]

_CHODONG_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("떼르세로 코스테스", PlaceType.RESTAURANT, latitude=37.563319, longitude=126.991503),
    CuratedPlaceConfig("비카인드 반미", PlaceType.RESTAURANT, latitude=37.563788, longitude=126.992295),
    CuratedPlaceConfig("우메돈", PlaceType.RESTAURANT, latitude=37.564027, longitude=126.992712),
    CuratedPlaceConfig("올디스타코", PlaceType.RESTAURANT, latitude=37.565064, longitude=126.992935),
    # 카페
    CuratedPlaceConfig("섹터커피 을지로점", PlaceType.CAFE, latitude=37.564589, longitude=126.992642),
    # Activity - 일본식주점 (BAR)
    CuratedPlaceConfig("간빠진새 을지로점", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.565018, longitude=126.992205),
]

_EULJIRO_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("안동장", PlaceType.RESTAURANT, latitude=37.566085, longitude=126.991579),
    CuratedPlaceConfig("을지하옥", PlaceType.RESTAURANT, latitude=37.565414, longitude=126.991311),
    CuratedPlaceConfig("타마고", PlaceType.RESTAURANT, latitude=37.566105, longitude=126.986225),
    # 카페
    CuratedPlaceConfig("아사시", PlaceType.CAFE, latitude=37.566184, longitude=126.992360),
    CuratedPlaceConfig("로우커피스탠드 을지로점", PlaceType.CAFE, latitude=37.566374, longitude=126.988844),
    CuratedPlaceConfig("피그먼츠 을지로입구점", PlaceType.CAFE, latitude=37.566493, longitude=126.983681),
    # Activity - 이자카야 (BAR)
    CuratedPlaceConfig("토리카미", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.565328, longitude=126.991485),
]

_JEODONG_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("실비바 파도", PlaceType.RESTAURANT, latitude=37.565087, longitude=126.990334),
    CuratedPlaceConfig("지유켄", PlaceType.RESTAURANT, latitude=37.565281, longitude=126.990217),
    # 카페
    CuratedPlaceConfig("젤라또먼트 을지로", PlaceType.CAFE, latitude=37.565199, longitude=126.990060),
    CuratedPlaceConfig("콘웨이커피 을지로", PlaceType.CAFE, latitude=37.564506, longitude=126.988800),
    # Activity - 호프/요리주점 (BAR)
    CuratedPlaceConfig("네평반", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.564431, longitude=126.989899),
]

_GWANCHEOL_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("진중 우육면관 본점", PlaceType.RESTAURANT, latitude=37.568555, longitude=126.986111),
    CuratedPlaceConfig("아리계곡 종각점", PlaceType.RESTAURANT, latitude=37.569632, longitude=126.985398),
    CuratedPlaceConfig("손정보쌈 종로점", PlaceType.RESTAURANT, latitude=37.568929, longitude=126.986179),
    CuratedPlaceConfig("파작", PlaceType.RESTAURANT, latitude=37.568924, longitude=126.984057),
    # 카페
    CuratedPlaceConfig("노우즈 종로점 에스프레소바", PlaceType.CAFE, latitude=37.569753, longitude=126.984040),
    CuratedPlaceConfig("아마츄어작업실 청계점", PlaceType.CAFE, latitude=37.568639, longitude=126.988358),
    # Activity - 해물 술집 (BAR)
    CuratedPlaceConfig("해물점 종각직영점", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.568816, longitude=126.984660),
]

_CHEONGJIN_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("쌤쌤쌤 광화문점", PlaceType.RESTAURANT, latitude=37.570832, longitude=126.978915),
    CuratedPlaceConfig("폴리스 광화문D타워점", PlaceType.RESTAURANT, latitude=37.571068, longitude=126.978927),
    # 카페
    CuratedPlaceConfig("리사르커피 종로점", PlaceType.CAFE, latitude=37.570445, longitude=126.980366),
    CuratedPlaceConfig("조앤도슨 광화문점", PlaceType.CAFE, latitude=37.571104, longitude=126.981390),
    CuratedPlaceConfig("콤포타블 광화문", PlaceType.CAFE, latitude=37.572257, longitude=126.980344),
    # Activity - 일식 술집 (BAR)
    CuratedPlaceConfig("카린지린가네스낵바 광화문점", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.571860, longitude=126.980740),
]

_GONGPYEONG_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("백부장집닭한마리 본관", PlaceType.RESTAURANT, latitude=37.571797, longitude=126.982690),
    CuratedPlaceConfig("공평동꼼장어 본점", PlaceType.RESTAURANT, latitude=37.571811, longitude=126.982807),
    # 카페
    CuratedPlaceConfig("히트커피로스터스 센트로폴리스점", PlaceType.CAFE, latitude=37.571681, longitude=126.983530),
]

_GWONNONG_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("이다", PlaceType.RESTAURANT, latitude=37.577016, longitude=126.991713),
    CuratedPlaceConfig("도시바 서순라길점", PlaceType.RESTAURANT, latitude=37.576322, longitude=126.991447),
    # Activity - 펍/요리주점 (BAR)
    CuratedPlaceConfig("퀸즈가드", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.575403, longitude=126.991442),
    CuratedPlaceConfig("서울집시 서순라길점", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.575025, longitude=126.991555),
]

_UNNI_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("포카 안국", PlaceType.RESTAURANT, latitude=37.576186, longitude=126.989403),
    CuratedPlaceConfig("소마", PlaceType.RESTAURANT, latitude=37.575640, longitude=126.989727),
    CuratedPlaceConfig("루시드", PlaceType.RESTAURANT, latitude=37.575619, longitude=126.989512),
    # 카페
    CuratedPlaceConfig("텅", PlaceType.CAFE, latitude=37.577189, longitude=126.988161),
    # Activity - 쇼핑 (SHOPPING)
    CuratedPlaceConfig("레몬서울", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.577088, longitude=126.988453),
    # Activity - 칵테일바 (BAR)
    CuratedPlaceConfig("인공위성", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.576084, longitude=126.989464),
]

_GYEDONG_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("쿄와우동", PlaceType.RESTAURANT, latitude=37.578102, longitude=126.986591),
    # 카페
    CuratedPlaceConfig("어니언컴퍼니 안국점", PlaceType.CAFE, latitude=37.577632, longitude=126.986574),
    CuratedPlaceConfig("런던베이글뮤지엄 안국점", PlaceType.CAFE, latitude=37.579178, longitude=126.986200),
    CuratedPlaceConfig("카페 델 꼬또네 북촌계동점", PlaceType.CAFE, latitude=37.579412, longitude=126.987462),
    CuratedPlaceConfig("무에", PlaceType.CAFE, latitude=37.580854, longitude=126.986641),
    CuratedPlaceConfig("마녹", PlaceType.CAFE, latitude=37.581142, longitude=126.986867),
]

_JAEDONG_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("호이식", PlaceType.RESTAURANT, latitude=37.577847, longitude=126.986291),
    CuratedPlaceConfig("북촌김치재", PlaceType.RESTAURANT, latitude=37.577826, longitude=126.986211),
    CuratedPlaceConfig("신라제면 안국점", PlaceType.RESTAURANT, latitude=37.578231, longitude=126.986227),
    CuratedPlaceConfig("깡통만두", PlaceType.RESTAURANT, latitude=37.578165, longitude=126.986085),
    CuratedPlaceConfig("로우파이브 안국", PlaceType.RESTAURANT, latitude=37.578639, longitude=126.985578),
    # Activity - 일본식주점 (BAR)
    CuratedPlaceConfig("프루", PlaceType.ACTIVITY, ActivityKind.BAR, latitude=37.579421, longitude=126.984377),
    # Activity - 쇼핑 (SHOPPING) - 상품전시매장
    CuratedPlaceConfig("오늘의집 북촌", PlaceType.ACTIVITY, ActivityKind.SHOPPING, latitude=37.579250, longitude=126.984266),
]

_ANGUKDONG_PLACES: List[CuratedPlaceConfig] = [
    # 레스토랑
    CuratedPlaceConfig("동백식당", PlaceType.RESTAURANT, latitude=37.576538, longitude=126.984262),
    CuratedPlaceConfig("오레노라멘 인사점", PlaceType.RESTAURANT, latitude=37.576457, longitude=126.984559),
    # 카페
    CuratedPlaceConfig("공공재커피클럽", PlaceType.CAFE, latitude=37.577552, longitude=126.983672),
    CuratedPlaceConfig("도트블랭킷", PlaceType.CAFE, latitude=37.577026, longitude=126.984097),
    CuratedPlaceConfig("콤포타블 안국", PlaceType.CAFE, latitude=37.576838, longitude=126.984206),
    CuratedPlaceConfig("리와인드 서울", PlaceType.CAFE, latitude=37.575906, longitude=126.983446),
]

_PILDONG_WITH_CHUNGMURO: List[CuratedPlaceConfig] = _PILDONG_PLACES + _CHUNGMURO_PLACES
_ANGUK_COMBINED: List[CuratedPlaceConfig] = (
    _UNNI_PLACES + _GYEDONG_PLACES + _JAEDONG_PLACES + _ANGUKDONG_PLACES
)
_EULJIRO_COMBINED: List[CuratedPlaceConfig] = (
    _CHODONG_PLACES
    + _EULJIRO_PLACES
    + _JEODONG_PLACES
    + _GWANCHEOL_PLACES
    + _CHEONGJIN_PLACES
    + _GONGPYEONG_PLACES
    + _GWONNONG_PLACES
    + _UNNI_PLACES
    + _GYEDONG_PLACES
    + _JAEDONG_PLACES
    + _ANGUKDONG_PLACES
)
_SINDANG_WITH_JANGCHUNG: List[CuratedPlaceConfig] = (
    _SINDANG_PLACES
    + _JANGCHUNG_PLACES
    + _PILDONG_PLACES
    + _CHUNGMURO_PLACES
    + _CHODONG_PLACES
    + _EULJIRO_PLACES
    + _JEODONG_PLACES
    + _GWANCHEOL_PLACES
    + _CHEONGJIN_PLACES
    + _GONGPYEONG_PLACES
    + _GWONNONG_PLACES
    + _UNNI_PLACES
    + _GYEDONG_PLACES
    + _JAEDONG_PLACES
    + _ANGUKDONG_PLACES
)

_YEONNAM_WITH_DONGGYO: List[CuratedPlaceConfig] = _YEONNAM_PLACES + _DONGGYO_PLACES
_MANGWON_COMBINED: List[CuratedPlaceConfig] = (
    _MANGWON_PLACES + _SEONGSAN_PLACES + _HAPJEONG_PLACES + _SANGSU_PLACES + _SEOGYO_PLACES
)
_HAPJEONG_WITH_SANGSU: List[CuratedPlaceConfig] = (
    _HAPJEONG_PLACES + _SANGSU_PLACES + _SEOGYO_PLACES
)
_HANGANGNO_COMBINED: List[CuratedPlaceConfig] = _HANGANGNO_PLACES + _HANGANGNO3_PLACES
_HAEBANGCHON_WITH_HUAM: List[CuratedPlaceConfig] = _YONGSAN_PLACES + _HUAM_PLACES
_YONGSAN_COMBINED: List[CuratedPlaceConfig] = (
    _YONGSAN_PLACES + _HUAM_PLACES + _HANGANGNO_PLACES + _HANGANGNO3_PLACES
)

_CURATED_BY_AREA: Dict[str, List[CuratedPlaceConfig]] = {
    "성수": _SEONGSU_PLACES,
    "성수동": _SEONGSU_PLACES,
    "성수역": _SEONGSU_PLACES,
    "한남": _HANNAM_PLACES,
    "한남동": _HANNAM_PLACES,
    "연남": _YEONNAM_WITH_DONGGYO,
    "연남동": _YEONNAM_WITH_DONGGYO,
    "연남역": _YEONNAM_WITH_DONGGYO,
    "동교": _DONGGYO_PLACES,
    "동교동": _DONGGYO_PLACES,
    "연희": _YEONHUI_PLACES,
    "연희동": _YEONHUI_PLACES,
    "이태원": _ITAEWON_PLACES,
    "이태원동": _ITAEWON_PLACES,
    "이태원역": _ITAEWON_PLACES,
    "용산": _YONGSAN_COMBINED,
    "용산동": _YONGSAN_COMBINED,
    "해방촌": _HAEBANGCHON_WITH_HUAM,
    "후암": _HUAM_PLACES,
    "후암동": _HUAM_PLACES,
    "남산": _HUAM_PLACES,
    "한강로": _HANGANGNO_COMBINED,
    "한강로1가": _HANGANGNO_PLACES,
    "한강로3가": _HANGANGNO3_PLACES,
    "신용산": _HANGANGNO_PLACES,
    "신용산역": _HANGANGNO_PLACES,
    "용산역": _HANGANGNO3_PLACES,
    "논현": _NONHYEON_PLACES,
    "논현동": _NONHYEON_PLACES,
    "논현역": _NONHYEON_PLACES,
    "신사": _SINSA_PLACES,
    "신사동": _SINSA_PLACES,
    "신사역": _SINSA_PLACES,
    "가로수길": _SINSA_PLACES,
    "압구정": _APGUJEONG_PLACES,
    "압구정동": _APGUJEONG_PLACES,
    "압구정역": _APGUJEONG_PLACES,
    "청담": _CHEONGDAM_PLACES,
    "청담동": _CHEONGDAM_PLACES,
    "잠실": _JAMSIL_PLACES,
    "잠실동": _JAMSIL_PLACES,
    "잠실역": _JAMSIL_PLACES,
    "망원": _MANGWON_COMBINED,
    "망원동": _MANGWON_COMBINED,
    "망원역": _MANGWON_COMBINED,
    "성산": _SEONGSAN_PLACES,
    "성산동": _SEONGSAN_PLACES,
    "합정": _HAPJEONG_WITH_SANGSU,
    "합정동": _HAPJEONG_WITH_SANGSU,
    "합정역": _HAPJEONG_WITH_SANGSU,
    "상수": _SANGSU_PLACES,
    "상수동": _SANGSU_PLACES,
    "상수역": _SANGSU_PLACES,
    "서교": _SEOGYO_PLACES,
    "서교동": _SEOGYO_PLACES,
    "홍대": _SEOGYO_PLACES,
    "홍대입구": _SEOGYO_PLACES,
    "홍대입구역": _SEOGYO_PLACES,
    "신당": _SINDANG_WITH_JANGCHUNG,
    "신당동": _SINDANG_WITH_JANGCHUNG,
    "신당역": _SINDANG_WITH_JANGCHUNG,
    "약수": _SINDANG_WITH_JANGCHUNG,
    "약수역": _SINDANG_WITH_JANGCHUNG,
    "장충": _JANGCHUNG_PLACES,
    "장충동": _JANGCHUNG_PLACES,
    "동대입구": _JANGCHUNG_PLACES,
    "동대입구역": _JANGCHUNG_PLACES,
    "필동": _PILDONG_WITH_CHUNGMURO,
    "충무로": _CHUNGMURO_PLACES,
    "충무로역": _CHUNGMURO_PLACES,
    "초동": _CHODONG_PLACES,
    "을지로": _EULJIRO_COMBINED,
    "을지로4가": _CHODONG_PLACES,
    "을지로4가역": _CHODONG_PLACES,
    "을지로2가": _EULJIRO_PLACES,
    "을지로3가": _EULJIRO_PLACES,
    "을지로3가역": _EULJIRO_PLACES,
    "을지로입구": _EULJIRO_PLACES,
    "을지로입구역": _EULJIRO_PLACES,
    "저동": _JEODONG_PLACES,
    "저동2가": _JEODONG_PLACES,
    "관철": _GWANCHEOL_PLACES,
    "관철동": _GWANCHEOL_PLACES,
    "종각": _GWANCHEOL_PLACES,
    "종각역": _GWANCHEOL_PLACES,
    "청진": _CHEONGJIN_PLACES,
    "청진동": _CHEONGJIN_PLACES,
    "광화문": _CHEONGJIN_PLACES,
    "광화문역": _CHEONGJIN_PLACES,
    "공평": _GONGPYEONG_PLACES,
    "공평동": _GONGPYEONG_PLACES,
    "권농": _GWONNONG_PLACES,
    "권농동": _GWONNONG_PLACES,
    "서순라길": _GWONNONG_PLACES,
    "종로3가": _GWONNONG_PLACES,
    "종로3가역": _GWONNONG_PLACES,
    "익선동": _GWONNONG_PLACES,
    "운니": _UNNI_PLACES,
    "운니동": _UNNI_PLACES,
    "안국": _ANGUK_COMBINED,
    "안국역": _ANGUK_COMBINED,
    "계": _GYEDONG_PLACES,
    "계동": _GYEDONG_PLACES,
    "북촌": _GYEDONG_PLACES,
    "재": _JAEDONG_PLACES,
    "재동": _JAEDONG_PLACES,
    "안국동": _ANGUKDONG_PLACES,
}


def get_curated_configs(area: str) -> List[CuratedPlaceConfig]:
    return _CURATED_BY_AREA.get(area.strip(), [])
