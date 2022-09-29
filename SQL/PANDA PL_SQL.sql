/*1.1*/
SET SERVEROUTPUT ON 
DECLARE 
V_FIO VARCHAR2(100); 
BEGIN 
SELECT FULL_NAME 
INTO V_FIO 
FROM SELLERS 
WHERE ID=106; 
DBMS_OUTPUT.PUT_LINE('������� ��������: '||V_FIO); 
EXCEPTION 
WHEN OTHERS THEN 
DBMS_OUTPUT.PUT_LINE('��������� ������!'); 
END; 
/                                                                      /*1.1.1*/

CREATE OR REPLACE FUNCTION GOOD_JOB RETURN VARCHAR2 
IS STR VARCHAR2(10 CHAR); 
BEGIN 
STR:='� �������!'; 
RETURN STR;
END; 
/

SET SERVEROUTPUT ON 
DECLARE 
S VARCHAR2(10 CHAR); 
BEGIN 
DBMS_OUTPUT.PUT_LINE(GOOD_JOB()); 
END; 
/                                                               /*1.1.2*/

DECLARE 
A SELLERS.ID%TYPE:=NULL; 
BEGIN 
IF A IS NULL THEN 
DBMS_OUTPUT.PUT_LINE('IT''S NULL!'); 
ELSE 
DBMS_OUTPUT.PUT_LINE('IT''S NOT NULL'); 
END IF; 
END;                                                                         
/                                                     /*1.1.3*/

DECLARE
TYPE ABC IS RECORD (ID NUMBER NOT NULL DEFAULT 100, FULL_NAME VARCHAR2(20 CHAR), DESCRIPTION VARCHAR2(50 CHAR));
V_STROKA ABC;
BEGIN
V_STROKA.ID:=101;
V_STROKA.FULL_NAME:='NAME';
V_STROKA.DESCRIPTION:='FOX';
DBMS_OUTPUT.PUT_LINE(V_STROKA.ID||' '||V_STROKA.FULL_NAME||' '||V_STROKA.DESCRIPTION);
END;    
/                                                                                           /*1.1.4*/

VARIABLE B NUMBER; 
BEGIN 
:B:=2; 
DBMS_OUTPUT.PUT_LINE(:B); 
:B:=:B+2; 
DBMS_OUTPUT.PUT_LINE(:B);
END; 
/ 
PRINT B;                                                                                /*1.1.6*/

/*2.1*/
SET SERVEROUTPUT ON 
VARIABLE TIME VARCHAR2(80 CHAR);
BEGIN
:TIME:=TO_CHAR(TRUNC(SYSDATE),'DD.MM.YYYY HH24:MI:SS');
END;
/
PRINT TIME;                                                         /*2.1.1*/

SET SERVEROUTPUT ON 
DECLARE
S NUMBER;
V NUMBER;
BEGIN
SELECT SUM(TOTAL_SUM) INTO S FROM ORDERS;
V:=SUM(TOTAL_SUM);
DBMS_OUTPUT.PUT_LINE(S);
END;
/                                                                  /*2.1.2*/

SET SERVEROUTPUT ON 
DECLARE
S VARCHAR2(300 CHAR);
V VARCHAR2(300 CHAR);
BEGIN
SELECT P.DESCRIPTION,S.FULL_NAME INTO S,V FROM 
PRODUCTS P INNER JOIN ORDERS O ON O.PRODUCT_CODE=P.CODE AND O.PRODUCT_MANUFACTURER=P.MANUFACTURER INNER JOIN SELLERS S ON O.SELLER_ID=S.ID
WHERE O.REF_NUMBER=(SELECT REF_NUMBER FROM (SELECT ORDER_DATE, REF_NUMBER FROM ORDERS ORDER BY ORDER_DATE DESC) WHERE ROWNUM=1);
DBMS_OUTPUT.PUT_LINE(V||' ������� '||S);
END;
/
SELECT ORDER_DATE FROM 
(SELECT ORDER_DATE, REF_NUMBER FROM ORDERS 
ORDER BY ORDER_DATE DESC, REF_NUMBER DESC) 
WHERE ROWNUM=1;                                                   /*2.1.3*/

DECLARE
S NUMBER;
C NUMBER;
V VARCHAR2(300 CHAR);
BEGIN
S:=110;
SELECT SELLER_ID INTO C FROM SELLERS WHERE ID=S;
IF C IS NULL THEN DBMS_OUTPUT.PUT_LINE('������������ �� ����������.');
ELSE
SELECT FULL_NAME INTO V FROM SELLERS WHERE ID=C;
DBMS_OUTPUT.PUT_LINE(V);
END IF;
END;
/                                                                    /*2.1.4*/


/
DECLARE
�_��� VARCHAR2(50);
MAXEM NUMBER(2);
MA ORDERS.PRODUCT_MANUFACTURER%TYPE;
MAXE ORDERS.PRODUCT_CODE%TYPE;
BEGIN
SELECT MAX(CH), PRODUCT_MANUFACTURER, PRODUCT_CODE INTO MAXEM, MA, MAXE 
FROM (SELECT COUNT(*) CH, PRODUCT_MANUFACTURER, PRODUCT_CODE FROM ORDERS GROUP BY PRODUCT_CODE, PRODUCT_MANUFACTURER) 
GROUP BY PRODUCT_MANUFACTURER, PRODUCT_CODE HAVING MAX(CH) = 3;
UPDATE PRODUCTS SET LIMIT = LIMIT * 1.1 WHERE MANUFACTURER = MA AND CODE = MAXE;
END;
/
SELECT COUNT(*) CH, PRODUCT_MANUFACTURER, PRODUCT_CODE FROM ORDERS GROUP BY PRODUCT_CODE, PRODUCT_MANUFACTURER;         /*2.1.5*/

BEGIN
DELETE FROM ORDERS WHERE SELLER_ID=103;
DBMS_OUTPUT.PUT_LINE(' ������� '||SQL%ROWCOUNT||' ������� ');
END;
/
ROLLBACK;                                                                               /*2.1.8*/

/*3.1*/
SET SERVEROUTPUT ON
DECLARE
S NUMBER;
BEGIN
SELECT NVL(SUM(TOTAL_SUM),0) INTO S FROM ORDERS WHERE CLIENT_ID=2112 AND TO_CHAR(TRUNC(ORDER_DATE,'MM'))=TO_CHAR(TRUNC(TO_DATE('02.12.12','DD.MM.YY'),'MM'));
IF S>=10000 THEN DBMS_OUTPUT.PUT_LINE('������ �������� "���������"');
ELSIF S<10000 THEN DBMS_OUTPUT.PUT_LINE('������ �� �������� "���������"');
ELSE DBMS_OUTPUT.PUT_LINE('������� �� ����');
END IF;
END;
/  
/*3.1.1*/
CREATE TABLE TAB(DAATAA DATE,CIFRA NUMBER);

SET SERVEROUTPUT ON
DECLARE
D DATE;
N NUMBER;
BEGIN
N:=0;
D:=TO_DATE('01.01.10','DD.MM.YYYY');
LOOP
SELECT NVL(SUM(TOTAL_SUM),0) INTO N FROM ORDERS WHERE TO_CHAR(ORDER_DATE)=TO_CHAR(D);
INSERT INTO TAB VALUES (D,N);
D:=D+1;
N:=0;
EXIT WHEN (D=TO_DATE('01.02.10','DD.MM.YYYY'));
END LOOP;
END;
/
SELECT * FROM TAB;                                                                  /*3.1.2*/

DECLARE
CURSOR F IS 
SELECT DESCRIPTION FROM PRODUCTS; 
BEGIN 
FOR N IN F LOOP 
DBMS_OUTPUT.PUT_LINE(N.DESCRIPTION); 
END LOOP; 
END;
/                                                                                   /*3.1.3*/

ALTER TABLE SELLERS ADD SEX VARCHAR2(4 CHAR);

DECLARE
CURSOR F IS 
SELECT ID FROM SELLERS; 
N NUMBER;
MAN NUMBER;
WOMAN NUMBER;
MX NUMBER;
BEGIN
FOR N IN F LOOP 
UPDATE SELLERS SET SEX='���.' WHERE ID=N.ID AND FULL_NAME LIKE '%�';
UPDATE SELLERS SET SEX='���.' WHERE ID=N.ID AND FULL_NAME NOT LIKE '%�';
END LOOP;
END;
/                                                                   /*3.1.4*/


/*4.1*/
CREATE TABLE TABLL (F1 NUMBER, F2 NUMBER);
CREATE OR REPLACE PROCEDURE RANDOMM_NUMBER
IS N NUMBER;
BEGIN
N:=1;
LOOP
INSERT INTO TABLL VALUES (DBMS_RANDOM.VALUE(1,100),DBMS_RANDOM.VALUE(1,100));
N:=N+1;
EXIT WHEN (N>10);
END LOOP;
END RANDOMM_NUMBER;
/
BEGIN
RANDOMM_NUMBER;
END;
/
SELECT * FROM TABLL;                                                 /*4.1.2*/


CREATE OR REPLACE FUNCTION SEX RETURN VARCHAR2 IS
F VARCHAR2(1);
BEGIN
SELECT SUBSTR(SUBSTR(FULL_NAME,1,INSTR(FULL_NAME,' ',1,1)-1),-1,1) INTO F FROM SELLERS;
IF F = '�' OR F = '�' OR F = '�' OR F = '�' THEN RETURN 'M';
ELSE RETURN '�';
END IF;
END;
/
SELECT* FROM SELLERS WHERE SEX = '�' ;
/                                                                /*4.1.3*/

CREATE OR REPLACE PACKAGE PAKETIK IS
FUNCTION RETURN_SYSDATE RETURN DATE;
PROCEDURE MODIFY_SYSDATE (D2 IN DATE);
D DATE;
END PAKETIK;
/
CREATE OR REPLACE PACKAGE BODY PAKETIK IS
FUNCTION RETURN_SYSDATE RETURN DATE
IS
BEGIN
RETURN D;
END RETURN_SYSDATE;

PROCEDURE MODIFY_SYSDATE (D2 IN DATE)
IS
BEGIN
D:=D2;
END MODIFY_SYSDATE;
END PAKETIK;
/
BEGIN
DBMS_OUTPUT.PUT_LINE(PAKETIK.RETURN_SYSDATE());
PAKETIK.MODIFY_SYSDATE(TO_DATE('24.01.12','DD.MM.YY'));
DBMS_OUTPUT.PUT_LINE(PAKETIK.RETURN_SYSDATE());
END;
/                                                                   /*4.1.4*/

DROP TABLE IZMENENIYA;
DROP TRIGGER DELET;
DROP TRIGGER INSER;
DROP TRIGGER UPDAT;
CREATE TABLE IZMENENIYA(DATAA DATE, POLZOVATEL VARCHAR(15), HAR_IZM VARCHAR(15));
/
CREATE  OR replace TRIGGER DELET BEFORE DELETE ON ORDERS FOR EACH ROW
BEGIN
INSERT INTO IZMENENIYA values(SYSDATE,USER, 'DELETE');
END;
/
CREATE OR replace TRIGGER INSER BEFORE INSERT ON ORDERS FOR EACH ROW
BEGIN
IF :NEW.ORDER_DATE = SYSDATE THEN
INSERT INTO IZMENENIYA VALUES(SYSDATE,USER,'INSERT');
ELSE
RAISE_APPLICATION_ERROR(-20022,'ERROR');
END IF;
END;
/
CREATE OR replace TRIGGER UPDAT BEFORE UPDATE ON ORDERS FOR EACH ROW
BEGIN
IF :NEW.ORDER_DATE = SYSDATE THEN
INSERT INTO IZMENENIYA VALUES(SYSDATE,USER,'UPDATE');
ELSE
RAISE_APPLICATION_ERROR(-20002,'ERROR');
END IF;
END;
/
INSERT INTO ORDERS VALUES(111111, '13.01.2020', 14, 11111, 2111, 'MFB',	'P04', 103);                    /*4.1.5*/


/*5.1*/
CREATE OR REPLACE PROCEDURE FU IS
CURSOR DS IS
SELECT ID,RESULT FROM SELLERS WHERE RESULT!=(SELECT SUM(TOTAL_SUM) FROM ORDERS WHERE SELLER_ID=SELLERS.ID);
N NUMBER;    
BEGIN
FOR S IN DS LOOP
SELECT SUM(TOTAL_SUM) INTO N FROM ORDERS WHERE SELLER_ID=S.ID;
UPDATE SELLERS SET RESULT = N WHERE ID=S.ID;
END LOOP;
END;
/
DECLARE
CURSOR DS IS
SELECT ID,RESULT FROM SELLERS WHERE RESULT!=(SELECT SUM(TOTAL_SUM) FROM ORDERS WHERE SELLER_ID=SELLERS.ID);
N NUMBER;    
BEGIN
FOR S IN DS LOOP
SELECT SUM(TOTAL_SUM) INTO N FROM ORDERS WHERE SELLER_ID=S.ID;
UPDATE SELLERS SET RESULT = N WHERE ID=S.ID;
END LOOP;
END;
/                                                               /*5.1.1*/

ALTER TABLE PRICELIST_LINES MODIFY PRODUCT_CODE VARCHAR2(9 CHAR);
INSERT INTO PRICELIST_LINES (PRODUCT_CODE,PRODUCT_NAME,PRODUCT_PRICE) SELECT MANUFACTURER||'_'||CODE, DESCRIPTION, PRICE FROM PRODUCTS WHERE MANUFACTURER!='ZOM'; 
SET SERVEROUTPUT ON
DECLARE
CURSOR C_TOV IS
SELECT MANUFACTURER,CODE,PRICE FROM PRODUCTS WHERE PRICE<1000;
TOV C_TOV%ROWTYPE;
N NUMBER;
BEGIN
FOR M IN C_TOV LOOP
SELECT COUNT(*) INTO N FROM ORDERS WHERE PRODUCT_MANUFACTURER=TOV.MANUFACTURER AND PRODUCT_CODE=TOV.CODE;
IF N=0 THEN
UPDATE PRODUCTS SET PRICE=0.95*PRICE WHERE MANUFACTURER=TOV.MANUFACTURER AND CODE=TOV.CODE;
UPDATE PRICELIST_LINES SET PRODUCT_PRICE=0.95*PRODUCT_PRICE,PRODUCT_CODE=PRODUCT_CODE||'*' WHERE PRODUCT_CODE=TOV.MANUFACTURER||'_'||TOV.CODE;
END IF;
END LOOP;
END;
/
ROLLBACK;                                                            /*5.1.2*/

ALTER TABLE PRICELIST_LINES MODIFY PRODUCT_CODE VARCHAR2(9 CHAR);
INSERT INTO PRICELIST_LINES (PRODUCT_CODE,PRODUCT_NAME,PRODUCT_PRICE) SELECT MANUFACTURER||'_'||CODE, DESCRIPTION, PRICE FROM PRODUCTS WHERE MANUFACTURER!='ZOM'; 
SET SERVEROUTPUT ON
DECLARE
N NUMBER;
C NUMBER;
CD VARCHAR2(4 CHAR);
PR NUMBER;
BEGIN
C:=0;
FOR TOV IN (SELECT MANUFACTURER,CODE FROM PRODUCTS WHERE PRICE<1000)
LOOP
SELECT COUNT(*) INTO N FROM ORDERS WHERE PRODUCT_MANUFACTURER=TOV.MANUFACTURER AND PRODUCT_CODE=TOV.CODE;
IF N=0 THEN
IF C<11 THEN
BEGIN
SELECT CODE,PRICE INTO CD,PR FROM PRODUCTS WHERE TOV.MANUFACTURER=MANUFACTURER AND TOV.CODE=CODE AND PRICE<1000 ORDER BY PRICE DESC;
UPDATE PRODUCTS SET PRICE=0.95*PRICE WHERE MANUFACTURER=TOV.MANUFACTURER AND CODE=CD;
UPDATE PRICELIST_LINES SET PRODUCT_PRICE=0.95*PRODUCT_PRICE,PRODUCT_CODE=PRODUCT_CODE||'*' WHERE PRODUCT_CODE=TOV.MANUFACTURER||'_'||TOV.CODE;
C:=C+1;
END;
ELSE
BEGIN
SELECT CODE,PRICE INTO CD,PR FROM PRODUCTS WHERE TOV.MANUFACTURER=MANUFACTURER AND TOV.CODE=CODE AND PRICE<1000 ORDER BY PRICE DESC;
UPDATE PRODUCTS SET PRICE=0.96*PRICE WHERE MANUFACTURER=TOV.MANUFACTURER AND CODE=CD;
UPDATE PRICELIST_LINES SET PRODUCT_PRICE=0.96*PRODUCT_PRICE,PRODUCT_CODE=PRODUCT_CODE||'*' WHERE PRODUCT_CODE=TOV.MANUFACTURER||'_'||TOV.CODE;
DBMS_OUTPUT.PUT_LINE('*');
C:=C+1;
END;
END IF;
END IF;
END LOOP;
END;
/
SHOW ERRORS;

SELECT PRODUCT_CODE FROM PRICELIST_LINES WHERE PRODUCT_CODE LIKE '%*';

SELECT * FROM PRODUCTS;
SELECT * FROM PRICELIST_LINES;
ROLLBACK;
/                                                           /*5.1.3*/


/*6.1*/
ROLLBACK;
SET SERVEROUTPUT ON
CREATE OR REPLACE PROCEDURE ADD_ORD (N NUMBER,D DATE,A NUMBER,T NUMBER,C NUMBER,M VARCHAR2,CD VARCHAR2,S NUMBER) IS
E1 NUMBER; E2 NUMBER; E3 NUMBER; E4 NUMBER; E5 NUMBER;
ERR_NUM EXCEPTION;
ERR_CL_ID EXCEPTION;
ERR_PR EXCEPTION;
ERR_S_ID EXCEPTION;
ERR_D EXCEPTION;
ERR_A EXCEPTION;
ERR_T EXCEPTION;
BEGIN
SELECT CASE WHEN EXISTS (SELECT 1 FROM ORDERS WHERE REF_NUMBER=N) THEN 0 ELSE 1 END CASE INTO E1 FROM DUAL;
IF E1=0 THEN RAISE ERR_NUM; END IF;
SELECT CASE WHEN EXISTS (SELECT 1 FROM CLIENTS WHERE ID=C) THEN 1 ELSE 0 END CASE INTO E2 FROM DUAL;
IF E2=0 THEN RAISE ERR_CL_ID; END IF;
SELECT CASE WHEN EXISTS (SELECT 1 FROM PRODUCTS WHERE MANUFACTURER=M) THEN 1 ELSE 0 END CASE INTO E3 FROM DUAL;
IF E3=0 THEN RAISE ERR_PR; END IF;
SELECT CASE WHEN EXISTS (SELECT 1 FROM SELLERS WHERE ID=S) THEN 1 ELSE 0 END CASE INTO E5 FROM DUAL;
IF E5=0 THEN RAISE ERR_S_ID; END IF;
IF D>SYSDATE THEN RAISE ERR_D; END IF;
IF A<1 THEN RAISE ERR_A; END IF;
IF T<0 THEN RAISE ERR_T; END IF;
INSERT INTO ORDERS VALUES (N,D,A,T,C,M,CD,S);
COMMIT;
EXCEPTION
WHEN ERR_NUM THEN DBMS_OUTPUT.PUT_LINE('����� ����� ������ ��� ����������');
WHEN ERR_CL_ID THEN DBMS_OUTPUT.PUT_LINE('������ ������� �� ����������');
WHEN ERR_PR THEN DBMS_OUTPUT.PUT_LINE('������ ������������� �� ����������');
WHEN ERR_S_ID THEN DBMS_OUTPUT.PUT_LINE('������ �������� �� ����������');
WHEN ERR_D THEN DBMS_OUTPUT.PUT_LINE('������������ ����');
WHEN ERR_A THEN DBMS_OUTPUT.PUT_LINE('���������� ������ ���� ������������� ������');
WHEN ERR_T THEN DBMS_OUTPUT.PUT_LINE('����� ������ ���� ������������� ������');
END ADD_ORD;
/
SHOW ERRORS;

BEGIN
ADD_ORD(2055,TO_DATE('29.12.16','DD.MM.YY'),5,22501,2113,'ZDI','PW21',139);
END;
/                                                                                 /*6.1.1*/

CREATE OR REPLACE FUNCTION RYK (S_ID NUMBER) RETURN VARCHAR2 IS
S NUMBER;
RYK_ID NUMBER;
RYKK VARCHAR2 (300 CHAR);
NO_SELLER EXCEPTION;
BEGIN
SELECT CASE WHEN EXISTS (SELECT 1 FROM SELLERS WHERE ID=S_ID) THEN 1 ELSE 0 END CASE INTO S FROM DUAL;
IF S=0 THEN RAISE NO_SELLER; END IF;
SELECT NVL(SELLER_ID,0) INTO RYK_ID FROM SELLERS WHERE ID=S_ID;
IF RYK_ID=0 THEN RYKK:='�� ����������'; ELSE
SELECT FULL_NAME INTO RYKK FROM SELLERS WHERE ID=RYK_ID;
END IF;
RETURN RYKK;
EXCEPTION
WHEN NO_SELLER THEN DBMS_OUTPUT.PUT_LINE('������������ �� ��������');
ROLLBACK;
END RYK;
/
SHOW ERRORS;

DECLARE
MN NUMBER;
MX NUMBER;
V VARCHAR2 (100 CHAR);
BEGIN
SELECT MIN(ID) INTO MN FROM SELLERS;
SELECT MAX(ID) INTO MX FROM SELLERS;
LOOP
SELECT FULL_NAME INTO V FROM SELLERS WHERE ID=MN;
DBMS_OUTPUT.PUT_LINE('� �������� '||V||' ������������ '||RYK(MN)||'.');
MN:=MN+1;
EXIT WHEN (MN>MX);
END LOOP;
END;
/

BEGIN
DBMS_OUTPUT.PUT_LINE('������������ '||RYK(102)||'.');
END;
/                                                                   /*6.1.2*/

CREATE OR REPLACE FUNCTION ORD (D DATE) RETURN VARCHAR2 IS
N NUMBER;
NO_ORD EXCEPTION;
ONE_ORD EXCEPTION;
MANY_ORD EXCEPTION;
BEGIN
SELECT COUNT(*) INTO N FROM ORDERS WHERE ORDER_DATE=D;
IF N=0 THEN RAISE NO_ORD; ELSIF
N=1 THEN RAISE ONE_ORD; ELSE
RAISE MANY_ORD; END IF;
EXCEPTION
WHEN NO_ORD THEN RETURN '�� ����';
WHEN ONE_ORD THEN RETURN '����';
WHEN MANY_ORD THEN RETURN '�����';
END ORD;
/
SHOW ERRORS;

BEGIN
DBMS_OUTPUT.PUT_LINE(ORD(TO_DATE('02.12.12','DD.MM.YY')));
END;
/

DECLARE
N DATE;
BEGIN
N:=TO_DATE('01.01.10','DD.MM.YY');
LOOP
DBMS_OUTPUT.PUT_LINE(ORD(N));
N:=N+1;
EXIT WHEN (N=TO_DATE('01.02.10','DD.MM.YY'));
END LOOP;
END;
/                                                               /*6.1.3*/

DECLARE
A NUMBER;
ERRORTEXT VARCHAR2(255);
BEGIN
A:=10;
A:=A/0;
DBMS_OUTPUT.PUT_LINE(A);
EXCEPTION
WHEN ZERO_DIVIDE THEN
ROLLBACK;
ERRORTEXT:=SQLERRM;
DBMS_OUTPUT.PUT_LINE(ERRORTEXT);
END;
/
SHOW ERRORS;                                                        /*6.1.4*/

/
CREATE OR REPLACE TRIGGER ZAPRET BEFORE INSERT
ON ORDERS FOR EACH ROW
DECLARE
DAT ORDERS.ORDER_DATE%TYPE;
ISK EXCEPTION;
BEGIN
IF :NEW.ORDER_DATE < SYSDATE THEN
RAISE ISK;
END IF;
EXCEPTION
WHEN ISK THEN
RAISE_APPLICATION_ERROR(-20011, '���� ������ ������ �������');
END;
/
INSERT INTO ORDERS VALUES(111111, '11.11.11', 4, 1111, 2111, 'MFB', 'P04', 103);                /*6.1.5*/
SELECT*FROM ORDERS;