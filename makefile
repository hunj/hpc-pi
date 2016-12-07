build: time/pi_*.py time.slurm
	mkdir time/result

1min: time/pi_monte-carlo.py time/pi_chudnovsky.py time/pi_brent-salamin.py time/pi_ramanujan-sato.py
	python time/pi_monte-carlo.py 1 >> time/result/monte-carlo-1min &
	python time/pi_chudnovsky.py 1 >> time/result/chudnovsky-1min &
	python time/pi_brent-salamin.py 1 >> time/result/pi_brent-salamin-1min &
	python time/pi_ramanujan-sato.py 1 >> time/result/ramanujan_sato-1min &
