import { Component, PLATFORM_ID, Inject } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';
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

  constructor(@Inject(PLATFORM_ID) private platformId: Object) {}

  ngOnInit() {
    // Dummy data to initialize Cytoscape.js
    // Check if the platform is browser before initializing Cytoscape.js
    if (isPlatformBrowser(this.platformId)) {
      const dummyData = {
        nodes: [
          { id: '1', label: 'Node 1' },
          { id: '2', label: 'Node 2' },
          { id: '3', label: 'Node 3' }
        ],
        edges: [
          { source: '1', target: '2', label: 'Edge 1-2' },
          { source: '1', target: '3', label: 'Edge 1-3' }
        ]
      };

      this.initCytoscape(dummyData);
    }
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
              'color': '#fff',
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
