## Gray Scale Program

```python
import cv2
img = cv2.imread(<img width="995" height="1014" alt="Screenshot 2026-02-27 160637" src="https://github.com/user-attachments/assets/b009d8b4-d34c-4ebc-9e7e-4f3fbbc38e93" />
)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()# ITA0527--Computer-Vision
