# Continuous Fetal Oxygenation Monitoring & Multi-Organ Prospective Study Design

## A Technology Landscape Review and Clinical Research Architecture

**Date:** 2026-03-03  
**Status:** COMPREHENSIVE REPORT — two integrated sections  
**Purpose:** (1) Assess whether technology exists to continuously monitor fetal oxygenation during pregnancy, and (2) design the prospective study that would test the alignment model's central prediction  
**Relationship to alignment model:** This document bridges *RESEARCH__gestational-impact-zones-oxygen-demand-alignment.md* (the theory) with the engineering and clinical infrastructure required to test it

---

# SECTION 1: CONTINUOUS FETAL OXYGENATION MONITORING — TECHNOLOGY LANDSCAPE

## The Core Question

The alignment model posits that if fetal oxygenation could be continuously measured during pregnancy, oxygen deprivation events could be overlaid on developmental vulnerability windows to predict which organ systems absorb injury. The question is: **how close is the technology to making this possible?**

**Short answer:** Not close. The gap between what exists and what the alignment model requires is substantial — but narrowing faster than most clinicians appreciate, driven by transabdominal NIRS, photoacoustic imaging, and MRI-based placental mapping. Current technology readiness is approximately TRL 3–4 (laboratory validation/animal models) for direct fetal SpO₂ measurement, with no device at TRL 7+ (clinical deployment) for continuous antepartum monitoring.

---

## 1A. Current Fetal Monitoring Technology

### 1A.1 Cardiotocography (CTG) / Electronic Fetal Monitoring (EFM)

**What it is:** The global standard for intrapartum fetal surveillance since the 1970s. Records fetal heart rate (FHR) patterns and uterine contractions via external transducers (Doppler ultrasound for FHR, tocodynamometer for contractions).

**What it actually detects:**
- Fetal heart rate baseline (normal 110–160 bpm)
- Variability (beat-to-beat fluctuations reflecting autonomic nervous system function)
- Accelerations (FHR increases — reassuring sign)
- Decelerations (FHR decreases — variable, early, late patterns)
- Uterine contraction frequency and relative timing

**What it misses:**
- **Does not measure oxygen.** CTG is an indirect proxy — it measures the fetal cardiac response to oxygen status, not oxygen itself
- **Catastrophic false positive rate.** CTG has a sensitivity of ~85–99% for detecting acidosis but a specificity of only 15–30% (Alfirevic et al., Cochrane 2017). For every genuinely hypoxic fetus identified, approximately 3–6 non-hypoxic fetuses are falsely flagged
- **Cannot detect chronic subacute hypoxia.** CTG is designed for acute intrapartum events. A fetus experiencing chronic placental insufficiency with SpO₂ at 45% (critically low) may show a perfectly normal CTG if the heart rate compensatory mechanisms are intact
- **Has not improved perinatal outcomes.** After 50+ years of universal adoption, CTG has not reduced cerebral palsy rates. It has increased cesarean delivery rates by 20–40% without corresponding outcome improvement (PMID: 17124017; PMID: 33824144)
- **Cannot timestamp discrete oxygen events.** Even when decelerations occur, they reflect cardiac autonomic responses, not SpO₂ values. A late deceleration tells you the fetus experienced a contraction-related oxygen dip; it does not tell you how low oxygen went or for how long

**Technology Readiness for alignment model use:** **TRL 9 (fully deployed) — but fundamentally wrong technology.** CTG monitors the fetal cardiac response, not the oxygen supply. It is like measuring engine RPM to infer fuel level.

**Cost:** ~$5,000–15,000 per unit; universally available in hospital settings.

**Citation:** Balayla & Shrem, 2020 — "Solving the obstetrical paradox" — reviews the fundamental limitation of using FHR as proxy for oxygenation (PMID: 32089884).

---

### 1A.2 Fetal Pulse Oximetry (Intrapartum)

**What it was:** A reflectance pulse oximeter sensor (Nellcor N-400 / OxiFirst, with FS-14 sensor) placed transcervically against the fetal cheek or temple during labour. Originally developed in the 1980s–1990s, FDA-cleared in May 2000.

**What it measured:**
- Fetal arterial oxygen saturation (SpO₂) via reflectance photoplethysmography
- Normal fetal SpO₂ range: 30–60% (much lower than postnatal)
- Critical threshold: SpO₂ <30% for ≥10 minutes associated with fetal acidosis

**Key Clinical Trials:**

1. **Garite et al., 2000** (PMID: 11084540) — Multicenter RCT, 9 centres, 1,010 patients with non-reassuring FHR. Found 50% reduction in cesarean for non-reassuring fetal status in the pulse oximetry group (4.5% vs 10.2%, P=.007). **However**, overall cesarean rate was unchanged (29% vs 26%, P=.49) due to a paradoxical increase in cesarean for dystocia. The sensor improved diagnostic accuracy for metabolic acidosis (higher sensitivity and specificity) but shifted the surgical indication rather than reducing surgery.

2. **Bloom et al., 2006** (PMID: 17124017) — NICHD MFMU Network RCT, 5,341 nulliparous women. **Definitive negative trial.** No significant difference in overall cesarean rate (26.3% vs 27.5%, P=.31), no difference in cesarean for non-reassuring FHR (7.1% vs 7.9%, P=.30), and no improvement in neonatal condition at birth. This trial killed clinical adoption.

3. **FOREMOST Trial (East et al., 2006)** (PMID: 16522387) — Australian multicenter RCT, 601 women. No significant reduction in operative delivery.

4. **Cochrane Review (East et al., 2014)** (PMID: 25287809) — Seven RCTs pooled. Concluded that fetal pulse oximetry does not reduce cesarean delivery rates or improve neonatal outcomes.

**What happened to it:** Following the Bloom 2006 trial, the FDA informed Nellcor that the device could no longer be marketed for the purpose of reducing cesarean rates (which was its primary clinical justification). Nellcor/Covidien voluntarily withdrew the OxiFirst sensor from the market. See Section 1C for detailed failure analysis.

**Technology Readiness for alignment model use:** **TRL 0 — wrong paradigm entirely.** The fetal pulse oximeter was designed for intrapartum use only (requires ruptured membranes, cervical access). It cannot be used antepartum. It measured SpO₂ during labour, not during the weeks/months of developmental vulnerability. Even if it had been clinically successful, it would provide zero data relevant to the alignment model.

---

### 1A.3 Near-Infrared Spectroscopy (NIRS) — Neonatal/Fetal

**What it is:** Light-based technology using wavelengths of 700–1000 nm that penetrate biological tissue. Measures regional tissue oxygen saturation (rStO₂ or cStO₂) based on the differential absorption of oxygenated vs deoxygenated haemoglobin.

**Current clinical applications:**

- **Neonatal cerebral oximetry:** TRL 9 — deployed in NICUs worldwide. The SafeBoosC-III trial (Hansen et al., 2023; PMID: 37075142) was a landmark RCT of 1,601 extremely preterm infants across 70+ NICUs in 17 countries. Cerebral NIRS monitoring *guided treatment* vs standard care. Result: No significant difference in death or severe brain injury (35.2% vs 33.5%, P=.47). Despite widespread use, cerebral oximetry has **not** been shown to improve clinical outcomes in neonates.

- **Fetal cerebral NIRS during labour:** TRL 4–5 — research tool only. Aldrich et al. (1994; PMID: 7936527) demonstrated that fetal cerebral oxygen saturation measured by NIRS shortly before delivery correlates with umbilical cord acid-base status. Aldrich et al. (1996; PMID: 8820001) showed correspondence between FHR decelerations during labour and NIRS-measured cerebral oxygenation changes. These studies used a fibre-optic probe placed on the exposed fetal head during labour — **not applicable antepartum**.

- **Transabdominal fetal NIRS:** TRL 2–3 — see Section 1B.

**Key systematic review:** Pritišanac et al. (2021; PMID: 34485197) — comprehensive review of fetal haemoglobin effects on NIRS measurements. Key finding: fetal haemoglobin (HbF) has a left-shifted oxygen dissociation curve, which affects NIRS calibration. Neonatal NIRS algorithms calibrated for adult haemoglobin may systematically underestimate tissue oxygenation in the fetus/neonate.

**Technology Readiness for alignment model use:** **TRL 2–3 for transabdominal application.** NIR light can penetrate maternal tissue to reach the fetus, but signal-to-noise ratios are terrible, and separating maternal from fetal signals is the core engineering challenge. See detailed analysis in Section 1B.

---

### 1A.4 Umbilical Artery Doppler Velocimetry

**What it is:** Pulsed-wave Doppler ultrasound of the umbilical artery, measuring flow velocity waveforms. Standard clinical tool for surveillance of high-risk pregnancies (FGR, PE, hypertension).

**What it measures:**
- Systolic/diastolic (S/D) ratio
- Pulsatility index (PI) and resistance index (RI)
- Presence of absent or reversed end-diastolic flow (AREDF)

**What it tells you about oxygenation:**
- **Indirect proxy for placental vascular resistance.** Elevated S/D ratio or PI reflects increased downstream (placental) resistance, which correlates with defective placentation
- **AREDF** is a critical finding — indicates ≥60–70% obliteration of the placental vascular bed. Associated with severe FGR and high perinatal mortality
- Combined with middle cerebral artery (MCA) Doppler → cerebroplacental ratio (CPR), which detects the "brain-sparing" redistribution

**What it does NOT tell you:**
- **Not a measurement of fetal oxygen.** Doppler measures blood flow velocity, not oxygen content. A fetus with normal Doppler can be hypoxic (if maternal blood has low oxygen). A fetus with abnormal Doppler may not yet be hypoxic (compensatory mechanisms)
- **Cannot be performed continuously.** Each assessment is a snapshot lasting 5–15 minutes
- **Cannot detect intermittent hypoxic episodes.** Doppler reveals chronic vascular remodelling, not episodic oxygen dips analogous to intermittent hypoxia events
- **Timing resolution is weeks, not seconds.** Doppler may show progressive worsening over days/weeks but cannot capture a 10-second oxygen dip

**Technology Readiness for alignment model use:** **TRL 9 for clinical deployment; TRL 0 for alignment model requirements.** Doppler is the best currently available indicator of placental insufficiency severity, but it provides no temporal resolution for mapping oxygen events against vulnerability windows.

**Cost:** Standard obstetric ultrasound equipment ($60,000–200,000); widely available.

---

### 1A.5 Cord Blood Gas Analysis

**What it is:** Measurement of pH, pO₂, pCO₂, base excess, and lactate from umbilical artery and vein blood samples obtained immediately after delivery.

**What it tells you:** The fetal oxygen/acid-base status at the exact moment of birth — a single-timepoint snapshot.

**Limitation for alignment model:** One data point at delivery. Tells you nothing about the oxygen trajectory during weeks 20–36.

---

## 1B. Emerging Technologies

### 1B.1 Transabdominal Fetal Pulse Oximetry (TFO)

**Lead research group:** Soheil Ghiasi Laboratory, UC Davis

**What it is:** A non-invasive device using near-infrared light sources and photodetectors placed on the maternal abdomen to measure fetal arterial oxygen saturation (fSpO₂) through maternal tissue, uterine wall, and amniotic fluid.

**Current state (TRL 4–5):**

- **Vintzileos et al. (2005; PMID: 15672014):** First feasibility study of transabdominal fetal pulse oximetry using continuous-wave NIRS. Demonstrated that fetal SpO₂ signals could be detected through the maternal abdomen, but signal quality was inconsistent.

- **Fong et al. (2020; PMID: 32542541):** Validated a novel transabdominal fetal oximeter in a hypoxic fetal lamb model. Demonstrated that the device could detect fetal SpO₂ changes during induced hypoxia through the abdominal wall. Key advance: confirmed the physics works in a controlled animal model.

- **Fong et al. (2021; PMID: 32746021):** In vivo evaluation of the transabdominal fetal pulse oximeter design. Demonstrated efficacy in pregnant ovine (sheep) models. NIR light at specific wavelengths successfully penetrated maternal tissue and returned signals from fetal vasculature.

- **Kasap et al. (2021; PMID: 34891473):** Multi-detector heart rate extraction method for TFO. Addressed the critical challenge of separating fetal from maternal heart signals — essential for calculating fetal SpO₂ (which requires isolating the fetal arterial pulsation from the much stronger maternal pulsation).

- **Kasap et al. (2024; PMID: 38728001):** Proof-of-concept demonstrating transcutaneous discrimination of fetal heart rate from maternal heart rate. Applied TFO in human patients for the first time. Successfully differentiated fetal and maternal heart signals. This is the closest any group has come to non-invasive fetal SpO₂ in human subjects.

- **Kasap et al. (2025; PMID: 41124068) — FOSTER pipeline:** Comprehensive computational pipeline for TFO validated in a large animal model. Represents the most advanced signal processing framework for extracting fetal oxygenation data from transabdominal measurements.

- **Qian et al. (2025; PMID: 40290857):** Non-invasive detection of instantaneous fetal hypoxemia in a large animal model. Demonstrated that diffuse optics can detect brief hypoxic events — key for the alignment model, which requires detection of intermittent hypoxia.

**Gap to alignment model requirements:**
- ✅ Can detect fetal SpO₂ (demonstrated in animal models)
- ✅ Can detect acute hypoxic events (demonstrated in animal models)
- ✅ Non-invasive (transabdominal placement)
- ❌ Not yet validated in human pregnancies for SpO₂ accuracy
- ❌ Not yet wearable/miniaturised for continuous 24-hour monitoring
- ❌ Signal quality degrades with maternal adipose tissue thickness
- ❌ No clinical trials for antepartum (weeks-long) monitoring
- ❌ Estimated 5–8 years from regulatory approval for clinical use

**Cost estimate:** Research prototype — $50,000–100,000. If commercialised, target device cost would likely be $2,000–5,000 per unit.

---

### 1B.2 Wearable Fetal Monitoring — Multimodal Sensors

**Key developments:**

- **Nguyen et al. (2024; PMID: 39451694):** NIH/NICHD group (Gandjbakhche lab). Developed a wireless, wearable multimodal sensor integrating NIRS for transabdominal placental oxygen saturation AND maternal physiological signals (heart rate, respiration, movement). This is the most directly relevant device to the alignment model's requirements. Uses NIRS to measure placental oxygen saturation (not fetal arterial SpO₂ directly, but placental oxygenation as a proxy). Wireless. Wearable. Designed for extended monitoring.

- **Ryu et al. (2021; PMID: 33972445):** Northwestern University / Rogers Lab. "Comprehensive pregnancy monitoring with a network of wireless, soft, and flexible sensors." Three sensors for maternal and fetal vital signs — tested in both high-resource (Chicago) and low-resource (Zambia) settings. Monitors fetal heart rate, maternal heart rate, respiration, temperature, activity. Published in PNAS. Limitation: **does not measure oxygen saturation.** Monitors FHR only.

- **Ahmed et al. (2024; PMID: 39338811):** Comprehensive review of textile-based wearable FHR monitoring. Focus on integrating sensors into clothing for continuous monitoring. Again: heart rate only, not oxygenation.

- **Yap et al. (2025; PMID: 41296871):** Compact wearable pressure-strain combo sensor for continuous fetal movement monitoring. Published in Science Advances. Measures fetal movement patterns, not oxygenation.

**Summary of wearable landscape:** Multiple groups have wearable fetal monitoring devices in development or early clinical trials, but almost all measure fetal heart rate, movement, or maternal physiology. **Only the Gandjbakhche/NIH group (Nguyen et al. 2024) has a wearable specifically designed to measure placental/fetal oxygenation.** This is TRL 3–4.

---

### 1B.3 Photoacoustic Imaging for Fetal Tissue Oxygenation

**What it is:** Combines pulsed laser light with ultrasound detection. Short laser pulses are absorbed by tissue (particularly haemoglobin), causing thermoelastic expansion and generating ultrasound waves. The ultrasound is detected and used to reconstruct an image. Because oxyhaemoglobin and deoxyhaemoglobin absorb different wavelengths, multispectral photoacoustic imaging can calculate tissue oxygen saturation.

**Why it matters for the alignment model:** Photoacoustic imaging offers 2–3 orders of magnitude better depth penetration than conventional optical imaging while retaining the spectroscopic ability to measure oxygen saturation. Theoretically capable of mapping placental and fetal tissue oxygenation through the maternal abdomen.

**Current state (TRL 2–4):**

- **Arthuis et al. (2017; PMID: 28081216):** Real-time monitoring of placental oxygenation during maternal hypoxia and hyperoxygenation using photoacoustic imaging in pregnant rats. Demonstrated that PA imaging can track placental oxygen saturation changes in real time across gestation. This was a landmark proof-of-concept.

- **Bayer et al. (2017; PMID: 28270982):** Ultrasound-guided spectral photoacoustic imaging of haemoglobin oxygenation during murine fetal development. Estimated tissue oxygenation longitudinally throughout pregnancy in mice. Showed developmental changes in oxygenation patterns.

- **Kang et al. (2018; PMID: 29927734):** Validated non-invasive photoacoustic measurements of sagittal sinus oxyhaemoglobin saturation in hypoxic neonatal piglets. Demonstrated that PA measurements correlate linearly with direct blood sampling — i.e., photoacoustic oximetry is accurate.

- **Shan et al. (2020; PMID: 31994834):** In vivo hemodynamic imaging of fetal brain oxygenation after prenatal ethanol exposure using photoacoustic tomography. Measured vessel diameter, density, AND oxygen saturation in fetal brain — precisely the multi-parameter data the alignment model needs.

- **Okawa et al. (2024; PMID: 38241840):** Real-time measurement of placental blood oxygen saturation by photoacoustic in a rabbit hypoxia model. Established basic technique for continuous monitoring. TRL 3 in animal models.

- **Zhang et al. (2026; PMID: 41640461):** Early identification of umbilical blood flow restriction and maternal placental hypoperfusion with photoacoustic imaging. Published January 2026. Demonstrates quantitative assessment of fetal cerebral oxygenation — what CTG and ultrasonography cannot do.

- **Jiang et al. (2025; PMID: 40655941):** Automatic photoacoustic monitoring of perinatal brain hypoxia with superior sagittal sinus detection. Neonatal piglet model. Key advance: automated detection of hypoxic events without operator intervention.

- **Lee & Kim et al. (2026; PMID: 41604485):** "From light to sound: Seeing and hearing the placenta in health and disease." Science Advances review (January 2026). Comprehensive overview of advanced ultrasound and photoacoustic techniques for placental assessment. Notes that photoacoustic imaging can provide quantitative oxygenation data that conventional ultrasound cannot.

**Gap to alignment model requirements:**
- ✅ Can measure tissue oxygen saturation (animal models)
- ✅ Depth penetration sufficient for transabdominal imaging
- ✅ Can detect acute oxygen changes in real time
- ✅ Can image placental AND fetal organ oxygenation
- ❌ No human pregnancy data yet
- ❌ Current devices are large, laboratory-based systems
- ❌ Laser safety concerns for prolonged fetal exposure
- ❌ Not yet miniaturised for continuous/wearable use
- ❌ Estimated 8–12 years from regulatory approval for clinical fetal monitoring

**Technology Readiness Level:** TRL 3–4 (laboratory/animal validation)

---

### 1B.4 MRI-Based Fetal Oxygenation Mapping (BOLD, T2*)

**What it is:** Blood oxygen level-dependent (BOLD) MRI and T2* mapping exploit the paramagnetic properties of deoxyhaemoglobin. In regions with more deoxyhaemoglobin, T2* signal decreases. By measuring T2* across the placenta and fetal organs, oxygenation can be mapped.

**Current state (TRL 5–6 for placental mapping, TRL 3–4 for fetal organ mapping):**

- **Schabel et al. (2022; PMID: 35853003):** Landmark longitudinal study — 316 pregnancies, 797 imaging studies at up to three time points between 11–38 weeks. Quantitative placental T2* mapping. Key findings:
  - Placental T2* follows a sigmoid curve across gestation — high early, decreasing through an inflection at ~30 weeks, reaching a lower plateau in late gestation
  - T2* was significantly lower in adverse pregnancy outcomes (hypertensive disorders, FGR, stillbirth) starting from **15 weeks** and continuing through **33 weeks**
  - AUC for predicting adverse outcomes: 0.71 overall, **0.76 at mid-gestation (20–30 weeks)**
  - This is the most directly relevant technology for the alignment model — it demonstrates that placental oxygenation can be quantified across gestation and predicts adverse outcomes

- **Abaci Turk, Grant et al. (2019; PMID: 31592995):** Human Placenta Project review (NIH-funded). Developing accurate quantitative MRI measures of placental oxygenation. Reviews BOLD, T2*, diffusion-weighted, and ASL approaches. Key conclusion: MRI can quantify placental function, but standardisation and validation are needed.

- **Sinding et al. (2017; PMID: 28012454):** Compared placental T2* with uterine artery Doppler for predicting low birth weight. T2* at 36 weeks was superior to Doppler PI for predicting birthweight <10th percentile.

- **Hall et al. (2024; PMID: 38956748):** Multimodal placental MRI prior to spontaneous preterm birth <32 weeks. Observational study in BJOG. Demonstrates feasibility of MRI placental assessment in the very population relevant to the alignment model (early preterm).

**Gap to alignment model requirements:**
- ✅ Can quantify placental T2* (oxygenation proxy) at specific gestational ages
- ✅ Demonstrated predictive value for adverse outcomes
- ✅ Non-invasive
- ✅ Can map spatial heterogeneity of placental oxygenation
- ✅ Can image fetal organs (brain, liver, kidneys)
- ❌ **Point-in-time measurement.** Each MRI is a ~45-minute scan providing a single snapshot. Cannot detect intermittent events
- ❌ **Cannot be performed continuously.** Maximum feasible frequency: monthly scans
- ❌ **Expensive.** Each fetal MRI costs $1,500–3,000. Serial scanning across pregnancy: $6,000–18,000 per patient
- ❌ **Requires lying still in scanner.** Not tolerable for continuous monitoring
- ❌ Fetal motion artefact remains a significant challenge

**Technology Readiness Level:** TRL 5–6 for placental mapping; research use only

**Cost:** $1,500–3,000 per scan; MRI systems $1–3 million

---

### 1B.5 AI-Enhanced CTG/Doppler Interpretation

**What it is:** Machine learning and deep learning algorithms applied to existing CTG and Doppler data to extract features that humans cannot reliably identify.

**Current state (TRL 5–7):**

- **Miyata et al. (2025; PMID: 40034878):** Direct comparison of AI vs human judgement for CTG assessment during delivery. Found AI outperformed clinicians in identifying fetal asphyxia. Notes that >70% of stillbirths involve substandard CTG interpretation.

- **Melaet et al. (2024; PMID: 38340594):** AI-based CTG assessment that distinguishes normal from pathological events using clinical decision-making–inspired algorithms. Full paper in EJOG.

- **Pardasani et al. (2025; PMID: 41035563):** Novel AI algorithm for interpreting FHR and uterine activity data in CTG. Published in Frontiers in Digital Health. Automated feature extraction addressing subjective inter-observer variability.

- **Hardalaç et al. (2024; PMID: 39367993):** Achieved 100% sensitivity for pathological cases and 98.8% specificity for normal cases on CTG datasets.

**Relevance to alignment model:**
- AI cannot overcome the fundamental limitation: **CTG does not measure oxygen.** Better interpretation of CTG data improves detection of *already-distressed* fetuses but does not provide the oxygenation data the alignment model needs
- AI applied to Doppler velocity waveforms could potentially extract more information about placental flow dynamics, but this is also an indirect proxy
- **Most promising application:** AI-enhanced integration of multiple data streams (CTG + Doppler + maternal biomarkers + gestational age) to create a composite hypoxia risk score

---

### 1B.6 Miniaturised Electrochemical Sensors

**Pla et al. (2021; PMID: 33541374):** Miniaturised electrochemical sensors for continuous monitoring of pH and oxygen in an animal model of acute hypoxia. These sensors were evaluated for performance in detecting oxygen and pH changes. Potential for implantable continuous monitoring, but currently invasive and at TRL 2–3.

---

## 1C. Why Fetal Pulse Oximetry Failed (and What It Tells Us)

### The Nellcor N-400 / OxiFirst Story

**Timeline:**
- **1980s–1990s:** Development period. Nellcor (later acquired by Tyco/Covidien, now Medtronic) developed a reflectance pulse oximetry sensor (FS-14) designed for transcervical placement
- **2000:** Initial multicenter trial (Garite et al., PMID: 11084540) showed reduction in cesarean for non-reassuring status but no overall cesarean reduction
- **2000 (May):** FDA 510(k) clearance granted for the OxiFirst system
- **2000–2005:** Clinical use expanded in the US and Europe. Multiple studies using the Nellcor N-400 / FS-14 sensor were conducted (PMID: 9134413; PMID: 9322629; PMID: 15852229; PMID: 19954413)
- **2006 (November):** Bloom et al. NEJM trial — 5,341 patients — definitive negative result. No reduction in cesarean rates, no improvement in neonatal outcomes
- **2006:** ACOG concluded that fetal pulse oximetry was not recommended for clinical use
- **2007–2009:** Nellcor/Covidien withdrew OxiFirst from the market

### Why It Failed — Technical and Clinical Reasons

**1. Wrong clinical endpoint.** The device was tested against cesarean section rates, not fetal outcomes. It was designed to *avoid unnecessary cesareans* by confirming fetal wellbeing when CTG was non-reassuring. This is an operational efficiency question, not a diagnostic improvement question. The technology worked — it measured SpO₂ — but the clinical pathway for using that information was wrong.

**2. CTG confounding.** In the Bloom trial, even when SpO₂ was reassuring, clinicians could not override non-reassuring CTG (because CTG was the medicolegal standard). The "open" group had SpO₂ data but were still bound by CTG-driven protocols. The information was available but structurally unused.

**3. Paradoxical dystocia effect.** In the Garite trial, knowing SpO₂ reduced cesarean for "non-reassuring fetal status" by 50% but increased cesarean for "dystocia" almost exactly compensating. This suggests clinicians shifted their indication rather than their decision. One possible explanation: when SpO₂ was reassuring despite non-reassuring CTG, clinicians waited longer. The longer they waited, the more likely they encountered a separate indication (dystocia from prolonged labour).

**4. Invasive placement.** Required ruptured membranes and adequate cervical dilation. Could not be placed early in labour, and not at all antepartum.

**5. Signal reliability.** Contact-dependent reflectance oximetry required continuous sensor-skin contact on the moving fetal presenting part. Signal dropout rates were 20–40% in some studies.

**6. The wrong question at the wrong time.** Fetal pulse oximetry was designed to reduce cesarean rates during labour — a period of minutes to hours. The alignment model's question is about oxygen delivery across weeks to months during development. The failure of intrapartum pulse oximetry says nothing about whether continuous antepartum monitoring would be valuable.

### What the Failure Tells Us

1. **The clinical framework matters as much as the technology.** Measuring SpO₂ during labour and providing it to clinicians already bound by CTG-based protocols was structurally ineffective. Any future fetal oxygenation monitoring technology must be integrated into a clinical decision pathway that can actually use the data.

2. **Transabdominal is the only viable pathway for antepartum monitoring.** Any device requiring membrane rupture or cervical access is limited to intrapartum use. The alignment model requires antepartum monitoring.

3. **The physics of fetal SpO₂ measurement was validated.** The N-400 did measure fetal oxygen saturation accurately (validated against fetal scalp blood pH). The technology worked; the clinical application failed.

4. **Specificity is the bottleneck, not sensitivity.** CTG has high sensitivity but catastrophic specificity. The next monitoring technology must improve specificity — i.e., reduce false positives by directly measuring oxygenation rather than inferring it from heart rate patterns.

---

## 1D. Gap Analysis: What the Alignment Model Requires vs. What Exists

### Required Specifications

For the alignment model to be directly testable via continuous monitoring, a device would need:

| Parameter | Requirement | Rationale |
|-----------|------------|-----------|
| **Measurement target** | Fetal arterial SpO₂ or placental tissue oxygenation (StO₂) | Direct measurement of what the fetus receives |
| **Resolution (amplitude)** | Detect events dropping below ~45% fetal SpO₂ (equivalent to ~80% neonatal SpO₂ given left-shifted HbF curve) | Must identify clinically significant hypoxic events vs normal fluctuations |
| **Resolution (temporal)** | ≤10-second event detection | Analogous to intermittent hypoxia (IH) events in the NICU — 10-second events drive injury |
| **Duration** | Continuous monitoring across weeks 20–40, or at minimum weeks 23–36 (the "super-window" where most vulnerability periods overlap) | Must capture the full exposure period |
| **Non-invasive** | Transabdominal, wearable, tolerable for weeks of use | Must not require membrane rupture or clinical procedures |
| **Data output** | Timestamped SpO₂/StO₂ values with gestational age | Must permit overlay on developmental windows |
| **Maternal/fetal discrimination** | Must reliably separate fetal from maternal oxygenation signals | The maternal signal is much stronger and will dominate without algorithmic separation |

### Current Technology vs. Requirements

| Requirement | Best Current Technology | Gap Size | Estimated Time to Close |
|-------------|----------------------|----------|------------------------|
| Direct fetal SpO₂ | UC Davis TFO (Ghiasi lab) | Large — animal validation only, no human antepartum data | 5–8 years |
| Placental oxygenation | NIH NIRS wearable (Nguyen 2024) / MRI T2* (Schabel 2022) | Medium — NIRS wearable at TRL 3–4; MRI at TRL 5–6 but not continuous | 3–5 years for NIRS; MRI snapshots available now |
| 10-second event detection | TFO (Qian 2025 — detects instantaneous hypoxemia) | Medium — demonstrated in animal models | 5–8 years for human validation |
| Continuous weeks 20–40 | **Nothing exists** | Very large | 8–15 years |
| Non-invasive wearable | NIH NIRS sensor (Nguyen 2024) | Medium — prototype exists | 3–5 years for clinical-grade device |
| Maternal/fetal separation | TFO signal processing (Kasap 2024) | Large — proof-of-concept in humans | 5–8 years |

### The Honest Assessment

**No technology currently exists that could provide the data the alignment model needs.** The closest approach would be:

1. **Serial MRI T2* mapping** (e.g., monthly scans from 20–36 weeks) providing snapshot placental oxygenation data at known gestational ages. This is feasible **today** for ~$15,000/patient but provides 4–5 data points, not continuous monitoring. It would show trends in placental oxygenation but miss intermittent events.

2. **Wearable transabdominal NIRS** providing continuous placental tissue oxygenation. This could be TRL 7+ within 5 years. It would measure placental rather than fetal arterial SpO₂ — an imperfect proxy but far better than nothing.

3. **The combination:** Serial MRI for placental mapping + continuous wearable NIRS for between-scan monitoring + standard Doppler assessment + maternal biomarkers (sFlt-1/PlGF ratio). This multi-modal approach could provide a reasonably comprehensive picture of fetal oxygen exposure even with current technology limitations.

### Technology Readiness Summary

| Technology | TRL | Timeline to Clinical Use | Cost per Patient |
|-----------|-----|------------------------|-----------------|
| CTG/EFM | 9 | Available now | $200–500/session |
| Umbilical Doppler | 9 | Available now | $300–800/scan |
| Fetal NIRS (intrapartum) | 4–5 | Uncertain | N/A |
| Transabdominal Fetal Pulse Oximetry | 4 | 5–8 years | $2,000–5,000 (estimate) |
| Wearable Placental NIRS | 3–4 | 3–5 years | $1,000–3,000 (estimate) |
| Photoacoustic Fetal Imaging | 3–4 | 8–12 years | Unknown |
| MRI Placental T2* Mapping | 5–6 | Available for research now | $1,500–3,000/scan |
| AI-Enhanced CTG/Doppler | 5–7 | 2–4 years | Marginal (software add-on) |

---

# SECTION 2: MULTI-ORGAN PROSPECTIVE STUDY DESIGN

## The Study That Should Exist But Doesn't

The alignment model predicts that gestational timing of preeclampsia onset determines which organ systems show deficit in offspring. No existing study has simultaneously measured multi-organ outcomes in a single PE cohort to test this prediction. This section designs that study.

**Study name proposal:** PRISM — **PR**eeclampsia **I**mpact on **S**ystem-specific **M**aturation

---

## 2A. Study Architecture

### 2A.1 Study Design

**Type:** Prospective, multi-centre, observational cohort study with nested Case-Control comparisons  
**Duration:** 20-year project (5-year enrolment + 18-year follow-up)  
**Registration:** ClinicalTrials.gov; protocol publication before first enrolment

### 2A.2 Population

**Exposed cohorts (n=600 total):**

| Group | Definition | Target n | Rationale |
|-------|-----------|----------|-----------|
| **EOPE** | PE onset <34+0 weeks | 200 | Primary "early window" exposure group |
| **LOPE** | PE onset ≥34+0 weeks | 200 | Primary "late window" exposure group |
| **Severe/HELLP** | PE with HELLP syndrome or eclampsia (any GA) | 100 | Maximum severity group — tests dose-response |
| **PE-FGR** | PE with concurrent FGR (<10th centile) | 100 | Combined vascular insult group |

**Control cohort (n=400):**

| Group | Definition | Target n | Rationale |
|-------|-----------|----------|-----------|
| **Normotensive term** | No hypertensive disorder, delivery ≥37 weeks | 200 | Primary control |
| **Normotensive preterm** | No PE, preterm delivery <34 weeks (preterm labour, PPROM) | 100 | Controls for prematurity confound |
| **Chronic HTN (no PE)** | Chronic hypertension without superimposed PE | 100 | Controls for maternal hypertension confound |

**Total enrolled:** 1,000 mother-offspring dyads

### 2A.3 Sample Size Justification

- **Primary comparison:** EOPE vs LOPE on white matter DTI fractional anisotropy (FA) at age 5
- **Expected effect size:** Based on Schlapakow et al. (2021), FA differences of 0.02–0.04 between preterm-born and term-born children. Assuming EOPE shows an additional FA reduction of 0.015 beyond prematurity effect, SD ~0.03
- **Power calculation:** For two-sided t-test, α=0.05, power=0.80, effect size d=0.50 → n=64 per group. With 200 per PE group, study is powered at >99% for the primary comparison and adequately powered for subgroup analyses
- **Attrition planning:** 40% expected loss to follow-up over 18 years → effective sample at 18-year assessment: ~600 retained. Minimum sample at each timepoint: 120 EOPE, 120 LOPE, 120 controls — still >90% power for primary analysis

### 2A.4 Recruitment Strategy

**Sites:** 4–6 tertiary referral centres with specialist PE services (e.g., King's College London, Brigham & Women's Boston, Erasmus MC Rotterdam, Oslo University Hospital, University of British Columbia, Monash University Melbourne)

**Recruitment approach:**
- Prospective screening of all PE admissions
- EOPE group: recruited at diagnosis (20–34 weeks) — advantage of longer enrolment window
- LOPE group: recruited at diagnosis (≥34 weeks) — shorter enrolment window but higher incidence
- Controls: recruited at same institution, matched for maternal age (±3 years), parity, ethnicity, and gestational age at delivery (for preterm controls)
- Informed consent for 18-year follow-up with re-consent at each assessment milestone

**Inclusion criteria:**
- Singleton pregnancy
- PE diagnosed per ISSHP 2018 criteria (hypertension + proteinuria or organ dysfunction after 20 weeks)
- No major congenital anomalies
- No chromosomal abnormalities
- Maternal age 18–45

**Exclusion criteria:**
- Multiple pregnancy
- Pre-existing diabetes mellitus (type 1 or 2)
- Chronic kidney disease
- Known fetal genetic syndrome
- Substance abuse (confounds neurodevelopment)
- Maternal autoimmune disease requiring immunosuppression (confounds immune outcomes)

### 2A.5 Ethical Considerations

- Long-term follow-up of children requires robust consent frameworks with child assent from age 12
- Incidental findings protocol (e.g., if MRI reveals unexpected pathology)
- Data protection for 20+ year dataset (GDPR-compliant for European centres)
- Equity in recruitment — ensure cohort reflects population diversity
- Payment/compensation for families at each assessment to reduce attrition bias

---

## 2B. Gestational Exposure Characterisation

### The "Input" — Quantifying the Oxygen Insult

The alignment model requires detailed characterisation of the oxygen deprivation exposure. For each PE case:

### 2B.1 Clinical PE Records

| Variable | Source | Timing |
|----------|--------|--------|
| GA at PE diagnosis | Clinical records | At diagnosis |
| GA at delivery | Clinical records | At delivery |
| Duration of PE exposure (diagnosis-to-delivery interval) | Calculated | Retrospective |
| Peak blood pressure (systolic and diastolic) | Serial measurements | Throughout PE episode |
| 24-hour urinary protein or spot protein/creatinine ratio | Lab results | At diagnosis and serially |
| Episodes of acute worsening (hypertensive crisis, headache, visual disturbance) | Clinical records | Throughout |
| Antihypertensive medications used | Clinical records | Throughout |
| Magnesium sulfate administration (eclampsia prophylaxis) | Clinical records | Intrapartum |
| Corticosteroid administration (for fetal lung maturity) | Clinical records | Antepartum |
| Mode of delivery and indication | Clinical records | At delivery |

### 2B.2 Ultrasound and Doppler Assessment

| Variable | Source | Timing |
|----------|--------|--------|
| Umbilical artery Doppler PI/RI and AREDF | US report | At diagnosis and weekly |
| Middle cerebral artery Doppler PI | US report | At diagnosis and weekly |
| Cerebroplacental ratio (CPR) | Calculated | At diagnosis and weekly |
| Ductus venosus waveform | US report | If available |
| Estimated fetal weight and growth centile | US report | Serial |
| Amniotic fluid volume (AFI or deepest pocket) | US report | Serial |
| Uterine artery Doppler (bilateral notching, mean PI) | US report | At diagnosis |

### 2B.3 MRI Placental Assessment (Substudy — n=200)

For a subset of 200 patients (50 EOPE, 50 LOPE, 50 severe/HELLP, 50 controls):

| Variable | Method | Timing |
|----------|--------|--------|
| Placental T2* mapping | BOLD MRI | At diagnosis, then 2-weekly until delivery |
| Placental volume | MRI volumetry | Same timepoints |
| T2* z-score relative to gestational age | Calculated per Schabel et al. methodology | |
| Fetal brain MRI volumes (where feasible) | Volumetric MRI | 3rd trimester |

**Cost for MRI substudy:** 200 patients × 3 scans average × $2,500 = **$1.5M**

### 2B.4 Placental Pathology

| Variable | Method | Timing |
|----------|--------|--------|
| Placental weight and weight centile | Standardised protocol | At delivery |
| Villous maldevelopment score | Amsterdam criteria (Khong et al., 2016) | Postpartum |
| Decidual vasculopathy (acute atherosis, fibrinoid necrosis) | Histopathology | Postpartum |
| Placental infarction (% parenchymal involvement) | Histopathology | Postpartum |
| Villous maturation (accelerated or delayed) | Histopathology | Postpartum |
| Fetal vascular malperfusion (FVM) | Histopathology | Postpartum |
| Maternal vascular malperfusion (MVM) | Histopathology | Postpartum |
| Chronic villitis of unknown aetiology (VUE) | Histopathology | Postpartum |

### 2B.5 Cord Blood and Biomarkers

| Variable | Method | Timing |
|----------|--------|--------|
| Cord arterial and venous blood gases (pH, pO₂, pCO₂, BE, lactate) | Blood gas analyser | At delivery |
| sFlt-1 / PlGF ratio (maternal) | Immunoassay | At PE diagnosis, weekly, and at delivery |
| sFlt-1 / PlGF ratio (cord blood) | Immunoassay | At delivery |
| Cord blood erythropoietin | Immunoassay | At delivery — marker of chronic fetal hypoxia |
| Cord blood cortisol | Immunoassay | At delivery — marker of fetal stress |
| Cord blood nucleated red blood cells (NRBC count) | Manual differential | At delivery — marker of chronic hypoxia |

### 2B.6 Neonatal Exposure (If NICU Admission)

For infants admitted to NICU (expected in most EOPE and some LOPE:

| Variable | Method | Timing |
|----------|--------|--------|
| Continuous SpO₂ recording | NICU pulse oximetry | Entire NICU stay |
| Intermittent hypoxia (IH) events | Automated detection: SpO₂ <80% for ≥10 seconds | Daily counts from admission to discharge |
| Duration of supplemental oxygen | NICU records | |
| Duration of mechanical ventilation | NICU records | |
| Caffeine therapy (frequency and duration) | NICU records | |
| Head ultrasound findings (IVH, PVL) | NICU protocol | Day 1, 3, 7, 28, 36 weeks PMA |
| BPD diagnosis | NICU records | 36 weeks PMA |
| NEC diagnosis | NICU records | |
| ROP staging | Ophthalmology records | |

### 2B.7 Epigenetic Markers (Biobank Substudy — n=400)

| Sample | Collection | Storage |
|--------|-----------|---------|
| Cord blood DNA | 2 × EDTA tubes (10 mL) | -80°C biobank |
| Placental tissue (4 quadrants + membranes) | Standardised protocol within 60 minutes of delivery | -80°C (RNA later + fresh frozen) |
| Maternal blood (PE diagnosis timepoint) | 2 × EDTA + 2 × serum tubes | -80°C biobank |
| Cord blood mononuclear cells (CBMCs) | Ficoll separation | Liquid nitrogen |

**Epigenetic analyses (deferred to funding cycles):**
- Genome-wide DNA methylation (Illumina EPIC v2 array) on cord blood and placental tissue
- Targeted bisulphite sequencing of candidate loci (HIF pathway, VEGF, IGF2/H19)
- Gene expression profiling (RNA-seq) on placental tissue

---

## 2C. Multi-Organ Outcome Assessment

### Assessment Schedule

| System | Assessment Tools | Age 2 yr | Age 5 yr | Age 8 yr | Age 10 yr | Age 18 yr |
|--------|-----------------|----------|----------|----------|-----------|-----------|
| **White matter** | MRI DTI (FA, MD, RD, AD), PLS-5/CELF-5 | DTI + PLS-5 | DTI + CELF-5 | DTI + CELF-5 | DTI + CELF-5 | DTI |
| **Cardiac** | Echocardiography, ambulatory BP, carotid IMT | — | Echo + BP | — | Echo + BP + cIMT | Echo + BP + cIMT |
| **Renal** | Cystatin C eGFR, urine ACR, renal US | — | CysC + ACR | — | CysC + ACR + US | CysC + ACR + US |
| **Hippocampal** | WRAML-3, volumetric MRI hippocampal | — | WRAML + MRI | — | WRAML + MRI | MRI |
| **Cerebellar** | MABC-2, clinical neuro exam | MABC-2 | MABC-2 | — | — | — |
| **Immune** | Flow cytometry (T-cell subsets), infection history | T-cells + hx | T-cells + hx | — | T-cells + hx | T-cells + hx |
| **Metabolic** | Fasting glucose, insulin, HbA1c, lipid panel, OGTT | — | — | — | Labs + OGTT | Labs + OGTT |
| **Pulmonary** | Spirometry (FEV1, FVC, FEV1/FVC), FeNO | — | Spirometry | — | Spirometry + FeNO | Spirometry + FeNO |
| **Retinal** | OCT, axial length, visual acuity | — | OCT + VA | — | OCT + VA | OCT |
| **Cortical** | WISC-V (age 5+), WAIS-IV (age 18), EEG | Bayley-4 | WISC-V + EEG | — | WISC-V + EEG | WAIS-IV |

### Detailed Assessment Descriptions

**White Matter (Primary Outcome System):**
- **MRI DTI:** 3T scanner, harmonised acquisition parameters across sites. Tract-based spatial statistics (TBSS) for whole-brain analysis. Region-of-interest analysis of: corpus callosum (genu, body, splenium), superior longitudinal fasciculus, inferior longitudinal fasciculus, corticospinal tracts
- **Fractional anisotropy (FA)** as primary DTI metric — reduced FA indicates white matter microstructural abnormality
- **Language measures:** PLS-5 (Preschool Language Scales) at age 2, CELF-5 (Clinical Evaluation of Language Fundamentals) from age 5+
- **Primary endpoint:** FA of corpus callosum body at age 5

**Cardiac:**
- **Echocardiography:** Left ventricular mass index (LVMI), relative wall thickness, E/A ratio, tissue Doppler (e', a', s'), global longitudinal strain (GLS)
- **Ambulatory blood pressure:** 24-hour ABPM at ages 5, 10, 18 (validated device appropriate for age/size)
- **Carotid intima-media thickness (cIMT):** Bilateral B-mode ultrasound at ages 10, 18 — early marker of atherosclerotic vascular disease

**Renal:**
- **Cystatin C–based eGFR:** Preferred over creatinine-based formulas in children (less influenced by muscle mass)
- **Urine albumin-to-creatinine ratio (ACR):** First morning void, microalbuminuria threshold >30 mg/g
- **Renal ultrasound:** Kidney length, cortical thickness, echogenicity — detects structural nephron deficit

**Hippocampal:**
- **Volumetric MRI:** Automated hippocampal segmentation (FreeSurfer or ASHS). Bilateral volume normalised to total intracranial volume
- **WRAML-3:** Wide Range Assessment of Memory and Learning — story memory, verbal working memory, visual memory indices

**Cerebellar:**
- **MABC-2:** Movement Assessment Battery for Children, 2nd edition — fine motor, gross motor, balance components
- **Clinical neurological exam:** Finger-to-nose, heel-to-shin, tandem gait, rapid alternating movements

**Immune:**
- **Flow cytometry panel:** CD3+, CD4+, CD8+, CD4/CD8 ratio, CD56+ NK cells, CD19+ B cells, Treg cells (CD4+CD25+FoxP3+), naïve vs memory T-cells
- **Infection history:** Parental questionnaire + medical record review — total hospitalizations for infection, antibiotic courses, recurrent infections

**Metabolic:**
- **Fasting labs:** Glucose, insulin, HOMA-IR, HbA1c, total cholesterol, LDL, HDL, triglycerides
- **OGTT (ages 10, 18):** Standard 75g oral glucose tolerance test with 2-hour glucose and insulin

**Pulmonary:**
- **Spirometry:** Pre- and post-bronchodilator FEV1, FVC, FEV1/FVC, FEF25-75. Expressed as z-scores per GLI-2012 reference
- **FeNO:** Fractional exhaled nitric oxide — marker of eosinophilic airway inflammation

**Retinal:**
- **OCT (optical coherence tomography):** Retinal nerve fibre layer (RNFL) thickness, macular thickness, foveal morphology — non-invasive, rapid, quantitative markers of neurovascular development
- **Axial length:** Biometry — marker of ocular growth trajectory
- **Visual acuity:** LogMAR chart

**Cortical/Cognitive:**
- **Bayley-4 (age 2):** Cognitive, language, motor composite scores
- **WISC-V (ages 5, 10):** Full Scale IQ, Verbal Comprehension Index, Working Memory Index, Processing Speed Index
- **WAIS-IV (age 18):** IQ assessment
- **EEG (ages 2, 5, 10):** Quantitative EEG — spectral power, coherence — sensitive marker of cortical maturation

---

## 2D. The Key Statistical Test

### 2D.1 Primary Hypothesis

The alignment model predicts a **specific interaction pattern:**

> **EOPE (exposure weeks 23–34) should produce MORE injury in systems whose vulnerability windows are concentrated in weeks 23–34, while LOPE (exposure ≥34 weeks) should produce MORE injury in systems whose windows extend into late gestation.**

### 2D.2 Predicted Interaction Matrix

Based on the vulnerability window map from *RESEARCH__gestational-impact-zones-oxygen-demand-alignment.md*:

| Organ System | Vulnerability Window Peak | Predicted EOPE Impact | Predicted LOPE Impact |
|--------------|--------------------------|----------------------|----------------------|
| White matter | Weeks 23–32 | ★★★ HIGH | ★ LOW |
| Cortical (subplate) | Weeks 20–32 | ★★★ HIGH | ★ LOW |
| Cerebellar | Weeks 24–40 | ★★★ HIGH | ★★ MODERATE |
| Renal (nephrogenesis) | Weeks 20–36 | ★★★ HIGH | ★★ MODERATE |
| Retinal (vascularisation) | Weeks 16–32 | ★★★ HIGH | ★ LOW |
| Hippocampal | Weeks 20–40 | ★★★ HIGH | ★★ MODERATE |
| Immune (thymic selection) | Weeks 16–40 | ★★ MODERATE | ★★ MODERATE |
| Cardiac (endowment) | Weeks 24–40 | ★★ MODERATE | ★★★ HIGH |
| Pulmonary (alveolarisation) | Weeks 24–40 | ★★ MODERATE | ★★★ HIGH |
| Hepatic (enzyme maturation) | Weeks 28–40 | ★ LOW | ★★★ HIGH |
| Pancreatic (β-cell) | Weeks 20–40 | ★★ MODERATE | ★★★ HIGH |
| Metabolic (composite) | Weeks 24–40 | ★★ MODERATE | ★★★ HIGH |

### 2D.3 Statistical Approach

**Primary analysis — Interaction test:**

$$Y_{ij} = \beta_0 + \beta_1 \cdot \text{PE\_group}_i + \beta_2 \cdot \text{System}_j + \beta_3 \cdot (\text{PE\_group}_i \times \text{System}_j) + \boldsymbol{\gamma} \cdot \mathbf{C}_i + \varepsilon_{ij}$$

Where:
- $Y_{ij}$ = standardised outcome z-score for patient $i$ in organ system $j$
- $\text{PE\_group}$ = categorical (EOPE, LOPE, control)
- $\text{System}$ = categorical (each organ system)
- $\beta_3$ = the interaction term — **this is the test of the alignment model**
- $\mathbf{C}_i$ = covariate vector (gestational age at delivery, birthweight z-score, sex, maternal BMI, socioeconomic status, corticosteroid exposure, NICU IH event count)

If $\beta_3$ is significant and follows the predicted pattern (EOPE → early-window systems injured more; LOPE → late-window systems injured more), the alignment model is supported.

**Secondary analyses:**

1. **Continuous GA exposure:** Replace categorical PE group with continuous variable (GA at PE onset in weeks). Fit interaction:

$$Y_{ij} = \beta_0 + \beta_1 \cdot \text{GA\_onset}_i + \beta_2 \cdot \text{Window\_midpoint}_j + \beta_3 \cdot (\text{GA\_onset}_i \times \text{Window\_midpoint}_j) + \boldsymbol{\gamma} \cdot \mathbf{C}_i + \varepsilon_{ij}$$

Prediction: negative $\beta_3$ — earlier onset × early-window system = greater deficit. This is the "alignment score" — how closely PE onset aligns with each system's vulnerability midpoint.

2. **Dose-response within EOPE:** Among EOPE cases, test whether PE severity metrics (sFlt-1/PlGF ratio, Doppler PI, placental T2* z-score, duration of PE exposure) predict magnitude of deficit in early-window organs.

3. **Prematurity separation:** Multiple regression controlling for GA at delivery as a continuous covariate. The alignment model predicts that PE onset timing has an effect BEYOND what is explained by GA at delivery. The prematurity-matched control group (non-PE preterm deliveries) directly tests this.

4. **Composite organ deficit score:** Create a weighted composite score for "early-window systems" (white matter + cortical + cerebellar + renal + retinal) and "late-window systems" (cardiac + pulmonary + hepatic + metabolic). Test:

$$\text{Ratio} = \frac{\text{Early\_composite\_deficit}}{\text{Late\_composite\_deficit}}$$

**Prediction:** This ratio should be significantly >1 in EOPE and significantly <1 in LOPE.

5. **Structural equation modelling (SEM):** Path analysis testing the causal chain:

$$\text{PE onset timing} \rightarrow \text{Placental pathology severity} \rightarrow \text{Fetal oxygen exposure} \rightarrow \text{System-specific deficit pattern}$$

**Multiple testing correction:** Benjamini-Hochberg FDR correction across organ systems, with α=0.05.

### 2D.4 The Critical Null Hypothesis It Must Distinguish From

The alignment model must be distinguished from two competing explanations:

1. **"All injury is prematurity":** EOPE offspring have more deficits simply because they are born more prematurely, and prematurity itself (via IH events, etc.) drives the injury. **Test:** Prematurity-matched control group + GA at delivery as covariate in all models. If effects disappear after controlling for GA at delivery, the alignment model is wrong.

2. **"All injury is dose-dependent":** EOPE is more severe than LOPE, so EOPE offspring have more of ALL deficits — uniformly, not in a pattern predicted by vulnerability windows. **Test:** If the PE group × System interaction is non-significant (all systems affected equally), the dose-response model is supported over the alignment model. The alignment model specifically predicts *differential* effects across systems, not uniform severity.

---

## 2E. Minimum Viable Version

### The PRISM-Lite Protocol

If the full PRISM study is unfunded, what is the minimum study that would provide proof-of-concept?

### 2E.1 Which 2–3 Organ Systems to Prioritise?

**Priority 1: White matter (DTI) + Language**
- Strongest prior evidence base
- Most sharply defined vulnerability window (weeks 23–32)
- Strongest predicted differential between EOPE and LOPE
- DTI is objective, quantitative, and standardised
- Language outcomes (CELF-5) are clinically meaningful

**Priority 2: Renal (Cystatin C eGFR + urine ACR)**
- Clear vulnerability window (nephrogenesis closes at ~36 weeks)
- Simple, cheap tests (blood + urine)
- EOPE should show deficit; LOPE offspring may have normal renal function
- Strong alignment model prediction: nephrogenesis window closes at 36 weeks → EOPE disrupts it, LOPE doesn't

**Priority 3: Cardiac (echocardiography + BP)**
- Vulnerability window extends late (cardiomyocyte endowment continues to term)
- The alignment model has a *counter-intuitive* prediction here: LOPE should show MORE cardiac deficit than EOPE because cardiac endowment peaks in late gestation
- If LOPE shows worse cardiac outcomes than EOPE despite being "milder" disease, this is strong evidence for the alignment model

**These three systems create a decisive test:** White matter (early window) vs cardiac (late window) vs renal (mid-window that closes). If EOPE > LOPE for white matter, EOPE > LOPE for renal, but LOPE > EOPE for cardiac — the alignment model is strongly supported.

### 2E.2 Minimum Sample Size

For a three-group comparison (EOPE, LOPE, control) on white matter FA:
- Effect size d=0.50 (moderate)
- α=0.05, power=0.80
- **n=64 per group = 192 total**
- With 25% attrition at 5 years: **enrol 256 total (85 per group)**

### 2E.3 Shortest Follow-Up Period

**5 years.** At age 5:
- DTI is reliable and interpretable
- CELF-5 language assessment can be administered
- Echocardiography is informative (LV mass index, strain)
- Ambulatory BP monitoring is feasible (with paediatric-sized cuff)
- Cystatin C and urine ACR are trivial to collect
- WISC-V can be administered for cognitive assessment

**Timeline: 2-year enrolment + 5-year follow-up = 7-year study**

### 2E.4 Most Accessible Cohort

**Twin option:** Recruit from a single large tertiary referral centre with a high PE volume (e.g., King's College London processes ~2,000 PE pregancies annually). With 85 per group needed, enrolment of 256 total could be completed in 12–18 months at a single high-volume site.

**Alternative:** Add multi-organ follow-up to an existing PE birth cohort that has already enrolled and characterised gestational exposure (see 2F). This eliminates the 2-year enrolment phase.

### 2E.5 Which Single Assessment Captures the Most Signal?

**MRI DTI at age 5.**

Rationale:
- Objective, quantitative, operator-independent
- Whole-brain coverage — can simultaneously assess white matter tracts, hippocampal volume, cerebellar volume, and cortical thickness from a single 30-minute scan
- FA reduction in white matter tracts is the single strongest biomarker of preterm-related brain injury
- From one scan, you get data on three organ systems (white matter, hippocampal, cerebellar)

**Cost of minimum viable study:**
- 256 patients × 1 MRI scan ($1,500) = $384,000
- 256 patients × blood/urine tests at age 5 ($150) = $38,400
- 256 patients × echocardiography ($500) = $128,000
- 256 patients × language/cognitive assessment ($300) = $76,800
- Clinical coordination, data management, statistics: $200,000
- **Total PRISM-Lite budget: ~$830,000**

This is fundable within a single major grant cycle (NIHR Programme Grant, NIH R01, EU Horizon Health).

---

## 2F. Existing Cohorts That Could Be Extended

### 2F.1 Cohorts With PE Data and Offspring Follow-Up

The following existing cohorts have already enrolled preeclampsia pregnancies and have varying degrees of offspring follow-up:

**1. Helsinki Birth Cohort Study (HBCS)**
- **Location:** Finland
- **N:** 13,345 born 1934–1944; 8,760 born 1943–1944
- **PE data:** Yes — maternal pregnancy records including hypertensive disorders
- **Offspring follow-up:** Clinical examinations at age 60–70 (Kajantie et al., 2017; PMID: 27823919). Found gestational hypertension associated with type 2 diabetes in adult offspring
- **Extensibility:** Offspring are now elderly. Not suitable for childhood assessment. But demonstrates multi-decade PE → offspring programming effects. Could inform the alignment model with adult-onset
- **Limitation:** Historical records — PE onset timing not precisely documented. No EOPE/LOPE stratification possible

**2. Generation R Study**
- **Location:** Rotterdam, Netherlands (Erasmus MC)
- **N:** 9,778 mothers enrolled 2002–2006
- **PE data:** Yes — well-characterised pregnancy complications including PE, with onset timing
- **Offspring follow-up:** Extensive — ages 2, 5, 9, 13, and ongoing (participants now ~20–24 years)
- **Existing data:** Cardiovascular (BP, cIMT), body composition, cognitive/behavioural, spirometry, retinal imaging
- **Extensibility:** **HIGHEST PRIORITY.** This cohort has the infrastructure, the PE characterisation, AND multi-organ outcome data. An EOPE vs LOPE subanalysis could be performed on EXISTING data
- **Key publications:** Jaddoe et al. (2014; PMID: 24458585) — first-trimester growth restriction and school-age cardiovascular risk
- **Gap:** White matter DTI not routinely performed. Would need to recall PE-exposed participants for MRI
- **Estimated cost to extend:** $200,000–500,000 for MRI substudy on PE subgroup

**3. Mater-University of Queensland Study of Pregnancy (MUSP)**
- **Location:** Brisbane, Australia
- **N:** 6,753 mother-child dyads, 1981–1983 births
- **PE data:** Yes
- **Offspring follow-up:** To age 21 (Mamun et al., 2011; PMID: 21509041). Examined BP at age 21 in offspring of PE mothers
- **Extensibility:** Limited — historical cohort, offspring now >40

**4. HAPO Follow-Up Study (Hyperglycemia and Adverse Pregnancy Outcome)**
- **Location:** Multi-national (Perak et al., 2021; PMID: 33591345)
- **N:** Multiple centres, examinations 2000–2006 with follow-up at age 10–14
- **PE data:** Maternal cardiovascular health characterised but primary focus was gestational diabetes
- **Offspring follow-up:** CV health at early adolescence
- **Extensibility:** PE not the primary exposure but data may be extractable
- **Limitation:** PE cases likely present but not the study focus

**5. Danish National Birth Cohort (DNBC) / Danish Registries**
- **Location:** Denmark
- **N:** 100,000+ births enrolled (1996–2002); linked to national health registries for entire population
- **PE data:** Yes — ICD codes in national registry. Huang et al. (2021; PMID: 34582464) used Danish registries for PE → offspring CVD analysis with median 18-year follow-up
- **Offspring follow-up:** Through registry linkage — hospitalizations, diagnoses, medications to present day
- **Extensibility:** **VERY HIGH.** PE timing data available (ICD codes distinguish early/late). Could perform registry-based EOPE vs LOPE analysis for CVD, diabetes, renal disease, and neuropsychiatric diagnoses. No biological samples or detailed phenotyping, but massive statistical power
- **Key paper:** Huang et al. (2021; PMID: 34582464) — PE and offspring CVD risk, stratified by timing and severity. Found timing-specific effects: preeclampsia with preterm birth had higher CVD risk than PE with term birth, consistent with alignment model

**6. Icelandic National Registry**
- **Location:** Iceland
- **N:** Population-level data
- **PE data:** Yes — Sverrisson et al. (2018; PMID: 30462738) — PE and academic performance in children. Used registry data
- **Extensibility:** Strong registries but limited biological samples

**7. nuMoM2b / nuMoM2b Heart Health Study**
- **Location:** USA, 8 centres
- **N:** 10,038 nulliparous women enrolled 2010–2013
- **PE data:** Prospectively characterised — detailed PE phenotyping with onset timing
- **Offspring follow-up:** Limited — primarily maternal follow-up (nuMoM2b-HHS for maternal cardiovascular health 2–7 years postpartum)
- **Extensibility:** **HIGH PRIORITY.** Well-characterised PE cohort with biological samples. Offspring are now 13–16 years old. Adding multi-organ offspring assessment would be transformative. EOPE/LOPE stratification is built into the dataset
- **Estimated cost:** $500,000–1M for offspring recall and assessment

**8. SCOPE Consortium**
- **Location:** International (Auckland, Adelaide, Cork, London, Manchester, Leeds)
- **N:** 5,690 nulliparous women recruited 2004–2008
- **PE data:** Yes — prospective with biological samples
- **Offspring follow-up:** Variable by site. Cork centre has longitudinal offspring data (BASELINE cohort)
- **Extensibility:** Moderate — offspring now 18–22 years old

**9. NICHD Fetal Growth Study**
- **Location:** USA, 12 centres
- **N:** 2,802 low-risk, 468 obese women
- **PE data:** PE cases occurred within the cohort
- **Offspring follow-up:** Limited
- **Extensibility:** Excellent fetal growth data but small PE subgroup

### 2F.2 Recommended Extension Strategy

**Immediate opportunities (existing data, no new recruitment):**

1. **Generation R** — request EOPE vs LOPE subgroup analysis on existing cardiovascular, cognitive, and spirometry data. Time: 6–12 months. Cost: <$50,000 (data analysis only)

2. **Danish Registries** — registry-based EOPE vs LOPE analysis for multi-organ diagnoses (CVD, diabetes, CKD, COPD, neuropsychiatric). Time: 6–12 months. Cost: <$30,000 (registry access + analysis)

**Medium-term opportunities (offspring recall, new assessments):**

3. **nuMoM2b offspring recall** at age 13–16 — DTI MRI, echocardiography, renal function, spirometry. Cost: $500,000–1M. Time: 2–3 years

4. **Generation R PE subgroup recall** for DTI MRI at age 20–24. Cost: $200,000–500,000. Time: 1–2 years

**Long-term (new cohort):**

5. **PRISM or PRISM-Lite** as designed above. Cost: $830,000 (Lite) to $8–15M (full). Time: 7–20 years

---

## Summary: The Two-Track Strategy

### Track 1: Technology Development (5–10 year horizon)
- Support transabdominal fetal pulse oximetry (UC Davis / Ghiasi lab) → human clinical trials
- Support wearable placental NIRS (NIH / Gandjbakhche lab) → commercialisation
- Support photoacoustic imaging → miniaturisation
- Deploy serial MRI T2* placental mapping in PE pregnancies NOW (feasible today)
- AI integration of multi-modal data streams (CTG + Doppler + biomarkers + gestational age → composite oxygenation score)

### Track 2: Clinical Study (Immediate → 7 years)
- **Immediate (months 0–12):** Generation R and Danish registry EOPE vs LOPE secondary analyses — tests the alignment model predictions with zero new recruitment
- **Near-term (months 12–36):** nuMoM2b offspring recall for multi-organ assessment — tests alignment model in well-characterised US cohort
- **Medium-term (years 2–7):** PRISM-Lite — 256 new enrolments, 3 key organ systems (white matter, renal, cardiac), 5-year follow-up. The decisive test

### The Convergence Point

When Track 1 delivers continuous fetal oxygenation monitoring AND Track 2 has validated the alignment model's timing predictions, the two tracks merge. At that point, it becomes possible to:

1. Continuously monitor fetal oxygenation during pregnancy
2. Overlay oxygen deprivation events on known vulnerability windows
3. Predict which organ systems will show latent deficits
4. Intervene — either by treating the maternal condition earlier, timing delivery differently, or targeting neonatal monitoring to the predicted deficit systems
5. Transform preeclampsia from "a disease of the mother" to "a developmental exposure whose consequences for the child can be mapped, predicted, and mitigated"

---

## Key Citations

1. Hansen ML et al. Cerebral oximetry monitoring in extremely preterm infants. N Engl J Med. 2023;388(16):1501-1511. PMID: 37075142
2. Bloom SL et al. Fetal pulse oximetry and cesarean delivery. N Engl J Med. 2006;355(21):2195-202. PMID: 17124017
3. Garite TJ et al. Multicenter controlled trial of fetal pulse oximetry. Am J Obstet Gynecol. 2000;183(5):1049-58. PMID: 11084540
4. Schabel MC et al. Quantitative longitudinal T2* mapping for placental function. PLoS One. 2022;17(7):e0270360. PMID: 35853003
5. Nguyen T et al. Wireless wearable multimodal sensor for placental oxygen saturation. Biosensors. 2024;14(10):481. PMID: 39451694
6. Kasap B et al. Transcutaneous discrimination of fetal/maternal heart rate: TFO proof-of-concept. Reprod Sci. 2024;31(8):2331-2341. PMID: 38728001
7. Kasap B et al. FOSTER: Comprehensive pipeline for transabdominal fetal pulse oximetry. IEEE Trans Biomed Eng. 2025. PMID: 41124068
8. Qian W et al. Non-invasive detection of instantaneous fetal hypoxemia. NPJ Biomed Innov. 2025;2(1):12. PMID: 40290857
9. Fong DD et al. Validation of transabdominal fetal oximeter in hypoxic fetal lamb model. Reprod Sci. 2020;27(10):1960-1966. PMID: 32542541
10. Fong DD et al. Design and in vivo evaluation of transabdominal fetal pulse oximeter. IEEE Trans Biomed Eng. 2021;68(1):256-266. PMID: 32746021
11. Okawa KS et al. Real-time fetal monitoring using photoacoustic measurement. Placenta. 2024;146:110-119. PMID: 38241840
12. Arthuis CJ et al. Real-time monitoring of placental oxygenation using photoacoustic imaging. PLoS One. 2017;12(1):e0169850. PMID: 28081216
13. Zhang L et al. Photoacoustic identification of umbilical blood flow restriction. Photoacoustics. 2026;48:100803. PMID: 41640461
14. Lee D et al. From light to sound: placenta in health and disease. Sci Adv. 2026;12(5):eaed2184. PMID: 41604485
15. Balayla J & Shrem G. Solving the obstetrical paradox: FETAL technique. J Pregnancy. 2020;2020:7801039. PMID: 32089884
16. East CE et al. Fetal pulse oximetry for fetal assessment in labour. Cochrane Database Syst Rev. 2014;(10):CD004075. PMID: 25287809
17. Abaci Turk E et al. Placental MRI: developing accurate quantitative measures of oxygenation. Top Magn Reson Imaging. 2019;28(5):285-297. PMID: 31592995
18. Ryu D et al. Comprehensive pregnancy monitoring with wireless, soft, flexible sensors. Proc Natl Acad Sci USA. 2021;118(20):e2100466118. PMID: 33972445
19. Miyata K et al. AI vs human judgement in CTG assessment. Cureus. 2025;17(1):e78282. PMID: 40034878
20. Pritišanac E et al. Fetal hemoglobin and tissue oxygenation measured with NIRS — systematic review. Front Pediatr. 2021;9:710465. PMID: 34485197
21. Gunther JE et al. Review of optical methods for fetal monitoring in utero. J Biophotonics. 2022;15(6):e202100343. PMID: 35285153
22. Huang C et al. Maternal HDP and offspring early-onset CVD. PLoS Med. 2021;18(9):e1003805. PMID: 34582464
23. Kajantie E et al. Gestational hypertension and offspring type 2 diabetes — Helsinki Birth Cohort. Am J Obstet Gynecol. 2017;216(3):281.e1-281.e7. PMID: 27823919
24. Perak AM et al. Maternal CVH in pregnancy and offspring CVH in adolescence — HAPO Follow-Up. JAMA. 2021;325(7):658-668. PMID: 33591345
25. Sverrisson FA et al. Preeclampsia and academic performance in children — Iceland. PLoS One. 2018;13(11):e0207884. PMID: 30462738
26. Kang J et al. Validation of photoacoustic oxyhemoglobin saturation in neonatal piglets. J Appl Physiol. 2018;125(4):983-989. PMID: 29927734
27. Vintzileos AM et al. Transabdominal fetal pulse oximetry with NIRS. Am J Obstet Gynecol. 2005;192(1):129-33. PMID: 15672014
28. Aldrich CJ et al. Fetal cerebral oxygenation measured by NIRS and acid-base status. Obstet Gynecol. 1994;84(5):861-6. PMID: 7936527
29. Pla L et al. Non-invasive monitoring of pH and oxygen using miniaturised sensors. J Transl Med. 2021;19(1):53. PMID: 33541374
30. Mamun AA et al. HDP and offspring BP at age 21. J Hum Hypertens. 2012;26(5):288-94. PMID: 21509041

---

*This document forms a bridge between the theoretical alignment model and its empirical test. The technology review demonstrates that while continuous fetal oxygenation monitoring is not yet possible, the components are converging. The study design provides a concrete protocol to test the alignment model's central prediction with currently available clinical tools — no future technology required.*
