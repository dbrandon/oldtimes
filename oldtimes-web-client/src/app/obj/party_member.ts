import { Creature, CreatureStats } from "./creature";


export class PartyMember extends Creature {

  constructor(name: string,
    stats: CreatureStats,
    uuid: string,
    private _cls: string) {
    super(name, stats, uuid);
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