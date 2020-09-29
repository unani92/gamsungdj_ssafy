<template>
    <div height>
        <b-colxx class="col-sm-8" style="display:inline-block; float:left">
            <b-row>
            <wordcloud
                :data="defaultWords"
                nameKey="name"
                valueKey="value"
                :color="myColors"
                :showTooltip="true"
                :wordClick="wordClickHandler"
            >
            </wordcloud>
            </b-row>
        </b-colxx>
        <b-colxx class="col-sm-3" style="display:inline-block; float:right">
            <b-row class="mb-3">
                <b-colxx>
                    <b-card class="h-100" title="분석1">
                        <div class="dashboard-donut-chart">
                            <doughnut-chart :data="doughnutChartData" shadow />
                        </div>
                    </b-card>
                </b-colxx>
            </b-row>
            <b-row>
                <b-colxx>
                    <b-card title="분석2">
                        <div v-for="(s,index) in profileStatuses" :key="index" class="mb-4">
                        <p class="mb-2">
                            {{ s.title }}
                            <span class="float-right text-muted">{{s.status}}/{{s.total}}</span>
                        </p>
                        <b-progress :value="(s.status / s.total) * 100"></b-progress>
                        </div>
                    </b-card>
                </b-colxx>
            </b-row>
        </b-colxx>
    </div>
</template>

<script>
import wordcloud from 'vue-wordcloud'
import { doughnutChartData } from "../../data/charts";
import DoughnutChart from "../../components/Charts/Doughnut";
export default {
    components: {
        wordcloud,
        "doughnut-chart": DoughnutChart
    },
    data() {
        return {
            myColors: ['#1f77b4', '#629fc9', '#94bedb', '#c9e0ef'],
            defaultWords:
            [
                {
                    "name": "Cat",
                    "value": 26
                },
                {
                    "name": "fish",
                    "value": 19
                },
                {
                    "name": "things",
                    "value": 18
                },
                {
                    "name": "look",
                    "value": 16
                },
                {
                    "name": "two",
                    "value": 15
                },
                {
                    "name": "fun",
                    "value": 9
                },
                {
                    "name": "know",
                    "value": 9
                },
                {
                    "name": "good",
                    "value": 9
                },
                {
                    "name": "play",
                    "value": 6
                }
            ],
            profileStatuses:
            [
                {
                    title: 'Basic Information',
                    total: 18,
                    status: 12
                },
                {
                    title: 'Portfolio',
                    total: 8,
                    status: 1
                },
                {
                    title: 'Billing Details',
                    total: 6,
                    status: 2
                },
                {
                    title: 'Interests',
                    total: 10,
                    status: 0
                },
                {
                    title: 'Legal Documents',
                    total: 2,
                    status: 1
                }
            ],
            doughnutChartData,
        }
    },
    methods: {
        wordClickHandler(name, value, vm) {
            console.log('wordClickHandler', name, value, vm);
        }
    },
}
</script>

<style>

</style>