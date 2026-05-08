# GetPositionEntity Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionEntity`

Gets the entity to which the camera is attached.
Gets the entity to which the camera is attached.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPositionEntity( _
   ByRef Point As MathPoint, _
   ByRef PercentPosition As System.Double _
) As System.Object
```

```

Dim instance As ICamera
Dim Point As MathPoint
Dim PercentPosition As System.Double
Dim value As System.Object
 
value = instance.GetPositionEntity(Point, PercentPosition)
```

```

System.object GetPositionEntity( 
   out MathPoint Point,
   out System.double PercentPosition
)
```

```

System.Object^ GetPositionEntity( 
   [Out] MathPoint^ Point,
   [Out] System.double PercentPosition
) 
```

#### Parameters

*Point*
:   [IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) object indicating the camera position

*PercentPosition*
:   Camera point distance along the entity

#### Return Value

Entity for the camera position

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md)  
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.md)  
[ICamera::GetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPosition.md)  
[ICamera::GetPositionCartesian Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionCartesian.md)  
[ICamera::GetPositionSpherical Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionSpherical.md)  
[ICamera::LockCameraPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~LockCameraPosition.md)  
[ICamera::PositionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~PositionType.md)  
[ICamera::SetPositionCartesian Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionCartesian.md)  
[ICamera::SetPositionEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionEntity.md)  
[ICamera::SetPositionSpherical Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionSpherical.md)
