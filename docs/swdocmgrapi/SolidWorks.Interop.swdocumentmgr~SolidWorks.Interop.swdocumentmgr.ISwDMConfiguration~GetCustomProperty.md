# GetCustomProperty Method (ISwDMConfiguration)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomProperty`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomProperty.html) on this topic. |
| GetCustomProperty Method (ISwDMConfiguration) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.md) : GetCustomProperty Method (ISwDMConfiguration) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*FieldName*
:   Name of the custom property

*type*
:   Type of custom property as defined by [SwDmCustomInfoType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCustomInfoType.md)

Gets the specified custom property for this configuration.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetCustomProperty( _    ByVal FieldName As System.String, _    ByRef type As SwDmCustomInfoType _ ) As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration Dim FieldName As System.String Dim type As SwDmCustomInfoType Dim value As System.String   value = instance.GetCustomProperty(FieldName, type) ``` | |

| C# |  |
| --- | --- |
| ``` System.string GetCustomProperty(     System.string FieldName,    out SwDmCustomInfoType type ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.String^ GetCustomProperty(  &   System.String^ FieldName, &   [Out] SwDmCustomInfoType type ) ``` | |

#### Parameters

*FieldName*
:   Name of the custom property

*type*
:   Type of custom property as defined by [SwDmCustomInfoType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCustomInfoType.md)

#### Return Value

Value of the custom property

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration::GetCustomProperty](swdocumentmgr~SwDMConfiguration~GetCustomProperty.md).

# Example

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
  
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

# Remarks

To get the names of all the custom properties for this configuration, call [ISwDMConfiguration::GetCustomPropertyNames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyNames.md).

This method returns an evaluated value:

- from when the file was last saved in SOLIDWORKS. If you used [ISwDMConfiguration::SetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~SetCustomProperty.md) to set a linked custom property, then you need to open and save the file in SOLIDWORKS before your DocumentMgr application calls this method to retrieve the evaluated value of the linked custom property.

- prefaced with **fromparent+** for external referenced documents. Use [ISwConfiguration14::GetCustomProperty2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration14~GetCustomProperty2.md) to return resolved evaluated values without the **fromparent+** preface.

# See Also

#### 

[ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.md)
  
[ISwDMConfiguration Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration_members.md)
  
[ISwDMConfiguration::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~AddCustomProperty.md)
  
[ISwDMConfiguration::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~DeleteCustomProperty.md)
  
[ISwDMConfiguration::GetCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyCount.md)
  
[ISwDMConfiguration4::GetAllCustomPropertyNamesAndValues Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4~GetAllCustomPropertyNamesAndValues.md)
  
[ISwDMConfiguration5::GetCustomPropertyValues Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5~GetCustomPropertyValues.md)
  
[ISwDMDocument::GetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomProperty.md)
  
[ISwDMDocument17::GetCustomProperty2 Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17~GetCustomProperty2.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS
