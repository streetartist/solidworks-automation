# GetRepresentationParent Method (ISwDMConfiguration17)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17~GetRepresentationParent`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17~GetRepresentationParent.html) on this topic. |
| GetRepresentationParent Method (ISwDMConfiguration17) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration17 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17.md) : GetRepresentationParent Method (ISwDMConfiguration17) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the Physical Product represented by this configuration in [SOLIDWORKS Connected](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm).

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetRepresentationParent() As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration17 Dim value As System.String   value = instance.GetRepresentationParent() ``` | |

| C# |  |
| --- | --- |
| ``` System.string GetRepresentationParent() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.String^ GetRepresentationParent(); ``` | |

#### Return Value

Physical Product name

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration17::GetRepresentationParent](swdocumentmgr~SwDMConfiguration17~GetRepresentationParent.md).

# Example

See the [ISwDMConfiguration17](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17.md) examples.

# Remarks

This method is valid only:

- For [SOLIDWORKS Connected](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm)

          - and -

- If [ISWDMConfiguration17::Get3DExperienceType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17~Get3DExperienceType.md) does not return 0.

# See Also

#### 

[ISwDMConfiguration17 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17.md)
  
[ISwDMConfiguration17 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17_members.md)

# Availability

SOLIDWORKS Document Manager API 2020 SP03.1
