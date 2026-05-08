# Transform Property (ISwDMComponent)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~Transform`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~Transform.html) on this topic. |
| Transform Property (ISwDMComponent) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMComponent Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent.md) : Transform Property (ISwDMComponent) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the transform for this component.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property Transform As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMComponent Dim value As System.Object   value = instance.Transform ``` | |

| C# |  |
| --- | --- |
| ``` System.object Transform {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.Object^ Transform {    System.Object^ get(); } ``` | |

#### Property Value

Array containing 16 elements that define the transform:

- First 12 elements are in a 4x3 matrix:   
  |a, b, c|  
  |d, e, f|  
  |g, h, i|  
  |j, k, l|
- Next 3 elements define translation:   
  |m, n, o|
- Last 1 element is the scaling value:   
  |n|

Be aware that the SOLIDWORKS API method IComponent2::Transform2 returns an IMathTransform object, whose 16 elements are ordered differently. See the SOLIDWORKS API Help for details about IComponent2::Transform2 and IMathTransform.

# Visual Basic for Applications (VBA) Syntax

See [SwDMComponent::Transform](swdocumentmgr~SwDMComponent~Transform.md).

# Remarks

This property only supports documents saved in SOLIDWORKS 2003 (Version 2200) and later. To get the version of a document, use [ISwDMDocument::GetVersion](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetVersion.md).

# See Also

#### 

[ISwDMComponent Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent.md)
  
[ISwDMComponent Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent_members.md)

# Availability

SOLIDWORKS Document Manager API 2004 SP1
