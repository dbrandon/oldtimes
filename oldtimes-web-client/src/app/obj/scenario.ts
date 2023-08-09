
export class ScenarioInfo {
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


export class ScenarioAction {
  constructor(private _name: string) {

  }

  public get name() {
    return this._name;
  }
}

class ScenarioEvent {
  constructor(private _text: string) {}

  public get text() {
    return this._text;
  }
}

export class ScenarioStatus {
  constructor(
    private _roomName: string,
    private _events: ScenarioEvent[],
    private _actions: ScenarioAction[]) {}

  public get actions() {
    return this._actions;
  }

  public get roomName() {
    return this._roomName;
  }

  public get events() {
    return this._events;
  }
}