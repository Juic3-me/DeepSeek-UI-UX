# Chart choices (dashboards and data pages)

| Data story | Best chart | Notes |
|---|---|---|
| Trend over time | Line / area | smooth lines for continuous series; max 5 series; label axes and units |
| Compare categories | Bar (horizontal for long labels, vertical for time) | sort bars; start at zero |
| Part of whole (2-4 parts) | Donut / stacked bar | more than 4 parts: use bar |
| Distribution | Histogram / box plot | show median and outliers |
| Correlation | Scatter / bubble | trend line, tooltips |
| Funnel / conversion | Funnel or stepped bars | show drop-off % per step |
| Progress to goal | Progress bar / gauge (sparingly) | include target value as text |
| Geographic | Choropleth / dot map | legend with scale; sequential color |
| Matrix / density | Heatmap | sequential single hue; don't rely on color alone |
| Flow / hierarchy | Sankey / treemap | only when relationships matter |
| KPI snapshot | Big number + sparkline + delta | 48-64px number; up/down icon, not only color |
| Exact values | Table with sort and filter | right-align numbers, tabular-nums |

Rules: max 5-6 colors (colorblind-safe; use `#2563EB, #F97316, #16A34A, #7C3AED, #64748B`), direct labels beat legends, tooltips on hover AND tap, text alternative or data table for screen readers, no 3D, no dual axes unless clearly labeled, empty/loading/error state for every chart. Libraries: Chart.js or inline SVG for simple, D3 for custom, ECharts for dense dashboards.
