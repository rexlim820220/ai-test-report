import pytest
from ai_test_report import logger

def test_server_config_structure():
    config_data = {
        "env": {
            "LOCAL": {
                "CPU_SERVER": {"TGI_HOST": "10.255.174.201", "TGI_MODEL": "GEMMA3_4B", "PORT": "8082"},
                "GPU_SERVER": {"TGI_HOST": "172.18.246.36", "TGI_MODEL": "GEMMA3_12B", "PORT": "8082"},
                "DB_HOST": "172.18.220.83",
                "DB_PORT": "3306",
                "LOG_FILE": "../../log/system/aichatter.log",
                "ORAN_TEST_ELK_URL": "http://172.18.220.86:5601",
                "SVP_URL": "https://localhost",
                "SERVER_ROOM_SWITCH": {
                    "F3": {"OS": "Dell_OS10", "IP": "10.255.174.21"},
                    "B1": {"OS": "CISCO", "IP": "10.255.174.59"},
                    "M1": {"OS": "CISCO", "IP": "10.255.174.46"},
                }
            },
            "DEV": {
                "CONTROL_PANEL_IP": "oran-booking-dev.pegatroncorp.com",
                "INFLUX_DB_HOST": "http://172.18.220.76:8086/",
                "GPU_SERVER": {"TGI_HOST": "172.18.246.36", "TGI_MODEL": "GEMMA3_12B", "PORT": "8082"}
            },
            "PROD": {
                "CONTROL_PANEL_IP": "oran-booking.pegatroncorp.com",
                "GPU_SERVER": {"TGI_HOST": "172.18.246.36", "TGI_MODEL": "GEMMA3_12B", "PORT": "8082"}
            }
        }
    }

    logger.info("Logging simplified infrastructure config")
    for env, details in config_data["env"].items():
        gpu = details.get("GPU_SERVER", {})
        switches = details.get("SERVER_ROOM_SWITCH", {})
        logger.info(f"[{env}] GPU → {gpu.get('TGI_MODEL')} @ {gpu.get('TGI_HOST')}:{gpu.get('PORT')}")
        if switches:
            for label, info in switches.items():
                logger.info(f"Switch {label} → {info['OS']} @ {info['IP']}")

    assert "LOCAL" in config_data["env"]
    assert "GPU_SERVER" in config_data["env"]["DEV"]
    assert isinstance(config_data["env"]["LOCAL"]["SERVER_ROOM_SWITCH"], dict)
    assert config_data["env"]["LOCAL"]["DB_PORT"] == "3306"
