class People {
    private static readonly Under16: Date = new Date(Date.now() - (15 * 365 * 24 * 60 * 60 * 1000));
    
    public name: string;
    public dob: Date;
    
    constructor(name: string, dob?: Date) {
        this.name = name;
        this.dob = dob || People.Under16;
    }
    
    public getName(): string {
        return this.name;
    }
    
    public getDOB(): Date {
        return this.dob;
    }
}

class BirthingUnit {
    /**
     * MaxItemsToRetrieve
     */
    private _people: People[];

    constructor() {
        this._people = [];
    }

    /**
     * GetPeoples
     * @param j
     * @returns List<object>
     */
    public getPeople(i: number): People[] {
        for (let j = 0; j < i; j++) {
            try {
                // Creates a dandon Name
                let name: string = "";
                const random = Math.random();
                if (Math.floor(random * 2) === 0) {
                    name = "Bob";
                } else {
                    name = "Betty";
                }
                // Adds new people to the list
                const age = Math.floor(Math.random() * (85 - 18) + 18) * 356;
                const birthDate = new Date(Date.now() - (age * 24 * 60 * 60 * 1000));
                this._people.push(new People(name, birthDate));
            } catch (e) {
                // Dont think this should ever happen
                throw new Error("Something failed in user creation");
            }
        }
        return this._people;
    }

    private getBobs(olderThan30: boolean): People[] {
        const thirtyYearsAgo = new Date(Date.now() - (30 * 356 * 24 * 60 * 60 * 1000));
        return olderThan30 
            ? this._people.filter(x => x.name === "Bob" && x.dob >= thirtyYearsAgo)
            : this._people.filter(x => x.name === "Bob");
    }

    public getMarried(p: People, lastName: string): string {
        if (lastName.includes("test"))
            return p.name;
        if ((p.name.length + lastName).length > 255) {
            (p.name + " " + lastName).substring(0, 255);
        }

        return p.name + " " + lastName;
    }
}

export { People, BirthingUnit };
