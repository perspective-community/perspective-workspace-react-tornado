import React, {useState} from "react";
import ReactDOM from "react-dom";
import perspective from "@finos/perspective";

import "@finos/perspective-workspace";
import "@finos/perspective-viewer-datagrid";
import "@finos/perspective-viewer-d3fc";

import Header from "./components/header";
import Footer from "./components/footer";
import Workspace from "./components/workspace";

import default_layout from "./layouts/default.json";

import "./index.css";
import "@finos/perspective-workspace/dist/umd/material.css";

function App() {
  /**
   * Tables
   */
  const websocket = perspective.websocket(`ws://${window.location.host}/websocket`);
  const defaultTables = {
    superstore: websocket.open_table("superstore"),
  };

  /**
   * Layout
   */
  const possibleCustomLayout = window.localStorage.getItem("perspective_workspace_react_tornado_demo");
  const [layout, changeLayout] = useState("Default");
  const [layouts, changeLayouts] = useState({
    Default: default_layout,
    ...(possibleCustomLayout ? {"Custom Layout": JSON.parse(possibleCustomLayout)} : {}),
  });

  /**
   * Return nodes
   */
  return (
    <div id="main" className="container">
      <Header layout={layout} changeLayout={changeLayout} layouts={layouts} changeLayouts={changeLayouts} />
      <Workspace tables={defaultTables} layout={layout} layouts={layouts} changeLayouts={changeLayouts} />
      <Footer />
    </div>
  );
}

window.addEventListener("load", () => {
  ReactDOM.render(<App />, document.getElementById("root"));
});
