# DimXpertPart Property (ISwDMConfiguration12)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12~DimXpertPart`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12~DimXpertPart.html) on this topic. |
| DimXpertPart Property (ISwDMConfiguration12) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration12 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12.md) : DimXpertPart Property (ISwDMConfiguration12) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the DimXpert part associated with this configuration.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property DimXpertPart As SwDMDimXpertPart ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration12 Dim value As SwDMDimXpertPart   value = instance.DimXpertPart ``` | |

| C# |  |
| --- | --- |
| ``` SwDMDimXpertPart DimXpertPart {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property SwDMDimXpertPart^ DimXpertPart {    SwDMDimXpertPart^ get(); } ``` | |

#### Property Value

[ISwDMDimXpertPart](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration12::DimXpertPart](swdocumentmgr~SwDMConfiguration12~DimXpertPart.md).

# Example

[Get DimXpert Block Tolerance (VB.NET)](Get_DimXpert_Block_Tolerance_Example_VBNET.htm)
  
[Get DimXpert Block Tolerance (C#)](Get_DimXpert_Block_Tolerance_Example_CSharp.htm)

# See Also

#### 

[ISwDMConfiguration12 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12.md)
  
[ISwDMConfiguration12 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
