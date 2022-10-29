def iou(box1,box2):        
    (box1_x1, box1_y1, box1_x2 ,box1_y2) = box1
    (box2_x1, box2_y1, box2_x2, box2_y2) = box2

    xi1 = max(box1_x1,box2_x1)
    yi1 = max(box1_y1,box2_y1)
    xi2 = min(box1_x2,box2_x2)
    yi2 = min(box1_y2,box2_y2)

    inter_width = max(0, yi2 - yi1)
    inter_height = max(0, xi2 - xi1)
    inter_area = inter_width * inter_height
    box1_area = (box1_x2-box1_x1) * ((box1_y2-box1_y1))
    box2_area = (box2_x2-box2_x1) * ((box2_y2-box2_y1))
    union_area = box1_area + box2_area - inter_area

    iou = inter_area/union_area
    return iou
box1 = (2,1,4,3)
box2 = (1,2,3,4)
print("iou sonucu: "+str(iou(box1,box2)))