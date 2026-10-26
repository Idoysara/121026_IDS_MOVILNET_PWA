#!/usr/bin/env python3
"""
scripts/generate_powerpoint_presentation.py
=============================================================================
Generador Oficial de la Presentación PowerPoint (.pptx) Ejecutiva
Proyecto: Asistente MOVI 4GMAX — Telecomunicaciones Movilnet C.A.
Audiencia Dual: Comité de Inversión (Economistas) & Dpto. de Mercadeo (Growth)
Modelo: Alianza Estratégica — Aporte en Especie de Movilnet (4.2M Usuarios + Marketing)
        Financiamiento Tecnológico Privado ($450k) con Revenue Share Acelerado
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
COLOR_ROSE = RGBColor(244, 63, 94)         # Rosa Fucsia Énfasis

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
    # SLIDE 1: PORTADA EJECUTIVA — MODELO DE ALIANZA ESTRATÉGICA
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1)

    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.2), Inches(0.12), Inches(3.2))
    bar.fill.solid()
    bar.fill.fore_color.rgb = COLOR_RED_MOVILNET
    bar.line.fill.background()

    tb = s1.shapes.add_textbox(Inches(1.2), Inches(1.1), Inches(11.0), Inches(3.4))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "DOSSIER ESTRATÉGICO DE INVERSIÓN & MODELO COMERCIAL"
    p0.font.size = Pt(11.5)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_RED_MOVILNET

    p1 = tf.add_paragraph()
    p1.text = "Ecosistema Conversacional MOVI 4GMAX"
    p1.font.size = Pt(34)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_WHITE
    p1.space_before = Pt(8)

    p2 = tf.add_paragraph()
    p2.text = "Alianza Público-Privada: Aporte en Canales de Movilnet (4.2M Usuarios + Marketing) & Capital Privado Tecnológico"
    p2.font.size = Pt(15.5)
    p2.font.color.rgb = COLOR_SLATE_LIGHT
    p2.space_before = Pt(8)

    p3 = tf.add_paragraph()
    p3.text = "Telecomunicaciones Movilnet C.A.  •  WhatsApp Master (+58 424 153 3712) + PWA con Cero Consumo de Datos"
    p3.font.size = Pt(11.5)
    p3.font.color.rgb = COLOR_SLATE_MUTED
    p3.space_before = Pt(14)

    # 4 KPI Highlights
    kpis = [
        ("Base Cautiva Movilnet", "4.2M Usuarios", COLOR_SKY, "Acceso directo inmediato (CAC = $0)"),
        ("Aporte de Marketing", "100% Cubierto", COLOR_AMBER, "POP, Banderines, Tours y RRSS por Movilnet"),
        ("Payback Inversión", "6.2 Meses", COLOR_EMERALD, "Retorno acelerado por Revenue Share 75/25"),
        ("TIR Anual (IRR)", "74.6%", COLOR_EMERALD, "Flujo recurrente libre de riesgo de demanda")
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
        cp1.font.size = Pt(23)
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
    # SLIDE 2: EL MODELO DE ALIANZA: SIMETRÍA PERFECTA DE APORTES
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2)
    add_header(s2, "Estructura del Negocio", "El Modelo de Alianza: Simetría de Aportes entre las Partes",
               "Movilnet no desembolsa fondos líquidos; aporta audiencia masiva y marketing nacional. El capital privado aporta tecnología.")

    # Columna Izquierda: Aporte Movilnet
    c_movilnet = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.9))
    c_movilnet.fill.solid()
    c_movilnet.fill.fore_color.rgb = COLOR_CARD_DARK
    c_movilnet.line.color.rgb = RGBColor(230, 32, 32)
    mtf = c_movilnet.text_frame
    mtf.word_wrap = True
    mtf.margin_top = Inches(0.25)
    mtf.margin_left = Inches(0.3)

    mp0 = mtf.paragraphs[0]
    mp0.text = "🏢 APORTE ESTRATÉGICO DE MOVILNET (CERO FONDOS LÍQUIDOS)"
    mp0.font.size = Pt(11.5)
    mp0.font.bold = True
    mp0.font.color.rgb = COLOR_RED_MOVILNET

    items_movilnet = [
        ("Base Cautiva de 4.2M Usuarios:", "Acceso exclusivo e inmediato a 4.2 millones de abonados activos sin costo de adquisición (CAC = $0)."),
        ("Material POP Nacional:", "Producción y montaje de banderines, pendones, tótems y habladores en oficinas y agentes autorizados."),
        ("Presencia Física en Tours y Ferias:", "Inclusión obligatoria en Tours Movilnet regionales/municipales, seminarios, charlas y eventos cubiertos 100% por Movilnet."),
        ("Ecosistema Digital Oficial:", "Difusión masiva en redes oficiales (Instagram, TikTok, X), portal web movilnet.com.ve y SMS institucionales."),
        ("Protagonismo Institucional:", "MOVI como protagonista e imagen oficial de la compañía.")
    ]
    for tit, dsc in items_movilnet:
        p_t = mtf.add_paragraph()
        p_t.text = f"• {tit} " + dsc
        p_t.font.size = Pt(9.5)
        p_t.font.color.rgb = COLOR_SLATE_LIGHT
        p_t.space_before = Pt(7)

    # Columna Derecha: Aporte Inversionista
    c_inversor = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.9))
    c_inversor.fill.solid()
    c_inversor.fill.fore_color.rgb = COLOR_CARD_DARK
    c_inversor.line.color.rgb = RGBColor(16, 185, 129)
    itf = c_inversor.text_frame
    itf.word_wrap = True
    itf.margin_top = Inches(0.25)
    itf.margin_left = Inches(0.3)

    ip0 = itf.paragraphs[0]
    ip0.text = "💼 APORTE DEL INVERSIONISTA PRIVADO (CAPITAL TECNOLÓGICO)"
    ip0.font.size = Pt(11.5)
    ip0.font.bold = True
    ip0.font.color.rgb = COLOR_EMERALD

    items_inversor = [
        ("Financiamiento Tecnológico Total:", "Aporte de USD $450.000 para cómputo elástico en la nube, clúster de servidores de alta concurrencia y edge CDN."),
        ("Inferencia de IA y Modelos LLM:", "Integración de Google Gemini 2.5 Flash Multimodal para visión bancaria OCR y transcripción de voz."),
        ("Pasarela FinTech SUDEBAN C2P:", "Conectores interbancarios en tiempo real para liquidación de cobros en 12 segundos."),
        ("Ingeniería SRE 24/7 & Seguridad:", "Blindaje criptográfico SHA-256, Zero-PII, SLA 99.95% y mantenimiento operativo continuo."),
        ("Esquema de Retorno Acelerado:", "Retiene el 75% del flujo de nuevos ingresos hasta recuperar el 100% de la inversión (Payback en 6.2 meses).")
    ]
    for tit, dsc in items_inversor:
        p_t = itf.add_paragraph()
        p_t.text = f"• {tit} " + dsc
        p_t.font.size = Pt(9.5)
        p_t.font.color.rgb = COLOR_SLATE_LIGHT
        p_t.space_before = Pt(7)

    add_footer(s2)

    # =========================================================================
    # SLIDE 3: MOVI: PROTAGONISTA PRINCIPAL DE MARCA Y MARKETING MASIVO
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3)
    add_header(s3, "Estrategia de Mercadeo", "MOVI: El Protagonista Principal en Calles, Eventos y Medios",
               "Despliegue integral cubierto y financiado 100% por el presupuesto habitual de Mercadeo de Movilnet.")

    pillars = [
        ("1. Material POP & Puntos de Venta", "Presencia en Cada Tienda", COLOR_RED_MOVILNET,
         ["• Banderines oficiales MOVI en agentes comerciales.",
          "• Pendones de alto impacto: 'Recarga en 12s por WhatsApp'.",
          "• Habladores en taquillas con QR dinámico para autogestión.",
          "• Tótems interactivos en centros comerciales del país."]),
        ("2. Tours Movilnet Nacionales", "Caravanas en Regiones y Plazas", COLOR_AMBER,
         ["• Presencia en charlas, conferencias, seminarios y ferias.",
          "• Activaciones en vivo: recarga y consulta en tarima pública.",
          "• Trivias gamificadas conducidas por la IA en WhatsApp.",
          "• Cobertura logística y viáticos 100% pagados por Movilnet."]),
        ("3. Ecosistema Digital & Web", "Redes Sociales y Masivos", COLOR_SKY,
         ["• Hero Banner principal en www.movilnet.com.ve.",
          "• Campaña viral en Instagram, TikTok, X y Facebook.",
          "• SMS push institucionales dirigidos a los 4.2M de usuarios.",
          "• Bono Freemium de 1.000 tokens para captar a la competencia."])
    ]

    for i, (title, sub, color, bullet_list) in enumerate(pillars):
        x = Inches(0.8 + i * 3.95)
        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(3.75), Inches(4.9))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = RGBColor(30, 58, 100)

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_top = Inches(0.2)
        ctf.margin_left = Inches(0.22)

        p0 = ctf.paragraphs[0]
        p0.text = title
        p0.font.size = Pt(11.5)
        p0.font.bold = True
        p0.font.color.rgb = color

        p1 = ctf.add_paragraph()
        p1.text = sub
        p1.font.size = Pt(14)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_WHITE
        p1.space_before = Pt(3)

        for b in bullet_list:
            pb = ctf.add_paragraph()
            pb.text = b
            pb.font.size = Pt(9.5)
            pb.font.color.rgb = COLOR_SLATE_LIGHT
            pb.space_before = Pt(9)

    add_footer(s3)

    # =========================================================================
    # SLIDE 4: EL PROBLEMA ECONÓMICO VS. LA SOLUCIÓN PRODUCTIVA
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4)
    add_header(s4, "Diagnóstico del Negocio Telco", "El Salto Cuántico: De Pozo de OPEX a Activo de Nuevos Ingresos",
               "Comparativa económica entre la atención humana tradicional y la plataforma autónoma MOVI.")

    c_left = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.9))
    c_left.fill.solid()
    c_left.fill.fore_color.rgb = COLOR_CARD_DARK
    c_left.line.color.rgb = RGBColor(127, 29, 29)
    ltf = c_left.text_frame
    ltf.word_wrap = True
    ltf.margin_top = Inches(0.25)
    ltf.margin_left = Inches(0.3)

    lp0 = ltf.paragraphs[0]
    lp0.text = "❌ EL MODELO TRADICIONAL (POZO DE OPEX)"
    lp0.font.size = Pt(12)
    lp0.font.bold = True
    lp0.font.color.rgb = COLOR_RED_MOVILNET

    lp1 = ltf.add_paragraph()
    lp1.text = "• Costo Rígido por Llamada: $0.85 USD promedio por ticket humano."
    lp1.font.size = Pt(10.5)
    lp1.font.color.rgb = COLOR_SLATE_LIGHT
    lp1.space_before = Pt(12)

    lp2 = ltf.add_paragraph()
    lp2.text = "• Ineficiencia Cognitiva: 62% del tráfico son preguntas obvias de saldo y corte."
    lp2.font.size = Pt(10.5)
    lp2.font.color.rgb = COLOR_SLATE_LIGHT
    lp2.space_before = Pt(10)

    lp3 = ltf.add_paragraph()
    lp3.text = "• Fricción en Recargas: Tiempos de espera de 7 a 15 min causan fuga de clientes (18% churn)."
    lp3.font.size = Pt(10.5)
    lp3.font.color.rgb = COLOR_SLATE_LIGHT
    lp3.space_before = Pt(10)

    lp4 = ltf.add_paragraph()
    lp4.text = "• Generación de Ingresos: CERO ventas adicionales en llamadas de reclamo."
    lp4.font.size = Pt(10.5)
    lp4.font.color.rgb = COLOR_SLATE_LIGHT
    lp4.space_before = Pt(10)

    c_right = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.9))
    c_right.fill.solid()
    c_right.fill.fore_color.rgb = COLOR_CARD_DARK
    c_right.line.color.rgb = RGBColor(6, 78, 59)
    rtf = c_right.text_frame
    rtf.word_wrap = True
    rtf.margin_top = Inches(0.25)
    rtf.margin_left = Inches(0.3)

    rp0 = rtf.paragraphs[0]
    rp0.text = "✅ LA PLATAFORMA MOVI (ACTIVO GENERADOR DE DINERO)"
    rp0.font.size = Pt(12)
    rp0.font.bold = True
    rp0.font.color.rgb = COLOR_EMERALD

    rp1 = rtf.add_paragraph()
    rp1.text = "• Costo Marginal Infinitesimal: $0.0044 USD por sesión (ahorro del 94.8%)."
    rp1.font.size = Pt(10.5)
    rp1.font.color.rgb = COLOR_SLATE_LIGHT
    rp1.space_before = Pt(12)

    rp2 = rtf.add_paragraph()
    rp2.text = "• Capacidad de Escala Elástica: 100.000 usuarios concurrentes sin colas de espera."
    rp2.font.size = Pt(10.5)
    rp2.font.color.rgb = COLOR_SLATE_LIGHT
    rp2.space_before = Pt(10)

    rp3 = rtf.add_paragraph()
    rp3.text = "• Recarga C2P en 12 Segundos: Pago Móvil integrado eleva recargas de 2.1 a 3.8 / mes."
    rp3.font.size = Pt(10.5)
    rp3.font.color.rgb = COLOR_SLATE_LIGHT
    rp3.space_before = Pt(10)

    rp4 = rtf.add_paragraph()
    rp4.text = "• Cross-Selling Automático: Venta de bolsas Extra Datos y cupones retail al consultar saldo."
    rp4.font.size = Pt(10.5)
    rp4.font.color.rgb = COLOR_SLATE_LIGHT
    rp4.space_before = Pt(10)

    add_footer(s4)

    # =========================================================================
    # SLIDE 5: LAS 5 VÍAS DIRECTAS DE NUEVOS INGRESOS EN CAJA
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5)
    add_header(s5, "Monetización Comercial", "Las 5 Vías Directas de Nuevos Ingresos en Caja",
               "Dónde y cómo se generan ingresos reales atribuibles a la gestión de mercadeo.")

    streams = [
        ("1. Extra Datos (Upselling)", "$840k / Año 1", COLOR_ROSE,
         "Detección predictiva cuando restan <200 MB. Oferta automática con tasa de conversión del 8.7%."),
        ("2. Mayor Frecuencia C2P", "+$1.35 ARPU", COLOR_SKY,
         "Recarga sin fricción bancaria en 12 seg. El abonado pasa de 2.1 a 3.8 recargas mensuales."),
        ("3. Retail Media Cazador", "$420k / Año 1", COLOR_AMBER,
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

        card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = RGBColor(30, 58, 100)

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_top = Inches(0.18)
        ctf.margin_left = Inches(0.25)

        p_t = ctf.paragraphs[0]
        p_t.text = stitle
        p_t.font.size = Pt(12)
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
        p_d.font.size = Pt(9.5)
        p_d.font.color.rgb = COLOR_SLATE_LIGHT
        p_d.space_before = Pt(5)

    add_footer(s5)

    # =========================================================================
    # SLIDE 6: EL FUNNEL CONVERSACIONAL EN 12 SEGUNDOS
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6)
    add_header(s6, "Funnel de Conversión", "El Embudo Conversacional: De Consulta a Venta en 12 Segundos",
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
        card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(2.8), Inches(4.9))
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
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_WHITE
        p1.space_before = Pt(4)

        p2 = ctf.add_paragraph()
        p2.text = f'"{dialog}"'
        p2.font.size = Pt(9.5)
        p2.font.italic = True
        p2.font.color.rgb = RGBColor(226, 232, 240)
        p2.space_before = Pt(12)

        p3 = ctf.add_paragraph()
        p3.text = expl
        p3.font.size = Pt(9)
        p3.font.color.rgb = COLOR_SLATE_MUTED
        p3.space_before = Pt(12)

    add_footer(s6)

    # =========================================================================
    # SLIDE 7: CAZADOR DE OFERTAS & RETAIL MEDIA (SPLIT 20/80)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7)
    add_header(s7, "Alianzas Estratégicas", "Cazador de Ofertas: La Red Publicitaria Retail Media",
               "Monetización de tráfico físico en comercios aliados con tecnología antifraude TOTP.")

    kpi_retail = [
        ("56 Marcas Aliadas", "Cadenas Comerciales Activas", COLOR_RED_MOVILNET, "Arturo's, Farmahorro, Cines Unidos, Traki, Automercados Plaza's."),
        ("204 Ofertas en Radar", "Descuentos Hiper-Geolocalizados", COLOR_AMBER, "Promociones con radio de cobertura dinámico de 500m a 50 km."),
        ("Split Comercial 20 / 80", "Ingreso Neto para Movilnet", COLOR_EMERALD, "Movilnet retiene $0.40 USD netos por cada cupón canjeado en tienda.")
    ]
    for i, (v, t, c, d) in enumerate(kpi_retail):
        x = Inches(0.8 + i * 3.95)
        card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(3.75), Inches(2.2))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = RGBColor(30, 58, 100)

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_top = Inches(0.2)
        ctf.margin_left = Inches(0.25)

        p0 = ctf.paragraphs[0]
        p0.text = v
        p0.font.size = Pt(21)
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
        p2.space_before = Pt(5)

    box_sec = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.3), Inches(11.7), Inches(2.4))
    box_sec.fill.solid()
    box_sec.fill.fore_color.rgb = COLOR_CARD_DARK
    box_sec.line.color.rgb = RGBColor(40, 70, 120)
    stf = box_sec.text_frame
    stf.word_wrap = True
    stf.margin_top = Inches(0.22)
    stf.margin_left = Inches(0.3)

    sp0 = stf.paragraphs[0]
    sp0.text = "🛡️ CÓMO FUNCIONA EL MODELO DE NEGOCIO Y LA SEGURIDAD ANTIFRAUDE"
    sp0.font.size = Pt(12)
    sp0.font.bold = True
    sp0.font.color.rgb = COLOR_SKY

    sp1 = stf.add_paragraph()
    sp1.text = "1. Generación de Cupones TOTP (60 Segundos): Código dinámico de un solo uso que expira en 60s, evitando capturas falsificadas en taquilla."
    sp1.font.size = Pt(10)
    sp1.font.color.rgb = COLOR_SLATE_LIGHT
    sp1.space_before = Pt(7)

    sp2 = stf.add_paragraph()
    sp2.text = "2. Liquidación Automática en Cero Inventario: Movilnet no compra ni almacena inventario. Solo cobra comisión al validarse el consumo en el POS aliado."
    sp2.font.size = Pt(10)
    sp2.font.color.rgb = COLOR_SLATE_LIGHT
    sp2.space_before = Pt(5)

    sp3 = stf.add_paragraph()
    sp3.text = "3. Margen Operativo Bruto >85%: Operación 100% sobre software en la nube, traduciéndose en beneficio neto directo."
    sp3.font.size = Pt(10)
    sp3.font.color.rgb = COLOR_EMERALD
    sp3.space_before = Pt(5)

    add_footer(s7)

    # =========================================================================
    # SLIDE 8: COSTO MARGINAL & ECONOMÍAS DE ESCALA (IA HÍBRIDA)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8)
    add_header(s8, "Economía de Escala", "Costo Marginal Tendiente a Cero: La Ventaja Tecnológica",
               "Cómo la combinación de Sistema 1 (FastPath) y Sistema 2 (IA Multimodal) maximiza el margen con CAC = $0.")

    c_arch = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.9))
    c_arch.fill.solid()
    c_arch.fill.fore_color.rgb = COLOR_CARD_DARK
    c_arch.line.color.rgb = RGBColor(30, 58, 100)
    atf = c_arch.text_frame
    atf.word_wrap = True
    atf.margin_top = Inches(0.25)
    atf.margin_left = Inches(0.25)

    ap0 = atf.paragraphs[0]
    ap0.text = "⚡ ARQUITECTURA HÍBRIDA DE CERO DESPERDICIO"
    ap0.font.size = Pt(11.5)
    ap0.font.bold = True
    ap0.font.color.rgb = COLOR_SKY

    ap1 = atf.add_paragraph()
    ap1.text = "• 85% de las Solicitudes (Sistema 1 FastPath):"
    ap1.font.size = Pt(10.5)
    ap1.font.bold = True
    ap1.font.color.rgb = COLOR_EMERALD
    ap1.space_before = Pt(10)

    ap1_d = atf.add_paragraph()
    ap1_d.text = "Consultas de saldo, corte y paquetes se resuelven en memoria RAM local en <1 ms a CERO costo de tokens ($0.0000 USD)."
    ap1_d.font.size = Pt(9.5)
    ap1_d.font.color.rgb = COLOR_SLATE_LIGHT
    ap1_d.space_before = Pt(3)

    ap2 = atf.add_paragraph()
    ap2.text = "• 15% Complejo (Sistema 2 Gemini Vision):"
    ap2.font.size = Pt(10.5)
    ap2.font.bold = True
    ap2.font.color.rgb = COLOR_PURPLE
    ap2.space_before = Pt(12)

    ap2_d = atf.add_paragraph()
    ap2_d.text = "Solo se activa para auditar imágenes de comprobantes bancarios y notas de voz con costo de $0.0008 USD."
    ap2_d.font.size = Pt(9.5)
    ap2_d.font.color.rgb = COLOR_SLATE_LIGHT
    ap2_d.space_before = Pt(3)

    c_scale = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.9))
    c_scale.fill.solid()
    c_scale.fill.fore_color.rgb = COLOR_CARD_DARK
    c_scale.line.color.rgb = RGBColor(30, 58, 100)
    stf = c_scale.text_frame
    stf.word_wrap = True
    stf.margin_top = Inches(0.25)
    stf.margin_left = Inches(0.25)

    sp0 = stf.paragraphs[0]
    sp0.text = "📉 COSTO POR USUARIO / MES AL ESCALAR (CAC = $0)"
    sp0.font.size = Pt(11.5)
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
        p_sc.font.size = Pt(10.5)
        p_sc.font.bold = True
        p_sc.font.color.rgb = COLOR_WHITE
        p_sc.space_before = Pt(12)

    sp_note = stf.add_paragraph()
    sp_note.text = "Conclusión para el Inversor: Al asumir Movilnet el 100% del marketing y aportar 4.2M de usuarios, el CAC es $0 y el margen operativo supera el 85%."
    sp_note.font.size = Pt(9.5)
    sp_note.font.italic = True
    sp_note.font.color.rgb = COLOR_SLATE_MUTED
    sp_note.space_before = Pt(16)

    add_footer(s8)

    # =========================================================================
    # SLIDE 9: ESTADO DE RESULTADOS PROYECTADO A 36 MESES (P&L)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_bg(s9)
    add_header(s9, "Plan Financiero", "Estado de Resultados Consolidado (36 Meses en Miles USD)",
               "Proyección financiera basada en la adopción masiva impulsada por los Tours y Canales Oficiales.")

    rows = 7
    cols = 4
    left = Inches(0.8)
    top = Inches(1.8)
    width = Inches(11.7)
    height = Inches(4.8)

    table_shape = s9.shapes.add_table(rows, cols, left, top, width, height)
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
        ("Ingresos Venta Extra Datos", "$840", "$2,100", "$3,360"),
        ("Comisiones Cupones Cazador (20%)", "$420", "$1,344", "$2,688"),
        ("Comisiones Pasarela FinTech C2P", "$252", "$756", "$1,344"),
        ("TOTAL INGRESOS Y AHORROS", "$2,736", "$6,648", "$10,656"),
        ("EBITDA OPERATIVO PROYECTADO", "$2,331 (85.2%)", "$6,008 (90.3%)", "$9,816 (92.1%)")
    ]

    for r, row_data in enumerate(pnl_data):
        for c, val in enumerate(row_data):
            cell = tbl.cell(r + 1, c)
            cell.fill.solid()
            if r == 4:
                cell.fill.fore_color.rgb = RGBColor(30, 50, 90)
            elif r == 5:
                cell.fill.fore_color.rgb = RGBColor(6, 78, 59)
            else:
                cell.fill.fore_color.rgb = COLOR_CARD_DARK

            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(10)
            p.font.bold = (r in [4, 5])
            p.font.color.rgb = COLOR_EMERALD if (r in [4, 5] and c > 0) else COLOR_WHITE

    add_footer(s9)

    # =========================================================================
    # SLIDE 10: RETORNO DEL INVERSOR: CAPITAL $450k & REVENUE SHARE 75/25
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_bg(s10)
    add_header(s10, "Decisión de Financiamiento", "Estructura de Capital Privado ($450k) y Plan de Retorno",
               "100% de la inversión asignada a tecnología e IA. Retorno acelerado mediante Revenue Share 75/25.")

    tramos = [
        ("TRAMO 1: Desembolso Inmediato", "$225.000 USD (50%)", COLOR_RED_MOVILNET,
         "• Clúster elástico en la nube y edge CDN.\n• Aseguramiento del gateway WhatsApp Enterprise.\n• Despliegue de recargas C2P en 12 segundos."),
        ("TRAMO 2: Mes 2 de Operación", "$135.000 USD (30%)", COLOR_AMBER,
         "• Homologación masiva C2P con 18 bancos.\n• Onboarding de 150 comercios en Cazador.\n• Motor OCR Gemini Flash para comprobantes."),
        ("TRAMO 3: Mes 4 de Operación", "$90.000 USD (20%)", COLOR_EMERALD,
         "• Lanzamiento de Portabilidad Express eSIM.\n• Acompañamiento a Tours Movilnet nacionales.\n• Reserva operativa de contingencia y expansión.")
    ]

    for i, (ttitle, tval, tcolor, tdesc) in enumerate(tramos):
        x = Inches(0.8 + i * 3.95)
        card = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(3.75), Inches(3.3))
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
        p0.font.color.rgb = COLOR_WHITE

        p1 = ctf.add_paragraph()
        p1.text = tval
        p1.font.size = Pt(17)
        p1.font.bold = True
        p1.font.color.rgb = tcolor
        p1.space_before = Pt(3)

        p2 = ctf.add_paragraph()
        p2.text = tdesc
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_SLATE_LIGHT
        p2.space_before = Pt(8)

    # Banner Inferior: Mecanismo de Retorno Waterfall
    box_ret = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.3), Inches(11.7), Inches(1.5))
    box_ret.fill.solid()
    box_ret.fill.fore_color.rgb = RGBColor(6, 78, 59)
    box_ret.line.color.rgb = COLOR_EMERALD

    rtf = box_ret.text_frame
    rtf.word_wrap = True
    rtf.margin_top = Inches(0.15)
    rtf.margin_left = Inches(0.3)

    rp0 = rtf.paragraphs[0]
    rp0.text = "🎯 MECANISMO WATERFALL DE RETORNO Y GANANCIA DEL INVERSIONISTA"
    rp0.font.size = Pt(12)
    rp0.font.bold = True
    rp0.font.color.rgb = COLOR_WHITE

    rp1 = rtf.add_paragraph()
    rp1.text = "• Fase 1 (Amortización Acelerada): El Inversor retiene el 75% del flujo neto hasta recuperar los $450k + 20% preferente. Payback en 6.2 Meses."
    rp1.font.size = Pt(10)
    rp1.font.color.rgb = RGBColor(209, 250, 229)
    rp1.space_before = Pt(4)

    rp2 = rtf.add_paragraph()
    rp2.text = "• Fase 2 (Utilidad Recurrente Compartida): Split 50% Inversor / 50% Movilnet. Flujo acumulado a 36 meses: $4.25M USD (ROI 9.4x)."
    rp2.font.size = Pt(10)
    rp2.font.color.rgb = RGBColor(209, 250, 229)
    rp2.space_before = Pt(3)

    add_footer(s10)

    # Guardar Presentación
    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "PRESENTACION_EJECUTIVA_MOVILNET_IA.pptx")
    prs.save(out_path)
    print(f"✅ Presentación PowerPoint guardada con éxito en: {out_path}")
    print(f"📊 Total de diapositivas generadas: {len(prs.slides)}")

if __name__ == "__main__":
    create_deck()
