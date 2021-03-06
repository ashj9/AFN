{
    "mode": "sr",
    "use_cl": true,
    "gpu_ids": [0],

    "scale": 8,
    "degradation": "BI",
    "is_train": false,
    "use_chop": false,
    "rgb_range": 255,
    "self_ensemble": false,
    "save_val_output" : false,
    "datasets": {
        "test_set1": {
            "mode": "LRHR",
            "dataroot_HR": "./results/HR/Set5/x4",
            "dataroot_LR": "./results/LR/LRBI/Set5/x4",
            "data_type": "img"
        }

    },

    "networks": {
        "which_model": "SRFBN",
        "num_features": 64,
        "in_channels": 1,
        "out_channels": 1,
        "num_steps": 4,
        "num_groups": 8
    },

    "solver": {
        "pretrained_path": "Update the paths accordingly"
    }
}
