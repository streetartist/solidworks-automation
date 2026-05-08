# GetTargetPointEntity Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetTargetPointEntity`

Gets the target point on the entity for the camera.
Gets the target point on the entity for the camera.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTargetPointEntity( _
   ByRef Point As MathPoint, _
   ByRef PercentTarget As System.Double _
) As System.Object
```

```

Dim instance As ICamera
Dim Point As MathPoint
Dim PercentTarget As System.Double
Dim value As System.Object
 
value = instance.GetTargetPointEntity(Point, PercentTarget)
```

```

System.object GetTargetPointEntity( 
   out MathPoint Point,
   out System.double PercentTarget
)
```

```

System.Object^ GetTargetPointEntity( 
   [Out] MathPoint^ Point,
   [Out] System.double PercentTarget
) 
```

#### Parameters

*Point*
:   [IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) object indicating the target point for the camera

*PercentTarget*
:   Target point distance along the entity

#### Return Value

Entity for the target point

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md)  
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.md)  
[ICamera::SetTargetPointEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetTargetPointEntity.md)  
[ICamera::TargetPointBySelection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~TargetPointBySelection.md)  
[ICamera::TargetPointPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~TargetPointPosition.md)
