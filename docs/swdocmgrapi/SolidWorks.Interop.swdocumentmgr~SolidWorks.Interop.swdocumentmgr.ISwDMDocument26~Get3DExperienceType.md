# Get3DExperienceType Method (ISwDMDocument26)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument26~Get3DExperienceType`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument26~Get3DExperienceType.html) on this topic. |
| Get3DExperienceType Method (ISwDMDocument26) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument26 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument26.md) : Get3DExperienceType Method (ISwDMDocument26) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the type of 3DEXPERIENCE application that created this document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function Get3DExperienceType() As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument26 Dim value As System.Integer   value = instance.Get3DExperienceType() ``` | |

| C# |  |
| --- | --- |
| ``` System.int Get3DExperienceType() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.int Get3DExperienceType(); ``` | |

#### Return Value

3DEXPERIENCE model type as defined by [swDm3DExperienceModelType\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDm3DExperienceModelType_e.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument26::Get3DExperienceType](swdocumentmgr~SwDMDocument26~Get3DExperienceType.md).

 

# See Also

#### 

[ISwDMDocument26 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument26.md)
  
[ISwDMDocument26 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument26_members.md)

# Availability

SOLIDWORKS Document Manager API 2021 SP0
