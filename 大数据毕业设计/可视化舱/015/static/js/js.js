$(function () {
    echarts_1();
    echarts_2();
    echarts_4();
    echarts_31();
    echarts_33();
    echarts_5();
    echarts_6();
    echarts_32();

    function echarts_1() {

        $.get('/brand_Sales', function (data) {

            // alert(data.x);
            var myChart = echarts.init(document.getElementById('echart1'));
            option = {
                //  backgroundColor: '#00265f',
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'shadow'
                    }
                },
                dataZoom: [
                    {
                        show: false,
                        realtime: true,
                        start: 0,
                        end: 8,
                        height: 10
                    },
                    {
                        type: 'inside',
                        realtime: true,
                        start: 0,
                        end: 10
                    }
                ],
                grid: {
                    left: '0%',
                    top: '10px',
                    right: '0%',
                    bottom: '4%',
                    containLabel: true
                },
                xAxis: [{
                    type: 'category',
                    data: data.x,
                    axisLine: {
                        show: true,
                        lineStyle: {

                            color: "rgba(255,255,255,.1)",
                            width: 1,
                            type: "solid"
                        },
                    },

                    axisTick: {
                        show: false,
                    },
                    axisLabel: {
                        interval: 0,
                        // rotate:50,
                        show: true,
                        splitNumber: 15,
                        textStyle: {
                            color: "rgba(255,255,255,.6)",
                            fontSize: '8',
                        },
                    },

                }],
                yAxis: [{
                    type: 'value',
                    axisLabel: {
                        //formatter: '{value} %'
                        show: false,
                        textStyle: {
                            color: "rgba(255,255,255,.6)",
                            fontSize: '12',
                        },
                    },
                    axisTick: {
                        show: false,
                    },
                    axisLine: {
                        show: true,
                        lineStyle: {
                            color: "rgba(255,255,255,.1	)",
                            width: 1,
                            type: "solid"
                        },
                    },
                    splitLine: {
                        lineStyle: {
                            color: "rgba(255,255,255,.1)",
                        }
                    }
                }],
                series: [
                    {
                        type: 'bar',
                        data: data.y,
                        barWidth: '35%', //柱子宽度
                        // barGap: 1, //柱子之间间距
                        itemStyle: {
                            normal: {
                                opacity: 1,
                                barBorderRadius: 5,
                                color: function (params) {
                                    var c = '';
                                    if (params.name === data.id) {
                                        c = 'red'
                                    } else {
                                        c = '#2f89cf'
                                    }
                                    return c;
                                },
                            },

                        }
                    },


                ]
            };
            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
            window.addEventListener("resize", function () {
                myChart.resize();
            });
        });
        // 基于准备好的dom，初始化echarts实例

    }

    function echarts_2() {
        $.get('/brand_Sales_price', function (data) {
            // 基于准备好的dom，初始化echarts实例
            var myChart = echarts.init(document.getElementById('echart2'));
            option = {
                //  backgroundColor: '#00265f',
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {type: 'shadow'}
                },
                dataZoom: [
                    {
                        show: false,
                        realtime: true,
                        start: 0,
                        end: 8,
                        height: 10
                    },
                    {
                        type: 'inside',
                        realtime: true,
                        start: 0,
                        end: 10
                    }
                ],

                grid: {
                    left: '0%',
                    top: '10px',
                    right: '0%',
                    bottom: '4%',
                    containLabel: true
                },
                legend: {
                    show: true,
                    selectedMode: 'single',
                    bottom: 10,
                    left: 50,
                    textStyle: {
                        color: '#666',
                        fontSize: 12
                    }
                },
                xAxis: [{
                    type: 'category',
                    data: data.x,
                    axisLine: {
                        show: true,
                        lineStyle: {
                            color: "rgba(255,255,255,.1)",
                            width: 1,
                            type: "solid"
                        },
                    },

                    axisTick: {
                        show: false,
                    },
                    axisLabel: {
                        interval: 0,
                        // rotate:50,
                        show: true,
                        splitNumber: 15,
                        textStyle: {
                            color: "rgba(255,255,255,.6)",
                            fontSize: '8',
                        },
                    },
                }],
                yAxis: [{
                    type: 'value',
                    name: '销量',
                    axisLabel: {
                        //formatter: '{value} %'
                        show: false,
                        textStyle: {
                            color: "rgba(255,255,255,.6)",
                            fontSize: '12',
                        },
                    },
                    axisTick: {
                        show: false,
                    },
                    axisLine: {
                        show: false,
                        lineStyle: {
                            color: "rgba(255,255,255,.1	)",
                            width: 1,
                            type: "solid"
                        },
                    },
                    splitLine: {
                        lineStyle: {
                            color: "rgba(255,255,255,.1)",
                        }
                    }
                }, {
                    type: 'value',
                    name: '价格',
                    show: false

                }],
                series: [
                    {

                        type: 'bar',
                        data: data.y_bar,
                        barWidth: '35%', //柱子宽度
                        // barGap: 1, //柱子之间间距
                        itemStyle: {
                            normal: {
                                opacity: 1,
                                barBorderRadius: 5,
                                color: function (params) {
                                    var c = '';
                                    if (params.name === data.id) {
                                        c = 'red'
                                    } else {
                                        c = '#27d08a'
                                    }
                                    return c;
                                },
                            },
                        }
                    }, {
                        type: 'line',
                        yAxisIndex: 1,
                        data: data.y_line,
                        itemStyle: {
                            normal: {
                                color: 'rgba(235,73,105,0.7)',

                            }
                        }
                    }

                ]
            };

            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
            window.addEventListener("resize", function () {
                myChart.resize();
            });

        });


    }

    function echarts_5() {
        $.get('/user_score_star', function (data) {
            data_pie = [];
            for (var i in data.x) {
                d = {};
                d['name'] = data.x[i];
                d['value'] = data.y[i];
                data_pie.push(d);
            }
            // 基于准备好的dom，初始化echarts实例
            var myChart = echarts.init(document.getElementById('echart5'));

            var option = {

                tooltip: {
                    trigger: 'item',
                    formatter: "{a} <br/>{b}: {c} ({d}%)",
                    position: function (p) {   //其中p为当前鼠标的位置
                        return [p[0] + 10, p[1] - 10];
                    }
                },
                legend: {

                    top: '90%',
                    itemWidth: 20,
                    itemHeight: 20,
                    data: data.x,
                    textStyle: {
                        color: 'rgba(255,255,255,.5)',
                        fontSize: '10',
                    }
                },
                series: [
                    {
                        name: '用户情感分析',
                        type: 'pie',
                        center: ['50%', '42%'],

                        color: ['#cd2ddb', '#11151e'],
                        label: {show: false},
                        labelLine: {show: false},
                        data: data_pie,


                    }


                ]
            };


            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
            window.addEventListener("resize", function () {
                myChart.resize();
            });
        });

    }

    function echarts_4() {
        $.get('/user_score', function (data) {
            // 基于准备好的dom，初始化echarts实例
            var myChart = echarts.init(document.getElementById('echart4'));

            option = {
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        lineStyle: {
                            color: '#dddc6b'
                        }
                    }
                },
                dataZoom: [
                    {
                        show: false,
                        realtime: true,
                        start: 0,
                        end: 25,
                        height: 10
                    },
                    {
                        type: 'inside',
                        realtime: true,
                        start: 0,
                        end: 10
                    }
                ],
                legend: {
                    top: '0%',
                    data: ['负面', '正面'],
                    textStyle: {
                        color: 'rgba(255,255,255,.5)',
                        fontSize: '12',
                    }
                },
                grid: {
                    left: '10',
                    top: '30',
                    right: '10',
                    bottom: '10',
                    containLabel: true
                },

                xAxis: [{
                    type: 'category',
                    boundaryGap: false,
                    axisLabel: {
                        textStyle: {
                            color: "rgba(255,255,255,.6)",
                            fontSize: 12,
                        },
                    },
                    axisLine: {
                        lineStyle: {
                            color: 'rgba(255,255,255,.2)'
                        }

                    },

                    data: data.x

                }, {

                    axisPointer: {show: false},
                    axisLine: {show: false},
                    position: 'bottom',
                    offset: 20,


                }],

                yAxis: [{
                    type: 'value',
                    axisTick: {show: false},
                    axisLine: {
                        lineStyle: {
                            color: 'rgba(255,255,255,.1)'
                        }
                    },
                    axisLabel: {
                        textStyle: {
                            color: "rgba(255,255,255,.6)",
                            fontSize: 12,
                        },
                    },

                    splitLine: {
                        lineStyle: {
                            color: 'rgba(255,255,255,.1)'
                        }
                    }
                }],
                series: [
                    {
                        name: '负面',
                        type: 'line',
                        smooth: true,
                        symbol: 'circle',
                        symbolSize: 5,
                        showSymbol: false,
                        lineStyle: {

                            normal: {
                                color: '#0184d5',
                                width: 2
                            }
                        },
                        areaStyle: {
                            normal: {
                                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                    offset: 0,
                                    color: 'rgba(1, 132, 213, 0.4)'
                                }, {
                                    offset: 0.8,
                                    color: 'rgba(1, 132, 213, 0.1)'
                                }], false),
                                shadowColor: 'rgba(0, 0, 0, 0.1)',
                            }
                        },
                        itemStyle: {
                            normal: {
                                color: '#0184d5',
                                borderColor: 'rgba(221, 220, 107, .1)',
                                borderWidth: 12
                            }
                        },
                        data: data.y_z

                    },
                    {
                        name: '正面',
                        type: 'line',
                        smooth: true,
                        symbol: 'circle',
                        symbolSize: 5,
                        showSymbol: false,
                        lineStyle: {

                            normal: {
                                color: '#00d887',
                                width: 2
                            }
                        },
                        areaStyle: {
                            normal: {
                                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                    offset: 0,
                                    color: 'rgba(0, 216, 135, 0.4)'
                                }, {
                                    offset: 0.8,
                                    color: 'rgba(0, 216, 135, 0.1)'
                                }], false),
                                shadowColor: 'rgba(0, 0, 0, 0.1)',
                            }
                        },
                        itemStyle: {
                            normal: {
                                color: '#00d887',
                                borderColor: 'rgba(221, 220, 107, .1)',
                                borderWidth: 12
                            }
                        },
                        data: data.y

                    },

                ]

            };

            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
            window.addEventListener("resize", function () {
                myChart.resize();
            });
        });


    }

    function echarts_6() {
        $.get('/user_opinion', function (data) {

            var wordCount = [];
            for (var i in data.x) {
                d = {};
                d['name'] = data.x[i];
                d['value'] = data.y[i];
                wordCount.push(d);
            }
            // 基于准备好的dom，初始化echarts实例
            var myChart = echarts.init(document.getElementById('echart6'));

            var option = {
                tooltip: {
                    show: true
                },
                series: [{
                    type: 'wordCloud',
                    sizeRange: [6, 66],
                    rotationRange: [-45, 90],
                    textPadding: 0,
                    autoSize: {
                        enable: true,
                        minSize: 6
                    },
                    textStyle: {
                        normal: {
                            color: function () {
                                return 'rgb(' + [
                                    Math.round(Math.random() * 160),
                                    Math.round(Math.random() * 160),
                                    Math.round(Math.random() * 160)
                                ].join(',') + ')';
                            }
                        },
                        emphasis: {
                            shadowBlur: 10,
                            shadowColor: '#333'
                        }
                    },
                    data: wordCount
                }]
            };


            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
            window.addEventListener("resize", function () {
                myChart.resize();
            });
        });

    }

    function echarts_31() {
        $.get('/sales_top10_brand', function (data) {
            // 基于准备好的dom，初始化echarts实例
            data_pie = [];
            for (var i in data.x) {
                d = {};
                d['name'] = data.x[i];
                d['value'] = data.y[i];
                data_pie.push(d);
            }
            var myChart = echarts.init(document.getElementById('fb1'));
            option = {

                title: [{
                    text: '销量TOP10型号按品牌分布',
                    left: 'center',
                    textStyle: {
                        color: '#fff',
                        fontSize: '12'
                    }

                }],
                tooltip: {
                    trigger: 'item',
                    formatter: "{a} <br/>{b}: {c} ({d}%)",
                    position: function (p) {   //其中p为当前鼠标的位置
                        return [p[0] + 10, p[1] - 10];
                    }
                },
                legend: {

                    top: '70%',
                    itemWidth: 10,
                    itemHeight: 10,
                    data: data.x,
                    textStyle: {
                        color: 'rgba(255,255,255,.5)',
                        fontSize: '8',
                    }
                },
                series: [
                    {
                        name: '销量TOP10型号品牌分布',

                        type: 'pie',
                        center: ['50%', '42%'],
                        radius: ['40%', '60%'],
                        color: ['#065aab', '#066eab', '#0682ab', '#0696ab', '#06a0ab', '#06b4ab', '#06c8ab', '#06dcab', '#06f0ab'],
                        label: {show: false},
                        labelLine: {show: false},
                        data: data_pie
                    }
                ]
            };

            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
            window.addEventListener("resize", function () {
                myChart.resize();
            });
        });


    }

    function echarts_32() {
        $.get('/sales_top10_brand', function (data) {
            // 基于准备好的dom，初始化echarts实例
            data_pie = [];
            for (var i in data.x) {
                d = {};
                d['name'] = data.x[i];
                d['value'] = data.y[i];
                data_pie.push(d);
            }
            var myChart = echarts.init(document.getElementById('fb2'));
            option = {

                title: [{
                    text: '销量TOP10型号按品牌分布',
                    left: 'center',
                    textStyle: {
                        color: '#fff',
                        fontSize: '12'
                    }

                }],
                tooltip: {
                    trigger: 'item',
                    formatter: "{a} <br/>{b}: {c} ({d}%)",
                    position: function (p) {   //其中p为当前鼠标的位置
                        return [p[0] + 10, p[1] - 10];
                    }
                },
                legend: {

                    top: '70%',
                    itemWidth: 10,
                    itemHeight: 10,
                    data: data.x,
                    textStyle: {
                        color: 'rgba(255,255,255,.5)',
                        fontSize: '8',
                    }
                },
                series: [
                    {
                        name: '销量TOP10型号品牌分布',

                        type: 'pie',
                        center: ['50%', '42%'],
                        radius: ['40%', '60%'],
                        color: ['#065aab', '#066eab', '#0682ab', '#0696ab', '#06a0ab', '#06b4ab', '#06c8ab', '#06dcab', '#06f0ab'],
                        label: {show: false},
                        labelLine: {show: false},
                        data: data_pie
                    }
                ]
            };

            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
            window.addEventListener("resize", function () {
                myChart.resize();
            });
        });


    }
    function echarts_33() {
        $.get('/sales_top10_brand', function (data) {
            // 基于准备好的dom，初始化echarts实例
            data_pie = [];
            for (var i in data.x) {
                d = {};
                d['name'] = data.x[i];
                d['value'] = data.y[i];
                data_pie.push(d);
            }
            var myChart = echarts.init(document.getElementById('fb3'));
            option = {

                title: [{
                    text: '销量TOP10型号按品牌分布',
                    left: 'center',
                    textStyle: {
                        color: '#fff',
                        fontSize: '12'
                    }

                }],
                tooltip: {
                    trigger: 'item',
                    formatter: "{a} <br/>{b}: {c} ({d}%)",
                    position: function (p) {   //其中p为当前鼠标的位置
                        return [p[0] + 10, p[1] - 10];
                    }
                },
                legend: {

                    top: '70%',
                    itemWidth: 10,
                    itemHeight: 10,
                    data: data.x,
                    textStyle: {
                        color: 'rgba(255,255,255,.5)',
                        fontSize: '8',
                    }
                },
                series: [
                    {
                        name: '销量TOP10型号品牌分布',

                        type: 'pie',
                        center: ['50%', '42%'],
                        radius: ['40%', '60%'],
                        color: ['#065aab', '#066eab', '#0682ab', '#0696ab', '#06a0ab', '#06b4ab', '#06c8ab', '#06dcab', '#06f0ab'],
                        label: {show: false},
                        labelLine: {show: false},
                        data: data_pie
                    }
                ]
            };

            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
            window.addEventListener("resize", function () {
                myChart.resize();
            });
        });


    }

    // function echarts_32() {
    //     // 基于准备好的dom，初始化echarts实例
    //     var myChart = echarts.init(document.getElementById('fb2'));
    //     option = {
    //
    //         title: [{
    //             text: '各品牌商家数量分布hhhhh',
    //             left: 'center',
    //             textStyle: {
    //                 color: '#fff',
    //                 fontSize: '12'
    //             }
    //
    //         }],
    //         tooltip: {
    //             trigger: 'item',
    //             formatter: "{a} <br/>{b}: {c} ({d}%)",
    //             position: function (p) {   //其中p为当前鼠标的位置
    //                 return [p[0] + 10, p[1] - 10];
    //             }
    //         },
    //         legend: {
    //
    //             top: '70%',
    //             itemWidth: 10,
    //             itemHeight: 10,
    //             data: ['1', '2', '3', '4', '5', '6'],
    //             textStyle: {
    //                 color: 'rgba(255,255,255,.5)',
    //                 fontSize: '12',
    //             }
    //         },
    //         series: [
    //             {
    //                 name: '年龄分布',
    //                 type: 'pie',
    //                 center: ['50%', '42%'],
    //                 radius: ['40%', '60%'],
    //                 color: ['#065aab', '#066eab', '#0682ab', '#0696ab', '#06a0ab', '#06b4ab', '#06c8ab', '#06dcab', '#06f0ab'],
    //                 label: {show: false},
    //                 labelLine: {show: false},
    //                 data: [
    //                     {value: 5, name: '1'},
    //                     {value: 1, name: '2'},
    //                     {value: 6, name: '3'},
    //                     {value: 2, name: '4'},
    //                     {value: 1, name: '5'},
    //                     {value: 1, name: '6'},
    //                 ]
    //             }
    //         ]
    //     };
    //
    //     // 使用刚指定的配置项和数据显示图表。
    //     myChart.setOption(option);
    //     window.addEventListener("resize", function () {
    //         myChart.resize();
    //     });
    // }

    // function echarts_33() {
    //     // 基于准备好的dom，初始化echarts实例
    //     var myChart = echarts.init(document.getElementById('fb3'));
    //     option = {
    //         title: [{
    //             text: '？？？？',
    //             left: 'center',
    //             textStyle: {
    //                 color: '#fff',
    //                 fontSize: '12'
    //             }
    //
    //         }],
    //         tooltip: {
    //             trigger: 'item',
    //             formatter: "{a} <br/>{b}: {c} ({d}%)",
    //             position: function (p) {   //其中p为当前鼠标的位置
    //                 return [p[0] + 10, p[1] - 10];
    //             }
    //         },
    //         legend: {
    //             top: '70%',
    //             itemWidth: 10,
    //             itemHeight: 10,
    //             data: ['1', '2', '3', '4', '5', '6'],
    //             textStyle: {
    //                 color: 'rgba(255,255,255,.5)',
    //                 fontSize: '12',
    //             }
    //         },
    //         series: [
    //             {
    //                 name: '？？？？',
    //                 type: 'pie',
    //                 center: ['50%', '42%'],
    //                 radius: ['40%', '60%'],
    //                 color: ['#065aab', '#066eab', '#0682ab', '#0696ab', '#06a0ab', '#06b4ab', '#06c8ab', '#06dcab', '#06f0ab'],
    //                 label: {show: false},
    //                 labelLine: {show: false},
    //                 data: [
    //                     {value: 2, name: '1'},
    //                     {value: 3, name: '2'},
    //                     {value: 1, name: '3'},
    //                     {value: 4, name: '4'},
    //                     {value: 8, name: '5'},
    //                     {value: 1, name: '6'},
    //                 ]
    //             }
    //         ]
    //     };
    //
    //     // 使用刚指定的配置项和数据显示图表。
    //     myChart.setOption(option);
    //     window.addEventListener("resize", function () {
    //         myChart.resize();
    //     });
    // }


});



		
		
		


		









