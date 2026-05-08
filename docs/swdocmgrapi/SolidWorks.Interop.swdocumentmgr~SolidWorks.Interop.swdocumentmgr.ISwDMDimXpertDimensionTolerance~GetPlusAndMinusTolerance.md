# GetPlusAndMinusTolerance Method (ISwDMDimXpertDimensionTolerance)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance~GetPlusAndMinusTolerance`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance~GetPlusAndMinusTolerance.html) on this topic. |
| GetPlusAndMinusTolerance Method (ISwDMDimXpertDimensionTolerance) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertDimensionTolerance Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance.md) : GetPlusAndMinusTolerance Method (ISwDMDimXpertDimensionTolerance) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Plus*
:   Plus tolerance value

*Minus*
:   Minus tolerance value

Gets the plus and minus tolerance values for this DimXpert dimension tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetPlusAndMinusTolerance( _    ByRef Plus As System.Double, _    ByRef Minus As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertDimensionTolerance Dim Plus As System.Double Dim Minus As System.Double Dim value As System.Boolean   value = instance.GetPlusAndMinusTolerance(Plus, Minus) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetPlusAndMinusTolerance(     out System.double Plus,    out System.double Minus ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetPlusAndMinusTolerance(  &   [Out] System.double Plus, &   [Out] System.double Minus ) ``` | |

#### Parameters

*Plus*
:   Plus tolerance value

*Minus*
:   Minus tolerance value

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertDimensionTolerance::GetPlusAndMinusTolerance](swdocumentmgr~SwDMDimXpertDimensionTolerance~GetPlusAndMinusTolerance.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertDimensionTolerance Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance.md)
  
[ISwDMDimXpertDimensionTolerance Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
