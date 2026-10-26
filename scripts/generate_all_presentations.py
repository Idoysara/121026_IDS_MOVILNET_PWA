#!/usr/bin/env python3
"""
scripts/generate_all_presentations.py
=============================================================================
Generador Maestro de Presentaciones PowerPoint (.pptx) para Movilnet IA 4GMAX
1. PRESENTACION_EJECUTIVA_INVERSIONISTA_ECONOMISTA.pptx (10 láminas financieras)
2. PRESENTACION_EJECUTIVA_DEPARTAMENTO_MERCADEO.pptx (10 láminas de marketing)
3. PRESENTACION_EJECUTIVA_MOVILNET_IA.pptx (Mazo ejecutivo consolidado)
=============================================================================
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# Paleta Corporativa Oficial
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

def setup_prs():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    return prs

def add_bg(prs, slide):
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

def add_footer(slide, category="Dossier Oficial"):
    footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.7), Inches(0.35))
    tf = footer_box.text_frame
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = f"🌐 Portal PWA 4GMAX: https://one21026-ids-movilnet-pwa-bxmz.onrender.com/ui/pwa_stitch/index.html  |  {category}  |  Telecomunicaciones Movilnet C.A."
    p.font.size = Pt(8.5)
    p.font.color.rgb = COLOR_SLATE_MUTED

# =============================================================================
# 1. DECK INVERSIONISTA & ECONOMISTA
# =============================================================================
def build_inversionista_deck(out_path):
    prs = setup_prs()
    layout = prs.slide_layouts[6]

    # Slide 1: Portada
    s1 = prs.slides.add_slide(layout)
    add_bg(prs, s1)
    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.2), Inches(0.12), Inches(3.2))
    bar.fill.solid()
    bar.fill.fore_color.rgb = COLOR_RED_MOVILNET
    bar.line.fill.background()

    tb = s1.shapes.add_textbox(Inches(1.2), Inches(1.1), Inches(11.0), Inches(3.4))
    tf = tb.text_frame
    tf.word_wrap = True
    p0 = tf.paragraphs[0]
    p0.text = "COMITÉ DE INVERSIÓN & EVALUACIÓN FINANCIERA — ECONOMISTAS"
    p0.font.size = Pt(11.5)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_RED_MOVILNET

    p1 = tf.add_paragraph()
    p1.text = "Propuesta de Financiamiento Tecnológico MOVI"
    p1.font.size = Pt(33)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_WHITE
    p1.space_before = Pt(8)

    p2 = tf.add_paragraph()
    p2.text = "Modelo de Alianza: Movilnet Aporta 4.2M Usuarios y Marketing Nacional | Inversión Privada $450k | Payback 6.2 Meses"
    p2.font.size = Pt(15)
    p2.font.color.rgb = COLOR_SLATE_LIGHT
    p2.space_before = Pt(8)

    kpis = [
        ("Base Cautiva", "4.2M Usuarios", COLOR_SKY, "Acceso directo inmediato (CAC = $0)"),
        ("Capital Requerido", "$450.000 USD", COLOR_AMBER, "100% tecnología e IA (3 tramos auditables)"),
        ("Payback Inversor", "6.2 Meses", COLOR_EMERALD, "Revenue Share 75/25 en Fase 1"),
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
        cp1.font.size = Pt(22)
        cp1.font.bold = True
        cp1.font.color.rgb = color
        cp1.space_before = Pt(4)

        cp2 = ctf.add_paragraph()
        cp2.text = desc
        cp2.font.size = Pt(9)
        cp2.font.color.rgb = COLOR_SLATE_LIGHT
        cp2.space_before = Pt(4)
    add_footer(s1, "Dossier Inversionista")

    # Slide 2: Simetría de Aportes
    s2 = prs.slides.add_slide(layout)
    add_bg(prs, s2)
    add_header(s2, "Estructura del Negocio", "Simetría de Aportes: Aporte en Especie vs Capital Privado",
               "Movilnet no aporta fondos económicos en efectivo. El inversor no gasta en publicidad.")
    c_m = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.9))
    c_m.fill.solid()
    c_m.fill.fore_color.rgb = COLOR_CARD_DARK
    c_m.line.color.rgb = RGBColor(230, 32, 32)
    mtf = c_m.text_frame
    mtf.word_wrap = True
    mtf.margin_top = Inches(0.25)
    mtf.margin_left = Inches(0.3)
    mp0 = mtf.paragraphs[0]
    mp0.text = "🏢 APORTE ESTRATÉGICO DE MOVILNET (CERO FONDOS LÍQUIDOS)"
    mp0.font.size = Pt(11.5)
    mp0.font.bold = True
    mp0.font.color.rgb = COLOR_RED_MOVILNET
    m_bullets = [
        "Base Cautiva de 4.2M de Clientes Activos (CAC = $0)",
        "Material POP Nacional (Banderines, Pendones, Habladores en Tiendas)",
        "Tours Movilnet en Regiones, Municipios y Plazas 100% Pagados",
        "Ecosistema Digital: Redes Sociales, Web movilnet.com.ve y SMS Push",
        "Protagonismo Absoluto de MOVI como Imagen Oficial"
    ]
    for b in m_bullets:
        pb = mtf.add_paragraph()
        pb.text = f"• {b}"
        pb.font.size = Pt(10)
        pb.font.color.rgb = COLOR_SLATE_LIGHT
        pb.space_before = Pt(10)

    c_i = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.9))
    c_i.fill.solid()
    c_i.fill.fore_color.rgb = COLOR_CARD_DARK
    c_i.line.color.rgb = RGBColor(16, 185, 129)
    itf = c_i.text_frame
    itf.word_wrap = True
    itf.margin_top = Inches(0.25)
    itf.margin_left = Inches(0.3)
    ip0 = itf.paragraphs[0]
    ip0.text = "💼 APORTE DEL INVERSIONISTA (CAPITAL TECNOLÓGICO: $450k)"
    ip0.font.size = Pt(11.5)
    ip0.font.bold = True
    ip0.font.color.rgb = COLOR_EMERALD
    i_bullets = [
        "Infraestructura Cloud Elástica y Edge CDN (Alta Concurrencia)",
        "Motores de Inteligencia Artificial Multimodal (Gemini 2.5 Flash)",
        "Pasarela SUDEBAN C2P Interbancaria (Cobro en 12 Segundos)",
        "Ingeniería SRE 24/7 y Blindaje Criptográfico Zero-PII",
        "Recuperación Acelerada Waterfall: 75% Flujo Neto (Payback 6.2m)"
    ]
    for b in i_bullets:
        pb = itf.add_paragraph()
        pb.text = f"• {b}"
        pb.font.size = Pt(10)
        pb.font.color.rgb = COLOR_SLATE_LIGHT
        pb.space_before = Pt(10)
    add_footer(s2, "Dossier Inversionista")

    # Slide 3: Diagnóstico Telco
    s3 = prs.slides.add_slide(layout)
    add_bg(prs, s3)
    add_header(s3, "Diagnóstico Macroeconómico", "De Pozo de OPEX ($0.85/ticket) a Activo Digital ($0.0044)",
               "La atención analógica ahoga los márgenes; la IA híbrida diluye el costo unitario a cero.")
    boxes_s3 = [
        ("❌ Call Center Analógico Humano", "$0.85 USD / Llamada", COLOR_RED_MOVILNET,
         ["• 62% del tráfico son consultas rutinarias sin valor comercial.",
          "• Tiempos de espera de 7 a 15 min causan fuga de clientes (18% churn).",
          "• Costo rígidamente variable: duplicar llamadas duplica la nómina.",
          "• Retorno de la interacción: CERO ingresos adicionales."]),
        ("✅ Asistente MOVI IA Híbrida", "$0.0044 USD / Sesión", COLOR_EMERALD,
         ["• Ahorro directo del 94.8% en costo unitario por interacción.",
          "• Capacidad elástica: 100.000 usuarios simultáneos sin colas.",
          "• Recarga Pago Móvil C2P en 12 segundos sin salir de WhatsApp.",
          "• Cross-selling activo: coloca Extra Datos y cupones retail."])
    ]
    for i, (btit, bsub, bcol, bbuls) in enumerate(boxes_s3):
        x = Inches(0.8 + i * 5.95)
        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(5.75), Inches(4.9))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = bcol
        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_top = Inches(0.25)
        ctf.margin_left = Inches(0.3)
        cp0 = ctf.paragraphs[0]
        cp0.text = btit
        cp0.font.size = Pt(12)
        cp0.font.bold = True
        cp0.font.color.rgb = bcol

        cp1 = ctf.add_paragraph()
        cp1.text = bsub
        cp1.font.size = Pt(17)
        cp1.font.bold = True
        cp1.font.color.rgb = COLOR_WHITE
        cp1.space_before = Pt(4)

        for b in bbuls:
            pb = ctf.add_paragraph()
            pb.text = b
            pb.font.size = Pt(10)
            pb.font.color.rgb = COLOR_SLATE_LIGHT
            pb.space_before = Pt(10)
    add_footer(s3, "Dossier Inversionista")

    # Slide 4: Módulos de Servicios en Operación
    s4 = prs.slides.add_slide(layout)
    add_bg(prs, s4)
    add_header(s4, "Activos Construidos", "5 Módulos de Servicios Certificados y Listos",
               "La inversión no financia prototipos de papel; la plataforma cuenta con 540+ tests 100% PASS.")
    mods = [
        ("M1: Core OCS & Saldo", "Consulta en tiempo real de saldos y megas sin fricción. Elimina 3.1M de llamadas/año.", COLOR_SKY),
        ("M2: FinTech C2P", "Pasarela interbancaria SUDEBAN. Recargas en 12 segundos con débito automático en cuenta.", COLOR_EMERALD),
        ("M3: Cazador de Ofertas", "Radar retail geolocalizado (56 marcas, 204 ofertas). Split comercial 20/80 por cupón.", COLOR_AMBER),
        ("M4: Visión OCR Bancaria", "Inferencia Gemini 2.5 Flash para comprobantes de pago. Cero mano de obra de conciliación.", COLOR_PURPLE),
        ("M5: Retención & EIR", "Aseguramiento de terminales y algoritmos de retención ML. Salvamento del 14.5% de clientes.", COLOR_ROSE)
    ]
    for i, (mtit, mdsc, mcol) in enumerate(mods):
        col = i % 3
        row = i // 3
        x = Inches(0.8 + col * 3.95)
        y = Inches(1.8 + row * 2.5)
        w = Inches(3.75) if i < 3 else Inches(5.75)
        h = Inches(2.2)
        card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = RGBColor(30, 58, 100)
        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_top = Inches(0.18)
        ctf.margin_left = Inches(0.22)
        cp0 = ctf.paragraphs[0]
        cp0.text = mtit
        cp0.font.size = Pt(12)
        cp0.font.bold = True
        cp0.font.color.rgb = mcol

        cp1 = ctf.add_paragraph()
        cp1.text = mdsc
        cp1.font.size = Pt(9.5)
        cp1.font.color.rgb = COLOR_SLATE_LIGHT
        cp1.space_before = Pt(6)
    add_footer(s4, "Dossier Inversionista")

    # Slide 5: Dinámica de Costos y Economías de Escala
    s5 = prs.slides.add_slide(layout)
    add_bg(prs, s5)
    add_header(s5, "Economía de Escala", "La Ley del Costo Marginal Decreciente: CAC = $0",
               "La combinación de Sistema 1 en RAM y Sistema 2 Gemini Flash diluye el costo por usuario a $0.003 USD.")
    c_arch = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.9))
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
    ap1.text = "• 85% de las Solicitudes (Sistema 1 FastPath en RAM):"
    ap1.font.size = Pt(10.5)
    ap1.font.bold = True
    ap1.font.color.rgb = COLOR_EMERALD
    ap1.space_before = Pt(10)

    ap1_d = atf.add_paragraph()
    ap1_d.text = "Consultas de saldo y paquetes resueltos en memoria RAM en <1 ms a CERO costo de tokens ($0.0000 USD)."
    ap1_d.font.size = Pt(9.5)
    ap1_d.font.color.rgb = COLOR_SLATE_LIGHT
    ap1_d.space_before = Pt(3)

    ap2 = atf.add_paragraph()
    ap2.text = "• 15% Complejo (Sistema 2 Gemini Vision Multimodal):"
    ap2.font.size = Pt(10.5)
    ap2.font.bold = True
    ap2.font.color.rgb = COLOR_PURPLE
    ap2.space_before = Pt(12)

    ap2_d = atf.add_paragraph()
    ap2_d.text = "Solo se activa para auditar comprobantes de pago bancarios y notas de voz con costo de $0.0008 USD."
    ap2_d.font.size = Pt(9.5)
    ap2_d.font.color.rgb = COLOR_SLATE_LIGHT
    ap2_d.space_before = Pt(3)

    c_scale = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.9))
    c_scale.fill.solid()
    c_scale.fill.fore_color.rgb = COLOR_CARD_DARK
    c_scale.line.color.rgb = RGBColor(30, 58, 100)
    stf = c_scale.text_frame
    stf.word_wrap = True
    stf.margin_top = Inches(0.25)
    stf.margin_left = Inches(0.25)
    sp0 = stf.paragraphs[0]
    sp0.text = "📉 COSTO POR USUARIO AL ESCALAR (CAC = $0)"
    sp0.font.size = Pt(11.5)
    sp0.font.bold = True
    sp0.font.color.rgb = COLOR_AMBER

    scenarios = [
        ("Base Inicial (100k usuarios)", "$0.048 USD / mes"),
        ("Base Media (1.5M usuarios)", "$0.009 USD / mes"),
        ("Base Total (4.2M usuarios)", "$0.003 USD / mes")
    ]
    for sc_name, sc_val in scenarios:
        p_sc = stf.add_paragraph()
        p_sc.text = f"{sc_name}: {sc_val}"
        p_sc.font.size = Pt(10.5)
        p_sc.font.bold = True
        p_sc.font.color.rgb = COLOR_WHITE
        p_sc.space_before = Pt(12)

    sp_note = stf.add_paragraph()
    sp_note.text = "Ventaja Insuperable: Con Movilnet absorbiendo el marketing y aportando 4.2M de usuarios, el capital privado obtiene un margen EBITDA >85%."
    sp_note.font.size = Pt(9.5)
    sp_note.font.italic = True
    sp_note.font.color.rgb = COLOR_SLATE_MUTED
    sp_note.space_before = Pt(16)
    add_footer(s5, "Dossier Inversionista")

    # Slide 6: Productividad Marginal de la IA
    s6 = prs.slides.add_slide(layout)
    add_bg(prs, s6)
    add_header(s6, "Productividad del Capital", "Por Qué la IA es la Palanca Financiera (No un Lujo)",
               "La IA sustituye cuellos de botella humanos y acelera la tasa de conversión comercial.")
    ai_pillars = [
        ("1. Conciliación Instantánea OCR", "480 Milisegundos", COLOR_SKY,
         "Sustituye a 45 auditores humanos. Procesa comprobantes de Pago Móvil, detecta fraudes y acredita saldo de inmediato."),
        ("2. Cross-Selling Predictivo (NBA)", "Conversión del 8.7%", COLOR_EMERALD,
         "Ofrece bolsas de Extra Datos cuando restan <200 MB, multiplicando por 7.9x la efectividad respecto al SMS ciego."),
        ("3. Cero Carritos Abandonados", "Checkout en 12 Segundos", COLOR_AMBER,
         "Flujo de cobro C2P cerrado dentro de WhatsApp sin redirecciones a portales bancarios externos."),
        ("4. Conquista de Competencia", "120k Nuevas Líneas / Año", COLOR_PURPLE,
         "Bono Freemium a números 0414/0424 y 0412 con migración digital inmediata a eSIM sin ir a taquilla.")
    ]
    for i, (atit, aval, acol, adsc) in enumerate(ai_pillars):
        x = Inches(0.8 + i * 2.95)
        card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(2.8), Inches(4.9))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = RGBColor(30, 58, 100)
        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_top = Inches(0.2)
        ctf.margin_left = Inches(0.2)
        cp0 = ctf.paragraphs[0]
        cp0.text = atit
        cp0.font.size = Pt(11)
        cp0.font.bold = True
        cp0.font.color.rgb = COLOR_WHITE
        cp1 = ctf.add_paragraph()
        cp1.text = aval
        cp1.font.size = Pt(14)
        cp1.font.bold = True
        cp1.font.color.rgb = acol
        cp1.space_before = Pt(6)
        cp2 = ctf.add_paragraph()
        cp2.text = adsc
        cp2.font.size = Pt(9.5)
        cp2.font.color.rgb = COLOR_SLATE_LIGHT
        cp2.space_before = Pt(14)
    add_footer(s6, "Dossier Inversionista")

    # Slide 7: Estado de Resultados Proyectado (P&L)
    s7 = prs.slides.add_slide(layout)
    add_bg(prs, s7)
    add_header(s7, "Plan Financiero", "Estado de Resultados Consolidado (36 Meses en Miles USD)",
               "Proyección conservadora impulsada por la masa crítica de 4.2M usuarios y Tours Movilnet.")
    table_shape = s7.shapes.add_table(7, 4, Inches(0.8), Inches(1.8), Inches(11.7), Inches(4.8))
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
            cell.fill.fore_color.rgb = RGBColor(6, 78, 59) if r == 5 else (RGBColor(30, 50, 90) if r == 4 else COLOR_CARD_DARK)
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(10)
            p.font.bold = (r in [4, 5])
            p.font.color.rgb = COLOR_EMERALD if (r in [4, 5] and c > 0) else COLOR_WHITE
    add_footer(s7, "Dossier Inversionista")

    # Slide 8: Estructura del Capital ($450k) en 3 Tramos
    s8 = prs.slides.add_slide(layout)
    add_bg(prs, s8)
    add_header(s8, "Asignación de Capital", "Presupuesto Privado ($450.000 USD) en 3 Tramos Auditables",
               "100% destinado a activos tecnológicos e IA. Desembolsos condicionados a cumplimiento de hitos.")
    tramos = [
        ("TRAMO 1: Inmediato (50%)", "$225.000 USD", COLOR_RED_MOVILNET,
         ["• Clúster elástico cloud y edge CDN.",
          "• Aseguramiento de WhatsApp Enterprise Master.",
          "• Despliegue de recargas C2P en 12 segundos.",
          "• Validación de 540 tests de arquitectura."]),
        ("TRAMO 2: Mes 2 (30%)", "$135.000 USD", COLOR_AMBER,
         ["• Homologación bancaria C2P con 18 bancos.",
          "• Onboarding de 150 comercios aliados en Cazador.",
          "• Inferencia OCR Gemini Flash para comprobantes.",
          "• Cuponería dinámica TOTP de 60 segundos."]),
        ("TRAMO 3: Mes 4 (20%)", "$90.000 USD", COLOR_EMERALD,
         ["• Lanzamiento Portabilidad Express eSIM.",
          "• Soporte tecnológico a los Tours Movilnet.",
          "• Carrier Billing para deportes y streaming.",
          "• Fondo de reserva operativa y contingencia."])
    ]
    for i, (ttit, tval, tcol, tbuls) in enumerate(tramos):
        x = Inches(0.8 + i * 3.95)
        card = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(3.75), Inches(4.9))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = RGBColor(30, 58, 100)
        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_top = Inches(0.25)
        ctf.margin_left = Inches(0.25)
        cp0 = ctf.paragraphs[0]
        cp0.text = ttit
        cp0.font.size = Pt(11)
        cp0.font.bold = True
        cp0.font.color.rgb = tcol
        cp1 = ctf.add_paragraph()
        cp1.text = tval
        cp1.font.size = Pt(20)
        cp1.font.bold = True
        cp1.font.color.rgb = COLOR_WHITE
        cp1.space_before = Pt(4)
        for b in tbuls:
            pb = ctf.add_paragraph()
            pb.text = b
            pb.font.size = Pt(9.5)
            pb.font.color.rgb = COLOR_SLATE_LIGHT
            pb.space_before = Pt(9)
    add_footer(s8, "Dossier Inversionista")

    # Slide 9: Mecanismo de Retorno Waterfall 75/25
    s9 = prs.slides.add_slide(layout)
    add_bg(prs, s9)
    add_header(s9, "Retorno del Inversionista", "Mecanismo Waterfall de Reparto: Payback en 6.2 Meses",
               "Garantía de amortización acelerada del capital con rendimiento preferente y sociedad a largo plazo.")
    w_boxes = [
        ("FASE 1: AMORTIZACIÓN ACELERADA", "Meses 1 a 6.2 (Recuperación)", COLOR_EMERALD,
         ["• El Inversionista retiene el 75% del flujo de nuevos ingresos.",
          "• Movilnet recibe el 25% restante y ahorra 100% de su call center.",
          "• El capital de $450k + 20% preferente se liquida en el Mes 6.2.",
          "• Riesgo de impago nulo gracias a la liquidación interbancaria C2P."]),
        ("FASE 2: UTILIDAD RECURRENTE COMPARTIDA", "Meses 7 en Adelante (Consolidación)", COLOR_SKY,
         ["• Split Equitativo: 50% Inversionista / 50% Movilnet.",
          "• Flujo neto acumulado para el Inversionista: $4.25M USD a 36 meses.",
          "• Retorno sobre el capital invertido (ROI): 9.44x.",
          "• Flujo pasivo perpetuo sobre una base consolidada de 4.2M de usuarios."])
    ]
    for i, (wtit, wsub, wcol, wbuls) in enumerate(w_boxes):
        x = Inches(0.8 + i * 5.95)
        card = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(5.75), Inches(4.9))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = wcol
        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_top = Inches(0.25)
        ctf.margin_left = Inches(0.3)
        cp0 = ctf.paragraphs[0]
        cp0.text = wtit
        cp0.font.size = Pt(12)
        cp0.font.bold = True
        cp0.font.color.rgb = wcol
        cp1 = ctf.add_paragraph()
        cp1.text = wsub
        cp1.font.size = Pt(15)
        cp1.font.bold = True
        cp1.font.color.rgb = COLOR_WHITE
        cp1.space_before = Pt(4)
        for b in wbuls:
            pb = ctf.add_paragraph()
            pb.text = b
            pb.font.size = Pt(10)
            pb.font.color.rgb = COLOR_SLATE_LIGHT
            pb.space_before = Pt(10)
    add_footer(s9, "Dossier Inversionista")

    # Slide 10: Dictamen y Próximos Pasos
    s10 = prs.slides.add_slide(layout)
    add_bg(prs, s10)
    add_header(s10, "Decisión Final", "Dictamen Financiero Recomendado: Aprobación Tramo 1",
               "Asimetría de riesgo positiva: demanda cautiva inmediata, CAC = $0 y 100% de la tecnología lista.")
    box_dec = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(11.7), Inches(4.9))
    box_dec.fill.solid()
    box_dec.fill.fore_color.rgb = COLOR_CARD_DARK
    box_dec.line.color.rgb = RGBColor(6, 78, 59)
    dtf = box_dec.text_frame
    dtf.word_wrap = True
    dtf.margin_top = Inches(0.35)
    dtf.margin_left = Inches(0.4)
    dp0 = dtf.paragraphs[0]
    dp0.text = "🎯 CONCLUSIÓN Y DICTAMEN DEL EVALUADOR ECONÓMICO"
    dp0.font.size = Pt(15)
    dp0.font.bold = True
    dp0.font.color.rgb = COLOR_EMERALD

    d_points = [
        ("Riesgo Comercial Cero:", "Movilnet no requiere fondos líquidos y garantiza los 4.2M de usuarios y la presencia física nacional."),
        ("Productividad del Capital:", "Con $450k se captura un flujo EBITDA de $2.3M en el Año 1 y más de $9.8M en el Año 3."),
        ("Margen Operativo Bruto >85%:", "Arquitectura de software con costo marginal que tiende asintóticamente a cero ($0.00018/transacción)."),
        ("Dictamen Recomendado:", "APROBACIÓN INMEDIATA DEL TRAMO 1 ($225.000 USD) para iniciar la captura de valor.")
    ]
    for tit, dsc in d_points:
        p_pt = dtf.add_paragraph()
        p_pt.text = f"• {tit} " + dsc
        p_pt.font.size = Pt(12)
        p_pt.font.color.rgb = COLOR_WHITE
        p_pt.space_before = Pt(12)
    add_footer(s10, "Dossier Inversionista")

    prs.save(out_path)
    print(f"✅ Presentación Inversionista (.pptx) guardada en: {out_path}")

# =============================================================================
# 2. DECK DEPARTAMENTO DE MERCADEO
# =============================================================================
def build_mercadeo_deck(out_path):
    prs = setup_prs()
    layout = prs.slide_layouts[6]

    # Slide 1: Portada Mercadeo
    s1 = prs.slides.add_slide(layout)
    add_bg(prs, s1)
    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.2), Inches(0.12), Inches(3.2))
    bar.fill.solid()
    bar.fill.fore_color.rgb = COLOR_ROSE
    bar.line.fill.background()

    tb = s1.shapes.add_textbox(Inches(1.2), Inches(1.1), Inches(11.0), Inches(3.4))
    tf = tb.text_frame
    tf.word_wrap = True
    p0 = tf.paragraphs[0]
    p0.text = "VICEPRESIDENCIA DE MERCADEO, MARCA, PRODUCTO & GROWTH"
    p0.font.size = Pt(11.5)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_ROSE

    p1 = tf.add_paragraph()
    p1.text = "MOVI 4GMAX: El Protagonista Principal"
    p1.font.size = Pt(33)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_WHITE
    p1.space_before = Pt(8)

    p2 = tf.add_paragraph()
    p2.text = "Estrategia de Activación POP, Tours Movilnet, Ecosistema Digital y Monetización Comercial en Tiempo Real"
    p2.font.size = Pt(15)
    p2.font.color.rgb = COLOR_SLATE_LIGHT
    p2.space_before = Pt(8)

    kpis_m = [
        ("Tasa de Apertura", "98.2%", COLOR_ROSE, "WhatsApp vs 12.4% en SMS tradicional"),
        ("Tasa de Conversión", "8.7%", COLOR_AMBER, "Ofertas contextuales Next-Best-Action"),
        ("Checkout C2P", "12 Segundos", COLOR_EMERALD, "Recarga sin salir de la conversación"),
        ("Presencia en Calle", "Tours Movilnet", COLOR_SKY, "Tarimas, POP, ferias y redes masivas")
    ]
    for i, (title, val, color, desc) in enumerate(kpis_m):
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
        cp1.font.size = Pt(22)
        cp1.font.bold = True
        cp1.font.color.rgb = color
        cp1.space_before = Pt(4)

        cp2 = ctf.add_paragraph()
        cp2.text = desc
        cp2.font.size = Pt(9)
        cp2.font.color.rgb = COLOR_SLATE_LIGHT
        cp2.space_before = Pt(4)
    add_footer(s1, "Dossier Mercadeo")

    # Slide 2: El Rol de Mercadeo (Cero Fondos Líquidos)
    s2 = prs.slides.add_slide(layout)
    add_bg(prs, s2)
    add_header(s2, "Estrategia de Marca", "El Rol Soberano de Mercadeo: Aporte en Canales y Difusión",
               "Movilnet no desembolsa fondos en efectivo: el capital tecnológico ($450k) lo aporta el inversionista.")
    c_m2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(11.7), Inches(4.9))
    c_m2.fill.solid()
    c_m2.fill.fore_color.rgb = COLOR_CARD_DARK
    c_m2.line.color.rgb = RGBColor(244, 63, 94)
    m2tf = c_m2.text_frame
    m2tf.word_wrap = True
    m2tf.margin_top = Inches(0.25)
    m2tf.margin_left = Inches(0.35)
    m2p0 = m2tf.paragraphs[0]
    m2p0.text = "🎯 EL PODER DEL APORTE DE MERCADEO DE MOVILNET"
    m2p0.font.size = Pt(13)
    m2p0.font.bold = True
    m2p0.font.color.rgb = COLOR_ROSE

    m2_bullets = [
        ("Base Cautiva de 4.2M de Usuarios:", "Acceso exclusivo y directo para campañas conversacionales sin pagar pauta publicitaria en Google o Meta."),
        ("Despliegue Nacional de Material POP:", "Producción y colocación de banderines oficiales, pendones, habladores en taquillas y tótems interactivos."),
        ("Presencia en Tours Movilnet:", "Caravanas y tarimas en regiones, plazas y municipios cubiertas por el presupuesto habitual de Mercadeo."),
        ("Ecosistema Digital Oficial:", "Banner principal en www.movilnet.com.ve, difusión viral en Instagram, TikTok, X y SMS push."),
        ("Protagonismo Absoluto:", "MOVI es la cara visible de la operadora, humanizando y modernizando la marca nacional.")
    ]
    for tit, dsc in m2_bullets:
        pb = m2tf.add_paragraph()
        pb.text = f"• {tit} " + dsc
        pb.font.size = Pt(10.5)
        pb.font.color.rgb = COLOR_SLATE_LIGHT
        pb.space_before = Pt(10)
    add_footer(s2, "Dossier Mercadeo")

    # Slide 3: Material POP y Puntos de Venta
    s3 = prs.slides.add_slide(layout)
    add_bg(prs, s3)
    add_header(s3, "Puntos de Venta", "Despliegue de Material POP en Agentes y Tiendas",
               "Transformar las oficinas físicas en canales de autogestión digital en 12 segundos.")
    pop_items = [
        ("1. Banderines Corporativos", "Fachada de Tiendas", COLOR_RED_MOVILNET,
         "Identificación oficial en la red de agentes comerciales y oficinas Movilnet anunciando a MOVI."),
        ("2. Pendones de Alto Impacto", "Zonas de Entrada", COLOR_ROSE,
         "'Recarga en 12 segundos por WhatsApp con MOVI — Sin filas ni esperas'."),
        ("3. Habladores en Taquillas", "Puntos de Cobro", COLOR_AMBER,
         "Código QR dinámico que permite al usuario que espera en fila recargar o consultar saldo en su propio teléfono."),
        ("4. Tótems Interactivos", "Centros Comerciales", COLOR_SKY,
         "Tabletas de demostración en centros de alto tráfico peatonal para probar la PWA 4GMAX sin consumo de datos.")
    ]
    for i, (ptit, psub, pcol, pdsc) in enumerate(pop_items):
        x = Inches(0.8 + i * 2.95)
        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(2.8), Inches(4.9))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = RGBColor(30, 58, 100)
        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_top = Inches(0.2)
        ctf.margin_left = Inches(0.2)
        cp0 = ctf.paragraphs[0]
        cp0.text = ptit
        cp0.font.size = Pt(11)
        cp0.font.bold = True
        cp0.font.color.rgb = pcol
        cp1 = ctf.add_paragraph()
        cp1.text = psub
        cp1.font.size = Pt(13)
        cp1.font.bold = True
        cp1.font.color.rgb = COLOR_WHITE
        cp1.space_before = Pt(4)
        cp2 = ctf.add_paragraph()
        cp2.text = pdsc
        cp2.font.size = Pt(9.5)
        cp2.font.color.rgb = COLOR_SLATE_LIGHT
        cp2.space_before = Pt(14)
    add_footer(s3, "Dossier Mercadeo")

    # Slide 4: Tours Movilnet Nacionales
    s4 = prs.slides.add_slide(layout)
    add_bg(prs, s4)
    add_header(s4, "Activación en Calle", "Tours Movilnet: Caravanas en Plazas, Regiones y Ferias",
               "Presencia física directa con tarima interactiva y trivias de IA cubiertas 100% por Movilnet.")
    tour_cols = [
        ("Caravanas Regionales", "Demostraciones en Vivo", COLOR_AMBER,
         ["• Activación en tarimas públicas en plazas Bolívar y centros comunitarios.",
          "• Los promotores retan a los asistentes a recargar saldo en vivo en <15s.",
          "• Conexión por WhatsApp (+58 424 153 3712) y portal PWA 4GMAX.",
          "• Cobertura logística y viáticos cubiertos por Mercadeo Movilnet."]),
        ("Trivias & Gamificación", "Premios y Participación", COLOR_EMERALD,
         ["• Trivias conducidas por MOVI vía WhatsApp sobre cultura, deportes y tecnología.",
          "• Asignación automática de bolsas de Extra Datos y cupones retail.",
          "• Captura de teléfonos y geolocalización consentida del usuario.",
          "• Dinamización de la comunidad juvenil y estudiantil."]),
        ("Ferias y Congresos", "Presencia Institucional", COLOR_SKY,
         ["• Participación en FITVEN, ferias tecnológicas y congresos de telecomunicaciones.",
          "• Stands interactivos con Inteligencia Artificial soberana.",
          "• Demostración de soberanía tecnológica y modernización pública.",
          "• Ruedas de negocios con grandes retailers para Cazador de Ofertas."])
    ]
    for i, (ttit, tsub, tcol, tbuls) in enumerate(tour_cols):
        x = Inches(0.8 + i * 3.95)
        card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(3.75), Inches(4.9))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = RGBColor(30, 58, 100)
        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_top = Inches(0.2)
        ctf.margin_left = Inches(0.25)
        cp0 = ctf.paragraphs[0]
        cp0.text = ttit
        cp0.font.size = Pt(12)
        cp0.font.bold = True
        cp0.font.color.rgb = tcol
        cp1 = ctf.add_paragraph()
        cp1.text = tsub
        cp1.font.size = Pt(14)
        cp1.font.bold = True
        cp1.font.color.rgb = COLOR_WHITE
        cp1.space_before = Pt(4)
        for b in tbuls:
            pb = ctf.add_paragraph()
            pb.text = b
            pb.font.size = Pt(9.5)
            pb.font.color.rgb = COLOR_SLATE_LIGHT
            pb.space_before = Pt(9)
    add_footer(s4, "Dossier Mercadeo")

    # Slide 5: Ecosistema Digital y Redes
    s5 = prs.slides.add_slide(layout)
    add_bg(prs, s5)
    add_header(s5, "Ecosistema Digital", "Canales Digitales Oficiales y Campañas Virales",
               "Integración en el portal web oficial, redes sociales masivas y difusión push por SMS.")
    d_channels = [
        ("Web movilnet.com.ve", "Hero Banner Principal", COLOR_RED_MOVILNET,
         "Banner interactivo en la portada oficial con llamada a la acción directa a WhatsApp y PWA."),
        ("Redes Sociales", "Instagram, TikTok, X", COLOR_ROSE,
         "Reels cortos mostrando recargas en 12s, comprobantes OCR escaneados y cupones retail."),
        ("Campañas Push SMS", "Difusión a los 4.2M", COLOR_SKY,
         "Mensajes institucionales con enlaces directos al chat oficial sin consumo de saldo."),
        ("Bono Freemium", "Captación Competencia", COLOR_PURPLE,
         "1.000 tokens de IA gratis para líneas 0414/0424 y 0412 para migrar a eSIM Movilnet.")
    ]
    for i, (dtit, dsub, dcol, ddsc) in enumerate(d_channels):
        x = Inches(0.8 + i * 2.95)
        card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(2.8), Inches(4.9))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = RGBColor(30, 58, 100)
        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_top = Inches(0.2)
        ctf.margin_left = Inches(0.2)
        cp0 = ctf.paragraphs[0]
        cp0.text = dtit
        cp0.font.size = Pt(11)
        cp0.font.bold = True
        cp0.font.color.rgb = dcol
        cp1 = ctf.add_paragraph()
        cp1.text = dsub
        cp1.font.size = Pt(13)
        cp1.font.bold = True
        cp1.font.color.rgb = COLOR_WHITE
        cp1.space_before = Pt(4)
        cp2 = ctf.add_paragraph()
        cp2.text = ddsc
        cp2.font.size = Pt(9.5)
        cp2.font.color.rgb = COLOR_SLATE_LIGHT
        cp2.space_before = Pt(14)
    add_footer(s5, "Dossier Mercadeo")

    # Slide 6: Las 5 Fuentes de Ingresos
    s6 = prs.slides.add_slide(layout)
    add_bg(prs, s6)
    add_header(s6, "Monetización Comercial", "Las 5 Fuentes Directas de Ingresos Atribuibles a Mercadeo",
               "Dónde y cómo se generan ingresos reales en caja a través de las campañas.")
    streams = [
        ("1. Extra Datos (Upselling)", "$840k / Año 1", COLOR_ROSE,
         "Detección predictiva cuando restan <200 MB. Oferta automática con tasa de conversión del 8.7%."),
        ("2. Frecuencia C2P", "+$1.35 ARPU", COLOR_SKY,
         "Recarga sin fricción bancaria en 12 seg. El abonado pasa de 2.1 a 3.8 recargas al mes."),
        ("3. Retail Media Cazador", "$420k / Año 1", COLOR_AMBER,
         "56 cadenas aliadas. Split publicitario 20/80 ($0.40 USD netos por cupón canjeado)."),
        ("4. Conquista de Competencia", "120.000 Líneas", COLOR_PURPLE,
         "Captación de Movistar/Digitel vía bono Freemium y Portabilidad Express eSIM en 3 minutos."),
        ("5. Carrier Billing & LVBP", "15% - 25% Fee", COLOR_EMERALD,
         "Paquetes temáticos y cobro a saldo de streaming, deportes y juegos móviles.")
    ]
    for i, (stitle, sval, scolor, sdesc) in enumerate(streams):
        col = i % 3
        row = i // 3
        x = Inches(0.8 + col * 3.95)
        y = Inches(1.8 + row * 2.5)
        w = Inches(3.75) if i < 3 else Inches(5.75)
        h = Inches(2.2)
        card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
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
    add_footer(s6, "Dossier Mercadeo")

    # Slide 7: Funnel Conversacional en 12s
    s7 = prs.slides.add_slide(layout)
    add_bg(prs, s7)
    add_header(s7, "Funnel de Conversión", "El Embudo Conversacional en 12 Segundos",
               "Cómo la IA acompaña al usuario en su propio chat sin carritos abandonados.")
    steps = [
        ("PASO 1: TOFU (0s)", "Consulta Pasiva", COLOR_SLATE_MUTED,
         "Usuario: 'Hola, ¿cuántos megas me quedan?'", "El usuario busca información rutinaria sin intención de compra inicial."),
        ("PASO 2: MOFU (3s)", "Diagnóstico con Urgencia", COLOR_SKY,
         "MOVI: 'Te quedan 180 MB y vence en 14 días. Los vas a agotar hoy.'", "El sistema crea conciencia de la necesidad antes de que quede desconectado."),
        ("PASO 3: BOFU (6s)", "Oferta Irresistible (CTA)", COLOR_AMBER,
         "MOVI: '¿Deseas activar Extra Datos 2GB por solo Bs. 45 con 1 clic?'", "Solución con precio exacto y botón directo de compra."),
        ("PASO 4: CIERRE (12s)", "Pago Inmediato C2P", COLOR_EMERALD,
         "Sistema: '¡Acreditación Exitosa! Ref: 894125 • +2 GB disponibles.'", "Dinero en cuenta bancaria y datos activos al instante.")
    ]
    for i, (title, sub, color, dialog, expl) in enumerate(steps):
        x = Inches(0.8 + i * 2.95)
        card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(2.8), Inches(4.9))
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
    add_footer(s7, "Dossier Mercadeo")

    # Slide 8: Cazador de Ofertas & Retail Media
    s8 = prs.slides.add_slide(layout)
    add_bg(prs, s8)
    add_header(s8, "Alianzas Comerciales", "Cazador de Ofertas: Retail Media con Split 20/80",
               "Monetización de tráfico físico en comercios aliados con tecnología antifraude TOTP de 60s.")
    kpi_retail = [
        ("56 Marcas Aliadas", "Cadenas Comerciales", COLOR_RED_MOVILNET, "Arturo's, Farmahorro, Cines Unidos, Traki, Automercados Plaza's."),
        ("204 Ofertas en Radar", "Descuentos Hiper-Geolocalizados", COLOR_AMBER, "Promociones con radio de cobertura dinámico de 500m a 50 km."),
        ("Split Comercial 20 / 80", "Ingreso Neto para Movilnet", COLOR_EMERALD, "Movilnet retiene $0.40 USD netos por cada cupón canjeado en tienda.")
    ]
    for i, (v, t, c, d) in enumerate(kpi_retail):
        x = Inches(0.8 + i * 3.95)
        card = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(3.75), Inches(2.2))
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

    box_sec = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.3), Inches(11.7), Inches(2.4))
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
    add_footer(s8, "Dossier Mercadeo")

    # Slide 9: Conquista de Competencia
    s9 = prs.slides.add_slide(layout)
    add_bg(prs, s9)
    add_header(s9, "Growth & Captación", "Cómo Capturamos Abonados de Digitel y Movistar",
               "Estrategia de conversión perimetral para migrar usuarios hacia Movilnet sin costo de adquisición.")
    conq_steps = [
        ("1. Detección Perimetral", "0414 / 0424 / 0412", COLOR_PURPLE,
         "El sistema identifica automáticamente cuando un usuario de la competencia chatea o entra a la PWA."),
        ("2. Gancho Freemium", "1.000 Tokens de Bienvenida", COLOR_AMBER,
         "Se le obsequia interacción gratis para probar la velocidad y resolver dudas, demostrando la superioridad del servicio."),
        ("3. Portabilidad Express eSIM", "Migración en 3 Minutos", COLOR_SKY,
         "Conserva su mismo número y se pasa a la red 4GMAX de Movilnet con una eSIM digital instantánea sin ir a tienda."),
        ("4. LTV del Abonado Captado", "$42 USD / Año por Línea", COLOR_EMERALD,
         "120.000 líneas captadas representan +$5.04M USD anuales con costo de adquisición (CAC) casi cero.")
    ]
    for i, (title, highlight, color, desc) in enumerate(conq_steps):
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
    add_footer(s9, "Dossier Mercadeo")

    # Slide 10: Cronograma Time-to-Money
    s10 = prs.slides.add_slide(layout)
    add_bg(prs, s10)
    add_header(s10, "Time-to-Money", "¿En Qué Tiempo se Ven los Ingresos de Mercadeo?",
               "Roadmap de ejecución comercial en 3 horizontes con facturación auditable desde el Mes 1.")
    phases_m = [
        ("FASE 1: QUICK WINS", "Meses 1 a 3", "$80k - $120k / mes", COLOR_ROSE,
         ["• Activación en WhatsApp y PWA de la base actual.",
          "• Recargas Pago Móvil C2P en 12 segundos.",
          "• Venta automática de Extra Datos al consultar saldo.",
          "• Despliegue de material POP en las primeras 50 oficinas."]),
        ("FASE 2: ESCALAMIENTO TERRITORIAL", "Meses 4 a 6", "$250k - $380k / mes", COLOR_AMBER,
         ["• Arranque de los Tours Movilnet nacionales y regionales.",
          "• Onboarding de 150 comercios en Cazador de Ofertas.",
          "• Campañas geolocalizadas con 56 cadenas comerciales.",
          "• Validación visual de comprobantes por OCR."]),
        ("FASE 3: CONQUISTA TOTAL", "Meses 7 a 12", "$500k - $800k / mes", COLOR_EMERALD,
         ["• Portabilidad Express eSIM para Digitel y Movistar.",
          "• Carrier Billing para deportes (LVBP) y streaming.",
          "• Consolidación de MOVI como el canal líder del país.",
          "• Régimen comercial permanente de alto margen."])
    ]
    for i, (pname, ptime, pmeta, pcolor, pitems) in enumerate(phases_m):
        x = Inches(0.8 + i * 3.95)
        card = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(3.75), Inches(4.9))
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
    add_footer(s10, "Dossier Mercadeo")

    prs.save(out_path)
    print(f"✅ Presentación Mercadeo (.pptx) guardada en: {out_path}")

def main():
    docs_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
    os.makedirs(docs_dir, exist_ok=True)

    # 1. Deck Inversionista
    p_inv = os.path.join(docs_dir, "PRESENTACION_EJECUTIVA_INVERSIONISTA_ECONOMISTA.pptx")
    build_inversionista_deck(p_inv)

    # 2. Deck Mercadeo
    p_mkt = os.path.join(docs_dir, "PRESENTACION_EJECUTIVA_DEPARTAMENTO_MERCADEO.pptx")
    build_mercadeo_deck(p_mkt)

    print("🎉 Todas las presentaciones PowerPoint han sido compiladas exitosamente.")

if __name__ == "__main__":
    main()
