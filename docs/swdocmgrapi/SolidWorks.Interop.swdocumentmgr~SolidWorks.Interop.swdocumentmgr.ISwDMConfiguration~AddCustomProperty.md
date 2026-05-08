# AddCustomProperty Method (ISwDMConfiguration)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~AddCustomProperty`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~AddCustomProperty.html) on this topic. |
| AddCustomProperty Method (ISwDMConfiguration) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.md) : AddCustomProperty Method (ISwDMConfiguration) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*FieldName*
:   Name of the custom property to add

*SwDmCustomInfoType*
:   Type of custom property as defined by [SwDmCustomInfoType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCustomInfoType.md)

*FieldValue*
:   Value for custom property to add

Adds a custom property to this configuration.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function AddCustomProperty( _    ByVal FieldName As System.String, _    ByVal SwDmCustomInfoType As SwDmCustomInfoType, _    ByVal FieldValue As System.String _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration Dim FieldName As System.String Dim SwDmCustomInfoType As SwDmCustomInfoType Dim FieldValue As System.String Dim value As System.Boolean   value = instance.AddCustomProperty(FieldName, SwDmCustomInfoType, FieldValue) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool AddCustomProperty(     System.string FieldName,    SwDmCustomInfoType SwDmCustomInfoType,    System.string FieldValue ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool AddCustomProperty(  &   System.String^ FieldName, &   SwDmCustomInfoType SwDmCustomInfoType, &   System.String^ FieldValue ) ``` | |

#### Parameters

*FieldName*
:   Name of the custom property to add

*SwDmCustomInfoType*
:   Type of custom property as defined by [SwDmCustomInfoType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCustomInfoType.md)

*FieldValue*
:   Value for custom property to add

#### Return Value

True if custom property is added, false if not

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration::AddCustomProperty](swdocumentmgr~SwDMConfiguration~AddCustomProperty.md).

# Remarks

If you call this method to add a linked custom property with an expression value, then you need to open and save the file in SOLIDWORKS before calling [ISwDMConfiguration::GetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomProperty.md), [ISwDMConfiguration14::GetCustomProperty2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration14~GetCustomProperty2.md), [ISwDMConfiguration4::GetAllCustomPropertyNamesAndValues](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4~GetAllCustomPropertyNamesAndValues.md), or [ISwDMConfiguration5::GetCustomPropertyValues](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5~GetCustomPropertyValues.md). SOLIDWORKS needs to process the linked custom property before your DocumentMgr application attempts to get its evaluated value.

# See Also

#### 

[ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.md)
  
[ISwDMConfiguration Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration_members.md)
  
[ISwDMConfiguration::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~DeleteCustomProperty.md)
  
[ISwDMConfiguration::GetCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyCount.md)
  
[ISwDMConfiguration::GetCustomPropertyNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyNames.md)
  
[ISwDMConfiguration::SetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~SetCustomProperty.md)
  
[ISwDMDocument::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~AddCustomProperty.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS
