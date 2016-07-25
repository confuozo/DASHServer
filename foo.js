$.post('http://localhost:5000/send',
                {data: JSON.stringify($scope.videoMetrics)}, function(d, c){}
            );

$.post('http://localhost:5000/sendaudio',
                {data: JSON.stringify($scope.audioMetrics)}, function(d, c){}
            );