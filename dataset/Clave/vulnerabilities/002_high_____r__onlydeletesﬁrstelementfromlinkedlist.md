# ❝❧❡❛r✭✮onlydeletesﬁrstelementfromlinkedlist

**Severity:** high
**Auditor:** Cantina
**Protocol:** Clave 
**Keywords:** linked list, delete, loop, iterator, advance, resetOwners, elements, temporary, for loop, solidity, function, clear, recovery, modules, definition, deletion, context, code, commit, verification

---

# ❝❧❡❛r✭✮onlydeletesﬁrstelementfromlinkedlist
**Severity:** High Risk  
**Context:** LinkedList.sol#L121-L130, LinkedList.sol#L292-L301  
**Description:** The linked list ❝❧❡❛r✭✮ functions have the following definition (using the ❆❞❞r❡ss▲✐♥❦❡❞▲✐st as an example):
\u0060\u0060\u0060
❢✉♥❝t✐♦♥ ❝❧❡❛r✭♠❛♣♣✐♥❣✭❛❞❞r❡ss ❂❃ ❛❞❞r❡ss✮ st♦r❛❣❡ s❡❧❢✮ ✐♥t❡r♥❛❧ ④
   ❢♦r ✭
       ❛❞❞r❡ss ❝✉rs♦r ❂ s❡❧❢❬❙❊◆❚■◆❊▲❴❆❉❉❘❊❙❙❪❀
       ✉✐♥t✶✻✵✭❝✉rs♦r✮ ❃ ❙❊◆❚■◆❊▲❴❯■◆❚❀
       ❝✉rs♦r ❂ s❡❧❢❬❝✉rs♦r❪
   ✮ ④
       ❞❡❧❡t❡ s❡❧❢❬❝✉rs♦r❪❀
   ⑥
   ❞❡❧❡t❡ s❡❧❢❬❙❊◆❚■◆❊▲❴❆❉❉❘❊❙❙❪❀
\u0060\u0060\u0060
## Improper Deletion in Loop
In this code, notice that the \u0060delete\u0060 statement will happen immediately before the \u0060advance\u0060 in the loop. Since \u0060delete\u0060 is being deleted before advancing, the loop will always exit after the first iteration, and the list won\u0027t be cleared as expected. As a consequence, the \u0060resetOwners\u0060 function (used by recovery modules) will not correctly clear the previous owners.

To properly delete all elements, use a temporary iterator value as follows:
\u0060\u0060\u0060solidity
iterator = list; 
while (iterator != 0) {
    iterator = list.next; 
    list = iterator;
}
\u0060\u0060\u0060

Alternatively, consider using a \u0060for\u0060 loop in a similar way:
\u0060\u0060\u0060solidity
for (iterator = list; iterator != 0; iterator = iterator.next) {
    list = iterator;
}
\u0060\u0060\u0060

Clave: Fixed in commit 2bba7a5e.  
CantinaManaged: Verified.
