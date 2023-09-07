model = dict(
    type='FAST', backbone=dict(
        type='fast_backbone',
        config='../FAST/config/fast/nas-configs/fast_base.config'
    ),
    neck=dict(
        type='fast_neck',
        config='../FAST/config/fast/nas-configs/fast_base.config'
    ),
    detection_head=dict(
        type='fast_head',
        config='../FAST/config/fast/nas-configs/fast_base.config',
        pooling_size=13,
        dropout_ratio=0.1,
        loss_text=dict(
            type='DiceLoss',
            loss_weight=0.5
        ),
        loss_kernel=dict(
            type='DiceLoss',
            loss_weight=1.0
        ),
        loss_emb=dict(
            type='EmbLoss_v1',
            feature_dim=4,
            loss_weight=0.25
        )
    )
)
repeat_times = 2
data = dict(
    batch_size=1,
    train=dict(
        type='FAST_TT',
        split='train',
        is_transform=True,
        img_size=640,
        short_size=640,
        pooling_size=9,
        read_type='cv2',
        repeat_times=repeat_times
    ),
    test=dict(
        type='FAST_TT',
        split='test',
        short_size=640,
        read_type='cv2'
    )
)
train_cfg = dict(
    lr=1e-3,
    schedule='polylr',
    epoch=10 // repeat_times,
    optimizer='Adam',
    pretrain='pretrained/fast_base_ic17mlt_640.pth',
    # https://github.com/czczup/FAST/releases/download/release/fast_base_ic17mlt_640.pth
    #save_interval=1 // repeat_times,
    save_interval=1,
)
test_cfg = dict(
    min_score=0.50,
    min_area=250,
    bbox_type='rect',
    result_path='outputs/submit_tt/'
)
