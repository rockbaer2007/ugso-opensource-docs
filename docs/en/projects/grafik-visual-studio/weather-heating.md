---
title: Weather and Heating
description: Install and configure the optional chart widget package.
---

# Weather and Heating

From **Studio 0.1.189**, you can install **Weather and Heating 1.2.0**. It contains **General Chart**, **Two Weeks Bar Chart** and **Weather Widget**. The functional reference is [ioBroker.vis-2-widgets-weather-and-heating](https://github.com/rg-engineering/ioBroker.vis-2-widgets-weather-and-heating); Studio uses an original SVG implementation. Other weather/heating widgets and ioBroker-specific adapter bindings are not included yet.

## Install

Download [ugso.weather-heating.wg](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/raw/refs/heads/master/ha_grafik_visual_studio/packages/weather-heating/ugso.weather-heating.wg). Open **Settings → Widget packages → Install local .wg / .wg.zip** and select the file. After reloading, a separate set appears with an automatically assigned color. This browser remembers its color across removal and reinstallation. The 74 built-in widgets remain available.

## Configure the chart

An installed 1.0.0 or 1.1.0 package can be updated to 1.2.0 through the same import. Existing charts and saved project values remain intact. Updates may only add widgets; changes to existing definitions and downgrades are rejected.

**General** provides a headline, series count (1–10), legend and display without a card. The first series can use the main entity. Each **Data [N]** group provides its own entity, optional attribute, preview JSON, X/Y keys, name, unit, color, line/bar type, left/right axis and difference calculation. A bound series reads only its entity state or attribute. Missing live data never falls back to preview JSON. The widget does not write HA states.

Example preview JSON or HA attribute:

```json
[
  {"x":"2026-10-03T08:00:00","value":12},
  {"x":"2026-10-03T09:00:00","value":18},
  {"x":"2026-10-03T10:00:00","value":15}
]
```

Default keys are `x` and `value`; custom keys and `[x,y]` pairs are supported. **Time** expects ISO dates or Unix milliseconds. **Category** displays text, such as year labels. Time points are sorted before difference calculation. Missing readings break lines and difference sequences; the first difference has no predecessor. Left/right axes scale independently.

**X axis** defaults to `ddd HH:mm`. Supported tokens: `YYYY`, `MM`, `DD`, `ddd`, `HH`, `mm`, `ss`. Colors are under **WIDGET → Chart CSS**. Input arrays may contain up to 20,000 rows; large series are reduced to at most 500 points each. The widget does not fetch HA history: its entity must already provide the data array.

![Installed set and chart preview](/images/grafik-visual-studio/weather-heating-chart.png)

## Two Weeks Bar Chart

**Current week** and **Previous week** each provide seven HA entity bindings, Monday through Sunday, plus editable preview values. Daily pairs appear side by side. The widget does not calculate weekly history or shift values at the start of a new week: its sensors must already provide the corresponding daily readings.

**Show weekly values** matches the original “Visible” option: disabled displays only preview values; enabled reads only the fourteen daily entities. Unbound, unavailable or non-numeric live readings have no bars. Zero is valid. Overall widget visibility remains controlled under **Visibility**.

**General** provides a headline and color, legend text color, unit, week colors, axis label color, left/right Y axis, 0–5 decimal places, legend and **Without card**. **X axis** has a separate color. Units and formatted values appear in the legend and bar tooltips; weekdays follow the app language. Configured colors are used as entered.

![Two Weeks Bar Chart in the installed set](/images/grafik-visual-studio/weather-heating-two-weeks.png)

## Weather Widget

**Data source** offers `home-assistant`, `json` and `individual`. **Data structure** selects five daily values (`daily`) or up to 24 hourly values (`hourly`). These sources replace ioBroker instance/OID selection with HA bindings.

With `home-assistant`, choose a `weather.*` entity. Studio's server reads forecasts through [weather.get_forecasts](https://www.home-assistant.io/integrations/weather/). Successful responses are cached for five minutes; failures retry no sooner than one minute later. The weather integration must support the selected forecast type. Temperature and precipitation units come from its attributes. A real HA request requires the running add-on/Supervisor connection.

With `json`, the widget reads the selected **Forecast attribute (JSON)**; an empty attribute reads the entity state. Supply an array, for example:

```json
[{"datetime":"2026-10-03T12:00:00Z","temperature":18,"templow":10,"precipitation":0,"cloud_coverage":25,"precipitation_probability":40}]
```

With `individual`, bind **Daily dates [1–5]** or **Timestamps [1–24]**, plus their corresponding temperature, rain, cloud and probability values, to individual sensors. Dates may be ISO strings or Unix milliseconds. Daily views use only the first five bindings in each value group. Invalid timestamps are omitted, missing values break lines, and zero is valid. Without a bound weather/JSON entity, the first two sources show editable preview data. Missing live data never falls back to preview values.

**Temperature**, **Rain**, **Clouds** and **Rain probability** can be enabled individually. Each group has colors and a left/right value axis; rain uses bars. **Show in separate chart** creates its own panel. Incompatible units on the same axis automatically split into separate panels. **Sun or clouds** displays cloud coverage or its complement as a percentage, not sunshine hours. Missing provider values are never inferred from weather conditions. Name, optional location entity, legend, colors, X date format, size and **Without card** are configurable.

![Weather Widget with temperature and rain](/images/grafik-visual-studio/weather-heating-weather.png)

The reproducible builder and validated manifest are in the [source repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/weather-heating). The [package contract](widget-packages.md) describes interface 0.2.
