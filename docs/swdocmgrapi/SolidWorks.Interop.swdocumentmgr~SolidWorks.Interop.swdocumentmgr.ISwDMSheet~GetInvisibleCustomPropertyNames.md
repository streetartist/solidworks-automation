# GetInvisibleCustomPropertyNames Method (ISwDMSheet)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet~GetInvisibleCustomPropertyNames`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet~GetInvisibleCustomPropertyNames.html) on this topic. |
| GetInvisibleCustomPropertyNames Method (ISwDMSheet) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMSheet Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet.md) : GetInvisibleCustomPropertyNames Method (ISwDMSheet) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the names of this sheet's invisible custom properties.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetInvisibleCustomPropertyNames() As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMSheet Dim value As System.Object   value = instance.GetInvisibleCustomPropertyNames() ``` | |

| C# |  |
| --- | --- |
| ``` System.object GetInvisibleCustomPropertyNames() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.Object^ GetInvisibleCustomPropertyNames(); ``` | |

#### Return Value

Array of strings of the names of the invisible custom properties for this sheet

# Visual Basic for Applications (VBA) Syntax

See [SwDMSheet::GetInvisibleCustomPropertyNames](swdocumentmgr~SwDMSheet~GetInvisibleCustomPropertyNames.md).

# Remarks

Before calling this method, call [ISwDMSheet::GetInvisibleCustomPropertyCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet~GetInvisibleCustomPropertyCount.md) to determine the size of the array.

Call this method before calling [ISwDMSheet::GetInvisibleCustomProperty](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet~GetInvisibleCustomProperty.md) to determine the name of the invisible custom property you want to use with that method.

# See Also

#### 

[ISwDMSheet Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet.md)
  
[ISwDMSheet Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet_members.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0
