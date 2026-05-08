# GetConfigurationNames2 Method (ISwDMConfigurationMgr2)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2~GetConfigurationNames2`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2~GetConfigurationNames2.html) on this topic. |
| GetConfigurationNames2 Method (ISwDMConfigurationMgr2) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfigurationMgr2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2.md) : GetConfigurationNames2 Method (ISwDMConfigurationMgr2) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*result*
:   Return code as defined in [swDMConfigurationError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDMConfigurationError.md)

Gets the names of the configurations in this document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetConfigurationNames2( _    ByRef result As SwDMConfigurationError _ ) As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfigurationMgr2 Dim result As SwDMConfigurationError Dim value As System.Object   value = instance.GetConfigurationNames2(result) ``` | |

| C# |  |
| --- | --- |
| ``` System.object GetConfigurationNames2(     out SwDMConfigurationError result ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.Object^ GetConfigurationNames2(  &   [Out] SwDMConfigurationError result ) ``` | |

#### Parameters

*result*
:   Return code as defined in [swDMConfigurationError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDMConfigurationError.md)

#### Return Value

Array of configuration names

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfigurationMgr2::GetConfigurationNames2](swdocumentmgr~SwDMConfigurationMgr2~GetConfigurationNames2.md).

# Example

See the [ISwDMConfigurationMgr2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2.md) examples.

# Remarks

Call this method before calling [ISwDMConfigurationMgr2::GetConfigurationByName2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2~GetConfigurationByName2.md).

# See Also

#### 

[ISwDMConfigurationMgr2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2.md)
  
[ISwDMConfigurationMgr2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2_members.md)
  
[ISwDMComponent::ConfigurationName Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~ConfigurationName.md)
  
[ISwDMConfiguration::GetParentConfigurationName Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetParentConfigurationName.md)
  
[ISwDMConfiguration7::Name2 Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~Name2.md)

# Availability

SOLIDWORKS Document Manager API 2019 SP0
