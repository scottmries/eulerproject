/* 

NOTE: THE ACTUAL SOLUTION IS FOR FOUR-SIDED DIE.

this should probably be solved from a small test case.

see if you can just solve the exact probably for Go, square 0, with a four-sided die, say.
how do you arrive at Go?
you can roll to it from any of its previous-1 15 squares. the rolls and combinations numbers of combinations are:
2: 1
3: 2
4: 3
5: 4
6: 3
7: 2
8: 1

16 (four squared) total possibilities

can this be solved by just building a huge set of linked lists?
for example, given only rolls as possibilites and a four-sided die and ignoring CC and CH for the moment, the only squares that could succeed Go are
2, 3, 4, 5, 6, 7, 8, and Jail
either by being rolled to directly or by three consecutive doubles
(since rolls here recur infinitely, at least theoretically, it's possible that a three-double is rolled from Go in all scenario, since the first, in which no rolls have been taken, is negligible).

the possibility space from Go to the next square then is:
Jail: 1/6 chance of a double, followed by 1/6 chance of another double, and 1/6 chance of a third double: (1/6)^3 chance
2: 1/16 * (5/6)^3
3: 2/16 * (5/6)^3
4: 3/16 * (5/6)^3
5: 4/16 * (5/6)^3
6: 3/16 * (5/6)^3
7: 2/16 * (5/6)^3
8: 1/16 * (5/6)^3

these probabilities at this point are now exact, except for the card squares, CC1 at 2, and CH1 at 7
there are 16 community chest cards, yielding 16! total combinations, but only 2 of these cards matter,
so relevant shuffles look like this:
Go _ _ _ Jail _ _ _ _ _ _ _ _ _ _ _
with go taking any of 16 initial positions, and Jail taking any of the remaining 15, 
there are only 16 choose 2 = 16!/14! = 16 * 15 = 240 relevant shuffles.
then we ask:
in how many of the relevant shuffles is Go at the top of the deck? 
Go is fixed in position, and Jail can take any of the remaining positions, so there are 15.
the same is true of Jail.
if we land on CC1, the chance that we will then move on to Go is 15 / 240 = 1 / 16
and 1 / 16 for Jail
and 14 / 16 to remain at CC1, which is index 2.
the probability space then from Go, factoring in Community Chest is

0 (Go): 1/16 * (5/6)^3 * 1/16
2: 1/16 * (5/6)^3 * 14/16
3: 2/16 * (5/6)^3
4: 3/16 * (5/6)^3
5: 4/16 * (5/6)^3
6: 3/16 * (5/6)^3
7: 2/16 * (5/6)^3
8: 1/16 * (5/6)^3
10 (Jail): 1/16 * (5/6)^3 * 1/16

now let's factor in Chance cards, of which there are 16.
each end state from Chance card is equally likely as those from Community Chest
Go
Jail
C1 (11)
E3 (24)
H2 (39)
R1 (5)
next R (5)
next R (5)
next U (12)
back 3 (37)
remain (7), six occurences

the Chance of landing on CH1 (7) to begin with is 2/16 * (5/6)^3, 
which is divided by 16 and given one share to end state above. 

Go: 2/16 * (5/6)^3 * 1 / 16
Jail: 2/16 * (5/6)^3 * 1 / 16
C1 (11): 2/16 * (5/6)^3 * 1 / 16
E3 (24): 2/16 * (5/6)^3 * 1 / 16
H2 (39): 2/16 * (5/6)^3 * 1 / 16
R1 (5): 2/16 * (5/6)^3 * 3 / 16 (three occurences)
next U (12): 2/16 * (5/6)^3 * 1 / 16
back 3 (37): 2/16 * (5/6)^3 * 1 / 16
remain (7): 2/16 * (5/6)^3 * 6 / 16 (six occurences)

these are then added to the previous possibilities, if any, 
except the Chance square, which is replaced with this possibility space

0 (Go): 1/16 * (5/6)^3 * 1/16 + 2/16 * (5/6)^3 * 1 / 16
2: 1/16 * (5/6)^3 * 14/16
3: 2/16 * (5/6)^3
4: 3/16 * (5/6)^3
5: 4/16 * (5/6)^3 + 2/16 * (5/6)^3 * 3 / 16
6: 3/16 * (5/6)^3
7: 2/16 * (5/6)^3 * 6 / 16
8: 1/16 * (5/6)^3
10 (Jail): 1/16 * (5/6)^3 * 1/16 + 2/16 * (5/6)^3 * 1 / 16
11: 2/16 * (5/6)^3 * 1 / 16
12: 2/16 * (5/6)^3 * 1 / 16
24: 2/16 * (5/6)^3 * 1 / 16
37: 2/16 * (5/6)^3 * 1 / 16
39: 2/16 * (5/6)^3 * 1 / 16

this is the complete possibility space of starting a turn at Go, which we can consider a zero state.
(nice that it's indexed zero)

the next step would be to find this possibility space for all 39 other squares, which is not so difficult to program

i think the necessary insight here, tho, is that although theoretically to obtain perfect accuracy we would need to run an infinite number of games,
since we know the exact possibility space of advancing from Go,
we can consider a unique sequence of possibilities P that begins on Go and ends on Go as a kind of closed loop.
and in considering all possible such closed loops, we can find the complete (and exact, since it will be rational), possibility space of the board

the above paragraph is not true. it's possible to roll an infinite number of times and never return to Go

it's also possible to roll a closed loop from Jail to Jail, if you were stuck in any of an infinite variety of Sisyphian infinite consecutive triple rolls

then question then is: what constitutes a closed loop?
starting at and then landing on or passing Go. 
since the only way to move backward in the game is via one Chance card that sends back three squares but is more than three squares from the start,
that can not affect whether or not Go has been decidedly passed.

so the strategy is this:
determine the probability for ending squares from Go

*/

// const dieSides = 4;

// const nonDoubleRolls = {
//     2: 1,
//     3: 2,
//     4: 3,
//     5: 4,
//     6: 3,
//     7: 2,
//     8: 1,
// }

// test 6-sided die

const dieSides = 6;

const nonDoubleRolls = {
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 6,
    8: 5,
    9: 4,
    10: 3,
    11: 2,
    12: 1,
}

const chanceOfTripleDoubles = 1 / (dieSides * dieSides * dieSides);

const squares = [];

for(var i = 0; i < 40; i++) {
    let value = 'common';
    switch (i) {
        case 0:
            value = 'GO';
            break;
        case 2:
        case 17:
        case 33:
            value = 'CC';
            break;
        case 5:
        case 15:
        case 25:
        case 35:
            value = 'R';
            break;
        case 7:
        case 22:
        case 36:
            value = 'CH';
            break;
        case 10:
            value = 'JAIL';
            break;
        case 12:
        case 28:
            value = 'U';
            break;
    }
    let nextSquareProbabilities = [];
    for(var j = 0; j < 40; j++) {
        nextSquareProbabilities[j] = 0.0;
    }
    squares[i] = {
        name: value,
        nextSquareProbabilities
    };
}

// account for rolls

squares.map((square, index) => {
    square.nextSquareProbabilities[10] = chanceOfTripleDoubles;
    const remainingProbability = 1 - chanceOfTripleDoubles;
    Object.entries(nonDoubleRolls).forEach(([value, combinations]) => {
        square.nextSquareProbabilities[(index + parseInt(value)) % 40] = remainingProbability * combinations / Object.keys(nonDoubleRolls).length;
    })
    return square;
})

// account for Chance and Community Chest

squares.map((square, index) => {
    square.nextSquareProbabilities.map((previousProbability, nextIndex) => {
        if (squares[nextIndex].name === 'CC') {
            square.nextSquareProbabilities[0] += previousProbability / 16.0;
            square.nextSquareProbabilities[10] += previousProbability / 16.0;
            square.nextSquareProbabilities[index] = 14.0 * previousProbability / 16.0;
        }
        if (squares[nextIndex].name === 'CH') {
            let nextR = index;
            while(squares[nextR].name !== 'R') {
                nextR = (nextR + 1) % 40;
            }
            let nextU = index;
            while(squares[nextU].name !== 'U') {
                nextU = (nextU + 1) % 40;
            }
            const threeBack = (index + 40 - 3) % 40;
            square.nextSquareProbabilities[0] += previousProbability / 16.0;
            square.nextSquareProbabilities[10] += previousProbability / 16.0;
            square.nextSquareProbabilities[11] += previousProbability / 16.0;
            square.nextSquareProbabilities[24] += previousProbability / 16.0;
            square.nextSquareProbabilities[39] += previousProbability / 16.0;
            square.nextSquareProbabilities[5] += previousProbability / 16.0;
            square.nextSquareProbabilities[nextR] += 2.0 * previousProbability / 16.0;
            square.nextSquareProbabilities[nextU] += previousProbability / 16.0;
            square.nextSquareProbabilities[threeBack] += previousProbability / 16.0;
            square.nextSquareProbabilities[index] = 6.0 * previousProbability / 16.0;
        }
    })
})

// i think we need some path-finding function here

const finalProbabilities = []

for(var i = 0; i < 40; i++) {
    let finalProbability = 0.0;
    squares.map(square => {
        finalProbability += square.nextSquareProbabilities[i];
    });
    finalProbabilities[i] = finalProbability;
}

const finalProbabilitiesSorted = [...finalProbabilities];

finalProbabilitiesSorted.sort().reverse();

console.log(finalProbabilitiesSorted);

for(var i = 0; i < 3; i++) {
    console.log(finalProbabilities.indexOf(finalProbabilitiesSorted[i]));
}