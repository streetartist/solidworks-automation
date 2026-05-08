# ConfigurationName Property (ISwDMComponent)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~ConfigurationName`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~ConfigurationName.html) on this topic. |
| ConfigurationName Property (ISwDMComponent) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMComponent Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent.md) : ConfigurationName Property (ISwDMComponent) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the name of the configuration for this component.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property ConfigurationName As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMComponent Dim value As System.String   value = instance.ConfigurationName ``` | |

| C# |  |
| --- | --- |
| ``` System.string ConfigurationName {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.String^ ConfigurationName {    System.String^ get(); } ``` | |

#### Property Value

Name of the configuration for this component

# Visual Basic for Applications (VBA) Syntax

See [SwDMComponent::ConfigurationName](swdocumentmgr~SwDMComponent~ConfigurationName.md).

# Example

[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
  
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)

# Remarks

This property only supports documents saved in SOLIDWORKS 2003 (Version 2200) and later. To get the version of a document, use [ISwDMDocument::GetVersion](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetVersion.md).

# See Also

#### 

[ISwDMComponent Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent.md)
  
[ISwDMComponent Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent_members.md)
  
[ISwDMComponent::Name Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~Name.md)
  
[ISwDMConfiguration::GetParentConfigurationName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetParentConfigurationName.md)
  
[ISwDMConfiguration7::Name2 Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~Name2.md)
  
[ISwDMConfigurationMgr::GetActiveConfigurationName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr~GetActiveConfigurationName.md)
  
[ISwDMConfigurationMgr::GetConfigurationByName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr~GetConfigurationByName.md)

# Availability

SOLIDWORKS Document Manager API 2004 SP1
