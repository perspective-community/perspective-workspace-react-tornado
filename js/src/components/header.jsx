import React from "react";

function Header(props) {
  const {layout, layouts} = props;
  const {changeLayout, changeLayouts} = props;

  return (
    <div className="header">
      <h1>Perspective / React / Tornado</h1>
      <div>
        <select
          className="layout_config"
          onChange={(e) => {
            changeLayout(e.target.value);
          }}
          value={layout}
        >
          {Object.keys(layouts).map((k) => (
            <option key={k} value={k}>
              {k}
            </option>
          ))}
        </select>
        <button
          className="text_button"
          type="button"
          onClick={async () => {
            const workspace = document.getElementById("workspace");
            const modifiedConfig = await workspace.save();

            window.localStorage.setItem("perspective_workspace_react_tornado_demo", JSON.stringify(modifiedConfig));

            changeLayouts({...layouts, "Custom Layout": modifiedConfig});
            changeLayout("Custom Layout");
          }}
        >
          Save Layout
        </button>
      </div>
    </div>
  );
}

export default Header;
