# GetTertiaryDatumModifiers Method (ISwDMDimXpertGeometricTolerance)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~GetTertiaryDatumModifiers`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~GetTertiaryDatumModifiers.html) on this topic. |
| GetTertiaryDatumModifiers Method (ISwDMDimXpertGeometricTolerance) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertGeometricTolerance Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance.md) : GetTertiaryDatumModifiers Method (ISwDMDimXpertGeometricTolerance) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets all of the material condition modifiers of the tertiary datum in this DimXpert geometric tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetTertiaryDatumModifiers() As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertGeometricTolerance Dim value As System.Object   value = instance.GetTertiaryDatumModifiers() ``` | |

| C# |  |
| --- | --- |
| ``` System.object GetTertiaryDatumModifiers() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.Object^ GetTertiaryDatumModifiers(); ``` | |

#### Return Value

Array of material condition modifiers as defined in [swDmDimXpertMaterialConditionModifier\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDimXpertMaterialConditionModifier_e.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertGeometricTolerance::GetTertiaryDatumModifiers](swdocumentmgr~SwDMDimXpertGeometricTolerance~GetTertiaryDatumModifiers.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertGeometricTolerance Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance.md)
  
[ISwDMDimXpertGeometricTolerance Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance_members.md)
  
[ISwDMDimXpertGeometricTolerance::IGetTertiaryDatumModifiers Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~IGetTertiaryDatumModifiers.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
