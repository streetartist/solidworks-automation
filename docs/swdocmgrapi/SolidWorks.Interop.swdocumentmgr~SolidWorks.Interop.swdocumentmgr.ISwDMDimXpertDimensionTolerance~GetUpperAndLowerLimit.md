# GetUpperAndLowerLimit Method (ISwDMDimXpertDimensionTolerance)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance~GetUpperAndLowerLimit`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance~GetUpperAndLowerLimit.html) on this topic. |
| GetUpperAndLowerLimit Method (ISwDMDimXpertDimensionTolerance) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertDimensionTolerance Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance.md) : GetUpperAndLowerLimit Method (ISwDMDimXpertDimensionTolerance) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Upper*
:   Upper tolerance limit

*Lower*
:   Lower tolerance limit

Gets the upper and lower tolerance limits for this DimXpert dimension tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetUpperAndLowerLimit( _    ByRef Upper As System.Double, _    ByRef Lower As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertDimensionTolerance Dim Upper As System.Double Dim Lower As System.Double Dim value As System.Boolean   value = instance.GetUpperAndLowerLimit(Upper, Lower) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetUpperAndLowerLimit(     out System.double Upper,    out System.double Lower ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetUpperAndLowerLimit(  &   [Out] System.double Upper, &   [Out] System.double Lower ) ``` | |

#### Parameters

*Upper*
:   Upper tolerance limit

*Lower*
:   Lower tolerance limit

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertDimensionTolerance::GetUpperAndLowerLimit](swdocumentmgr~SwDMDimXpertDimensionTolerance~GetUpperAndLowerLimit.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertDimensionTolerance Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance.md)
  
[ISwDMDimXpertDimensionTolerance Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
