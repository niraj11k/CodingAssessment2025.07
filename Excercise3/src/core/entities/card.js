export default class Card {
    constructor(rank, suit) {
        // Ranks & suits used to generate filenames. User specified numeric ranks like '02'..'10'.
            const validRanks = ['02','03','04','05','06','07','08','09','10','J','Q','K','A'];
            const validSuits = ['spades','hearts','diamonds','clubs']; // Spades, Hearts, Diamonds, Clubs
            if (!validSuits.includes(suit))
                throw new Error('Invalid Suit');

            if (!validRanks.includes(rank))
                throw new Error('Invalid Rank');

            this.suit = suit;
            this.rank = rank;
    }
}