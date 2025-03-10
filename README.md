# InsightsAI Semantic Document Search Tool

**[Try the Live Demo](https://insights-ai-nhe1.vercel.app/insight)**

## Overview
InsightsAI is an advanced semantic search tool that allows users to quickly find specific information across multiple documents. By using a priority-based approach to context extraction, the system delivers highly relevant search results even from large document collections. The intuitive interface makes it easy for users to upload, organize, and search through documents of any complexity.

## Core Features

### 1. Intelligent Document Processing
- **Priority-Based Context Extraction**: Documents in the priority zone receive enhanced context extraction at the backend
- **Smart Document Organization**: Two-zone system for differentiating critical vs. standard reference materials
- **Efficient Document Management**: Easy upload, organization, and removal of documents

### 2. Powerful Semantic Search
- **Natural Language Queries**: Search using everyday language rather than exact keywords
- **Instant Results**: Real-time search results as you type in the search bar
- **Structured Result Display**: Well-organized dropdown with relevant excerpts from documents
- **Source Attribution**: Each result is paired with its source file name for easy reference

### 3. Interactive Document Zones
- **Priority Zone**: Documents that require more thorough context extraction for critical information
- **Normal Zone**: Standard documents for regular searching
- **Drag & Drop Interface**: Easily reorganize and prioritize documents based on importance

### 4. User-Friendly Search Experience
- **Quick Search**: Rapidly find specific details within large documents
- **Contextual Results**: Search results include surrounding context for better understanding
- **Visual Distinction**: Clear identification of search results by document source

## User Flow

1. **Upload Documents**: Users add documents to the system
2. **Organize by Priority**: Drag critical documents to the priority zone for enhanced context extraction
3. **Search Content**: Use the search bar to query information across all documents
4. **Interact with Results**: Explore the dropdown of semantically relevant results
5. **Find Specific Details**: Quickly locate exact information within large documents
6. **Identify Sources**: See which document each result comes from

## Implementation Showcase

### Screenshots

#### Search Bar Implementation
![Search Bar Screenshot](/screenshots/search-bar.png)
*The intelligent search bar allows users to input natural language queries and displays semantic search results in real-time.*

#### Document Organization System
![Document Zones Screenshot](/screenshots/doc-base.png)
*Our dual-zone document system enables users to distinguish between priority documents (receiving enhanced context extraction) and regular reference materials.*


## Technical Architecture

### Frontend Stack
- **React with TypeScript**: For type-safe, component-based UI development
- **Next.js**: For optimized rendering and improved performance
- **Tailwind CSS**: For responsive, utility-first styling
- **Radix UI**: For accessible UI components

### Key Design Decisions

#### 1. Dual Priority System
Documents are organized into priority and normal zones, which affects how thoroughly the backend processes and extracts context from each document, leading to more accurate search results for high-priority materials.

#### 2. Real-Time Semantic Search
The application provides immediate search results as users type, using semantic understanding rather than simple keyword matching to deliver more relevant content.

#### 3. Streamlined User Experience
The drag-and-drop interface combined with the real-time search results creates a fluid experience that minimizes friction when working with large document collections.

#### 4. Rich Search Results
Search results display in an organized dropdown that shows not just matching text but relevant surrounding context, making it easier to determine which result contains the needed information.

## Future Enhancements

- Mobile-friendly interface
- Keyboard shortcuts for power users
- Dark mode support
- PDF annotation tools
- Saved searches

InsightsAI transforms the document search experience by combining intelligent context extraction with intuitive user interaction, making it remarkably simple to find specific information across multiple complex documents.
