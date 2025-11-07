import sqlite3

with sqlite3.connect('concrete.db') as conn:
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # 1. SHOW ALL TESTS
    print('ALL TESTS')

    query1 = '''SELECT a.*
                , CASE WHEN a.passed = 1 then "PASS" else "FAIL" end as "result_text" 
                FROM concrete_tests a '''
    cursor.execute(query1)
    rows = cursor.fetchall()

    for row in rows:
        print(f"{row['project_name']}: {row['actual_strength']} PSI - {row['result_text']}")



    # 2. Show ONLY failed tests
    print('\nFAILED TESTS')
    query2 = 'SELECT * from concrete_tests where passed = 0';
    cursor.execute(query2)
    
    while row := cursor.fetchone():
        print(f"{row['project_name']} on {row['test_date']}\n  "
             f"Required: {row['required_strength']} PSI\n  Actual: {row['actual_strength']} PSI\n")

    #rows = cursor.fetchall()
    #for row in rows:
      #  print(f"{row['project_name']} on {row['test_date']}\n  "
      #        f"Required: {row['required_strength']} PSI\n  Actual: {row['actual_strength']} PSI\n")



    # 3. Count tests by project
    print('TESTS PER PRODUCT')
    query3 = '''SELECT project_name
            , SUM(CASE WHEN passed = 1 then 1 else 0 end) as passed_tests, count(*) as all_tests
            from concrete_tests group by project_name'''
    
    cursor.execute(query3)

    rows = cursor.fetchall()
    for row in rows:
        print(f"{row['project_name']}: {row['passed_tests']}/{row['all_tests']} passed")