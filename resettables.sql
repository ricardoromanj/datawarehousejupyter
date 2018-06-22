
alter table FactDischarge drop constraint FK_FactDischarge_Provider;
truncate table DimProvider;
alter table FactDischarge add constraint FK_FactDischarge_Provider
foreign key (ProviderKey) references DimProvider (ProviderKey);

alter table FactDischarge drop constraint FK_FactDischarge_Date;
truncate table DimDate;
alter table FactDischarge add constraint FK_FactDischarge_Date
foreign key (DateKey) references DimDate (DateKey);

alter table FactDischarge drop constraint FK_FactDischarge_Admission;
truncate table DimAdmission;
alter table FactDischarge add constraint FK_FactDischarge_Admission
foreign key (AdmissionKey) references DimAdmission (AdmissionKey);

alter table FactDischarge drop constraint FK_FactDischarge_ClinicClass;
truncate table DimClinicClass;
alter table FactDischarge add constraint FK_FactDischarge_ClinicClass
foreign key (ClinicClassKey) references DimClinicClass (ClinicClassKey);

alter table FactDischarge drop constraint FK_FactDischarge_APRClassification;
truncate table DimAPRClassification;
alter table FactDischarge add constraint FK_FactDischarge_APRClassification
foreign key (AprKey) references DimAPRClassification (AprKey);

alter table FactDischarge drop constraint FK_FactDischarge_Payment;
truncate table DimPayment;
alter table FactDischarge add constraint FK_FactDischarge_Payment
foreign key (PaymentKey) references DimPayment (PaymentKey);

alter table FactDischarge drop constraint FK_FactDischarge_Demographics;
truncate table DimDemograhics;
alter table FactDischarge add constraint FK_FactDischarge_Demographics
foreign key (DemographicsKey) references DimDemograhics (DemographicsKey);

alter table FactDischarge drop constraint FK_FactDischarge_Location;
truncate table DimLocation;
alter table FactDischarge add constraint FK_FactDischarge_Location
foreign key (LocationKey) references DimLocation (LocationKey);
