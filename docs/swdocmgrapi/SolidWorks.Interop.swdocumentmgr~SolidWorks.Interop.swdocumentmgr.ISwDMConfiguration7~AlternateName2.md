# AlternateName2 Property (ISwDMConfiguration7)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~AlternateName2`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~AlternateName2.html) on this topic. |
| AlternateName2 Property (ISwDMConfiguration7) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration7 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7.md) : AlternateName2 Property (ISwDMConfiguration7) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets or sets the user-specified name of the configuration.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Property AlternateName2 As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration7 Dim value As System.String   instance.AlternateName2 = value   value = instance.AlternateName2 ``` | |

| C# |  |
| --- | --- |
| ``` System.string AlternateName2 {get; set;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.String^ AlternateName2 {    System.String^ get();    void set ( &   System.String^ value); } ``` | |

#### Property Value

Alternate or user-specified name of the configuration

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration7::AlternateName2](swdocumentmgr~SwDMConfiguration7~AlternateName2.md).

# Remarks

This property only supports documents saved in SOLIDWORKS 2005 and later. To get the version of a document, use [ISwDMDocument::GetVersion](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetVersion.md).

If you set [ISwDMConfiguration11::BOMPartNoSource](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~BOMPartNoSource.md) to anything other than [swDmBOMPartNumberSource](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmBOMPartNumberSource.md).swDmBOMPartNumber\_UserSpecified, then this property is set to an empty string.

# See Also

#### 

[ISwDMConfiguration7 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7.md)
  
[ISwDMConfiguration7 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7_members.md)

# Availability

SOLIDWORKS Document Manager API 2007 FCS
