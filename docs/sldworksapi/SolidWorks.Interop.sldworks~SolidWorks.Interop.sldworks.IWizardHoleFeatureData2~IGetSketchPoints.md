# IGetSketchPoints Method (IWizardHoleFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~IGetSketchPoints`

Gets the center-hole sketch points in this Hole Wizard feature.
Gets the center-hole sketch points in this Hole Wizard feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSketchPoints( _
   ByVal NCount As System.Integer _
) As SketchPoint
```

```

Dim instance As IWizardHoleFeatureData2
Dim NCount As System.Integer
Dim value As SketchPoint
 
value = instance.IGetSketchPoints(NCount)
```

```

SketchPoint IGetSketchPoints( 
   System.int NCount
)
```

```

SketchPoint^ IGetSketchPoints( 
   System.int NCount
) 
```

#### Parameters

*NCount*
:   Number of center-hole sketch points

#### Return Value

Array of center-hole [sketch points](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)

Remarks

Before calling this method, call [IWizardHoleFeatureData2::GetSketchPointCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~GetSketchPointCount.md) to get NCount.

To add or remove sketch points in a Hole Wizard feature sketch (also called a location sketch), you must edit the sketch. After editing the sketch, update the Hole Wizard feature by calling [IModelDoc2::ForceRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md)  
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.md)  
[IWizardHoleFeatureData2::GetSketchPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~GetSketchPoints.md)
