champdle = Champdle
champdle-index-subtitle = #{$puzzle_number}
champdle-rank-subtitle = Rank of #{$puzzle_number}

og-description = Guess today's Champion! Type a Champion name, it tells you how close you are.

language-locale-en = English
language-locale-ko = 한국어

guess-input-input = 
  .placeholder = Champion Name
guess-input-button = Guess

error-no-such-champion = No such Champion.
error-no-rank = No such Rank.
error-invalid-request = This request is not valid.
error-unknown = Unknown error.

guess-result-header-index = #
guess-result-header-name = Name
guess-result-header-similarity = Similarity
guess-result-header-formula = Breakdown
guess-result-header-rank = Rank

correct-guess = Found!

share-title = {champdle} #{$puzzle_number} Solved!
share-champion-name = Answer: {$name}

share-guess-count-title = Guesses
share-guess-count-value = {$value}
share-guess-count-average = Avg. {$value}

share-best-rank-title = Best Rank
share-best-rank-value = {$value}
share-best-rank-similarity = Similarity {$value}

share-streak-title = Streak
share-streak-value = {$value}
share-streak-best = Best {$value}

share-button = Share
share-hide-answer-checkbox-label = Hide answer
share-clipboard-text = {champdle} #{$puzzle_number} Solved!
  I found the Champion on { NUMBER($guess_count, type: "ordinal") ->
    [one] the {$guess_count}st guess
    [two] the {$guess_count}nd guess
    [few] the {$guess_count}rd guess
    *[other] the {$guess_count}th guess
  }.
  My best rank is {$best_rank}, and its similarity is {$best_similarity}.
share-clipboard-text-alert = Copied to clipboard.

show-rank-list-button = Show all ranks

faq-what-it-is-title = What is {champdle}?
faq-what-it-is-description = {champdle} is the game to guess today's Champion inspired by {$semantle_link}.
  If you guess today's Champion, {champdle} tells you how similar it is to the answer.
  .semantle-link-label = Semantle

faq-generation-title = What kinds of Champions are included?
faq-generation-description = It includes all League of Legends Champions. In total, there are {$number} Champions.

faq-show-info-title = Can I see the details of Champions?
faq-show-info-description = Yes, click on the Champion you guessed in the list to see the details.

faq-similarity-title = How does it calculate the similarity?
faq-similarity-description = Similarity is calculated on a 100-point total scale (Categories 80 pts + Stats 20 pts):
  1. Categories (80 pts / 7 items, ~11.43 pts each):
  - Region, Attack Type, Resource, Gender: 100% full points for exact match.
  - Species: 100% for exact match, 50% for partial match (e.g. Human/Cyborg vs Human).
  - Role (Tag 1 & 2): 100% for exact match, 80% for Tag 1 match, 70% for swapped match, 50% for Tag 2 partial match.
  - Release Order: Linear scaling based on release index difference (1 to 173).
  2. Stats (20 pts / 18 items, ~1.11 pts each):
  - Min-Max scaling across 18 numerical stats (HP, MP, Range, Movespeed, AD, AS, Armor, MR, Regen).

faq-once-per-day-title = Can I play more than once a day?
faq-once-per-day-description = Unfortunately, you can only play once a day.
  We believe the core of Wordle-like games is "Once a day, everyone has the same answer".

faq-yesterday-title = What was the answer yesterday?
faq-yesterday-description = It was {$name}. You can see the whole rank list {$yesterday_rank_link}.
  .yesterday-rank-link-label = here

faq-sort-title = Can I sort my guesses in a different way?
faq-sort-description = Yes, you can click on the header of the table to sort your guesses.

faq-source-code-title = Can I see the source code?
faq-source-code-description = Yes, you can check it out on {$source_code_link}.
  .source-code-link-label = {champdle} Github

faq-issue-title = Can I report an issue or give feedback?
faq-issue-description = Yes, please open an issue on {$issue_link}.
  .issue-link-label = {champdle} Github issue page

go-back-to-main = Go back to main page

champion-info-release-order = Release Order
champion-info-resource = Resource
champion-info-range = Range
champion-info-role-1 = Primary Role
champion-info-role-2 = Secondary Role
champion-info-gender = Gender
champion-info-species = Species
champion-info-region = Region
champion-info-attack-type = Attack Type
champion-info-hp = HP (Base/Max)
champion-info-mp = MP (Base/Max)
champion-info-hp-regen = HP Regen (Base/Max)
champion-info-mp-regen = MP Regen (Base/Max)
champion-info-movespeed = Move Speed
champion-info-attack-damage = Attack Damage (Base/Max)
champion-info-attack-speed = Attack Speed (Base/Max)
champion-info-armor = Armor (Base/Max)
champion-info-spellblock = Spell Block (Base/Max) (MR)