import { Routes } from '@angular/router';
import { MenuMeta, RouteComponent } from 'componentex';
import { ReportesListComponent } from './reportes/reportes.component';
import { ReportesService } from './reportes/reportes.service';

export const NovedadesRoutes: Routes = [
    {
        path: '', children: [
            {
                path: 'reportes', component: RouteComponent, data: { miga: 'Reportes' }, children: [
                    { path: '', component: ReportesListComponent }
                ]
            }
        ]
    }
]

export const NovedadesMenuMeta: MenuMeta[] = [
    { title: 'Reportes', url: '/novedades/reportes', icon: 'report' }
]