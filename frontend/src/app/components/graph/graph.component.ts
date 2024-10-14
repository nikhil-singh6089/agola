import { Component, PLATFORM_ID, Inject } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import cytoscape from 'cytoscape';

@Component({
  selector: 'app-graph',
  standalone: true,
  imports: [],
  templateUrl: './graph.component.html',
  styleUrl: './graph.component.css'
})
export class GraphComponent {
  cy: any;
  apiUrl: string = 'http://127.0.0.1:5000/api/graph-data';

  constructor(@Inject(PLATFORM_ID) private platformId: Object, private http: HttpClient ) {}

  ngOnInit() {
    // Dummy data to initialize Cytoscape.js
    // Check if the platform is browser before initializing Cytoscape.js
    if (isPlatformBrowser(this.platformId)) {
      this.fetchGraphData();
    }
  }

  fetchGraphData() {
    this.http.get(this.apiUrl).subscribe(
      (data: any) => {
        console.log('Graph data:', data);
        this.initCytoscape(data); // Initialize Cytoscape.js with API data
      },
      (error) => {
        console.error('Error fetching graph data:', error);
      }
    );
  }

  // Initialize Cytoscape.js with graph data
  initCytoscape(graphData: any) {
    const elements = this.prepareElements(graphData);

    // Only run if platform is browser
    if (isPlatformBrowser(this.platformId)) {
      this.cy = cytoscape({
        container: document.getElementById('cy'),
        elements: elements,
        style: [
          {
            selector: 'node',
            style: {
              'label': 'data(label)',
              'background-color': '#0074D9',
              'color': '#000',
              'text-valign': 'center',
              'text-halign': 'center',
              'font-size': '8px'
            }
          },
          {
            selector: 'edge',
            style: {
              'label': 'data(label)',
              'width': 3,
              'color': '#000',
              'line-color': '#aaa',
              'target-arrow-color': '#aaa',
              'target-arrow-shape': 'triangle'
            }
          }
        ],
        layout: {
          name: 'cose',
          padding: 10
        }
      });
    }
  }

  prepareElements(graphData: any) {
    const elements : any[] = [];

    graphData.nodes.forEach((node: any) => {
      elements.push({ data: { id: node.id, label: node.label } });
    });

    graphData.edges.forEach((edge: any) => {
      elements.push({
        data: { source: edge.source, target: edge.target, label: edge.label }
      });
    });

    return elements;
  }
}
