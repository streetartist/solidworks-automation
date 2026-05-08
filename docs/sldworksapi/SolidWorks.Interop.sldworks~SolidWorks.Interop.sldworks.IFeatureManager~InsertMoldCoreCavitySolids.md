# InsertMoldCoreCavitySolids Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldCoreCavitySolids`

Creates a core/cavity solid feature.
Creates a core/cavity solid feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertMoldCoreCavitySolids( _
   ByVal Dist1 As System.Double, _
   ByVal Dist2 As System.Double, _
   ByVal Setback As System.Boolean, _
   ByVal Angle As System.Double _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Dist1 As System.Double
Dim Dist2 As System.Double
Dim Setback As System.Boolean
Dim Angle As System.Double
Dim value As Feature
 
value = instance.InsertMoldCoreCavitySolids(Dist1, Dist2, Setback, Angle)
```

```

Feature InsertMoldCoreCavitySolids( 
   System.double Dist1,
   System.double Dist2,
   System.bool Setback,
   System.double Angle
)
```

```

Feature^ InsertMoldCoreCavitySolids( 
   System.double Dist1,
   System.double Dist2,
   System.bool Setback,
   System.double Angle
) 
```

#### Parameters

*Dist1*
:   Length of the extrusion in Direction 1

*Dist2*
:   Length of the extrusion in Direction 2

*Setback*
:   True to enable setback surface, false to not

*Angle*
:   Draft angle for the setback surface

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

To use this method:

- The Parting Line feature must exist.
- The parting surface must be generated.
- The part must be separated into core and cavity (sheet bodies).
- A sketch describing the outline of the mold block must exist. The sketch must be perpendicular to the pull direction. Usually, the sketch is a rectangle that includes the part (core and cavity).

The location of the sketch plane specifies the parting plane in the setback surface option.

- Without the setback surface option, the parting surface must extend beyond the block sketch so that the parting surface is cut off by the block.
- With the setback surface option, the parting surface should be included within the block sketch. The parting plane (sketch plane) cannot intersect with the parting surface. Therefore, the parting plane must be either higher or lower than the parting surface. From the parting surface, a set of ruled surfaces is generated to be trimmed by the parting plane.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::InsertMoldPartingLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldPartingLine.md)  
[IFeatureManager::InsertMoldPartingSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldPartingSurface.md)  
[IFeatureManager::InsertMoldShutOffSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldShutOffSurface.md)  
[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.md)  
[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.md)
