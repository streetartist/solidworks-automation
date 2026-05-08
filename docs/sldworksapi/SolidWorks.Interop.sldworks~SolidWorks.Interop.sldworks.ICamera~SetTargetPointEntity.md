# SetTargetPointEntity Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetTargetPointEntity`

Gets the target point on the entity for the camera.
Gets the target point on the entity for the camera.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetTargetPointEntity( _
   ByVal Point As MathPoint, _
   ByVal PercentTarget As System.Double, _
   ByVal TargetPointEntity As System.Object _
) 
```

```

Dim instance As ICamera
Dim Point As MathPoint
Dim PercentTarget As System.Double
Dim TargetPointEntity As System.Object
 
instance.SetTargetPointEntity(Point, PercentTarget, TargetPointEntity)
```

```

void SetTargetPointEntity( 
   MathPoint Point,
   System.double PercentTarget,
   System.object TargetPointEntity
)
```

```

void SetTargetPointEntity( 
   MathPoint^ Point,
   System.double PercentTarget,
   System.Object^ TargetPointEntity
) 
```

#### Parameters

*Point*
:   Pointer to the [IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) object indicating the target point for the camera

*PercentTarget*
:   Target point distance along the entity

*TargetPointEntity*
:   Entity for the target point

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md)  
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.md)  
[ICamera::GetTargetPointEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetTargetPointEntity.md)  
[ICamera::TargetPointBySelection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~TargetPointBySelection.md)  
[ICamera::TargetPointPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~TargetPointPosition.md)
