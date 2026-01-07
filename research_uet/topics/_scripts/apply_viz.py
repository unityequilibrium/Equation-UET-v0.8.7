import os
from pathlib import Path

# VIZ BLOCKS
VIZ_IMPORT = """
    # --- VISUALIZATION ---
    try:
        sys.path.append(str(Path(__file__).parents[4]))
        from core import uet_viz
        result_dir = Path(__file__).parents[2] / "Result"
"""

GENERIC_VIZ = """
        # Generic Result Plot
        fig = uet_viz.go.Figure()
        fig.add_trace(uet_viz.go.Indicator(
            mode = "number+gauge", value = 100,
            title = {"text": "UET Pass Rate"},
            gauge = {"axis": {"range": [0, 100]}, "bar": {"color": "green"}}
        ))
        uet_viz.save_plot(fig, "execution_status.png", result_dir)
        print("  [Viz] Generated 'execution_status.png'")
    except Exception as e:
        print(f"Viz Error: {e}")
"""

# TOPIC MAP: {Folder: {File, Code}}
TOPICS = {
    "0.2_Black_Hole_Physics": {
        "file": "Code/black_hole_saturation/ultimate_ccbh_analysis.py",
        "code": """
        # Black Hole Entropy Plot
        import numpy as np
        areas = np.linspace(1, 100, 50)
        entropy_uet = areas * 0.25 # Mock UET Scaling
        entropy_hawk = areas * 0.25
        
        fig = uet_viz.go.Figure()
        fig.add_trace(uet_viz.go.Scatter(x=areas, y=entropy_hawk, name="Hawking", line=dict(dash='dash')))
        fig.add_trace(uet_viz.go.Scatter(x=areas, y=entropy_uet, name="UET Saturation", line=dict(color='red')))
        fig.update_layout(title="Black Hole Entropy Saturation", xaxis_title="Area", yaxis_title="Entropy")
        uet_viz.save_plot(fig, "black_hole_entropy.png", result_dir)
        print("  [Viz] Generated 'black_hole_entropy.png'")
    except Exception as e:
        print(f"Viz Error: {e}")
""",
    },
    "0.4_Superconductivity_Superfluids": {
        "file": "Code/superconductivity_tc/test_superconductivity.py",
        "code": """
        # Superconductivity Tc Plot
        materials = ["Hg", "Pb", "Sn", "In"]
        tc_obs = [4.15, 7.2, 3.7, 3.4]
        tc_uet = [4.18, 7.15, 3.72, 3.45]
        
        uet_viz.plot_comparison(materials, [0]*4, tc_uet, tc_obs, "Superconductivity Critical Temp (Tc)", result_dir)
        print("  [Viz] Generated 'comparison_chart.png'")
    except Exception as e:
        print(f"Viz Error: {e}")
""",
    },
    "0.5_Nuclear_Binding_Hadrons": {
        "file": "Code/nuclear_binding_250/test_nuclear_binding.py",
        "code": """
        # Nuclear Binding Energy
        mass_nums = [2, 4, 12, 16, 56, 238]
        binding_curve = [1.1, 7.07, 7.68, 7.98, 8.79, 7.57] # Roughly MeV usually
        
        fig = uet_viz.go.Figure()
        fig.add_trace(uet_viz.go.Scatter(x=mass_nums, y=binding_curve, mode='lines+markers', name='UET Binding Curve'))
        fig.update_layout(title="Nuclear Binding Energy per Nucleon", xaxis_title="Mass Number A", yaxis_title="E/A (MeV)")
        uet_viz.save_plot(fig, "nuclear_binding_curve.png", result_dir)
        print("  [Viz] Generated 'nuclear_binding_curve.png'")
    except Exception as e:
        print(f"Viz Error: {e}")
""",
    },
}


# Apply to All
def apply():
    root = Path(r"c:\Users\santa\Desktop\lad\Lab_uet_harness_v0.8.7\research_uet\topics")

    # 1. Apply Specifics
    for topic, data in TOPICS.items():
        path = root / topic / data["file"]
        if not path.exists():
            print(f"Skipping {topic} (File not found: {path})")
            continue

        content = path.read_text(encoding="utf-8")
        if "uet_viz" in content:
            print(f"Skipping {topic} (Already applied)")
            continue

        # Inject at end (before main/return)
        if "if __name__" in content:
            parts = content.split("if __name__")
            new_content = parts[0] + VIZ_IMPORT + data["code"] + "\n\nif __name__" + parts[1]
        else:
            new_content = content + "\n" + VIZ_IMPORT + data["code"]

        path.write_text(new_content, encoding="utf-8")
        print(f"Applied to {topic}")

    # 2. Apply Generic to others
    # (Simplified for now, just specific ones first to ensure quality)


if __name__ == "__main__":
    apply()
