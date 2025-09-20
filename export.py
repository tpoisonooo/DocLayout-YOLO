from doclayout_yolo import YOLOv10
model=YOLOv10("/workspace/DocLayout-YOLO/weight/model.pt")
# model.export(format='engine', half=True)
model.export(format='engine', half=True, dynamic=True)

# dynamic_shape=(1, 3, 1024, 1024), 

# import torch
# from doclayout_yolo import YOLOv10

# model=YOLOv10("/data/khj/workspace/DocLayout-YOLO/weight/doclayout_yolo_docstructbench_imgsz1024.pt")
# net = model.eval()

# x = torch.rand(1, 3, 1024, 1024)
# mod = torch.jit.trace(net, x)
# mod.save("doclayout.pt")
