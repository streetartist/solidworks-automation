# Subject Property (ISwDMDocument)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Subject`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Subject.html) on this topic. |
| Subject Property (ISwDMDocument) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md) : Subject Property (ISwDMDocument) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets or sets the subject text for this document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Property Subject As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument Dim value As System.String   instance.Subject = value   value = instance.Subject ``` | |

| C# |  |
| --- | --- |
| ``` System.string Subject {get; set;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.String^ Subject {    System.String^ get();    void set ( &   System.String^ value); } ``` | |

#### Property Value

Subject text

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument::Subject](swdocumentmgr~SwDMDocument~Subject.md).

# Example

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
  
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

# See Also

#### 

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md)
  
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.md)
  
[ISwDMDocument::Author Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Author.md)
  
[ISwDMDocument::Comments Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Comments.md)
  
[ISwDMDocument::CreationDate Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~CreationDate.md)
  
[ISwDMDocument19::CreationDate2 Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~CreationDate2.md)
  
[ISwDMDocument::Keywords Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Keywords.md)
  
[ISwDMDocument::LastSavedBy Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedBy.md)
  
[ISwDMDocument::LastSavedDate Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~LastSavedDate.md)
  
[ISwDMDocument19::LastSavedDate2 Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~LastSavedDate2.md)
  
[ISwDMDocument::Title Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Title.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS
