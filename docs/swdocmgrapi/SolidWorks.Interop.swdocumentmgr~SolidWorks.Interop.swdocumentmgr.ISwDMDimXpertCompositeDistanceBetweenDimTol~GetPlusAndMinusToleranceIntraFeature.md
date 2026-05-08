# GetPlusAndMinusToleranceIntraFeature Method (ISwDMDimXpertCompositeDistanceBetweenDimTol)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol~GetPlusAndMinusToleranceIntraFeature`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol~GetPlusAndMinusToleranceIntraFeature.html) on this topic. |
| GetPlusAndMinusToleranceIntraFeature Method (ISwDMDimXpertCompositeDistanceBetweenDimTol) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol.md) : GetPlusAndMinusToleranceIntraFeature Method (ISwDMDimXpertCompositeDistanceBetweenDimTol) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Plus*
:   Plus tolerance value for feature-locating

*Minus*
:   Minus tolerance value for feature-locating

Gets the plus and minus tolerance values used by the feature-locating portion of this DimXpert composite distance-between dimension tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetPlusAndMinusToleranceIntraFeature( _    ByRef Plus As System.Double, _    ByRef Minus As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertCompositeDistanceBetweenDimTol Dim Plus As System.Double Dim Minus As System.Double Dim value As System.Boolean   value = instance.GetPlusAndMinusToleranceIntraFeature(Plus, Minus) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetPlusAndMinusToleranceIntraFeature(     out System.double Plus,    out System.double Minus ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetPlusAndMinusToleranceIntraFeature(  &   [Out] System.double Plus, &   [Out] System.double Minus ) ``` | |

#### Parameters

*Plus*
:   Plus tolerance value for feature-locating

*Minus*
:   Minus tolerance value for feature-locating

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertCompositeDistanceBetweenDimTol::GetPlusAndMinusToleranceIntraFeature](swdocumentmgr~SwDMDimXpertCompositeDistanceBetweenDimTol~GetPlusAndMinusToleranceIntraFeature.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol.md)
  
[ISwDMDimXpertCompositeDistanceBetweenDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
