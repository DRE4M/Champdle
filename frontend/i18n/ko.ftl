champdle = Champdle
champdle-index-subtitle = #{$puzzle_number}
champdle-rank-subtitle = #{$puzzle_number} 전체 순위

og-description = 오늘의 챔피언을 맞춰보세요! 유사도는 카테고리 7종(80점) + 스탯 18종 Min-Max(20점) 총 100점 기준입니다. 훈협지 화이팅!

language-locale-en = English
language-locale-ko = 한국어

guess-input-input = 
  .placeholder = 챔피언 이름
guess-input-button = 추측하기

error-no-such-champion = 잘못된 챔피언 이름입니다.
error-no-rank = 잘못된 순위 정보입니다.
error-invalid-request = 잘못된 요청입니다.
error-unknown = 알 수 없는 오류입니다.

guess-result-header-index = #
guess-result-header-name = 이름
guess-result-header-similarity = 유사도
guess-result-header-formula = 계산 구성
guess-result-header-rank = 순위

correct-guess = 정답!

share-title = {champdle} #{$puzzle_number} 성공!
share-champion-name = 정답: {$name}

share-guess-count-title = 추측 횟수
share-guess-count-value = {$value}회
share-guess-count-average = 평균 {$value}회

share-best-rank-title = 최고 유사 순위
share-best-rank-value = {$value}위
share-best-rank-similarity = 유사도 {$value}

share-streak-title = 연속 정답
share-streak-value = {$value}회
share-streak-best = 최고기록 {$value}회

share-button = 공유하기
share-hide-answer-checkbox-label = 정답 숨기기
share-clipboard-text = {champdle} #{$puzzle_number} 성공!
  {$guess_count}번째 추측에서 챔피언을 맞췄습니다.
  가장 유사한 추측의 순위는 {$best_rank}위이며, 유사도는 {$best_similarity}입니다.
share-clipboard-text-alert = 결과를 클립보드에 복사했습니다.

show-rank-list-button = 전체 순위 보기

faq-what-it-is-title = {champdle}이 뭔가요?
faq-what-it-is-description = {champdle}은 오늘의 챔피언을 맞추는 게임입니다.
  오늘의 챔피언을 추측하면, 추측한 챔피언이 정답 챔피언과 얼마나 비슷한지 알려줍니다.
  {champdle}은 {$semantle_link}에서 영감을 받아 만들어졌습니다.
  .semantle-link-label = Semantle

faq-generation-title = 어떤 챔피언이 포함되어 있나요?
faq-generation-description = 리그 오브 레전드의 모든 챔피언 총 {$number} 명이 포함되어 있습니다.

faq-show-info-title = 챔피언의 상세 정보를 볼 수 있나요?
faq-show-info-description = 네. 추측한 챔피언을 목록에서 클릭하면 상세 정보가 표시됩니다.

faq-similarity-title = 유사도는 어떻게 계산하나요?
faq-similarity-description = 유사도는 총 100점 만점(카테고리 7종 80점 + 스탯 18종 20점)을 기준으로 가중치 산출됩니다:
  1. 카테고리 항목 (총 80점 만점 / 희귀도 가중치 반영)
  - 소속 지역 (18점) & 종족 (18점): 14개 지역 및 다양한 종족 중 희귀 일치 시 18점 부여 (종족 부분 일치 9점)
  - 역할군 1·2 (15점): 주/부 순서·종류 완벽 일치 15점(100%), 주역할 12점(80%), 주/부 교차 10.5점(70%), 부역할 부분 7.5점(50%)
  - 자원 유형 (12점): 마나/기력/노마나 등 일치 시 12점
  - 공격 방식 (7점) & 성별 (5점): 선택지 수가 적어 각 7점, 5점 반영
  - 출시 순서 (5점): 1번부터 173번까지 순서 격차(Min-Max) 비율로 최대 5점 반영 (격차 조정 하향)
  2. 스탯 항목 (총 20점 만점 / 핵심 스탯 가중치 반영)
  - 핵심 스탯 가중치: 이동속도(4.0점), 사거리(4.0점)에 높은 가중치 부여 (두 항목 총 8.0점)
  - 기타 스탯: 체력, 마나, 공격력, 방어력, 마저, 재생력 등 나머지 16개 능력치는 각 0.75점씩 반영됩니다 (총 12.0점).

faq-once-per-day-title = 하루에 한 번 이상 플레이할 수 있나요?
faq-once-per-day-description = 아니오. 하루에 한 번만 플레이할 수 있습니다.
  저희는 Wordle과 같은 게임의 핵심 요소는 "하루에 한 번만, 모두가 동일한 정답"이라고 생각합니다.

faq-yesterday-title = 어제의 정답은 뭐였나요?
faq-yesterday-description = {$name} 입니다. 전체 순위 목록은 {$yesterday_rank_link}에서 볼 수 있습니다.
  .yesterday-rank-link-label = 여기

faq-sort-title = 내 추측을 다른 방식으로 정렬할 수 있나요?
faq-sort-description = 네. 추측 목록 상단 헤더를 클릭하여 정렬 방식을 변경할 수 있습니다.

faq-source-code-title = 소스 코드를 확인할 수 있나요?
faq-source-code-description = {$source_code_link}에서 확인할 수 있습니다.
  .source-code-link-label = {champdle} Github

faq-issue-title = 다른 질문이나 피드백은 어떻게 보내나요?
faq-issue-description = {$issue_link}에서 문의해주세요.
  .issue-link-label = {champdle} Github 이슈

go-back-to-main = 메인 페이지로 돌아가기

champion-info-release-order = 출시 순서
champion-info-resource = 자원
champion-info-range = 사거리
champion-info-role-1 = 역할군 1
champion-info-role-2 = 역할군 2
champion-info-gender = 성별
champion-info-species = 종족
champion-info-region = 소속 지역
champion-info-attack-type = 공격 방식
champion-info-hp = 체력 (기본/최대)
champion-info-mp = 마나 (기본/최대)
champion-info-hp-regen = 체력 재생 (기본/최대)
champion-info-mp-regen = 마나 재생 (기본/최대)
champion-info-movespeed = 이동 속도
champion-info-attack-damage = 공격력 (기본/최대)
champion-info-attack-speed = 공격 속도 (기본/최대)
champion-info-armor = 방어력 (기본/최대)
champion-info-spellblock = 마법 저항력 (기본/최대)

# Champion Names

champion-name-annie = 애니
champion-name-olaf = 올라프
champion-name-galio = 갈리오
champion-name-twisted-fate = 트위스티드 페이트
champion-name-xin-zhao = 신 짜오
champion-name-urgot = 우르곳
champion-name-leblanc = 르블랑
champion-name-vladimir = 블라디미르
champion-name-fiddlesticks = 피들스틱
champion-name-kayle = 케일
champion-name-master-yi = 마스터 이
champion-name-alistar = 알리스타
champion-name-ryze = 라이즈
champion-name-sion = 사이온
champion-name-sivir = 시비르
champion-name-soraka = 소라카
champion-name-teemo = 티모
champion-name-tristana = 트리스타나
champion-name-warwick = 워윅
champion-name-nunu-willump = 누누와 윌럼프
champion-name-miss-fortune = 미스 포츈
champion-name-ashe = 애쉬
champion-name-tryndamere = 트린다미어
champion-name-jax = 잭스
champion-name-morgana = 모르가나
champion-name-zilean = 질리언
champion-name-singed = 신지드
champion-name-evelynn = 이블린
champion-name-twitch = 트위치
champion-name-karthus = 카서스
champion-name-cho-gath = 초가스
champion-name-amumu = 아무무
champion-name-rammus = 람머스
champion-name-anivia = 애니비아
champion-name-shaco = 샤코
champion-name-dr-mundo = 문도 박사
champion-name-sona = 소나
champion-name-kassadin = 카사딘
champion-name-irelia = 이렐리아
champion-name-janna = 잔나
champion-name-gangplank = 갱플랭크
champion-name-corki = 코르키
champion-name-karma = 카르마
champion-name-taric = 타릭
champion-name-veigar = 베이가
champion-name-trundle = 트런들
champion-name-swain = 스웨인
champion-name-caitlyn = 케이틀린
champion-name-blitzcrank = 블리츠크랭크
champion-name-malphite = 말파이트
champion-name-katarina = 카타리나
champion-name-nocturne = 녹턴
champion-name-maokai = 마오카이
champion-name-renekton = 레넥톤
champion-name-jarvan-iv = 자르반 4세
champion-name-elise = 엘리스
champion-name-orianna = 오리아나
champion-name-wukong = 오공
champion-name-brand = 브랜드
champion-name-lee-sin = 리 신
champion-name-vayne = 베인
champion-name-rumble = 럼블
champion-name-cassiopeia = 카시오페아
champion-name-skarner = 스카너
champion-name-heimerdinger = 하이머딩거
champion-name-nasus = 나서스
champion-name-nidalee = 니달리
champion-name-udyr = 우디르
champion-name-poppy = 뽀삐
champion-name-gragas = 그라가스
champion-name-pantheon = 판테온
champion-name-ezreal = 이즈리얼
champion-name-mordekaiser = 모데카이저
champion-name-yorick = 요릭
champion-name-akali = 아칼리
champion-name-kennen = 케넨
champion-name-garen = 가렌
champion-name-leona = 레오나
champion-name-malzahar = 말자하
champion-name-talon = 탈론
champion-name-riven = 리븐
champion-name-kog-maw = 코그모
champion-name-shen = 쉔
champion-name-lux = 럭스
champion-name-xerath = 제라스
champion-name-shyvana = 쉬바나
champion-name-ahri = 아리
champion-name-graves = 그레이브즈
champion-name-fizz = 피즈
champion-name-volibear = 볼리베어
champion-name-rengar = 렝가
champion-name-varus = 바루스
champion-name-nautilus = 노틸러스
champion-name-viktor = 빅토르
champion-name-sejuani = 세주아니
champion-name-fiora = 피오라
champion-name-ziggs = 직스
champion-name-lulu = 룰루
champion-name-draven = 드레이븐
champion-name-hecarim = 헤카림
champion-name-kha-zix = 카직스
champion-name-darius = 다리우스
champion-name-jayce = 제이스
champion-name-lissandra = 리산드라
champion-name-diana = 다이애나
champion-name-quinn = 퀸
champion-name-syndra = 신드라
champion-name-aurelion-sol = 아우렐리온 솔
champion-name-kayn = 케인
champion-name-zoe = 조이
champion-name-zyra = 자이라
champion-name-kai-sa = 카이사
champion-name-seraphine = 세라핀
champion-name-gnar = 나르
champion-name-zac = 자크
champion-name-yasuo = 야스오
champion-name-vel-koz = 벨코즈
champion-name-taliyah = 탈리야
champion-name-camille = 카밀
champion-name-akshan = 아크샨
champion-name-bel-veth = 벨베스
champion-name-braum = 브라움
champion-name-jhin = 진
champion-name-kindred = 킨드레드
champion-name-zeri = 제리
champion-name-jinx = 징크스
champion-name-tahm-kench = 탐 켄치
champion-name-briar = 브라이어
champion-name-viego = 비에고
champion-name-senna = 세나
champion-name-lucian = 루시안
champion-name-zed = 제드
champion-name-kled = 클레드
champion-name-ekko = 에코
champion-name-qiyana = 키아나
champion-name-vi = 바이
champion-name-aatrox = 아트록스
champion-name-nami = 나미
champion-name-azir = 아지르
champion-name-yuumi = 유미
champion-name-samira = 사미라
champion-name-thresh = 쓰레쉬
champion-name-illaoi = 일라오이
champion-name-rek-sai = 렉사이
champion-name-ivern = 아이번
champion-name-kalista = 칼리스타
champion-name-bard = 바드
champion-name-rakan = 라칸
champion-name-xayah = 자야
champion-name-ornn = 오른
champion-name-sylas = 사일러스
champion-name-neeko = 니코
champion-name-aphelios = 아펠리오스
champion-name-rell = 렐
champion-name-pyke = 파이크
champion-name-vex = 벡스
champion-name-yone = 요네
champion-name-ambessa = 암베사
champion-name-mel = 멜
champion-name-yunara = 유나라
champion-name-locke = 로크
champion-name-sett = 세트
champion-name-lillia = 릴리아
champion-name-gwen = 그웬
champion-name-renata-glasc = 레나타 글라스크
champion-name-aurora = 오로라
champion-name-nilah = 닐라
champion-name-k-sante = 크산테
champion-name-smolder = 스몰더
champion-name-milio = 밀리오
champion-name-zaahen = 자헨
champion-name-hwei = 흐웨이
champion-name-naafiri = 나피리
