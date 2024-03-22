build:
	cp main.py koff
	chmod +x ./koff

install:
	cp ./koff ~/.local/bin
	cp ./koff.service ~/.config/systemd/user
	systemctl --user daemon-reload

uninstall:
	systemctl --user stop koff
	systemctl --user disable koff
	rm ~/.local/bin/koff
	rm ~/.config/systemd/user/koff.service
	systemctl --user daemon-reload

clean:
	rm ./koff