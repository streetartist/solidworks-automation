# BrokenStatus Property (ISwDMExternalReferenceOption2)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption2~BrokenStatus`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption2~BrokenStatus.html) on this topic. |
| BrokenStatus Property (ISwDMExternalReferenceOption2) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMExternalReferenceOption2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption2.md) : BrokenStatus Property (ISwDMExternalReferenceOption2) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets whether the external references are broken in the document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property BrokenStatus As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMExternalReferenceOption2 Dim value As System.Object   value = instance.BrokenStatus ``` | |

| C# |  |
| --- | --- |
| ``` System.object BrokenStatus {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.Object^ BrokenStatus {    System.Object^ get(); } ``` | |

#### Property Value

Array of integers of the statuses of the external references as defined in [swDmReferenceStatus](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmReferenceStatus.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMExternalReferenceOption2::BrokenStatus](swdocumentmgr~SwDMExternalReferenceOption2~BrokenStatus.md).

# Example

[Get External References for Part (C#)](Get_External_References_for_Part_Example_CSharp.htm)
  
[Get External References for Part (VB.NET)](Get_External_References_for_Part_Example_VBNET.htm)

# Remarks

# See Also

#### 

[ISwDMExternalReferenceOption2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption2.md)
  
[ISwDMExternalReferenceOption2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption2_members.md)

# Availability

SOLIDWORKS Document Manager API 2014 SP0
