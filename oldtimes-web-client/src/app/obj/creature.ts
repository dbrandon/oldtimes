

export class CreatureStats {
  private _health : number = 0;
  private _mana : number = 0;

  constructor(
    private _strength: number,
    private _intellect: number,
    private _endurance: number) {}

  public get health() {
    return this._health;
  }
  public set health(health: number) {
    this._health = health;
  }

  public get mana() {
    return this._mana;
  }

  public get strength() {
    return this._strength;
  }
  protected set strength(strength: number) {
    this._strength = strength;
  }

  public get intellect() {
    return this._intellect;
  }
  protected set intellect(intellect: number) {
    this._intellect = intellect;
  }

  public get endurance() {
    return this._endurance;
  }
  protected set endurance(endurance: number) {
    this._endurance = endurance;
  }
}

export class Creature {
  constructor(private _name: string,
    private _stats: CreatureStats,
    private _uuid: string) {}

  public get name() {
    return this._name;
  }

  public get stats() {
    return this._stats;
  }

  public get uuid() {
    return this._uuid;
  }
}