## Add your own custom Makefile targets here
RUN = poetry run

scratch/BioCoreDataModel_generated.yaml: src/biocore_data_model_linkml_template/schema/BioCoreDataModel.yaml
	$(RUN) gen-linkml --format yaml --output $@ $<
