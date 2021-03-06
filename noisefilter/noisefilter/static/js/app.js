if (filter == 'ann'){
createannchart()
}
else  if(filter == 'kalman'){
createkalmanchart()
}

function createannchart() {
    var layers = {
	  x: ly_tests,
	  y: ly_pred,
	  mode: 'markers',
	  type: 'scatter',
	  name: 'Layers',
	  marker: { size: 12 }
	};

	var epochs = {
	  x: ep_tests,
	  y: ep_pred,
	  mode: 'markers',
	  type: 'scatter',
	  name: 'Epochs',
	  marker: { size: 12 }
	};

	var data = [ layers ];
	var data1 = [ epochs ];

	var layout = {
	  xaxis: {
	    range: [ 0, 10 ]
	  },
	  yaxis: {
	    range: [18, 22]
	  },
	  title:'Neural Network Testing: Layers'
	};

	var layout1 = {
	  xaxis: {
	    range: [ 4000, 111000 ]
	  },
	  yaxis: {
	    range: [18, 22]
	  },
	  title:'Neural Network Testing: Epochs'
	};

	Plotly.newPlot('chart', data, layout);
	Plotly.newPlot('chart1', data1, layout1);	
}

function createkalmanchart() {
	var est = {
  y: estimates,
  mode: 'lines',
  type: 'scatter',
  name: 'Estimate',
};

var noisyd = {
  y: noisydata,
  mode: 'lines',
  type: 'scatter',
  name: 'Noisy Data',
};

var trueline = {
  x: [0, estimates.length],
  y: [true_value, true_value],
  mode: 'lines',
  type: 'scatter',
  name: 'True Value',
};


var data2 = [ est, trueline, noisyd ];

var layout2 = {
	  yaxis: {
	    range: [17, 23]
	  },
	  title:'Kalman Testing'
	};

Plotly.newPlot('chart2', data2, layout2);
}