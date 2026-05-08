# GetLastUpdateStamp Method (ISwDMConfiguration)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetLastUpdateStamp`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetLastUpdateStamp.html) on this topic. |
| GetLastUpdateStamp Method (ISwDMConfiguration) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.md) : GetLastUpdateStamp Method (ISwDMConfiguration) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the date that this configuration was last updated.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetLastUpdateStamp() As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration Dim value As System.Integer   value = instance.GetLastUpdateStamp() ``` | |

| C# |  |
| --- | --- |
| ``` System.int GetLastUpdateStamp() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.int GetLastUpdateStamp(); ``` | |

#### Return Value

Date last updated

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration::GetLastUpdateStamp](swdocumentmgr~SwDMConfiguration~GetLastUpdateStamp.md).

# Example

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
  
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

# Remarks

The update stamp is essentially an integer form of a time stamp. The update stamp in a SOLIDWORKS document is incremented when:

- the state of the model changes (for example, you suppress or unsuppress a feature in a part or an assembly)
- the geometry changes (for example, any action that requires a rebuild)

This time stamp is not incremented for such operations as color changes, feature or configuration name changes, and so on.

# See Also

#### 

[ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.md)
  
[ISwDMConfiguration Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration_members.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS
