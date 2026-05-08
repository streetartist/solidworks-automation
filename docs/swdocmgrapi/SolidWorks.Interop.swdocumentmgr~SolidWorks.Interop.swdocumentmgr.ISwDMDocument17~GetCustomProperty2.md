# GetCustomProperty2 Method (ISwDMDocument17)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17~GetCustomProperty2`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17~GetCustomProperty2.html) on this topic. |
| GetCustomProperty2 Method (ISwDMDocument17) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument17 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17.md) : GetCustomProperty2 Method (ISwDMDocument17) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*FieldName*
:   Name of custom property (see **Remarks**)

*type*
:   Type of custom property as defined by [SwDmCustomInfoType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCustomInfoType.md)

Gets the specified custom property for this document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetCustomProperty2( _    ByVal FieldName As System.String, _    ByRef type As SwDmCustomInfoType _ ) As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument17 Dim FieldName As System.String Dim type As SwDmCustomInfoType Dim value As System.String   value = instance.GetCustomProperty2(FieldName, type) ``` | |

| C# |  |
| --- | --- |
| ``` System.string GetCustomProperty2(     System.string FieldName,    out SwDmCustomInfoType type ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.String^ GetCustomProperty2(  &   System.String^ FieldName, &   [Out] SwDmCustomInfoType type ) ``` | |

#### Parameters

*FieldName*
:   Name of custom property (see **Remarks**)

*type*
:   Type of custom property as defined by [SwDmCustomInfoType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCustomInfoType.md)

#### Return Value

Value of custom property

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument17::GetCustomProperty2](swdocumentmgr~SwDMDocument17~GetCustomProperty2.md).

# Example

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
  
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

# Remarks

To populate FieldName, use [ISwDMDocument::GetCustomPropertyNames](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyNames.md) to get the names of all of the custom properties.

This method returns an evaluated value:

- from when the document was last saved in SOLIDWORKS.

  If you called [ISwDMDocument::SetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~SetCustomProperty.md) to set a linked custom property, then you must open and save the file in SOLIDWORKS before calling this method. SOLIDWORKS must process the linked custom property before your DocumentMgr application can retrieve its evaluated value.
- without the **fromparent+** preface for externally referenced documents. Use [ISwDMDocument::GetCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomProperty.md) to return resolved evaluated values prefaced with **fromparent+**.

# See Also

#### 

[ISwDMDocument17 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17.md)
  
[ISwDMDocument17 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17_members.md)
  
[ISwDMDocument::AddCustomProperty Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~AddCustomProperty.md)
  
[ISwDMDocument::DeleteCustomProperty Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~DeleteCustomProperty.md)
  
[ISwDMDocument::GetCustomPropertyCount Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetCustomPropertyCount.md)
  
[ISwDMDocument5::GetCustomPropertyValues Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5~GetCustomPropertyValues.md)
  
[ISwDMConfiguration::GetCustomProperty Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetCustomProperty.md)
  
[ISwDMConfiguration14::GetCustomProperty2 Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration14~GetCustomProperty2.md)

# Availability

SOLIDWORKS Document Manager API 2013 FCS
