# Script para analizar abandono de clientes
# Proyecto por desarrollar
df['segmento_valor'] = pd.qcut(df['valor'], 3, labels=['bajo','medio', 'alto'])