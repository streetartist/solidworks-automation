# CreateChamfer Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateChamfer`

Creates a chamfer between two selected sketch entities.
Creates a chamfer between two selected sketch entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateChamfer( _
   ByVal Type As System.Integer, _
   ByVal Distance As System.Double, _
   ByVal AngleORdist As System.Double _
) As SketchSegment
```

```

Dim instance As ISketchManager
Dim Type As System.Integer
Dim Distance As System.Double
Dim AngleORdist As System.Double
Dim value As SketchSegment
 
value = instance.CreateChamfer(Type, Distance, AngleORdist)
```

```

SketchSegment CreateChamfer( 
   System.int Type,
   System.double Distance,
   System.double AngleORdist
)
```

```

SketchSegment^ CreateChamfer( 
   System.int Type,
   System.double Distance,
   System.double AngleORdist
) 
```

#### Parameters

*Type*
:   Type of chamfer as defined in [swSketchChamferType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.interop.swconst~SOLIDWORKS.interop.swconst.swSketchChamferType_e.html)

*Distance*
:   Distance of the chamfer

*AngleORdist*
:   - If Type = swSketchChamfer\_DistanceDistance, then the second chamfer distance
    - If Type = swSketchChamfer\_DistanceAngle, then the second chamfer angle
    - If Type = swSketchChamfer\_DistanceEqual, then this argument is ignored because Distance  
      is used for both edges

#### Return Value

[Sketch segment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) for the chamfer

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
