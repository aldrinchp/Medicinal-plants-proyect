
CREATE TABLE PLANTS (
                ID_PLANT_PK INTEGER NOT NULL,
                CURRENT_NAME VARCHAR(100) NOT NULL,
                SCIENTIFIC_NAME VARCHAR(100) NOT NULL,
                CONSTRAINT ID_PLANT_PK PRIMARY KEY (ID_PLANT_PK)
);


CREATE TABLE LOCATIONS (
                ID_LOCATION_PK INTEGER NOT NULL,
                CITY_NAME VARCHAR(100) NOT NULL,
                PROVINCE_NAME VARCHAR(100) NOT NULL,
                CONSTRAINT ID_LOCATION_PK PRIMARY KEY (ID_LOCATION_PK)
);


CREATE TABLE PLANTS_LOCATIONS (
                ID_PLANT_PK INTEGER NOT NULL,
                ID_LOCATION_PK INTEGER NOT NULL,
                CONSTRAINT PK_PLANTS_LOCATION PRIMARY KEY (ID_PLANT_PK, ID_LOCATION_PK)
);


CREATE TABLE TOPONIMOS (
                ID_TOPONIMO_PK INTEGER NOT NULL,
                ID_PLANT_PK INTEGER NOT NULL,
                ID_LOCATION_PK INTEGER NOT NULL,
                ORIGIN VARCHAR,
                COMMERCIAL_DISTRIBUTION VARCHAR(400),
                DISTRIBUTION VARCHAR(400),
                CONSTRAINT ID_TOPONIMO_PK PRIMARY KEY (ID_TOPONIMO_PK, ID_PLANT_PK, ID_LOCATION_PK)
);


CREATE TABLE INTERVIEW_CUSTOMERS (
                ID_INTERVIEWS_CUSTOMER_PK INTEGER NOT NULL,
                ID_LOCATION_PK INTEGER NOT NULL,
                LINK VARCHAR(500) NOT NULL,
                Q1 VARCHAR(255),
                Q2 VARCHAR(255),
                Q3 VARCHAR(255),
                Q4 VARCHAR(255),
                Q5 VARCHAR(255),
                Q6 VARCHAR(255),
                Q7 VARCHAR(255),
                Q8 VARCHAR(255),
                Q9 VARCHAR(255),
                Q10 VARCHAR(255),
                Q11 VARCHAR(255),
                Q12 VARCHAR(255),
                Q13 VARCHAR(255),
                Q14 VARCHAR(255),
                Q15 VARCHAR(255),
                Q16 VARCHAR(255),
                Q17 VARCHAR(255),
                Q18 VARCHAR(255),
                Q19 VARCHAR(255),
                Q20 VARCHAR(255),
                Q21 VARCHAR(255),
                Q22 VARCHAR(255),
                Q23 VARCHAR(255),
                Q24 VARCHAR(255),
                CONSTRAINT ID_INTERVIEWS_CUSTOMER_PK PRIMARY KEY (ID_INTERVIEWS_CUSTOMER_PK, ID_LOCATION_PK)
);


CREATE TABLE INTERVIEW_VENDORS (
                ID_INTERVIEWS_VENDOR_PK INTEGER NOT NULL,
                ID_LOCATION_PK INTEGER NOT NULL,
                LINK VARCHAR(500) NOT NULL,
                Q1 VARCHAR(255),
                Q2 VARCHAR(255),
                Q3 VARCHAR(255),
                Q4 VARCHAR(255),
                Q5 VARCHAR(255),
                Q6 VARCHAR(255),
                Q7 VARCHAR(255),
                Q8 VARCHAR(255),
                Q9 VARCHAR(255),
                Q10 VARCHAR(255),
                Q11 VARCHAR(255),
                Q12 VARCHAR(255),
                Q13 VARCHAR(255),
                Q14 VARCHAR(255),
                Q15 VARCHAR(255),
                Q16 VARCHAR(255),
                Q17 VARCHAR(255),
                Q18 VARCHAR(255),
                Q19 VARCHAR(255),
                Q20 VARCHAR(255),
                Q21 VARCHAR(255),
                Q22 VARCHAR(255),
                Q23 VARCHAR(255),
                CONSTRAINT ID_INTERVIEWS_VENDOR_PK PRIMARY KEY (ID_INTERVIEWS_VENDOR_PK, ID_LOCATION_PK)
);


CREATE TABLE USES (
                ID_USE_PK INTEGER NOT NULL,
                ID_PLANT_PK INTEGER NOT NULL,
                ID_LOCATION_PK INTEGER NOT NULL,
                DESCRIPTION VARCHAR NOT NULL,
                TYPE_USE VARCHAR(200) NOT NULL,
                CONSTRAINT ID_USE_PK PRIMARY KEY (ID_USE_PK, ID_PLANT_PK, ID_LOCATION_PK)
);


CREATE TABLE PREVIOUS_RESEARCHS (
                ID_RESEARCH_PK INTEGER NOT NULL,
                ID_PLANT_PK INTEGER NOT NULL,
                ID_LOCATION_PK INTEGER NOT NULL,
                TITLE VARCHAR(255) NOT NULL,
                LINK VARCHAR,
                CONSTRAINT ID_RESEARCH_PK PRIMARY KEY (ID_RESEARCH_PK, ID_PLANT_PK, ID_LOCATION_PK)
);


CREATE TABLE IMAGES (
                ID_IMAGE_PK INTEGER NOT NULL,
                ID_PLANT_PK INTEGER NOT NULL,
                ID_LOCATION_PK INTEGER NOT NULL,
                LINK VARCHAR NOT NULL,
                DATE DATE NOT NULL,
                PLACE VARCHAR(100) NOT NULL,
                CONSTRAINT ID_IMAGE_PK PRIMARY KEY (ID_IMAGE_PK, ID_PLANT_PK, ID_LOCATION_PK)
);


ALTER TABLE PLANTS_LOCATIONS ADD CONSTRAINT PLANTS_PLANTS_LOCATION_fk
FOREIGN KEY (ID_PLANT_PK)
REFERENCES PLANTS (ID_PLANT_PK)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE INTERVIEW_CUSTOMERS ADD CONSTRAINT LOCATION_INTERVIEW_CUSTOMERS_fk
FOREIGN KEY (ID_LOCATION_PK)
REFERENCES LOCATIONS (ID_LOCATION_PK)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE INTERVIEW_VENDORS ADD CONSTRAINT LOCATION_INTERVIEW_VENDORS_fk
FOREIGN KEY (ID_LOCATION_PK)
REFERENCES LOCATIONS (ID_LOCATION_PK)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE PLANTS_LOCATIONS ADD CONSTRAINT LOCATION_PLANTS_LOCATION_fk
FOREIGN KEY (ID_LOCATION_PK)
REFERENCES LOCATIONS (ID_LOCATION_PK)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE IMAGES ADD CONSTRAINT PLANTS_LOCATION_IMAGE_fk
FOREIGN KEY (ID_PLANT_PK, ID_LOCATION_PK)
REFERENCES PLANTS_LOCATIONS (ID_PLANT_PK, ID_LOCATION_PK)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE PREVIOUS_RESEARCHS ADD CONSTRAINT PLANTS_LOCATION_PREVIOUS_RESEARCHS_fk
FOREIGN KEY (ID_PLANT_PK, ID_LOCATION_PK)
REFERENCES PLANTS_LOCATIONS (ID_PLANT_PK, ID_LOCATION_PK)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE USES ADD CONSTRAINT PLANTS_LOCATION_USE_fk
FOREIGN KEY (ID_PLANT_PK, ID_LOCATION_PK)
REFERENCES PLANTS_LOCATIONS (ID_PLANT_PK, ID_LOCATION_PK)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE TOPONIMOS ADD CONSTRAINT PLANTS_LOCATION_TOPONIMO_fk
FOREIGN KEY (ID_PLANT_PK, ID_LOCATION_PK)
REFERENCES PLANTS_LOCATIONS (ID_PLANT_PK, ID_LOCATION_PK)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;