# GetConfigurationByName2 Method (ISwDMConfigurationMgr2)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2~GetConfigurationByName2`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2~GetConfigurationByName2.html) on this topic. |
| GetConfigurationByName2 Method (ISwDMConfigurationMgr2) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfigurationMgr2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2.md) : GetConfigurationByName2 Method (ISwDMConfigurationMgr2) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*ConfigurationName*
:   Name of configuration to get (see **Remarks**)

*result*
:   Return code as defined in [swDMConfigurationError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDMConfigurationError.md)

Gets the specified configuration in the document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetConfigurationByName2( _    ByVal ConfigurationName As System.String, _    ByRef result As SwDMConfigurationError _ ) As SwDMConfiguration ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfigurationMgr2 Dim ConfigurationName As System.String Dim result As SwDMConfigurationError Dim value As SwDMConfiguration   value = instance.GetConfigurationByName2(ConfigurationName, result) ``` | |

| C# |  |
| --- | --- |
| ``` SwDMConfiguration GetConfigurationByName2(     System.string ConfigurationName,    out SwDMConfigurationError result ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDMConfiguration^ GetConfigurationByName2(  &   System.String^ ConfigurationName, &   [Out] SwDMConfigurationError result ) ``` | |

#### Parameters

*ConfigurationName*
:   Name of configuration to get (see **Remarks**)

*result*
:   Return code as defined in [swDMConfigurationError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDMConfigurationError.md)

#### Return Value

Pointer to an [ISwDMConfiguration](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.md) object

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfigurationMgr2::GetConfigurationByName2](swdocumentmgr~SwDMConfigurationMgr2~GetConfigurationByName2.md).

# Example

See the [ISwDMConfigurationMgr2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2.md) examples.

# Remarks

Call [ISwDMConfigurationMgr2::GetConfigurationNames2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2~GetConfigurationNames2.md) before calling this method.

# See Also

#### 

[ISwDMConfigurationMgr2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2.md)
  
[ISwDMConfigurationMgr2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2_members.md)
  
[ISwDMComponent::ConfigurationName Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~ConfigurationName.md)
  
[ISwDMConfiguration::GetParentConfigurationName Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetParentConfigurationName.md)
  
[ISwDMConfiguration7::Name2 Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~Name2.md)

# Availability

SOLIDWORKS Document Manager API 2019 SP0
