import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts

def analisis():
    options = {
        "title": {"text": "Porcentaje de Canciones por Álbum", "left": "center"},
        "tooltip": {"trigger": "item"},
        "legend": {"orient": "vertical", "left": "left",},
        "series": [
            {
                "name": "访问来源",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 1048, "name": "搜索引擎"},
                    {"value": 735, "name": "直接访问"},
                    {"value": 580, "name": "邮件营销"},
                    {"value": 484, "name": "联盟广告"},
                    {"value": 300, "name": "视频广告"},
                ],
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
            }
        ],
    }
    st_echarts(
        options=options, height="600px",
    )

