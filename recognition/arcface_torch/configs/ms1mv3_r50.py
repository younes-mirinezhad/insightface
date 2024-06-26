from easydict import EasyDict as edict

# make training faster
# our RAM is 256G
# mount -t tmpfs -o size=140G  tmpfs /train_tmp

config = edict()
config.margin_list = (1.0, 0.5, 0.0)
config.network = "r50"
config.resume = False
config.output = None
config.embedding_size = 512
config.sample_rate = 1.0
config.fp16 = True
config.momentum = 0.9
config.weight_decay = 5e-4
config.batch_size = 128
config.lr = 0.1
config.verbose = 2000
config.dali = False

# Full dataset
config.rec = "/train_tmp/ms1m-retinaface-t1"
config.num_classes = 93431
config.num_image = 5179510
config.num_epoch = 20
config.warmup_epoch = 0
config.val_targets = ['lfw', 'cfp_fp', "agedb_30"]

# Test dataset
# config.rec = "/media/chiko/HDD_1/Work/InsightFace/faces_emore_Test"
# config.num_classes = 500
# config.num_image = 34225
# config.num_epoch = 20
# config.warmup_epoch = 0
# config.val_targets = ['agedb_30']

# Finetune
# config.finetune = True
# config.freezing_percentage = 70
# config.pretrained = '/media/chiko/HDD_1/Work/InsightFace/Model/backbone.pth'

# config.save_all_states = True
