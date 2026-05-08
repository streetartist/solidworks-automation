# Get3DExperienceType Method (ISwDMConfiguration17)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17~Get3DExperienceType`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17~Get3DExperienceType.html) on this topic. |
| Get3DExperienceType Method (ISwDMConfiguration17) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration17 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17.md) : Get3DExperienceType Method (ISwDMConfiguration17) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets how [SOLIDWORKS Connected](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm) views this configuration.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function Get3DExperienceType() As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration17 Dim value As System.Integer   value = instance.Get3DExperienceType() ``` | |

| C# |  |
| --- | --- |
| ``` System.int Get3DExperienceType() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.int Get3DExperienceType(); ``` | |

#### Return Value

Treatment of this configuration as defined by [swDm3DExperienceCfgType\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDm3DExperienceCfgType_e.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration17::Get3DExperienceType](swdocumentmgr~SwDMConfiguration17~Get3DExperienceType.md).

# Example

See the [ISwDMConfiguration17](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17.md) examples.

# See Also

#### 

[ISwDMConfiguration17 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17.md)
  
[ISwDMConfiguration17 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17_members.md)
  
[ISwDMConfiguration17::GetRepresentationParent Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17~GetRepresentationParent.md)

# Availability

SOLIDWORKS Document Manager API 2020 SP03.1
