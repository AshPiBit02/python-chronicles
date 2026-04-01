from origin import MonthlyReportBuilder,Director
builder=MonthlyReportBuilder()
director=Director(builder)
report=director.construct(income=50000,expenses=20000,tax_rate=0.2)
report.show()