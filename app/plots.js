$(document).ready(function(){
  var cc = {
    'XAR': {
      'rmse':{
        'lr': [3.78,1.94,1.71,1.7,1.701,1.666,1.664],
        'rf': [1.707,1.598,1.541,1.522,1.524,1.512,1.506],
        'bdt': [1.733,1.589,1.524,1.492,1.476,1.469,1.477],
        'svm': [2.25,2.249,2.251,2.248,2.25,2.25,2.249],
        'mars': [1.966,1.768,1.79,1.669,1.681,1.743,1.707]
      },
      'rs': {
        'lr': [0.577,0.627,0.678,0.671,0.673,0.696,0.699],
        'rf': [0.671,0.74,0.748,0.753,0.754,0.759,0.768],
        'bdt': [0.631,0.72,0.735,0.742,0.748,0.748,0.753],
        'svm': [null,null, null, null, null, null, null],
        'mars': [0.55,0.643,0.616,0.678,0.674,0.633,0.656]
      },
      'rp': {
        'lr': [0.403,0.553,0.656,0.664,0.667,0.69,0.691],
        'rf': [0.672,0.742,0.756,0.764,0.764,0.766,0.771],
        'bdt': [0.636,0.723,0.744,0.756,0.761,0.766,0.767],
        'svm': [null,null, null, null, null, null, null],
        'mars': [0.509,0.628,0.615,0.68,0.675,0.636,0.66]
      }
    },
    'X': {
      'rmse':{
        'lr': [1.818,1.824,1.81,1.8,1.801,1.799,1.798],
        'rf': [1.816,1.793,1.744,1.703,1.711,1.71,1.703],
        'bdt': [1.904,1.874,1.845,1.792,1.796,1.77,1.755],
        'svm': [2.232,2.203,2.184,2.18,2.183,2.162,2.163],
        'mars': [1.846,1.833,1.817,1.792,1.812,1.776,1.783]
      },
      'rs': {
        'lr': [0.623,0.625,0.637,0.64,0.637,0.64,0.643],
        'rf': [0.593,0.618,0.64,0.654,0.648,0.648,0.65],
        'bdt': [0.551,0.535,0.577,0.606,0.603,0.62,0.608],
        'svm': [0.182,0.241,0.256,0.27,0.239,0.312,0.309],
        'mars': [0.596,0.612,0.617,0.635,0.621,0.635,0.63]
      },
      'rp': {
        'lr': [0.615,0.618,0.625,0.625,0.625,0.626,0.627],
        'rf': [0.6,0.62,0.641,0.662,0.659,0.66,0.665],
        'bdt': [0.539,0.555,0.574,0.604,0.603,0.617,0.627],
        'svm': [0.165,0.237,0.281,0.272,0.259,0.305,0.301],
        'mars': [0.587,0.607,0.61,0.613,0.606,0.634,0.631]
      }
    },
    'ALL': {
      'rmse':{
        'lr': [],
        'rf': [],
        'bdt': [],
        'svm': [],
        'mars': []
      },
      'rs': {
        'lr': [],
        'rf': [],
        'bdt': [],
        'svm': [],
        'mars': []
      },
      'rp': {
          'lr': [],
          'rf': [],
          'bdt': [],
          'svm': [],
          'mars': []
      }
    }
  };

  set_chart('XAR Features', 'RMSE', 'rmse_xar', cc['XAR']['rmse']);
  set_chart('X Features', 'RMSE', 'rmse_x', cc['X']['rmse']);
  set_chart('All Features', 'RMSE', 'rmse_all', cc['ALL']['rmse']);
  set_chart('XAR Features', 'Rs', 'rs_xar', cc['XAR']['rs']);
  set_chart('X Features', 'Rs', 'rs_x', cc['X']['rs']);
  set_chart('All Features', 'Rs', 'rs_all', cc['ALL']['rs']);
  set_chart('XAR Features', 'Rp', 'rp_xar', cc['XAR']['rp']);
  set_chart('X Features', 'Rp', 'rp_x', cc['X']['rp']);
  set_chart('All Features', 'Rp', 'rp_all', cc['ALL']['rp']);
});

function set_chart(titlename, yaxis, containeridname, dat){
  Highcharts.chart(containeridname, {

      title: {
          text: titlename
      },

      subtitle: {
          text: 'Random test set'
      },

      yAxis: {
          title: {
              text: yaxis
          }
      },
      xAxis: {
        categories: [500, 1000, 1500, 2000, 2500, 3000, 3250],
      	title: {
        	text: 'Number of Training Complexes'
        }
      },
      legend: {
          layout: 'vertical',
          align: 'right',
          verticalAlign: 'middle'
      },

      plotOptions: {
          series: {
              label: {
                  connectorAllowed: false
              }
              }
      },

      series: [{
          name: 'LR',
          data: dat['lr']
      }, {
          name: 'RF',
          data: dat['rf']
      }, {
          name: 'BDT',
          data: dat['bdt']
      }, {
          name: 'SVM',
          data: dat['svm']
      }, {
          name: 'MARS',
          data: dat['mars']
      }],

      responsive: {
          rules: [{
              condition: {
                  maxWidth: 500
              },
              chartOptions: {
                  legend: {
                      layout: 'horizontal',
                      align: 'center',
                      verticalAlign: 'bottom'
                  }
              }
          }]
      }

  });

}
