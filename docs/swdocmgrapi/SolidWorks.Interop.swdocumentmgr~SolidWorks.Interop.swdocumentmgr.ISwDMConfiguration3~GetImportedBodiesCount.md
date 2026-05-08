# GetImportedBodiesCount Method (ISwDMConfiguration3)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration3~GetImportedBodiesCount`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration3~GetImportedBodiesCount.html) on this topic. |
| GetImportedBodiesCount Method (ISwDMConfiguration3) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration3.md) : GetImportedBodiesCount Method (ISwDMConfiguration3) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the number of imported solid bodies in this configuration.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetImportedBodiesCount() As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration3 Dim value As System.Integer   value = instance.GetImportedBodiesCount() ``` | |

| C# |  |
| --- | --- |
| ``` System.int GetImportedBodiesCount() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.int GetImportedBodiesCount(); ``` | |

#### Return Value

Number of imported solid bodies; this is a 0-based index

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration3::GetImportedBodiesCount](swdocumentmgr~SwDMConfiguration3~GetImportedBodiesCount.md).

# Remarks

This method does not include the number of imported surface bodies, if any.

Call this method before [ISwDMConfiguration3::GetImportedBody](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration3~GetImportedBody.md).

# See Also

#### 

[ISwDMConfiguration3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration3.md)
  
[ISwDMConfiguration3 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration3_members.md)
  
[ISwDMConfiguration::GetBodiesCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetBodiesCount.md)
  
[ISwDMConfiguration::GetBody Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetBody.md)

# Availability

SOLIDWORKS Document Manager API 2004 SP2
