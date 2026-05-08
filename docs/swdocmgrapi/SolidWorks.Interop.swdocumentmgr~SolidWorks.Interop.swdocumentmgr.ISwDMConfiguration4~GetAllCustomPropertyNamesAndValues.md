# GetAllCustomPropertyNamesAndValues Method (ISwDMConfiguration4)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4~GetAllCustomPropertyNamesAndValues`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4~GetAllCustomPropertyNamesAndValues.html) on this topic. |
| GetAllCustomPropertyNamesAndValues Method (ISwDMConfiguration4) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4.md) : GetAllCustomPropertyNamesAndValues Method (ISwDMConfiguration4) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*names*
:   Array of Property Names

*types*
:   Array of Types as defined in [SwDmCustomInfoType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCustomInfoType.md)

*linkedTo*
:   Array of Estimated Values

*values*
:   Array of linked to Values/Text Expressions (see **Remarks**)

Gets all of the custom properties for this configuration.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Sub GetAllCustomPropertyNamesAndValues( _    ByRef names As System.Object, _    ByRef types As System.Object, _    ByRef linkedTo As System.Object, _    ByRef values As System.Object _ ) ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration4 Dim names As System.Object Dim types As System.Object Dim linkedTo As System.Object Dim values As System.Object   instance.GetAllCustomPropertyNamesAndValues(names, types, linkedTo, values) ``` | |

| C# |  |
| --- | --- |
| ``` void GetAllCustomPropertyNamesAndValues(     out System.object names,    out System.object types,    out System.object linkedTo,    out System.object values ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` void GetAllCustomPropertyNamesAndValues(  &   [Out] System.Object^ names, &   [Out] System.Object^ types, &   [Out] System.Object^ linkedTo, &   [Out] System.Object^ values ) ``` | |

#### Parameters

*names*
:   Array of Property Names

*types*
:   Array of Types as defined in [SwDmCustomInfoType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCustomInfoType.md)

*linkedTo*
:   Array of Estimated Values

*values*
:   Array of linked to Values/Text Expressions (see **Remarks**)

#### Return Value

|  |  |
| --- | --- |
| **If the properties are...** | **Then this method returns...** |
| Linked | The evaluated results of values |
| Not linked | Empty strings.  This method returns the same values as returned by [ISwDMConfiguration::GetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomProperty.md) |

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration4::GetAllCustomPropertyNamesAndValues](swdocumentmgr~SwDMConfiguration4~GetAllCustomPropertyNamesAndValues.md).

# Remarks

If you called [ISwDMConfiguration::SetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~SetCustomProperty.md) to set a linked custom property, then you must open and save the file in SOLIDWORKS before calling this method. SOLIDWORKS must process the linked custom property before your DocumentMgr application can retrieve its evaluated value.

# See Also

#### 

[ISwDMConfiguration4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4.md)
  
[ISwDMConfiguration4 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4_members.md)
  
[ISwDMConfiguration::AddCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~AddCustomProperty.md)
  
[ISwDMConfiguration::DeleteCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~DeleteCustomProperty.md)
  
[ISwDMConfiguration::GetCustomPropertyCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyCount.md)
  
[ISwDMConfiguration::GetCustomPropertyNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomPropertyNames.md)
  
[ISwDMConfiguration5::GetCustomPropertyValues Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5~GetCustomPropertyValues.md)
  
[ISwDMDocument3::GetAllCustomPropertyNamesAndValues Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3~GetAllCustomPropertyNamesAndValues.md)
  
[ISwDMConfiguration14::GetCustomProperty2 Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration14~GetCustomProperty2.md)
  
[ISwDMConfiguration15::IsCustomPropertyEditable Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration15~IsCustomPropertyEditable.md)

# Availability

SOLIDWORKS Document Manager API 2004 SP4
