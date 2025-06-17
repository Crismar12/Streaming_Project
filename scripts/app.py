import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configuración visual general
st.set_page_config(layout="wide")
sns.set(style="whitegrid")

# Cargar datasets
df = pd.read_parquet("data/df_streaming_completo.parquet")
top5_por_plataforma = pd.read_parquet("data/top5_por_plataforma.parquet")
df_anual = pd.read_parquet("data/df_anual.parquet")
top5_productivos = pd.read_parquet("data/top5_productivos.parquet")
top5_paises_por_plataforma = pd.read_parquet("data/top5_paises_por_plataforma.parquet")
top5_rating_por_plataforma = pd.read_parquet("data/top5_rating_por_plataforma.parquet")
top5_rating_por_tipo = pd.read_parquet("data/top5_rating_por_tipo.parquet")

# Diccionario de descripciones de rating
descripciones_rating = {
    "tv-ma": {"desc": "Solo para adultos. Contenido explícito.", "icon": "🔞", "color": "red"},
    "r": {"desc": "Restringido. Se requiere acompañamiento adulto.", "icon": "🚫", "color": "darkred"},
    "tv-14": {"desc": "Supervisión sugerida para menores de 14 años.", "icon": "⚠️", "color": "orange"},
    "pg-13": {"desc": "Algunas escenas pueden ser inapropiadas para menores de 13.", "icon": "👀", "color": "orange"},
    "tv-pg": {"desc": "Puede contener lenguaje o situaciones moderadas.", "icon": "📺", "color": "goldenrod"},
    "pg": {"desc": "Apto para todo público con supervisión.", "icon": "👨‍👩‍👧", "color": "olive"},
    "g": {"desc": "General. Apto para todas las edades.", "icon": "✅", "color": "green"},
    "tv-g": {"desc": "Sin contenido objetable. Ideal para todos.", "icon": "🌟", "color": "green"},
    "tv-y7": {"desc": "Para niños mayores de 7 años. Humor o acción leve.", "icon": "🎯", "color": "teal"},
    "tv-y": {"desc": "Diseñado para niños pequeños.", "icon": "🐣", "color": "turquoise"},
    "all": {"desc": "Apto para todo público.", "icon": "👌", "color": "green"},
    "13+": {"desc": "Apto para mayores de 13 años.", "icon": "📌", "color": "orange"},
    "16+": {"desc": "Apto para mayores de 16 años.", "icon": "📌", "color": "orange"},
    "desconocido": {"desc": "Clasificación desconocida.", "icon": "❓", "color": "gray"}
}

from contextlib import contextmanager

@contextmanager
def custom_expander(label, size=24):
    styled_subheader(label, size)
    with st.expander("", expanded=False) as container:
        yield container


def styled_subheader(text, size=24):
    st.markdown(f"<h3 style='font-size:{size}px;'>{text}</h3>", unsafe_allow_html=True)

def styled_label(text, size=18):
    st.markdown(f"<p style='font-size:{size}px; font-weight:bold;'>{text}</p>", unsafe_allow_html=True)
    
# TÍTULO
st.title("Análisis de Contenido Streaming 2008–2021 📺")

opcion = st.radio(
    "Navegación",
    options=["🔎 Contenido General", "🌍 Países y Ratings", "🎭 Clasificaciones Detalladas"],
    index=0,
    key="navegador" 
)

if opcion == "🔎 Contenido General":
    styled_label("🔎 Contenido General")
    with custom_expander("📊 Distribución por tipo de contenido"):
        styled_label("Selecciona una plataforma:")
        plataforma = st.selectbox("", df["plataforma"].unique(), key="tipo_general")
        df_filtrado = df[df["plataforma"] == plataforma]
        fig, ax = plt.subplots()
        sns.countplot(data=df_filtrado, x="type", ax=ax, palette="Set2")
        for p in ax.patches:
            height = p.get_height()
            if height > 0:
                ax.annotate(f'{int(height)}', (p.get_x() + p.get_width() / 2, height),
                            ha='center', va='bottom', fontsize=9)
        st.pyplot(fig)

    with custom_expander("🔝 Top 5 géneros más populares por plataforma"):
        styled_label("Selecciona una plataforma:")
        plataforma_top5 = st.selectbox("", top5_por_plataforma["plataforma"].unique(), key="top5_plataforma")
        top5_filtrado = top5_por_plataforma[top5_por_plataforma["plataforma"] == plataforma_top5]
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(data=top5_filtrado, x="listed_in", y="conteo", ax=ax, palette="pastel")
        for p in ax.patches:
            height = p.get_height()
            if height > 0:
                ax.annotate(f'{int(height)}', (p.get_x() + p.get_width() / 2, height),
                            ha='center', va='bottom', fontsize=9)
        st.pyplot(fig)

    with custom_expander("📅 Cantidad de películas y series al año por plataforma"):
        styled_label("Selecciona una plataforma:")
        plataforma_type = st.selectbox("", df_anual['plataforma'].unique(), key="plataforma_type")
        styled_label("Selecciona un año:")
        plataforma_anual = st.selectbox("", sorted(df_anual['year_added'].unique()), key="plataforma_anual")
        df_anual_filtrado = df_anual[
            (df_anual['plataforma'] == plataforma_type) & 
            (df_anual['year_added'] == plataforma_anual)
        ]
        tipos = ['movie', 'tv show']
        df_base = pd.DataFrame({'type': tipos})
        df_anual_filtrado = df_base.merge(df_anual_filtrado, on='type', how='left')
        df_anual_filtrado['conteo'] = df_anual_filtrado['conteo'].fillna(0)
        if df_anual_filtrado['conteo'].sum() == 0:
            st.warning("No hay datos disponibles para la combinación seleccionada.")
        else:
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.barplot(data=df_anual_filtrado, x="type", y="conteo", ax=ax, palette="pastel")
            ax.set_title(f"{plataforma_type} en {plataforma_anual}")
            for p in ax.patches:
                height = p.get_height()
                if height > 0:
                    ax.annotate(f'{int(height)}', (p.get_x() + p.get_width() / 2, height),
                                ha='center', va='bottom', fontsize=9)
            st.pyplot(fig)

elif opcion == "🌍 Países y Ratings":
    styled_label("🌍 Países y Ratings")
    with custom_expander("🏆 Top 5 años más productivos por plataforma"):
        styled_label("Selecciona una plataforma:")
        plataforma_productiva = st.selectbox("", top5_productivos['plataforma'].unique(),key="plataforma_productiva")
        df_top = top5_productivos[top5_productivos['plataforma'] == plataforma_productiva]
        df_base_productivos = pd.DataFrame({'year_added': df_top['year_added'].unique()})
        df_top = df_base_productivos.merge(df_top, on='year_added', how='left')
        df_top['conteo'] = df_top['conteo'].fillna(0)
        if df_top['conteo'].sum() == 0:
            st.warning("No hay datos disponibles para la plataforma seleccionada.")
        else:
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(data=df_top, x="year_added", y="conteo", ax=ax, palette="Blues")
            for p in ax.patches:
                height = p.get_height()
                if height > 0:
                    ax.annotate(f'{int(height)}', (p.get_x() + p.get_width() / 2, height),
                                ha='center', va='bottom', fontsize=9)
            st.pyplot(fig)

    with custom_expander("🌍 Top 5 países con más contenido por plataforma"):
        styled_label("Selecciona una plataforma:")
        plataforma_contenido = st.selectbox("", top5_paises_por_plataforma["plataforma"].unique(), key="plataforma_contenido")
        paises_filtrada = top5_paises_por_plataforma[top5_paises_por_plataforma["plataforma"] == plataforma_contenido]
        fig, ax = plt.subplots(figsize=(10,5))
        sns.barplot(data=paises_filtrada, x="country", y="conteo", ax=ax, palette="Set3")
        for p in ax.patches:
            height = p.get_height()
            if height > 0:
                ax.annotate(f'{int(height)}', (p.get_x() + p.get_width() / 2, height),
                            ha='center', va='bottom', fontsize=9)
        st.pyplot(fig)


elif opcion == "🎭 Clasificaciones Detalladas":
    styled_label("🎭 Clasificaciones Detalladas")
    with custom_expander("⭐ Top 5 clasificaciones de contenido por plataforma"):
        styled_label("Selecciona una plataforma:")
        plataforma_rating = st.selectbox("", top5_rating_por_plataforma["plataforma"].unique(), key="plataforma_rating")
        df_rating = top5_rating_por_plataforma[top5_rating_por_plataforma["plataforma"] == plataforma_rating]
        fig, ax = plt.subplots(figsize=(10, 5))
        # Gráfico de top 5 ratings por plataforma
        sns.barplot(data=df_rating, x="rating", y="conteo", ax=ax, palette="coolwarm")
        ax.set_xlabel("Clasificación", fontsize=14)
        ax.set_ylabel("Cantidad de títulos", fontsize=14)
        ax.tick_params(axis='x', labelsize=12)

        for p in ax.patches:
            height = p.get_height()
            if height > 0:
                ax.annotate(f'{int(height)}',
                            (p.get_x() + p.get_width() / 2, height),
                            ha='center', va='bottom', fontsize=9, color='black')

        st.pyplot(fig)

        # Visualizar descripción del rating seleccionado
        rating_opciones = sorted(df_rating["rating"].unique())
        styled_label("Selecciona una clasificación para ver su significado:")
        rating_seleccionado = st.selectbox(
            "",
            rating_opciones,
            key="descripcion_rating"
        )

        clave = rating_seleccionado.lower()
        info = descripciones_rating.get(clave, {"desc": "Descripción no disponible.", "icon": "❓", "color": "gray"})
        st.markdown(
            f"""
            <div style="background-color: {info['color']}; padding: 10px; border-radius: 5px;">
                <h4 style="color: white;">{info['icon']} {rating_seleccionado} - {info['desc']}</h4>
            </div>
            """,
            unsafe_allow_html=True
        )
        

    with custom_expander("🎭 Top 5 clasificaciones por tipo de contenido"):
        styled_label("Selecciona un tipo de contenido:")
        tipo_rating = st.selectbox("", top5_rating_por_tipo["type"].unique(), key="tipo_rating")
        df_tipo = top5_rating_por_tipo[top5_rating_por_tipo["type"] == tipo_rating]

        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(data=df_tipo, x="rating", y="conteo", ax=ax, palette="Set2")
        ax.set_xlabel("Clasificación", fontsize=14)
        ax.set_ylabel("Cantidad de títulos", fontsize=14)
        ax.tick_params(axis='x', labelsize=12)

        for p in ax.patches:
            height = p.get_height()
            if height > 0:
                ax.annotate(f'{int(height)}',
                            (p.get_x() + p.get_width() / 2, height),
                            ha='center', va='bottom', fontsize=9)

        st.pyplot(fig)
        # Visualizar descripción del rating seleccionado
        rating_opciones_tipo = sorted(df_tipo["rating"].unique())
        styled_label("Selecciona una clasificación para ver su significado:")
        rating_seleccionado_tipo = st.selectbox(
            "",
            rating_opciones_tipo,
            key="descripcion_rating_tipo"
        )
        clave_tipo = rating_seleccionado_tipo.lower()
        info_tipo = descripciones_rating.get(clave_tipo, {"desc": "Descripción no disponible.", "icon": "❓", "color": "gray"})
        st.markdown(
            f"""
            <div style="background-color: {info_tipo['color']}; padding: 10px; border-radius: 5px;">
                <h4 style="color: white;">{info_tipo['icon']} {rating_seleccionado_tipo} - {info_tipo['desc']}</h4>
            </div>
            """,
            unsafe_allow_html=True
        )
    
# Footer
st.markdown(
    """
    <style>
        footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px;
        }
    </style>
    <footer>
        <p>Hecho con ❤️ por Francis Esculpi | Datos de Kaggle</p>
    </footer>
    """,
    unsafe_allow_html=True
)