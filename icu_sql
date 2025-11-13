CREATE OR REPLACE TABLE 
  model_data.icu_survivors AS
WITH drg_first AS (
  SELECT 
    hadm_id,
    drg_severity,
    drg_mortality,
    ROW_NUMBER() OVER (PARTITION BY hadm_id ORDER BY drg_code) AS rn
  FROM `physionet-data.mimiciv_3_1_hosp.drgcodes`
),
prior_icu_info AS (
  SELECT
    ie.subject_id,
    ie.intime as current_intime,
    COUNT(DISTINCT ie_prior.stay_id) as prior_icu_admits_last_year,
    MAX(ie_prior.outtime) as last_icu_outtime
  FROM
    `physionet-data.mimiciv_3_1_icu.icustays` ie
  LEFT JOIN
    `physionet-data.mimiciv_3_1_icu.icustays` ie_prior
    ON ie.subject_id = ie_prior.subject_id
    AND ie_prior.intime < ie.intime
    AND DATETIME_DIFF(ie.intime, ie_prior.intime, DAY) <= 365
  GROUP BY
    ie.subject_id, ie.intime
),
procedure_counts AS (
  SELECT
    hadm_id,
    COUNT(DISTINCT icd_code) as num_icd_procedures,
    COUNT(DISTINCT icd_code) as num_unique_procedure_codes
  FROM
    `physionet-data.mimiciv_3_1_hosp.procedures_icd`
  GROUP BY
    hadm_id
),
diagnosis_counts AS (
  SELECT
    hadm_id,
    COUNT(*) as num_diagnoses,
    COUNT(DISTINCT icd_code) as num_unique_icd_codes,
    MAX(seq_num) as max_diagnosis_seq
  FROM
    `physionet-data.mimiciv_3_1_hosp.diagnoses_icd`
  GROUP BY
    hadm_id
),
lab_aggregates AS (
  SELECT
    hadm_id,
    COUNT(DISTINCT itemid) AS num_lab_items,
    COUNT(*) AS total_lab_events,
    COUNT(DISTINCT specimen_id) AS num_specimens
  FROM
    `physionet-data.mimiciv_3_1_hosp.labevents`
  GROUP BY
    hadm_id
),
microbiology_aggregates AS (
  SELECT
    hadm_id,
    COUNT(*) AS num_micro_tests,
    COUNT(DISTINCT test_itemid) AS num_unique_micro_tests,
    COUNT(DISTINCT org_itemid) AS num_organisms_identified,
    CASE WHEN COUNT(DISTINCT org_itemid) > 0 THEN 1 ELSE 0 END AS has_infection
  FROM
    `physionet-data.mimiciv_3_1_hosp.microbiologyevents`
  GROUP BY
    hadm_id
),
medication_aggregates AS (
  SELECT
    hadm_id,
    COUNT(DISTINCT pharmacy_id) AS num_pharmacy_items,
    COUNT(*) AS total_med_administrations
  FROM
    `physionet-data.mimiciv_3_1_hosp.emar`
  GROUP BY
    hadm_id
),
comorbidities AS (
  SELECT
    hadm_id,
    MAX(CASE WHEN icd_code LIKE 'I50%' OR icd_code LIKE '428%' THEN 1 ELSE 0 END) as chf,
    MAX(CASE WHEN icd_code LIKE 'I25%' OR icd_code LIKE '414%' THEN 1 ELSE 0 END) as cad,
    MAX(CASE WHEN icd_code LIKE 'E11%' OR icd_code LIKE '250%' THEN 1 ELSE 0 END) as diabetes,
    MAX(CASE WHEN icd_code LIKE 'J44%' OR icd_code LIKE '496%' THEN 1 ELSE 0 END) as copd,
    MAX(CASE WHEN icd_code LIKE 'N18%' OR icd_code LIKE '585%' THEN 1 ELSE 0 END) as ckd,
    MAX(CASE WHEN icd_code LIKE 'I48%' OR icd_code LIKE '4273%' THEN 1 ELSE 0 END) as afib,
    MAX(CASE WHEN icd_code LIKE 'C%' OR icd_code LIKE '1%' OR icd_code LIKE '2%' THEN 1 ELSE 0 END) as cancer
  FROM
    `physionet-data.mimiciv_3_1_hosp.diagnoses_icd`
  GROUP BY
    hadm_id
),
icu_with_next AS (
  SELECT 
    ie.subject_id,
    ie.hadm_id,
    ie.stay_id,
    ie.intime,
    ie.outtime,
    ie.los as length_of_stay,
    a.admittime,
    a.dischtime,
    a.discharge_location,
    a.admission_type,
    a.admission_location,
    p.anchor_age,
    p.anchor_year,
    p.gender,
    d.drg_severity,
    d.drg_mortality,
    (p.anchor_year - p.anchor_age) AS birth_year,
    (EXTRACT(YEAR FROM a.admittime) - (p.anchor_year - p.anchor_age)) AS age,
    DATETIME_DIFF(a.dischtime, a.admittime, DAY) as hospital_days,
    COALESCE(pic.prior_icu_admits_last_year, 0) as prior_icu_admits_last_year,
    COALESCE(DATETIME_DIFF(ie.intime, pic.last_icu_outtime, DAY), 999) as days_since_last_icu,
    
    -- Original procedure and diagnosis counts
    COALESCE(pc.num_icd_procedures, 0) as num_procedures,
    COALESCE(dc.num_diagnoses, 0) as num_diagnoses,
    
    -- NEW: Additional lab, micro, and medication features
    COALESCE(la.num_lab_items, 0) as num_lab_items,
    COALESCE(la.total_lab_events, 0) as total_lab_events,
    COALESCE(la.num_specimens, 0) as num_specimens,
    COALESCE(pc.num_icd_procedures, 0) as num_icd_procedures,
    COALESCE(pc.num_unique_procedure_codes, 0) as num_unique_procedure_codes,
    COALESCE(dc.num_unique_icd_codes, 0) as num_unique_icd_codes,
    COALESCE(dc.max_diagnosis_seq, 0) as max_diagnosis_seq,
    COALESCE(mb.num_micro_tests, 0) as num_micro_tests,
    COALESCE(mb.num_unique_micro_tests, 0) as num_unique_micro_tests,
    COALESCE(mb.num_organisms_identified, 0) as num_organisms_identified,
    COALESCE(mb.has_infection, 0) as has_infection,
    COALESCE(med.num_pharmacy_items, 0) as num_pharmacy_items,
    COALESCE(med.total_med_administrations, 0) as total_med_administrations,
    
    -- Comorbidities
    COALESCE(cm.chf, 0) as chf,
    COALESCE(cm.cad, 0) as cad,
    COALESCE(cm.diabetes, 0) as diabetes,
    COALESCE(cm.copd, 0) as copd,
    COALESCE(cm.ckd, 0) as ckd,
    COALESCE(cm.afib, 0) as afib,
    COALESCE(cm.cancer, 0) as cancer,
    
    CASE 
      WHEN ie.los < 1 THEN 0
      WHEN ie.los < 3 THEN 1
      WHEN ie.los < 7 THEN 2
      ELSE 3
    END AS los_category,
    LEAD(ie.intime) OVER (PARTITION BY ie.subject_id ORDER BY ie.intime) AS next_icu_intime
  FROM 
    `physionet-data.mimiciv_3_1_icu.icustays` ie
  INNER JOIN 
    `physionet-data.mimiciv_3_1_hosp.admissions` a
    ON ie.hadm_id = a.hadm_id
  INNER JOIN 
    `physionet-data.mimiciv_3_1_hosp.patients` p
    ON ie.subject_id = p.subject_id
  LEFT JOIN
    drg_first d
    ON ie.hadm_id = d.hadm_id AND d.rn = 1
  LEFT JOIN
    prior_icu_info pic
    ON ie.subject_id = pic.subject_id AND ie.intime = pic.current_intime
  LEFT JOIN
    procedure_counts pc
    ON ie.hadm_id = pc.hadm_id
  LEFT JOIN
    diagnosis_counts dc
    ON ie.hadm_id = dc.hadm_id
  LEFT JOIN
    lab_aggregates la
    ON ie.hadm_id = la.hadm_id
  LEFT JOIN
    microbiology_aggregates mb
    ON ie.hadm_id = mb.hadm_id
  LEFT JOIN
    medication_aggregates med
    ON ie.hadm_id = med.hadm_id
  LEFT JOIN
    comorbidities cm
    ON ie.hadm_id = cm.hadm_id
  WHERE 
    a.hospital_expire_flag = 0
)
SELECT
  *,
  CASE 
    WHEN DATETIME_DIFF(next_icu_intime, outtime, DAY) <= 30
         AND DATETIME_DIFF(next_icu_intime, outtime, DAY) >= 1
    THEN 1
    ELSE 0
  END AS readmitted_30day
FROM icu_with_next;
