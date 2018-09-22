// Name
of
the
downloaded
my
cascades..
string
cascadeHead = "cascadeH5.xml";
string
cascadeName = "cascadG.xml";

// Load
the
cascade
CascadeClassifier
detectorBody;
bool
loaded1 = detectorBody.load(cascadeName);
CascadeClassifier
detectorHead;
bool
loaded2 = detectorHead.load(cascadeHead);

// save
original
make
img
gray
// draw
rectangle
back
to
the
original
colored
sample
Mat
original;
img.copyTo(original);
// Prepare
vector
for results
    vector < Rect > human;
vector < Rect > head;
// Prepare
gray
image
cvtColor(img, img, CV_BGR2GRAY);
// equalize
Histogram
equalizeHist(img, img);
// detect
body and head in the
img
// Set
the
proper
min and max
size
for your case
    detectorBody.detectMultiScale(img, human, 1.04, 4, 0 | 1, Size(30, 80), Size(80, 200));
    detectorHead.detectMultiScale(img, head, 1.1, 4, 0 | 1, Size(40, 40), Size(100, 100));

    if (human.size() > 0) {
    for (int gg = 0; gg < human.size(); gg++) {

    rectangle(original, human[gg].tl(), human[gg].br(), Scalar(0, 0, 255), 2, 8, 0);

    }
    }

    if (head.size() > 0) {
    for (int gg = 0; gg < head.size(); gg++) {

    rectangle(original, head[gg].tl(), head[gg].br(), Scalar(0, 0, 255), 2, 8, 0);

    }
    }