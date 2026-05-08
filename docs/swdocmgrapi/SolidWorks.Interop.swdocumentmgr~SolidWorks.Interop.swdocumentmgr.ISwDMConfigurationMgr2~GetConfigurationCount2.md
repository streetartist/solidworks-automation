# GetConfigurationCount2 Method (ISwDMConfigurationMgr2)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2~GetConfigurationCount2`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2~GetConfigurationCount2.html) on this topic. |
| GetConfigurationCount2 Method (ISwDMConfigurationMgr2) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfigurationMgr2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2.md) : GetConfigurationCount2 Method (ISwDMConfigurationMgr2) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*result*
:   Return code as defined in [swDMConfigurationError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDMConfigurationError.md)

Gets the number of configurations in this document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetConfigurationCount2( _    ByRef result As SwDMConfigurationError _ ) As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfigurationMgr2 Dim result As SwDMConfigurationError Dim value As System.Integer   value = instance.GetConfigurationCount2(result) ``` | |

| C# |  |
| --- | --- |
| ``` System.int GetConfigurationCount2(     out SwDMConfigurationError result ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.int GetConfigurationCount2(  &   [Out] SwDMConfigurationError result ) ``` | |

#### Parameters

*result*
:   Return code as defined in [swDMConfigurationError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDMConfigurationError.md)

#### Return Value

Number of configurations

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfigurationMgr2::GetConfigurationCount2](swdocumentmgr~SwDMConfigurationMgr2~GetConfigurationCount2.md).

# Example

See the [ISwDMConfigurationMgr2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2.md) examples.

# See Also

#### 

[ISwDMConfigurationMgr2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2.md)
  
[ISwDMConfigurationMgr2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2_members.md)

# Availability

SOLIDWORKS Document Manager API 2019 SP0
