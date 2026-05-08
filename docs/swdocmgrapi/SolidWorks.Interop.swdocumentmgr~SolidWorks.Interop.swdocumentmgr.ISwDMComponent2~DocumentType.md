# DocumentType Property (ISwDMComponent2)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent2~DocumentType`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent2~DocumentType.html) on this topic. |
| DocumentType Property (ISwDMComponent2) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMComponent2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent2.md) : DocumentType Property (ISwDMComponent2) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the component's document type.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property DocumentType As SwDmDocumentType ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMComponent2 Dim value As SwDmDocumentType   value = instance.DocumentType ``` | |

| C# |  |
| --- | --- |
| ``` SwDmDocumentType DocumentType {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property SwDmDocumentType DocumentType {    SwDmDocumentType get(); } ``` | |

#### Property Value

Component's document type as defined in [swDMDocumentType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDocumentType.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMComponent2::DocumentType](swdocumentmgr~SwDMComponent2~DocumentType.md).

# Remarks

This property can distinguish between components and sub-assemblies whose names are the same.

# See Also

#### 

[ISwDMComponent2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent2.md)
  
[ISwDMComponent2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent2_members.md)

# Availability

SOLIDWORKS Document Manager API 2005 FCS
