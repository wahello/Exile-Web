import { Component, OnInit, ElementRef } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { CallService } from './call.service';

declare var $: any;
// declare var fetch: any;
@Component({
    selector: 'exile-app',
    templateUrl: './app.component.html'
})

export class AppComponent implements OnInit {
    constructor(private elRef: ElementRef, private _cl: CallService) {
        this._cl.conf('104.236.33.228', '8000');
    }

    ngOnInit() {
        let body = document.getElementsByTagName('body')[0];
        let isWindows = navigator.platform.indexOf('Win') > -1 ? true : false;
        if (isWindows) {
            body.classList.add('perfect-scrollbar-on');
        } else {
            body.classList.add('perfect-scrollbar-off');
        }
        $.material.init();
    }
}