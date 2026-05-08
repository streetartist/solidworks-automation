# GetPlaneFeatures Method (ISwDMDimXpertCompoundNotchFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature~GetPlaneFeatures`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature~GetPlaneFeatures.html) on this topic. |
| GetPlaneFeatures Method (ISwDMDimXpertCompoundNotchFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertCompoundNotchFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature.md) : GetPlaneFeatures Method (ISwDMDimXpertCompoundNotchFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Plane1*
:   [ISwDMDimXpertPlaneFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPlaneFeature.md)

*Plane2*
:   [ISwDMDimXpertPlaneFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPlaneFeature.md)

Gets the DimXpert plane features for both sides of this DimXpert compound notch.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetPlaneFeatures( _    ByRef Plane1 As SwDMDimXpertPlaneFeature, _    ByRef Plane2 As SwDMDimXpertPlaneFeature _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertCompoundNotchFeature Dim Plane1 As SwDMDimXpertPlaneFeature Dim Plane2 As SwDMDimXpertPlaneFeature Dim value As System.Boolean   value = instance.GetPlaneFeatures(Plane1, Plane2) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetPlaneFeatures(     out SwDMDimXpertPlaneFeature Plane1,    out SwDMDimXpertPlaneFeature Plane2 ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetPlaneFeatures(  &   [Out] SwDMDimXpertPlaneFeature^ Plane1, &   [Out] SwDMDimXpertPlaneFeature^ Plane2 ) ``` | |

#### Parameters

*Plane1*
:   [ISwDMDimXpertPlaneFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPlaneFeature.md)

*Plane2*
:   [ISwDMDimXpertPlaneFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPlaneFeature.md)

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertCompoundNotchFeature::GetPlaneFeatures](swdocumentmgr~SwDMDimXpertCompoundNotchFeature~GetPlaneFeatures.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertCompoundNotchFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature.md)
  
[ISwDMDimXpertCompoundNotchFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
