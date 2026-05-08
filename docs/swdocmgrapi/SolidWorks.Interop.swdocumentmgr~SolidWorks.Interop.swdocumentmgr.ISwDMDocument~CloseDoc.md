# CloseDoc Method (ISwDMDocument)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~CloseDoc`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~CloseDoc.html) on this topic. |
| CloseDoc Method (ISwDMDocument) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md) : CloseDoc Method (ISwDMDocument) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Closes the document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Sub CloseDoc() ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument   instance.CloseDoc() ``` | |

| C# |  |
| --- | --- |
| ``` void CloseDoc() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` void CloseDoc(); ``` | |

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument::CloseDoc](swdocumentmgr~SwDMDocument~CloseDoc.md).

# Example

[Open and Close Document (C++)](Open_and_Close_Document_Example_CPlusCPlus_COM.htm)
  
[Get Drawing Sheets' Properties (C#)](Get_Drawing_Sheets_Properties_Example_CSharp.htm)
  
[Get Drawing Sheets' Properties (VB.NET)](Get_Drawing_Sheets_Properties_Example_vbnet.htm)

# Remarks

You must call this method to close a document before calling:

- [ISwDMApplication::CopyDocument](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~CopyDocument.md)
- [ISwDMApplication::MoveDocument](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~MoveDocument.md)

If you update a document, call this method to close it before attempting to create a new assembly with it.

# See Also

#### 

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md)
  
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS
