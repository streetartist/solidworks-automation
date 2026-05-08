# IsVirtual Property (ISwDMComponent3)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent3~IsVirtual`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent3~IsVirtual.html) on this topic. |
| IsVirtual Property (ISwDMComponent3) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMComponent3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent3.md) : IsVirtual Property (ISwDMComponent3) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets whether this component is a virtual component.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Property IsVirtual As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMComponent3 Dim value As System.Boolean   instance.IsVirtual = value   value = instance.IsVirtual ``` | |

| C# |  |
| --- | --- |
| ``` System.bool IsVirtual {get; set;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.bool IsVirtual {    System.bool get();    void set ( &   System.bool value); } ``` | |

#### Property Value

True if this component is virtual, false if not

# Visual Basic for Applications (VBA) Syntax

See [SwDMComponent3::IsVirtual](swdocumentmgr~SwDMComponent3~IsVirtual.md).

# Remarks

This property is only valid for assemblies saved in SOLIDWORKS 2008 and later. See the SOLIDWORKS Help for information about virtual components.

# See Also

#### 

[ISwDMComponent3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent3.md)
  
[ISwDMComponent3 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent3_members.md)

# Availability

SOLIDWORKS Document Manager API 2008 FCS
