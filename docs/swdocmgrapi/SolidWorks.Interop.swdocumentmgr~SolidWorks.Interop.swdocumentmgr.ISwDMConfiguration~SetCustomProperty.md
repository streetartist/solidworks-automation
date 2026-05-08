# SetCustomProperty Method (ISwDMConfiguration)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~SetCustomProperty`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~SetCustomProperty.html) on this topic. |
| SetCustomProperty Method (ISwDMConfiguration) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.md) : SetCustomProperty Method (ISwDMConfiguration) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*FieldName*
:   Custom property to set

*newValue*
:   Value for custom property

Obsolete. Superseded by [ISwDMConfiguration18::SetCustomProperty2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration18~SetCustomProperty2.md).

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Sub SetCustomProperty( _    ByVal FieldName As System.String, _    ByVal newValue As System.String _ ) ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration Dim FieldName As System.String Dim newValue As System.String   instance.SetCustomProperty(FieldName, newValue) ``` | |

| C# |  |
| --- | --- |
| ``` void SetCustomProperty(     System.string FieldName,    System.string newValue ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` void SetCustomProperty(  &   System.String^ FieldName, &   System.String^ newValue ) ``` | |

#### Parameters

*FieldName*
:   Custom property to set

*newValue*
:   Value for custom property

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration::SetCustomProperty](swdocumentmgr~SwDMConfiguration~SetCustomProperty.md).

# Remarks

Before calling this method, call [ISwDMConfiguration::GetCustomPropertyNames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyNames.md) to populate FieldName.

If you call this method to set a linked custom property with an expression value, then you need to open and save the file in SOLIDWORKS before calling [ISwDMConfiguration::GetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomProperty.md), [ISwDMConfiguration14::GetCustomProperty2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration14~GetCustomProperty2.md), [ISwDMConfiguration4::GetAllCustomPropertyNamesAndValues](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4~GetAllCustomPropertyNamesAndValues.md), or [ISwDMConfiguration5::GetCustomPropertyValues](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5~GetCustomPropertyValues.md). SOLIDWORKS needs to process the linked custom property before your DocumentMgr application attempts to get its evaluated value.

# See Also

#### 

[ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.md)
  
[ISwDMConfiguration Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration_members.md)
  
[ISwDMConfiguration::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~AddCustomProperty.md)
  
[ISwDMConfiguration::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~DeleteCustomProperty.md)
  
[ISwDMConfiguration::GetCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyCount.md)
  
[ISwDMConfiguration::GetCustomPropertyNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyNames.md)
  
[ISwDMDocument::SetCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SetCustomProperty.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS
