help:
	@echo "    run"
	@echo "        Runs the bot on the command line."
	@echo "    run-actions"
	@echo "        Runs the action server."
	@echo "    run-core"
	@echo "        Runs the core server."
	@echo "    train-nlu"
	@echo "        Train the natural language understanding using Rasa NLU."
	@echo "    train-core"
	@echo "        Train a dialogue model using Rasa core."

run:
	make run-actions&
	make run-core

run-actions:
	python -m rasa_core_sdk.endpoint --actions actions

run-core: #3 cmdline
	python -m rasa_core.run --nlu models/nlu/default/current --core models/dialogue --endpoints endpoints.yml

train-nlu: #1
	python bot.py train-nlu

	or

	python -m rasa_nlu.train -c nlu_model_config.yml --fixed_model_name current --data ./data/nlu_data.md --path ./models/nlu

train-core:#2
	python bot.py train-dialogue

Running Interactive Learning:
	python -m rasa_core_sdk.endpoint --actions actions

	python -m rasa_core.train interactive -o models/dialogue -d domain.yml -c default_config.yml -s data/stories.md --nlu models/nlu/default/current --endpoints endpoints.yml

Running the HTTP server:
python -m rasa_core.run --enable_api -d models/dialogue -u models/nlu/default/current -o out.log

Running custom action:
python -m rasa_core.run --enable_api -d models/dialogue -u models/nlu/default/current --endpoints endpoint.py -o out.log

python -m rasa_core.run --auth_token rasabot -d models/dialogue -u models/nlu/default/current -o out.log --endpoints endpoints.yml --enable_api



C:\Users\IKRAM\Desktop\work\rasa_core-master\rasa_core-master\rasa_core
C:\Users\IKRAM\Desktop\work\rasa_core-master\rasa_core-master\examples\restaurantbot


	
