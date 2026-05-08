# RemoveSearchPath Method (ISwDMSearchOption)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption~RemoveSearchPath`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption~RemoveSearchPath.html) on this topic. |
| RemoveSearchPath Method (ISwDMSearchOption) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMSearchOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.md) : RemoveSearchPath Method (ISwDMSearchOption) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*remPath*
:   Search path to remove; for example, C:\parts

Removes the specified search path.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Sub RemoveSearchPath( _    ByVal remPath As System.String _ ) ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMSearchOption Dim remPath As System.String   instance.RemoveSearchPath(remPath) ``` | |

| C# |  |
| --- | --- |
| ``` void RemoveSearchPath(     System.string remPath ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` void RemoveSearchPath(  &   System.String^ remPath ) ``` | |

#### Parameters

*remPath*
:   Search path to remove; for example, C:\parts

# Visual Basic for Applications (VBA) Syntax

See [SwDMSearchOption::RemoveSearchPath](swdocumentmgr~SwDMSearchOption~RemoveSearchPath.md).

 

# See Also

#### 

[ISwDMSearchOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.md)
  
[ISwDMSearchOption Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption_members.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS
