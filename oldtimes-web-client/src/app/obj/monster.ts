import { Creature, CreatureStats } from "./creature";

export class Monster extends Creature {
  constructor(name: string,
    uuid: string,
    private _kind: string,
    stats: CreatureStats
    ) 
  {
    super(name, stats, uuid)
  }

  public get kind() {
    return this._kind;
  }
}