# GetCustomProperty Method (ISwDMComponent12)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent12~GetCustomProperty`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent12~GetCustomProperty.html) on this topic. |
| GetCustomProperty Method (ISwDMComponent12) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMComponent12 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent12.md) : GetCustomProperty Method (ISwDMComponent12) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*FieldName*
:   Name of custom property

*type*
:   Type of custom property as defined by [SwDMCustomInfoType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCustomInfoType.md)

Gets the specified custom property for this component.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetCustomProperty( _    ByVal FieldName As System.String, _    ByRef type As System.Integer _ ) As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMComponent12 Dim FieldName As System.String Dim type As System.Integer Dim value As System.String   value = instance.GetCustomProperty(FieldName, type) ``` | |

| C# |  |
| --- | --- |
| ``` System.string GetCustomProperty(     System.string FieldName,    out System.int type ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.String^ GetCustomProperty(  &   System.String^ FieldName, &   [Out] System.int type ) ``` | |

#### Parameters

*FieldName*
:   Name of custom property

*type*
:   Type of custom property as defined by [SwDMCustomInfoType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmCustomInfoType.md)

#### Return Value

Value of the custom property

# Visual Basic for Applications (VBA) Syntax

See [SwDMComponent12::GetCustomProperty](swdocumentmgr~SwDMComponent12~GetCustomProperty.md).

# Example

[Get Configuration-Specific Custom Properties for Components (VB.NET)](Get_Configuration-Specific_Custom_Properties_Example_VBNET.htm)
  
[Get Configuration-Specific Custom Properties for Components (C#)](Get_Configuration-Specific_Custom_Properties_Example_CSharp.htm)

# See Also

#### 

[ISwDMComponent12 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent12.md)
  
[ISwDMComponent12 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent12_members.md)

# Availability

SOLIDWORKS Document Manager API 2024 SP0
