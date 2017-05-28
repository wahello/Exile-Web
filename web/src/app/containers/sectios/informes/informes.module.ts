import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

import { InformesRoutes } from './informes.route';

@NgModule({
    imports: [
        RouterModule.forChild(InformesRoutes),
        CommonModule
    ],
    declarations: [],
    providers: []
})
export class InformesModule { } 
