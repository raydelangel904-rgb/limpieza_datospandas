import json

notebook_path = "/Users/raymundodelangel/prueba_cienciadatos/limpieza_datospandas/limpieza_datos.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Define the sources for the 6 new cells
sources = [
    # 1. Evolución Mensual
    [
        "# 1. Evolución Mensual del Total de Delitos a Nivel Nacional\n",
        "delitos_mensuales = df_tidy.groupby('mes')['cantidad'].sum().reindex(['Enero', 'Febrero', 'Marzo', 'Abril']).reset_index()\n",
        "\n",
        "plt.figure(figsize=(10, 5))\n",
        "sns.lineplot(\n",
        "    data=delitos_mensuales,\n",
        "    x='mes',\n",
        "    y='cantidad',\n",
        "    marker='o',\n",
        "    markersize=10,\n",
        "    linewidth=3,\n",
        "    color='#1a5f7a'\n",
        ")\n",
        "\n",
        "plt.title(\"Evolución Mensual del Total de Delitos Registrados en México (Cuatrimestre 2026)\", fontsize=13, fontweight='bold', pad=15)\n",
        "plt.xlabel(\"Mes de Registro\", fontsize=11, labelpad=10)\n",
        "plt.ylabel(\"Total de Delitos Registrados\", fontsize=11, labelpad=10)\n",
        "plt.grid(True, linestyle=\"--\", alpha=0.6)\n",
        "\n",
        "for x, y in zip(delitos_mensuales['mes'], delitos_mensuales['cantidad']):\n",
        "    plt.text(x, y + 1500, f\"{int(y):,}\", ha='center', va='bottom', fontsize=10, fontweight='bold', color=\"#1a5f7a\")\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()"
    ],
    # 2. Distribución por Bien Jurídico Afectado
    [
        "# 2. Distribución de Delitos por Bien Jurídico Afectado\n",
        "bienes_afectados = df_tidy.groupby('bien_juridico_afectado')['cantidad'].sum().sort_values(ascending=False).reset_index()\n",
        "\n",
        "plt.figure(figsize=(10, 6))\n",
        "colors = sns.color_palette(\"plasma\", len(bienes_afectados))\n",
        "plt.pie(\n",
        "    bienes_afectados['cantidad'],\n",
        "    labels=bienes_afectados['bien_juridico_afectado'],\n",
        "    autopct='%1.1f%%',\n",
        "    startangle=140,\n",
        "    colors=colors,\n",
        "    wedgeprops={'edgecolor': 'white', 'linewidth': 1, 'antialiased': True}\n",
        ")\n",
        "\n",
        "plt.title(\"Distribución Porcentual de Delitos por Bien Jurídico Afectado (2026)\", fontsize=13, fontweight='bold', pad=15)\n",
        "plt.tight_layout()\n",
        "plt.show()"
    ],
    # 3. Top 10 Entidades Federativas
    [
        "# 3. Top 10 Entidades Federativas con Mayor Incidencia Delictiva\n",
        "entidades_incidencia = df_tidy.groupby('entidad')['cantidad'].sum().sort_values(ascending=False).head(10).reset_index()\n",
        "\n",
        "plt.figure(figsize=(12, 6))\n",
        "sns.barplot(\n",
        "    data=entidades_incidencia,\n",
        "    x='cantidad',\n",
        "    y='entidad',\n",
        "    palette=\"flare\"\n",
        ")\n",
        "\n",
        "plt.title(\"Top 10 Entidades Federativas con Mayor Número de Delitos (Ene - Abr 2026)\", fontsize=13, fontweight='bold', pad=15)\n",
        "plt.xlabel(\"Total de Delitos Registrados\", fontsize=11, labelpad=10)\n",
        "plt.ylabel(\"Entidad Federativa\", fontsize=11, labelpad=10)\n",
        "plt.grid(axis='x', linestyle=\"--\", alpha=0.6)\n",
        "\n",
        "for index, value in enumerate(entidades_incidencia['cantidad']):\n",
        "    plt.text(value + 1000, index, f\"{int(value):,}\", va='center', fontsize=10, fontweight='bold')\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()"
    ],
    # 4. Top 10 de Tipos de Delito
    [
        "# 4. Top 10 de Tipos de Delito Más Frecuentes\n",
        "delitos_tipos = df_tidy.groupby('tipo_delito')['cantidad'].sum().sort_values(ascending=False).head(10).reset_index()\n",
        "\n",
        "plt.figure(figsize=(12, 6))\n",
        "sns.barplot(\n",
        "    data=delitos_tipos,\n",
        "    x='cantidad',\n",
        "    y='tipo_delito',\n",
        "    palette=\"viridis\"\n",
        ")\n",
        "\n",
        "plt.title(\"Top 10 de Tipos de Delitos Más Frecuentes en México (Ene - Abr 2026)\", fontsize=13, fontweight='bold', pad=15)\n",
        "plt.xlabel(\"Cantidad de Delitos Registrados\", fontsize=11, labelpad=10)\n",
        "plt.ylabel(\"Tipo de Delito\", fontsize=11, labelpad=10)\n",
        "plt.grid(axis='x', linestyle=\"--\", alpha=0.6)\n",
        "\n",
        "for index, value in enumerate(delitos_tipos['cantidad']):\n",
        "    plt.text(value + 1000, index, f\"{int(value):,}\", va='center', fontsize=10, fontweight='bold')\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()"
    ],
    # 5. Top 10 Subtipos de Delitos
    [
        "# 5. Top 10 Subtipos de Delitos Más Recurrentes\n",
        "subtipos_incidencia = df_tidy.groupby('subtipo_delito')['cantidad'].sum().sort_values(ascending=False).head(10).reset_index()\n",
        "\n",
        "plt.figure(figsize=(12, 6))\n",
        "sns.barplot(\n",
        "    data=subtipos_incidencia,\n",
        "    x='cantidad',\n",
        "    y='subtipo_delito',\n",
        "    palette=\"crest\"\n",
        ")\n",
        "\n",
        "plt.title(\"Top 10 Subtipos de Delitos Más Recurrentes (Ene - Abr 2026)\", fontsize=13, fontweight='bold', pad=15)\n",
        "plt.xlabel(\"Total de Incidencias\", fontsize=11, labelpad=10)\n",
        "plt.ylabel(\"Subtipo de Delito\", fontsize=11, labelpad=10)\n",
        "plt.grid(axis='x', linestyle=\"--\", alpha=0.6)\n",
        "\n",
        "for index, value in enumerate(subtipos_incidencia['cantidad']):\n",
        "    plt.text(value + 500, index, f\"{int(value):,}\", va='center', fontsize=10, fontweight='bold')\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()"
    ],
    # 6. Top 10 Modalidades de Comisión
    [
        "# 6. Top 10 Modalidades de Comisión de Delitos\n",
        "modalidades_incidencia = df_tidy.groupby('modalidad')['cantidad'].sum().sort_values(ascending=False).head(10).reset_index()\n",
        "\n",
        "plt.figure(figsize=(12, 6))\n",
        "sns.barplot(\n",
        "    data=modalidades_incidencia,\n",
        "    x='cantidad',\n",
        "    y='modalidad',\n",
        "    palette=\"mako\"\n",
        ")\n",
        "\n",
        "plt.title(\"Top 10 Modalidades de Comisión de Delitos (Ene - Abr 2026)\", fontsize=13, fontweight='bold', pad=15)\n",
        "plt.xlabel(\"Total de Incidencias\", fontsize=11, labelpad=10)\n",
        "plt.ylabel(\"Modalidad\", fontsize=11, labelpad=10)\n",
        "plt.grid(axis='x', linestyle=\"--\", alpha=0.6)\n",
        "\n",
        "for index, value in enumerate(modalidades_incidencia['cantidad']):\n",
        "    plt.text(value + 500, index, f\"{int(value):,}\", va='center', fontsize=10, fontweight='bold')\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()"
    ]
]

# Generate new cells with correct metadata IDs
new_cells = []
import uuid
for src in sources:
    cell_id = str(uuid.uuid4())[:8]
    new_cells.append({
        "cell_type": "code",
        "execution_count": None,
        "id": cell_id,
        "metadata": {},
        "outputs": [],
        "source": src
    })

# Replace cells 16, 17, 18, 19 with the 6 new cells
# Cells list: nb["cells"]
# Slice index 16 to 20 (not including 20) is replaced by new_cells
nb["cells"][16:20] = new_cells

# Write updated notebook
with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook updated successfully!")
