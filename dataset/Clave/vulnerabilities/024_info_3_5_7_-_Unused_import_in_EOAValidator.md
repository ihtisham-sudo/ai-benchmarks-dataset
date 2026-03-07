# 3.5.7 - Unused import in EOAValidator

**Severity:** info
**Auditor:** Cantina
**Protocol:** Clave 
**Keywords:** import, unused, code cleanup, refactoring, EOAValidator, smart contract, programming, software design, best practices, development, code review, bug prevention, maintenance, optimization, performance, clarity, readability, efficiency, modularity, dependency management

---

# 3.5.7  Linked list iteration can be simplified
**Severity:** Informational  
**Context:** LinkedList.sol  
**Description:** In the two linked list libraries, the r❡♣❧❛❝❡✭✮, r❡♠♦✈❡✭✮, ❝❧❡❛r✭✮, s✐③❡✭✮ and ❧✐st✭✮ functions traverse the linked list using a ❝✉rs♦r that is initialized to s❡❧❢❬❙❊◆❚■◆❊▲❴❱❆▲❯❊❪ (where ❙❊◆❚■◆❊▲❴✲ ❱❆▲❯❊ is either ❙❊◆❚■◆❊▲❴❇❨❚❊❙ or ❙❊◆❚■◆❊▲❴❆❉❉❘❊❙❙, depending on which version you are using). In the particular case of r❡♣❧❛❝❡✭✮ and r❡♠♦✈❡✭✮, the main loop checks whether s❡❧❢❬❝✉rs♦r❪ equals the value of interest, and if so, it updates the linked list. This means that the first loop iteration will inspect s❡❧❢❬s❡❧❢❬❙❊◆❚■◆❊▲❴❱❆▲❯❊❪❪, which is the second value in the list. Since the linked list is in a loop, this doesn\u0027t actually cause problems, because the first value will eventually be reached. However, this behavior is counter-intuitive and could be prevented by initializing the traversal one step backward.  
**Recommendation:** For the r❡♣❧❛❝❡✭✮ and r❡♠♦✈❡✭✮ functions, consider initializing the ❝✉rs♦r to ❙❊◆✲ ❚■◆❊▲❴❱❆▲❯❊ instead of s❡❧❢❬❙❊◆❚■◆❊▲❴❱❆▲❯❊❪.  
**Clave:** Fixed with commits 2bba7a5e and ed64e82e.  
**CantinaManaged:** Verified.
**Severity:** Informational  
**Context:** ERC20Paymaster.sol#L60-L63  
**Description:** ❊❘❈✷✵P❛②♠❛st❡r\u0027s constructor skips for tokens for which wrong data has been passed (zero address or out-of-range ♣r✐❝❡▼❛r❦✉♣):  
❝♦♥str✉❝t♦r✭❚♦❦❡♥■♥♣✉t❬❪ ♠❡♠♦r② t♦❦❡♥s✮ ④  
   ❢♦r ✭✉✐♥t✷✺✻ ✐ ❂ ✵❀ ✐ ❁ t♦❦❡♥s✳❧❡♥❣t❤❀ ✐✰✰✮ ④  
       ✴✴ ❙❦✐♣ ③❡r♦✲❛❞❞r❡ss❡s  
       ✐❢ ✭t♦❦❡♥s❬✐❪✳t♦❦❡♥❆❞❞r❡ss ❂❂ ❛❞❞r❡ss✭✵✮✮ ❝♦♥t✐♥✉❡❀  
       ✴✴ ❙❦✐♣ ❢❛❧s❡ ♠❛r❦✉♣ ✈❛❧✉❡s  
       ✐❢ ✭t♦❦❡♥s❬✐❪✳♣r✐❝❡▼❛r❦✉♣ ❁ ✺✵✵✵ ⑤⑤ t♦❦❡♥s❬✐❪✳♣r✐❝❡▼❛r❦✉♣ ❃❂ ✶✵✵✵✵✵✮ ❝♦♥t✐♥✉❡❀  
       ✉✐♥t✶✾✷ ♣r✐❝❡▼❛r❦✉♣ ❂ ✉✐♥t✶✾✷✭t♦❦❡♥s❬✐❪✳♣r✐❝❡▼❛r❦✉♣ ✯ ✭▼❆❘❑❯P❴◆❖▼■◆❆❚❖❘ ✴ ✶❡✹✮✮❀  
       ❛❧❧♦✇❡❞❚♦❦❡♥s❬t♦❦❡♥s❬✐❪✳t♦❦❡♥❆❞❞r❡ss❪ ❂ ❚♦❦❡♥❉❛t❛✭t♦❦❡♥s❬✐❪✳❞❡❝✐♠❛❧s✱ ♣r✐❝❡▼❛r❦✉♣✮❀  
   ⑥  
   ⑥  
It\u0027s better to revert for incorrect arguments as a safety measure. It may indicate towards a problem with how those arguments were generated.  
**Recommendation:** Revert instead of skipping tokens with incorrect data:  
   ✴✴ ❙❦✐♣ ③❡r♦✲❛❞❞r❡ss❡s  
   ✲ ✐❢ ✭t♦❦❡♥s❬✐❪✳t♦❦❡♥❆❞❞r❡ss ❂❂ ❛❞❞r❡ss✭✵✮✮ ❝♦♥t✐♥✉❡❀  
   ✰ ✐❢ ✭t♦❦❡♥s❬✐❪✳t♦❦❡♥❆❞❞r❡ss ❂❂ ❛❞❞r❡ss✭✵✮✮ r❡✈❡rt❀  
   ✴✴ ❙❦✐♣ ❢❛❧s❡ ♠❛r❦✉♣ ✈❛❧✉❡s  
   ✲ ✐❢ ✭t♦❦❡♥s❬✐❪✳♣r✐❝❡▼❛r❦✉♣ ❁ ✺✵✵✵ ⑤⑤ t♦❦❡♥s❬✐❪✳♣r✐❝❡▼❛r❦✉♣ ❃❂ ✶✵✵✵✵✵✮ ❝♦♥t✐♥✉❡❀  
   ✰ ✐❢ ✭t♦❦❡♥s❬✐❪✳♣r✐❝❡▼❛r❦✉♣ ❁ ✺✵✵✵ ⑤⑤ t♦❦❡♥s❬✐❪✳♣r✐❝❡▼❛r❦✉♣ ❃❂ ✶✵✵✵✵✵✮ r❡✈❡rt❀  
**Clave:** Fixed in PR 716.  
**Cantina Managed:** Verified.  

**Severity:** Informational  
**Context:** ERC20Paymaster.sol#L226-L230  
**Description:** ❝❛❧❧❖r❛❝❧❡✭✮ returns ✉✐♥t✷✺✻ but its Natspec says it returns ✉✐♥t✷✺✻❬❪.  
**Recommendation:** Fix the Natspec.  
**Clave:** Fixed in PR 716.  
**Cantina Managed:** Verified.  

**Severity:** Informational  
**Context:** EOAValidator.sol#L5  
**Description:** Following import is not used and can be removed:  
✐♠♣♦rt ④❚r❛♥s❛❝t✐♦♥⑥ ❢r♦♠ ✬❅♠❛tt❡r❧❛❜s✴③❦s②♥❝✲❝♦♥tr❛❝ts✴❧✷✴s②st❡♠✲❝♦♥tr❛❝ts✴❧✐❜r❛r✐❡s✴❚r❛♥s❛❝t✐♦♥❍❡❧♣❡r✳s♦❧✬❀  
**Recommendation:** Remove the import.  
**Clave:** Fixed with commit 9b22c453.  
**Cantina Managed:** Verified.
PAGE END
