import { Link, Store } from "../store/model";
import { Logger } from "../logger";
import { Config } from "../config";
import { PythonShell } from "python-shell";

const python = Config.notifications.python;

export function sendToPython(link: Link, store: Store) {
  const { openCartAction, screenshot, ...data } = link;
  Logger.info("↗ opening Python shell");

  const pyshell: PythonShell = new PythonShell(python.script_path, {
    pythonPath: python.interpreter,
  });
  pyshell.send(JSON.stringify(data));
  pyshell.on("message", (msg: string) => Logger.info(msg));
  pyshell.end((err: any) => {
    if (err) throw err;
    Logger.info("✔ finished running Python script");
  });
}
