data = [({
  'COUNTRY_ID': 121,
  'UNIQUE_ID': '3xrxmPITDSosaqzVgfwcKA5+2cvffV/mNepQVJd0shskpBr4MGMJSQ==',
  'PROFILE_DATA': json.dumps({
    'awards': None,
    'certifications': None,
    'country': 'Norway',
    'countryId': 121,
    'currentIndustry': '',
    'educations': [
      {
        'campus': 'University of Oslo (UiO)',
        'campusUuid': 'd49d6722576811e691cd42010af00009',
        'endDate': '01-01-1976',
        'major': 'German \'grunnfag\'',
        'sequenceNo': 5,
        'specialization': 'Cand. mag.',
        'startDate': '01-01-1975',
        'universityUrl': None
      },
      {
        'campus': 'Norwegian School of Sport Sciences (NIH)',
        'campusUuid': 'b94bc5d6629a11e5aeef42010af0acfd',
        'endDate': '01-01-1975',
        'major': None,
        'sequenceNo': 4,
        'specialization': None,
        'startDate': '01-01-1973',
        'universityUrl': None
      },
      {
        'campus': 'Fergus Falls State Junior College',
        'campusUuid': None,
        'endDate': '01-01-1971',
        'major': None,
        'sequenceNo': 1,
        'specialization': None,
        'startDate': '01-01-1970',
        'universityUrl': None
      }
    ],
    'externalProfiles': [
      {
        'externalProfileIconUrl': 'http://enterprise.swooptalent.com/images/linkedin.png',
        'externalProfileType': 'LinkedIn',
        'externalProfileUrl': 'http://linkedin.com/in/anne-sesseng-hoff-b278237b'
      }
    ],
    'firstName': 'Anne',
    'languages': None,
    'lastName': 'Sesseng Hoff',
    'title': 'Teacher at Aretta Ungdomsskole',
    'uniqueId': '3xrxmPITDSosaqzVgfwcKA5+2cvffV/mNepQVJd0smgtpBr4MGMFJQ=='
  }),
  'ADDED_DT': '2018-05-14T17:07:05.832-04:00',
  'UPDATED_DT': '2018-05-15T01:43:02.929-04:00',
  'REPROCESSED_DT': '2018-05-15T01:43:02.929-04:00'
}),
({
'COUNTRY_ID': 160,
  'UNIQUE_ID': '3xrxmPITDSosaqzVgfwcKA5+2cvffV/mNepQVJd0smgtpBr4MGMFJQ==',
  'PROFILE_DATA': json.dumps({
    'awards': None,
    'certifications': None,
    'country': 'Norway',
    'countryId': 160,
    'currentIndustry': '',
    'educations': [
      {
        'campus': 'University of Oslo (UiO)',
        'campusUuid': 'd49d6722576811e691cd42010af00009',
        'endDate': '01-01-1976',
        'major': 'German \'grunnfag\'',
        'sequenceNo': 5,
        'specialization': 'Cand. mag.',
        'startDate': '01-01-1975',
        'universityUrl': None
      }
    ],
    'externalProfiles': [
      {
        'externalProfileIconUrl': 'http://enterprise.swooptalent.com/images/linkedin.png',
        'externalProfileType': 'LinkedIn',
        'externalProfileUrl': 'http://linkedin.com/in/anne-sesseng-hoff-b278237b'
      }
    ],
    'firstName': 'Anna',
    'languages': None,
    'lastName': 'Hazare',
    'title': 'Teacher at Aretta Ungdomsskole',
  }),
  'ADDED_DT': '2018-05-14T17:07:05.832-04:00',
  'UPDATED_DT': '2018-05-15T01:43:02.929-04:00',
  'REPROCESSED_DT': '2018-05-15T01:43:02.929-04:00'
}
)]

df = spark.createDataFrame(data)

profile_schema = StructType([
            StructField('awards', StringType(), True),
            StructField('certifications', StringType(), True),
            StructField('country', StringType(), True),
            StructField('countryId', IntegerType(), True),
            StructField('currentIndustry', StringType(), True),
            StructField('educations', ArrayType(StructType([
               StructField('campus', StringType(), True),
               StructField('campusUuid', StringType(), True),
               StructField('endDate', StringType(), True),
               StructField('major', StringType(), True),
               StructField('sequenceNo', IntegerType(), True),
               StructField('specialization', StringType(), True),
               StructField('startDate', StringType(), True),
               StructField('universityUrl', StringType(), True)
            ]),True),True),
            StructField('externalProfiles', ArrayType(StructType([
              StructField('externalProfileIconUrl', StringType(), True),
              StructField('externalProfileType', StringType(), True),
              StructField('externalProfileUrl', StringType(), True)
            ]), True), True),
            StructField('firstName', StringType(), True),
            StructField('languages', ArrayType(StringType(),True), True),
            StructField('lastName', StringType(), True),
            StructField('title', StringType(), True)
    ])


profiles_df = (df.withColumn("PROFILE_DATA_JSON", from_json(df.PROFILE_DATA, profile_schema)).drop("PROFILE_DATA").withColumnRenamed("PROFILE_DATA_JSON", "PROFILE_DATA"))

partial_profiles_df = (profiles_df
        .select([
            "UNIQUE_ID",
            "UPDATED_DT",
            "PROFILE_DATA.country",
            "PROFILE_DATA.countryId",
            "PROFILE_DATA.currentIndustry",
            "PROFILE_DATA.firstName",
            "PROFILE_DATA.languages",
            "PROFILE_DATA.lastName",
            "PROFILE_DATA.title"
        ])
      )


education_history_df = (profiles_df
        .select(["UPDATED_DT", explode("PROFILE_DATA.educations").alias("education")])
        .select(["UPDATED_DT", "education.*"])
    )
