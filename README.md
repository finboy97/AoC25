# AoC25

#### day 1
- Dreadful; I didn't remember wraparound indexing and tried vscode copilot for the first time - feel 10 iq worse off for having my errors shown by a bot. Still, had the right idea I suppose, but not the final execution.

#### day 2
- Much better - copilot firmly turned off. Definitely could be neater but it shows the steps I took thinking it through. Looking up later, I learned that instead of the concat string code I did, you can just do concatenated_string = string * repetitions. 

#### day 3
- Part 1 done using brute force method (itertools.combinations) - didn't work in part 2 once it had to do each possible combination of 12. Hint online suggested using stack instead, which I then implemented in an ugly way - could touch up but... eh, the problem is solved and won't be repeated.

#### day 4
- No sticking points today. Just a robotic typing of each grid location in relation to a coordinate and checking if it is a paper stack or not. Part 2 was able to reuse this.

#### day 5
- part 1 simple
- part 2 - spent a while thinking about linkedlist or tree to order ranges properly. Then saw a much better idea I hadn't thought of - sorting the list of ranges by range start after listing them all. After that logic is mine. Poor show.

#### day 6
- part 1 - fairly simple
- part 2 - once I decided to just flip the columnar numbers into their own list entry, then it was quite easy. Most happy that I didn't get any outside influence on my answer.