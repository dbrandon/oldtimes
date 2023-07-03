
export class Scenario {
  constructor(
    private _name: string,
    private _id: string
  ) {}

  public get id() {
    return this._id;
  }

  public get name() {
    return this._name;
  }
};