import { Creature, CreatureStats } from "./creature";


export class PartyMember extends Creature {

  constructor(name: string,
    stats: CreatureStats,
    private _cls: string) {
    super(name, stats);
  }

  public get cls() {
    return this._cls;
  }
};

export class Party {
  private _members: PartyMember[] = [];

  public get members() {
    return this._members;
  }
}