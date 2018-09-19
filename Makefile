BASEDIR=$(CURDIR)

HOST=tuxcanfly.me
PORT=774
USER=tuxcanfly

COINTAP=/home/tuxcanfly/build/cointap
VIRTUALENV=$(COINTAP)/.env

MEDIA=media
DB_FILE=db.sqlite3
HTML=$(MEDIA)/html
MANAGE=$(COINTAP)/manage.py
STATIC=$(COINTAP)/static

help:
	@echo 'Makefile for cointap website                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make init                        initialize project                 '
	@echo '   make clean                       remove the generated files         '
	@echo '   make shell                       drop to server shell               '
	@echo '   make nukedb                      nuked the server db (use CAUTION)  '
	@echo '   make deploy                      deploy the web site via SSH        '
	@echo '                                                                       '

warning:
	@printf "Are you sure? (y/n) "; \
	read reply; \
	if [[ ! $$reply =~ ^[Yy]$$ ]]; then \
		exit 1;\
	fi;

init: clean $(HTML)
	$(MANAGE) migrate
	@echo 'Done'

$(HTML):
	mkdir -p $(HTML)

clean:
	rm -r $(MEDIA) $(DB_FILE)

shell:
	ssh -t -p $(PORT) $(USER)@$(HOST) "source $(VIRTUALENV)/bin/activate && $(MANAGE) shell_plus"

nukedb: warning
	ssh -p $(PORT) $(USER)@$(HOST) "cd $(COINTAP) && rm -r $(MEDIA) $(DB_FILE)"
	ssh -p $(PORT) $(USER)@$(HOST) "cd $(COINTAP) && source $(VIRTUALENV)/bin/activate && $(MANAGE) migrate --no-input"
	ssh -p $(PORT) $(USER)@$(HOST) "cd $(COINTAP) && mkdir -p $(HTML)"

deploy:
	ssh -p $(PORT) $(USER)@$(HOST) "cd $(COINTAP) && git pull origin master"
	ssh -p $(PORT) $(USER)@$(HOST) "cd $(COINTAP) && rm -rf $(STATIC)"
	ssh -p $(PORT) $(USER)@$(HOST) "cd $(COINTAP) && npm run build"
	ssh -p $(PORT) $(USER)@$(HOST) "source $(VIRTUALENV)/bin/activate && $(MANAGE) collectstatic --no-input"
	ssh -t -p $(PORT) $(USER)@$(HOST) "sudo supervisorctl restart cointap"

.PHONY: init clean deploy
