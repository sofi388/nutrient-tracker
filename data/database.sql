USE nutrient_track_db;

CREATE TABLE nutrient_intake (
    id INT AUTO_INCREMENT PRIMARY KEY,
    age_low INT NOT NULL,
    age_high INT NOT NULL,
    male_low_activity INT NOT NULL,
    male_moderate_activity INT NOT NULL,
    male_high_activity INT NOT NULL,
    female_low_activity INT NOT NULL,
    female_moderate_activity INT NOT NULL,
    female_high_activity INT NOT NULL
);

LOAD DATA INFILE 'calorie_need.csv'
INTO TABLE NutrientIntake
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(age_low, age_high, male_low_activity, male_moderate_activity, male_high_activity, female_low_activity, female_moderate_activity, female_high_activity);
