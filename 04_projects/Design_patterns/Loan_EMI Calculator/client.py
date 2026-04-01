from origin import EMILoanBuilder,Director
build=EMILoanBuilder()
dir=Director(build)
report=dir.construct(principle=500000,rate=12,years=5)
report.show()