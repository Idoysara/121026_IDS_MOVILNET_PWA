#!/usr/bin/env python3
"""
scripts/generate_powerpoint_presentation.py
=============================================================================
Generador Oficial de la Presentación PowerPoint (.pptx) Ejecutiva
Proyecto: Asistente MOVI 4GMAX — Telecomunicaciones Movilnet C.A.
Audiencia Dual: Comité de Inversión (Economistas) & Dpto. de Mercadeo (Growth)
=============================================================================
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# Definición de Colores Corporativos Ejecutivos
COLOR_BG_DARK = RGBColor(11, 19, 43)       # #0B132B Azul Noche Profundo
COLOR_CARD_DARK = RGBColor(18, 30, 58)     # #121E3A Tarjeta Azul Pizarra
COLOR_RED_MOVILNET = RGBColor(230, 32, 32) # #E62020 Rojo Movilnet Oficial
COLOR_WHITE = RGBColor(255, 255, 255)       # Blanco Puro
COLOR_SLATE_LIGHT = RGBColor(203, 213, 225)# Gris Claro Texto
COLOR_SLATE_MUTED = RGBColor(148, 163, 184)# Gris Medio Metadatos
COLOR_EMERALD = RGBColor(16, 185, 129)     # Verde Éxito Financiero
COLOR_SKY = RGBColor(14, 165, 233)         # Azul Cielo Datos
COLOR_AMBER = RGBColor(245, 158, 11)       # Ámbar Alertas / Cupones
COLOR_PURPLE = RGBColor(168, 85, 247)      # Púrpura IA / Competencia

def create_deck():
    prs = Presentation()
    # Relación de Aspecto Widescreen 16:9 (13.333 x 7.5 pulgadas)
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # Blank slide

    def add_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG_DARK
        bg.line.fill.background()
        return bg

    def add_header(slide, tag_text, title_text, subtitle_text=None, tag_color=COLOR_RED_MOVILNET):
        # Header banner
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_tag = tf.paragraphs[0]
        p_tag.text = tag_text.upper()
        p_tag.font.size = Pt(10)
        p_tag.font.bold = True
        p_tag.font.color.rgb = tag_color

        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_WHITE
        p_title.space_before = Pt(3)

        if subtitle_text:
            p_sub = tf.add_paragraph()
            p_sub.text = subtitle_text
            p_sub.font.size = Pt(11)
            p_sub.font.color.rgb = COLOR_SLATE_MUTED
            p_sub.space_before = Pt(2)

    def add_footer(slide):
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.7), Inches(0.35))
        tf = footer_box.text_frame
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = "🌐 Portal PWA 4GMAX: https://one21026-ids-movilnet-pwa-bxmz.onrender.com/ui/pwa_stitch/index.html  |  Telecomunicaciones Movilnet C.A."
        p.font.size = Pt(8.5)
        p.font.color.rgb = COLOR_SLATE_MUTED

    # =========================================================================
    # SLIDE 1: PORTADA EJECUTIVA DE INVERSIÓN Y MERCADEO
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1)

    # Accent Red Bar
    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.2), Inches(0.12), Inches(3.2))
    bar.fill.solid()
    bar.fill.fore_color.rgb = COLOR_RED_MOVILNET
    bar.line.fill.background()

    tb = s1.shapes.add_textbox(Inches(1.2), Inches(1.1), Inches(11.0), Inches(3.4))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "DOSSIER EJECUTIVO ESTRATÉGICO & PLAN FINANCIERO"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_RED_MOVILNET

    p1 = tf.add_paragraph()
    p1.text = "Ecosistema Conversacional MOVI 4GMAX"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_WHITE
    p1.space_before = Pt(8)

    p2 = tf.add_paragraph()
    p2.text = "De Centro de Costos Operativos a Canal Dominante de Nuevos Ingresos Recurrentes"
    p2.font.size = Pt(17)
    p2.font.color.rgb = COLOR_SLATE_LIGHT
    p2.space_before = Pt(8)

    p3 = tf.add_paragraph()
    p3.text = "Telecomunicaciones Movilnet C.A.  •  WhatsApp Master + PWA con Cero Consumo de Datos"
    p3.font.size = Pt(12)
    p3.font.color.rgb = COLOR_SLATE_MUTED
    p3.space_before = Pt(14)

    # 4 KPI Highlights
    kpis = [
        ("Payback Inversión", "7.2 Meses", COLOR_EMERALD, "Retorno acelerado por ahorro OPEX"),
        ("TIR Anual (IRR)", "68.4%", COLOR_EMERALD, "WACC descontado al 15%"),
        ("Open Rate WhatsApp", "98.2%", COLOR_AMBER, "vs. 12.4% SMS tradicional"),
        ("Costo Marginal", "→ $0.00", COLOR_SKY, "$0.85 humano vs. $0.0044 IA")
    ]
    for i, (title, val, color, desc) in enumerate(kpis):
        x = Inches(0.8 + i * 2.95)
        card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(4.8), Inches(2.8), Inches(1.8))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = RGBColor(30, 58, 100)

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_top = Inches(0.2)
        cp0 = ctf.paragraphs[0]
        cp0.text = title.upper()
        cp0.font.size = Pt(9.5)
        cp0.font.bold = True
        cp0.font.color.rgb = COLOR_SLATE_MUTED

        cp1 = ctf.add_paragraph()
        cp1.text = val
        cp1.font.size = Pt(24)
        cp1.font.bold = True
        cp1.font.color.rgb = color
        cp1.space_before = Pt(4)

        cp2 = ctf.add_paragraph()
        cp2.text = desc
        cp2.font.size = Pt(9)
        cp2.font.color.rgb = COLOR_SLATE_LIGHT
        cp2.space_before = Pt(4)

    add_footer(s1)

    # =========================================================================
    # SLIDE 2: EL PROBLEMA ECONÓMICO VS. LA SOLUCIÓN PRODUCTIVA
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2)
    add_header(s2, "Diagnóstico del Negocio Telco", "El Salto Cuántico: De Costo Lineal a Activo Productivo",
               "Comparativa económica entre el modelo de call center analógico y la plataforma autónoma MOVI.")

    # Columna Izquierda: Problema
    c_left = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.9))
    c_left.fill.solid()
    c_left.fill.fore_color.rgb = COLOR_CARD_DARK
    c_left.line.color.rgb = RGBColor(127, 29, 29) # Borde rojo sutil
    ltf = c_left.text_frame
    ltf.word_wrap = True
    ltf.margin_top = Inches(0.25)
    ltf.margin_left = Inches(0.3)

    lp0 = ltf.paragraphs[0]
    lp0.text = "❌ EL MODELO TRADICIONAL (POZO DE OPEX)"
    lp0.font.size = Pt(13)
    lp0.font.bold = True
    lp0.font.color.rgb = COLOR_RED_MOVILNET

    lp1 = ltf.add_paragraph()
    lp1.text = "• Costo Rígido por Llamada: $0.85 USD promedio por ticket humano."
    lp1.font.size = Pt(11)
    lp1.font.color.rgb = COLOR_SLATE_LIGHT
    lp1.space_before = Pt(12)

    lp2 = ltf.add_paragraph()
    lp2.text = "• Ineficiencia Cognitiva: 62% del tráfico son preguntas obvias de saldo y corte."
    lp2.font.size = Pt(11)
    lp2.font.color.rgb = COLOR_SLATE_LIGHT
    lp2.space_before = Pt(10)

    lp3 = ltf.add_paragraph()
    lp3.text = "• Fricción en Recargas: Tiempos de espera de 7 a 15 min causan fuga de clientes (18% churn)."
    lp3.font.size = Pt(11)
    lp3.font.color.rgb = COLOR_SLATE_LIGHT
    lp3.space_before = Pt(10)

    lp4 = ltf.add_paragraph()
    lp4.text = "• Generación de Ingresos: CERO ventas adicionales en llamadas de reclamo."
    lp4.font.size = Pt(11)
    lp4.font.color.rgb = COLOR_SLATE_LIGHT
    lp4.space_before = Pt(10)

    # Columna Derecha: Solución
    c_right = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.9))
    c_right.fill.solid()
    c_right.fill.fore_color.rgb = COLOR_CARD_DARK
    c_right.line.color.rgb = RGBColor(6, 78, 59) # Borde verde esmeralda
    rtf = c_right.text_frame
    rtf.word_wrap = True
    rtf.margin_top = Inches(0.25)
    rtf.margin_left = Inches(0.3)

    rp0 = rtf.paragraphs[0]
    rp0.text = "✅ LA PLATAFORMA MOVI (ACTIVO GENERADOR DE DINERO)"
    rp0.font.size = Pt(13)
    rp0.font.bold = True
    rp0.font.color.rgb = COLOR_EMERALD

    rp1 = rtf.add_paragraph()
    rp1.text = "• Costo Marginal Infinitesimal: $0.0044 USD por sesión (ahorro del 94.8%)."
    rp1.font.size = Pt(11)
    rp1.font.color.rgb = COLOR_SLATE_LIGHT
    rp1.space_before = Pt(12)

    rp2 = rtf.add_paragraph()
    rp2.text = "• Capacidad de Escala Elástica: 100.000 usuarios concurrentes sin colas de espera."
    rp2.font.size = Pt(11)
    rp2.font.color.rgb = COLOR_SLATE_LIGHT
    rp2.space_before = Pt(10)

    rp3 = rtf.add_paragraph()
    rp3.text = "• Recarga C2P en 12 Segundos: Pago Móvil integrado eleva recargas de 2.1 a 3.8 / mes."
    rp3.font.size = Pt(11)
    rp3.font.color.rgb = COLOR_SLATE_LIGHT
    rp3.space_before = Pt(10)

    rp4 = rtf.add_paragraph()
    rp4.text = "• Cross-Selling Automático: Venta de bolsas Extra Datos y cupones de retail al consultar saldo."
    rp4.font.size = Pt(11)
    rp4.font.color.rgb = COLOR_SLATE_LIGHT
    rp4.space_before = Pt(10)

    add_footer(s2)

    # =========================================================================
    # SLIDE 3: LAS 5 VÍAS DE NUEVOS INGRESOS (MERCADEO)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3)
    add_header(s3, "Monetización Comercial", "Las 5 Vías Directas de Nuevos Ingresos en Caja",
               "Dónde y cómo se generan ingresos reales atribuibles a la gestión de mercadeo.")

    streams = [
        ("1. Extra Datos (Upselling)", "$720k / Año 1", COLOR_ROSE_OR_RED := RGBColor(244, 63, 94),
         "Detección predictiva cuando restan <200 MB. Oferta automática con tasa de conversión del 8.7%."),
        ("2. Mayor Frecuencia C2P", "+$1.35 ARPU", COLOR_SKY,
         "Recarga sin fricción bancaria en 12 seg. El abonado pasa de 2.1 a 3.8 recargas mensuales."),
        ("3. Retail Media Cazador", "$360k / Año 1", COLOR_AMBER,
         "56 cadenas aliadas con 204 ofertas. Split publicitario 20/80 ($0.40 USD netos por cupón canjeado)."),
        ("4. Conquista de Competencia", "120.000 Líneas", COLOR_PURPLE,
         "Captación de Movistar/Digitel vía bono Freemium y Portabilidad Express eSIM en 3 minutos."),
        ("5. Carrier Billing & LVBP", "15% - 25% Fee", COLOR_EMERALD,
         "Paquetes de datos temáticos y cobro a saldo de suscripciones de streaming, béisbol y juegos.")
    ]

    for i, (stitle, sval, scolor, sdesc) in enumerate(streams):
        col = i % 3
        row = i // 3
        x = Inches(0.8 + col * 3.95)
        y = Inches(1.8 + row * 2.5)
        w = Inches(3.75) if i < 3 else Inches(5.75)
        h = Inches(2.2)

        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = RGBColor(30, 58, 100)

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_top = Inches(0.18)
        ctf.margin_left = Inches(0.25)

        p_t = ctf.paragraphs[0]
        p_t.text = stitle
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_WHITE

        p_v = ctf.add_paragraph()
        p_v.text = sval
        p_v.font.size = Pt(18)
        p_v.font.bold = True
        p_v.font.color.rgb = scolor
        p_v.space_before = Pt(3)

        p_d = ctf.add_paragraph()
        p_d.text = sdesc
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = COLOR_SLATE_LIGHT
        p_d.space_before = Pt(5)

    add_footer(s3)

    # =========================================================================
    # SLIDE 4: EL FUNNEL CONVERSACIONAL EN 12 SEGUNDOS
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4)
    add_header(s4, "Funnel de Conversión", "El Embudo Conversacional: De Consulta a Venta en 12 Segundos",
               "Cómo la inteligencia artificial acompaña al usuario en su propio chat sin carritos abandonados.")

    steps = [
        ("PASO 1: TOFU (Segundo 0)", "Consulta Pasiva", COLOR_SLATE_MUTED,
         "Usuario: 'Hola, ¿cuántos megas me quedan?'", "El usuario busca información rutinaria sin intención de compra inicial."),
        ("PASO 2: MOFU (Segundo 3)", "Diagnóstico con Urgencia", COLOR_SKY,
         "MOVI: 'Te quedan 180 MB y tu plan vence en 14 días. Los vas a agotar hoy.'", "El sistema crea conciencia de la necesidad antes de que el usuario quede incomunicado."),
        ("PASO 3: BOFU (Segundo 6)", "Oferta Irresistible (CTA)", COLOR_AMBER,
         "MOVI: '¿Deseas activar una bolsa Extra Datos 2GB por solo Bs. 45 con 1 clic?'", "Presentación de la solución con precio exacto y botón directo de compra."),
        ("PASO 4: CIERRE (Segundo 12)", "Pago Inmediato C2P", COLOR_EMERALD,
         "Sistema: '¡Acreditación Exitosa! Ref: 894125 • +2 GB disponibles.'", "Dinero en cuenta bancaria y datos activos al instante. Cero carritos abandonados.")
    ]

    for i, (title, sub, color, dialog, expl) in enumerate(steps):
        x = Inches(0.8 + i * 2.95)
        card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(2.8), Inches(4.9))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = RGBColor(30, 58, 100)

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_top = Inches(0.2)
        ctf.margin_left = Inches(0.2)

        p0 = ctf.paragraphs[0]
        p0.text = title
        p0.font.size = Pt(10)
        p0.font.bold = True
        p0.font.color.rgb = color

        p1 = ctf.add_paragraph()
        p1.text = sub
        p1.font.size = Pt(14)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_WHITE
        p1.space_before = Pt(4)

        # Bubble dialog
        p2 = ctf.add_paragraph()
        p2.text = f'"{dialog}"'
        p2.font.size = Pt(10)
        p2.font.italic = True
        p2.font.color.rgb = RGBColor(226, 232, 240)
        p2.space_before = Pt(14)

        p3 = ctf.add_paragraph()
        p3.text = expl
        p3.font.size = Pt(9.5)
        p3.font.color.rgb = COLOR_SLATE_MUTED
        p3.space_before = Pt(14)

    add_footer(s4)

    # =========================================================================
    # SLIDE 5: CAZADOR DE OFERTAS & RETAIL MEDIA (SPLIT 20/80)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5)
    add_header(s5, "Alianzas Estratégicas", "Cazador de Ofertas: La Red Publicitaria Retail Media",
               "Monetización de tráfico físico en comercios aliados con tecnología antifraude TOTP.")

    # 3 Cajas Superiores
    kpi_retail = [
        ("56 Marcas Aliadas", "Cadenas Comerciales Activas", COLOR_RED_MOVILNET, "Arturo's, Farmahorro, Cines Unidos, Traki, Automercados Plaza's."),
        ("204 Ofertas en Radar", "Descuentos Hiper-Geolocalizados", COLOR_AMBER, "Promociones con radio de cobertura dinámico de 500m a 50 km."),
        ("Split Comercial 20 / 80", "Ingreso Neto para Movilnet", COLOR_EMERALD, "Movilnet retiene $0.40 USD netos por cada cupón canjeado en tienda.")
    ]
    for i, (v, t, c, d) in enumerate(kpi_retail):
        x = Inches(0.8 + i * 3.95)
        card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(3.75), Inches(2.2))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = RGBColor(30, 58, 100)

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_top = Inches(0.2)
        ctf.margin_left = Inches(0.25)

        p0 = ctf.paragraphs[0]
        p0.text = v
        p0.font.size = Pt(22)
        p0.font.bold = True
        p0.font.color.rgb = c

        p1 = ctf.add_paragraph()
        p1.text = t
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_WHITE
        p1.space_before = Pt(3)

        p2 = ctf.add_paragraph()
        p2.text = d
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_SLATE_LIGHT
        p2.space_before = Pt(6)

    # Caja Inferior: Seguridad y Dinámica Antifraude
    box_sec = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.3), Inches(11.7), Inches(2.4))
    box_sec.fill.solid()
    box_sec.fill.fore_color.rgb = COLOR_CARD_DARK
    box_sec.line.color.rgb = RGBColor(40, 70, 120)
    stf = box_sec.text_frame
    stf.word_wrap = True
    stf.margin_top = Inches(0.25)
    stf.margin_left = Inches(0.3)

    sp0 = stf.paragraphs[0]
    sp0.text = "🛡️ CÓMO FUNCIONA EL MODELO DE NEGOCIO Y LA SEGURIDAD ANTIFRAUDE"
    sp0.font.size = Pt(13)
    sp0.font.bold = True
    sp0.font.color.rgb = COLOR_SKY

    sp1 = stf.add_paragraph()
    sp1.text = "1. Generación de Cupones TOTP (60 Segundos): Cada cupón contiene un código dinámico de un solo uso que expira en 60s, evitando duplicados o capturas de pantalla falsificadas en taquilla."
    sp1.font.size = Pt(10.5)
    sp1.font.color.rgb = COLOR_SLATE_LIGHT
    sp1.space_before = Pt(8)

    sp2 = stf.add_paragraph()
    sp2.text = "2. Liquidación Automática en Cero Inventario: Movilnet no compra ni almacena productos físicos. Solo cobra su comisión publicitaria al momento de la validación del consumo en el POS aliado."
    sp2.font.size = Pt(10.5)
    sp2.font.color.rgb = COLOR_SLATE_LIGHT
    sp2.space_before = Pt(6)

    sp3 = stf.add_paragraph()
    sp3.text = "3. Margen Operativo Bruto >85%: Al operar sobre infraestructura de software en la nube, el margen de ganancia de esta línea de ingresos no-tarifarios es casi puro beneficio."
    sp3.font.size = Pt(10.5)
    sp3.font.color.rgb = COLOR_EMERALD
    sp3.space_before = Pt(6)

    add_footer(s5)

    # =========================================================================
    # SLIDE 6: CRONOGRAMA TIME-TO-MONEY (EN QUÉ TIEMPO SE VEN LOS INGRESOS)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6)
    add_header(s6, "Horizonte de Retorno", "¿En Qué Tiempo se Visualizan los Ingresos?",
               "Roadmap comercial en 3 etapas con metas de facturación auditables desde el Mes 1.")

    phases = [
        ("FASE 1: QUICK WINS", "Meses 1 a 3", "$80k - $120k / mes", COLOR_ROSE_OR_RED,
         ["• Activación en WhatsApp y PWA de la base actual.",
          "• Recargas Pago Móvil C2P en 12 segundos.",
          "• Venta automática de Extra Datos al consultar saldo.",
          "• Impacto en caja visible en los primeros 30 días."]),
        ("FASE 2: ESCALAMIENTO RETAIL", "Meses 4 a 6", "$250k - $380k / mes", COLOR_AMBER,
         ["• Onboarding de 150 comercios en Cazador de Ofertas.",
          "• Campañas geolocalizadas por radiobases.",
          "• Validación visual de comprobantes bancarios por OCR.",
          "• Facturación publicitaria masiva en grandes cadenas."]),
        ("FASE 3: CONQUISTA TOTAL", "Meses 7 a 12", "$500k - $800k / mes", COLOR_EMERALD,
         ["• Portabilidad Express eSIM para Digitel y Movistar.",
          "• Carrier Billing para deportes (LVBP) y streaming.",
          "• Micro-seguros con cobro directo a saldo.",
          "• Consolidación del régimen comercial permanente."])
    ]

    for i, (pname, ptime, pmeta, pcolor, pitems) in enumerate(phases):
        x = Inches(0.8 + i * 3.95)
        card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(3.75), Inches(4.9))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = RGBColor(30, 58, 100)

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_top = Inches(0.25)
        ctf.margin_left = Inches(0.25)

        p0 = ctf.paragraphs[0]
        p0.text = pname
        p0.font.size = Pt(11)
        p0.font.bold = True
        p0.font.color.rgb = pcolor

        p1 = ctf.add_paragraph()
        p1.text = ptime
        p1.font.size = Pt(16)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_WHITE
        p1.space_before = Pt(3)

        p2 = ctf.add_paragraph()
        p2.text = f"Meta: {pmeta}"
        p2.font.size = Pt(12)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_EMERALD
        p2.space_before = Pt(6)

        for item in pitems:
            pi = ctf.add_paragraph()
            pi.text = item
            pi.font.size = Pt(9.5)
            pi.font.color.rgb = COLOR_SLATE_LIGHT
            pi.space_before = Pt(8)

    add_footer(s6)

    # =========================================================================
    # SLIDE 7: COSTO MARGINAL & ECONOMÍAS DE ESCALA (IA HÍBRIDA)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7)
    add_header(s7, "Economía de Escala", "Costo Marginal Tendiente a Cero: La Ventaja Tecnológica",
               "Cómo la combinación de Sistema 1 (FastPath) y Sistema 2 (IA Multimodal) maximiza el margen.")

    # Columna Izquierda: Arquitectura de Costos
    c_arch = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.9))
    c_arch.fill.solid()
    c_arch.fill.fore_color.rgb = COLOR_CARD_DARK
    c_arch.line.color.rgb = RGBColor(30, 58, 100)
    atf = c_arch.text_frame
    atf.word_wrap = True
    atf.margin_top = Inches(0.25)
    atf.margin_left = Inches(0.25)

    ap0 = atf.paragraphs[0]
    ap0.text = "⚡ ARQUITECTURA HÍBRIDA DE CERO DESPERDICIO"
    ap0.font.size = Pt(12)
    ap0.font.bold = True
    ap0.font.color.rgb = COLOR_SKY

    ap1 = atf.add_paragraph()
    ap1.text = "• 85% de las Solicitudes (Sistema 1 FastPath):"
    ap1.font.size = Pt(11)
    ap1.font.bold = True
    ap1.font.color.rgb = COLOR_EMERALD
    ap1.space_before = Pt(10)

    ap1_d = atf.add_paragraph()
    ap1_d.text = "Consultas de saldo, corte y paquetes se resuelven en memoria RAM local en <1 milisegundo a CERO costo de tokens ($0.0000 USD)."
    ap1_d.font.size = Pt(10)
    ap1_d.font.color.rgb = COLOR_SLATE_LIGHT
    ap1_d.space_before = Pt(3)

    ap2 = atf.add_paragraph()
    ap2.text = "• 15% Complejo (Sistema 2 Gemini Vision):"
    ap2.font.size = Pt(11)
    ap2.font.bold = True
    ap2.font.color.rgb = COLOR_PURPLE
    ap2.space_before = Pt(12)

    ap2_d = atf.add_paragraph()
    ap2_d.text = "Solo se activa para auditar imágenes de comprobantes de pago bancarios y notas de voz con costo mínimo de $0.0008 USD."
    ap2_d.font.size = Pt(10)
    ap2_d.font.color.rgb = COLOR_SLATE_LIGHT
    ap2_d.space_before = Pt(3)

    # Columna Derecha: Comparativa de Escala
    c_scale = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.9))
    c_scale.fill.solid()
    c_scale.fill.fore_color.rgb = COLOR_CARD_DARK
    c_scale.line.color.rgb = RGBColor(30, 58, 100)
    stf = c_scale.text_frame
    stf.word_wrap = True
    stf.margin_top = Inches(0.25)
    stf.margin_left = Inches(0.25)

    sp0 = stf.paragraphs[0]
    sp0.text = "📉 COSTO POR USUARIO / MES AL ESCALAR"
    sp0.font.size = Pt(12)
    sp0.font.bold = True
    sp0.font.color.rgb = COLOR_AMBER

    scenarios = [
        ("Base Inicial (100.000 usuarios)", "$0.048 USD / mes"),
        ("Base Media (1.500.000 usuarios)", "$0.009 USD / mes"),
        ("Base Total (4.200.000 usuarios)", "$0.003 USD / mes")
    ]
    for sc_name, sc_val in scenarios:
        p_sc = stf.add_paragraph()
        p_sc.text = f"{sc_name}: {sc_val}"
        p_sc.font.size = Pt(11)
        p_sc.font.bold = True
        p_sc.font.color.rgb = COLOR_WHITE
        p_sc.space_before = Pt(12)

    sp_note = stf.add_paragraph()
    sp_note.text = "Conclusión Económica: A mayor volumen de usuarios, el costo unitario tiende asintóticamente a cero, expandiendo el margen bruto por encima del 80%."
    sp_note.font.size = Pt(10)
    sp_note.font.italic = True
    sp_note.font.color.rgb = COLOR_SLATE_MUTED
    sp_note.space_before = Pt(16)

    add_footer(s7)

    # =========================================================================
    # SLIDE 8: ESTADO DE RESULTADOS PROYECTADO A 36 MESES (P&L)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8)
    add_header(s8, "Plan Financiero", "Estado de Resultados Proyectado (36 Meses en Miles USD)",
               "Proyección financiera consolidada basada en supuestos conservadores de adopción.")

    # Tabla P&L
    rows = 7
    cols = 4
    left = Inches(0.8)
    top = Inches(1.8)
    width = Inches(11.7)
    height = Inches(4.8)

    table_shape = s8.shapes.add_table(rows, cols, left, top, width, height)
    tbl = table_shape.table

    tbl.columns[0].width = Inches(4.5)
    tbl.columns[1].width = Inches(2.4)
    tbl.columns[2].width = Inches(2.4)
    tbl.columns[3].width = Inches(2.4)

    headers = ["Renglón Financiero", "Año 1 (Adopción)", "Año 2 (Escala)", "Año 3 (Madurez)"]
    for c, h in enumerate(headers):
        cell = tbl.cell(0, c)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(20, 35, 65)
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE

    pnl_data = [
        ("Ahorro Neto OPEX Call Center", "$1,224", "$2,448", "$3,264"),
        ("Ingresos Venta Extra Datos", "$720", "$1,800", "$2,880"),
        ("Comisiones Cupones Cazador (20%)", "$360", "$1,152", "$2,304"),
        ("Comisiones Pasarela FinTech C2P", "$216", "$648", "$1,152"),
        ("TOTAL INGRESOS Y AHORROS", "$2,520", "$6,048", "$9,600"),
        ("EBITDA OPERATIVO PROYECTADO", "$1,975 (78.4%)", "$5,198 (85.9%)", "$8,520 (88.8%)")
    ]

    for r, row_data in enumerate(pnl_data):
        for c, val in enumerate(row_data):
            cell = tbl.cell(r + 1, c)
            cell.fill.solid()
            # Fila total o normal
            if r == 4:
                cell.fill.fore_color.rgb = RGBColor(30, 50, 90)
            elif r == 5:
                cell.fill.fore_color.rgb = RGBColor(6, 78, 59) # Verde EBITDA
            else:
                cell.fill.fore_color.rgb = COLOR_CARD_DARK

            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(10.5)
            p.font.bold = (r in [4, 5])
            p.font.color.rgb = COLOR_EMERALD if (r in [4, 5] and c > 0) else COLOR_WHITE

    add_footer(s8)

    # =========================================================================
    # SLIDE 9: ESTRATEGIA DE CONQUISTA DE DIGITEL Y MOVISTAR
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_bg(s9)
    add_header(s9, "Growth & Adquisición", "Cómo Capturamos Usuarios de la Competencia",
               "Estrategia perimetral para migrar abonados de Digitel y Movistar a costo de adquisición mínimo.")

    steps_conq = [
        ("1. Detección Perimetral", "0414 / 0424 / 0412", COLOR_PURPLE,
         "El firewall identifica cuando un usuario de la competencia entra al portal o escribe a WhatsApp."),
        ("2. Gancho Freemium", "1.000 Tokens de Bienvenida", COLOR_AMBER,
         "Se le permite interactuar gratis con MOVI para consultar promociones, demostrando la superioridad del servicio."),
        ("3. Portabilidad Express eSIM", "Migración en 3 Minutos", COLOR_SKY,
         "Se le ofrece conservar su mismo número y pasarse a la red 4GMAX de Movilnet con una eSIM digital instantánea."),
        ("4. LTV del Abonado Captado", "$42 USD / Año por Línea", COLOR_EMERALD,
         "120.000 líneas captadas representan +$5.04M USD anuales con costo de adquisición (CAC) casi cero.")
    ]

    for i, (title, highlight, color, desc) in enumerate(steps_conq):
        x = Inches(0.8 + i * 2.95)
        card = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(2.8), Inches(4.9))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = RGBColor(30, 58, 100)

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_top = Inches(0.25)
        ctf.margin_left = Inches(0.2)

        p0 = ctf.paragraphs[0]
        p0.text = title
        p0.font.size = Pt(12)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_WHITE

        p1 = ctf.add_paragraph()
        p1.text = highlight
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = color
        p1.space_before = Pt(8)

        p2 = ctf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(10)
        p2.font.color.rgb = COLOR_SLATE_LIGHT
        p2.space_before = Pt(14)

    add_footer(s9)

    # =========================================================================
    # SLIDE 10: SOLICITUD DE FONDOS, TRAMOS Y PRÓXIMOS PASOS
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_bg(s10)
    add_header(s10, "Decisión de Financiamiento", "Estructura de Capital Solicitado y Próximos Pasos",
               "Presupuesto de USD $850.000 estructurado en 3 tramos auditables contra entregables.")

    tramos = [
        ("TRAMO 1 (Desembolso Inmediato)", "$340.000 USD (40%)", COLOR_RED_MOVILNET,
         "• Infraestructura elástica y redundancia en Render Cloud.\n• Aseguramiento del canal WhatsApp Enterprise.\n• Despliegue de recargas C2P en 12 segundos."),
        ("TRAMO 2 (Mes 3 de Operación)", "$297.500 USD (35%)", COLOR_AMBER,
         "• Homologación masiva C2P con los 18 bancos nacionales.\n• Onboarding de 150 comercios aliados en Cazador.\n• Motor OCR avanzado para comprobantes bancarios."),
        ("TRAMO 3 (Mes 6 de Operación)", "$212.500 USD (25%)", COLOR_EMERALD,
         "• Lanzamiento nacional de Portabilidad Express eSIM.\n• Integración de Carrier Billing para streaming y LVBP.\n• Reserva operativa de contingencia y expansión.")
    ]

    for i, (ttitle, tval, tcolor, tdesc) in enumerate(tramos):
        x = Inches(0.8 + i * 3.95)
        card = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(3.75), Inches(3.4))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = RGBColor(30, 58, 100)

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_top = Inches(0.2)
        ctf.margin_left = Inches(0.25)

        p0 = ctf.paragraphs[0]
        p0.text = ttitle
        p0.font.size = Pt(11)
        p0.font.bold = True
        p0.font.color.rgb = tcolor

        p1 = ctf.add_paragraph()
        p1.text = tval
        p1.font.size = Pt(17)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_WHITE
        p1.space_before = Pt(4)

        p2 = ctf.add_paragraph()
        p2.text = tdesc
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_SLATE_LIGHT
        p2.space_before = Pt(10)

    # Banner Final de Conclusión
    callout = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.4), Inches(11.7), Inches(1.4))
    callout.fill.solid()
    callout.fill.fore_color.rgb = RGBColor(30, 20, 40)
    callout.line.color.rgb = COLOR_RED_MOVILNET

    ctf_call = callout.text_frame
    ctf_call.word_wrap = True
    ctf_call.margin_top = Inches(0.18)
    ctf_call.margin_left = Inches(0.3)

    cp0 = ctf_call.paragraphs[0]
    cp0.text = "🎯 CONCLUSIÓN CONJUNTA: UN PROYECTO GANADOR PARA MERCADEO Y FINANZAS"
    cp0.font.size = Pt(12)
    cp0.font.bold = True
    cp0.font.color.rgb = COLOR_WHITE

    cp1 = ctf_call.add_paragraph()
    cp1.text = "Para Finanzas: Payback menor a 8 meses, TIR del 68.4% y ahorro masivo de OPEX.  |  Para Mercadeo: +$1.29M en ingresos Año 1, ARPU de +43.5% y 120k nuevos clientes."
    cp1.font.size = Pt(10)
    cp1.font.color.rgb = COLOR_SLATE_LIGHT
    cp1.space_before = Pt(4)

    add_footer(s10)

    output_path = "/Users/ismael/Desktop/121026_CORE_MOVILNET/Movilnet_161026/docs/PRESENTACION_EJECUTIVA_MOVILNET_IA.pptx"
    prs.save(output_path)
    print(f"✅ Presentación PowerPoint generada exitosamente en: {output_path}")
    return output_path

if __name__ == "__main__":
    create_deck()
