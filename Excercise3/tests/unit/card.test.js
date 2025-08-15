test('Card creation validates suit and value', () =>{

    expect(() => new Card('Spades', 5)). toThrow();
    expect(() => new Card('Heart', 'A')).not.toThrow();
});