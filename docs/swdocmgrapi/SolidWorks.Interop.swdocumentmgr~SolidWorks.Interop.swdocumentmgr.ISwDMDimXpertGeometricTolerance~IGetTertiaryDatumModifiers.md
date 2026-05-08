# IGetTertiaryDatumModifiers Method (ISwDMDimXpertGeometricTolerance)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~IGetTertiaryDatumModifiers`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~IGetTertiaryDatumModifiers.html) on this topic. |
| IGetTertiaryDatumModifiers Method (ISwDMDimXpertGeometricTolerance) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertGeometricTolerance Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance.md) : IGetTertiaryDatumModifiers Method (ISwDMDimXpertGeometricTolerance) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*Count*
:   Number of tertiary datum modifiers

Gets all of the material condition modifiers of the tertiary datum in this DimXpert geometric tolerance.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function IGetTertiaryDatumModifiers( _    ByVal Count As System.Integer _ ) As swDmDimXpertMaterialConditionModifier_e ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertGeometricTolerance Dim Count As System.Integer Dim value As swDmDimXpertMaterialConditionModifier_e   value = instance.IGetTertiaryDatumModifiers(Count) ``` | |

| C# |  |
| --- | --- |
| ``` swDmDimXpertMaterialConditionModifier_e IGetTertiaryDatumModifiers(     System.int Count ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` swDmDimXpertMaterialConditionModifier_e IGetTertiaryDatumModifiers(  &   System.int Count ) ``` | |

#### Parameters

*Count*
:   Number of tertiary datum modifiers

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [SwDMDimXpertMaterialConditionModifier\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDimXpertMaterialConditionModifier_e.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

# Remarks

Use [ISwDMDimXpertGeometricTolerance::GetTertiaryDatumCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~GetTertiaryDatumCount.md) to populate the Count argument.

# See Also

#### 

[ISwDMDimXpertGeometricTolerance Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance.md)
  
[ISwDMDimXpertGeometricTolerance Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance_members.md)
  
[ISwDMDimxpertGeometricTolerance::GetTertiaryDatumModifiers Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~GetTertiaryDatumModifiers.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
