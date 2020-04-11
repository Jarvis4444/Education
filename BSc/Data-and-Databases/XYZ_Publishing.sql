--CREATE SCRIPTS
CREATE TABLE institution_tbl (
    institution_id varchar(4) NOT NULL PRIMARY KEY,
    institution_name varchar(255) NOT NULL
);
commit;

CREATE TABLE academic_tbl (
    academic_id varchar(4) NOT NULL PRIMARY KEY,
    academic_name varchar(255) NOT NULL
);
commit;

CREATE TABLE article_tbl (
    article_name varchar(255) NOT NULL,
    article_id varchar(255) NOT NULL PRIMARY KEY,
	submission_date DATE,
	total_pages int CHECK (total_pages > 0)
);
commit;

CREATE TABLE authoring_tbl (
    fk_academic_id REFERENCES academic_tbl(academic_id),
    fk_article_id REFERENCES article_tbl(article_id),
	PRIMARY KEY (fk_academic_id, fk_article_id)
);
commit;

CREATE TABLE review_tbl (
    fk_academic_id REFERENCES academic_tbl(academic_id),
	fk_article_id REFERENCES article_tbl(article_id),
    review_date DATE,
	PRIMARY KEY (fk_academic_id, fk_article_id)
);
commit;

CREATE TABLE affiliation_tbl (
	fk_academic_id REFERENCES academic_tbl(academic_id),
	fk_institution_id REFERENCES institution_tbl(institution_id),
	start_date Date,
	PRIMARY KEY (fk_academic_id, fk_institution_id)
);
commit;

--INSERT SCRIPTS
/* institution_tbl */
INSERT INTO institution_tbl(institution_id, institution_name)
	VALUES ('BU01', 'Bournemouth University');
INSERT INTO institution_tbl(institution_id, institution_name)
	VALUES ('SU01', 'Southampton University');
INSERT INTO institution_tbl(institution_id, institution_name)
	VALUES ('PU01', 'Portsmouth University');
commit;

/* academic_tbl */
INSERT INTO academic_tbl(academic_id, academic_name)
	VALUES ('PJ01', 'Paul-David Jarvis');
INSERT INTO academic_tbl(academic_id, academic_name)
	VALUES ('MS01', 'Mantas Sasnauskas');
INSERT INTO academic_tbl(academic_id, academic_name)
	VALUES ('VA01', 'Vlad Apopei');
INSERT INTO academic_tbl(academic_id, academic_name)
	VALUES ('CS01', 'Charlie Wordley Stewart');
commit;

/* article_tbl */
INSERT INTO article_tbl(article_name, article_id, submission_date, total_pages)
	VALUES ('Data sets and data quality in software engineering: Eight years on.', 'dsdq2016',  TO_DATE('19/07/2016', 'dd/mm/yyyy'), 182);
INSERT INTO article_tbl(article_name, article_id, submission_date, total_pages)
	VALUES ('Culturally-Aware Motivation for Smart Services: An Exploratory Study of the UAE', 'cms2016', TO_DATE('19/07/2018', 'dd/mm/yyyy'), 119);
INSERT INTO article_tbl(article_name, article_id, submission_date, total_pages)
	VALUES ('Filtering, robust filtering, polishing: Techniques for addressing quality in software data', 'frp2007', TO_DATE('31/12/2007', 'dd/mm/yyyy'), 106);
INSERT INTO article_tbl(article_name, article_id, submission_date, total_pages)
	VALUES ('Software Productivity Analysis of a Large Data Set and Issues of Confidentiality and Data Quality.', 'spa2005', TO_DATE('06/12/2006', 'dd/mm/yyyy'), 182);
INSERT INTO article_tbl(article_name, article_id, submission_date, total_pages)
	VALUES ('Assessing the Quality and Cleaning of a Software Project Data Set: An Experience Report.', 'aqcs2006', TO_DATE('06/05/2012', 'dd/mm/yyyy'), 126);
commit;

/* aurthoring_tbl */
INSERT INTO authoring_tbl(fk_academic_id, fk_article_id)
	VALUES ('PJ01', 'dsdq2016');
INSERT INTO authoring_tbl(fk_academic_id, fk_article_id)
	VALUES ('PJ01', 'aqcs2006');
INSERT INTO authoring_tbl(fk_academic_id, fk_article_id)
	VALUES ('MS01', 'cms2016');
INSERT INTO authoring_tbl(fk_academic_id, fk_article_id)
	VALUES ('VA01', 'frp2007');
INSERT INTO authoring_tbl(fk_academic_id, fk_article_id)
	VALUES ('CS01', 'spa2005');
commit;

/* review_tbl */
INSERT INTO review_tbl(fk_academic_id, fk_article_id, review_date)
	VALUES ('PJ01', 'dsdq2016', TO_DATE('18/12/2017', 'dd/mm/yyyy'));
INSERT INTO review_tbl(fk_academic_id, fk_article_id, review_date)
	VALUES ('PJ01', 'frp2007', TO_DATE('15/07/2008', 'dd/mm/yyyy'));
INSERT INTO review_tbl(fk_academic_id, fk_article_id, review_date)
	VALUES ('VA01', 'cms2016', TO_DATE('25/08/2017', 'dd/mm/yyyy'));
INSERT INTO review_tbl(fk_academic_id, fk_article_id, review_date)
	VALUES ('MS01', 'frp2007', TO_DATE('18/04/2008', 'dd/mm/yyyy'));
INSERT INTO review_tbl(fk_academic_id, fk_article_id, review_date)
	VALUES ('CS01', 'aqcs2006', TO_DATE('06/05/2012', 'dd/mm/yyyy'));
INSERT INTO review_tbl(fk_academic_id, fk_article_id, review_date)
	VALUES ('PJ01', 'spa2005', TO_DATE('15/08/2013', 'dd/mm/yyyy'));
INSERT INTO review_tbl(fk_academic_id, fk_article_id, review_date)
	VALUES ('CS01', 'frp2007', TO_DATE('15/12/2008', 'dd/mm/yyyy'));
commit;

/* affiliation_tbl */
INSERT INTO affiliation_tbl(fk_academic_id, fk_institution_id, start_date)
	VALUES ('PJ01', 'BU01', TO_DATE('19/05/2018', 'dd/mm/yyyy'));
INSERT INTO affiliation_tbl(fk_academic_id, fk_institution_id, start_date)
	VALUES ('CS01', 'BU01', TO_DATE('01/04/2013', 'dd/mm/yyyy'));
INSERT INTO affiliation_tbl(fk_academic_id, fk_institution_id, start_date)
	VALUES ('CS01', 'PU01', TO_DATE('09/05/2018', 'dd/mm/yyyy'));
INSERT INTO affiliation_tbl(fk_academic_id, fk_institution_id, start_date)
	VALUES ('MS01', 'SU01', TO_DATE('09/05/2018', 'dd/mm/yyyy'));
commit;

--DROP SCRIPT
DROP TABLE authoring_tbl;
DROP TABLE review_tbl;
DROP TABLE affiliation_tbl;
DROP TABLE institution_tbl;
DROP TABLE academic_tbl;
DROP TABLE article_tbl;
commit;

--SELECT SCRIPT
/* Required Report 1 */
SELECT academic_id, academic_name
	FROM academic_tbl;

/* Required Report 2 */
SELECT academic_tbl.academic_name, institution_tbl.institution_name
	FROM academic_tbl, institution_tbl, affiliation_tbl
	WHERE affiliation_tbl.fk_institution_id = institution_tbl.institution_id 
		and affiliation_tbl.fk_academic_id = academic_tbl.academic_id 
		and institution_tbl.institution_id = 'BU01';

/* Required Report 3 */
SELECT institution_tbl.institution_name, COUNT(affiliation_tbl.fk_academic_id) AS number_of_academics
	FROM affiliation_tbl
		LEFT JOIN institution_tbl ON affiliation_tbl.fk_institution_id = institution_tbl.institution_id
		group by institution_tbl.institution_name

/* Required Report 4 */
SELECT academic_tbl.academic_name, institution_tbl.institution_name, review_count
    FROM institution_tbl institution_tbl, academic_tbl academic_tbl, affiliation_tbl,
		(SELECT academic_tbl.academic_id, COUNT(review_tbl.fk_article_id) as review_count FROM academic_tbl, review_tbl
			WHERE review_tbl.fk_academic_id = academic_tbl.academic_id
			GROUP BY academic_tbl.academic_id
			ORDER BY review_count) review_count_tbl

			WHERE institution_tbl.institution_id = affiliation_tbl.fk_institution_id	
			AND academic_tbl.academic_id = affiliation_tbl.fk_academic_id
			AND academic_tbl.academic_id = review_count_tbl.academic_id
			AND review_count = (SELECT MAX(review_count) 
			FROM(SELECT academic_tbl.academic_id, COUNT(review_tbl.fk_article_id) as review_count
				FROM academic_tbl academic_tbl, review_tbl review_tbl
				WHERE review_tbl.fk_academic_id = academic_tbl.academic_id
				GROUP BY academic_tbl.academic_id
				ORDER BY review_count)
);