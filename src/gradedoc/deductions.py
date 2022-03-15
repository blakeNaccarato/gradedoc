from dynaconf import Dynaconf

all_deductions = Dynaconf(
    settings_files=["config.yaml", "config_lab_specific.yaml"],
    merge_enabled=True,
)
