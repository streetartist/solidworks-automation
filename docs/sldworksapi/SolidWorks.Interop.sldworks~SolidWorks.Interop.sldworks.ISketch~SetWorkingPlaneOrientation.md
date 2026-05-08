# SetWorkingPlaneOrientation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~SetWorkingPlaneOrientation`

Sets the orientation for sketching geometry in a 3D sketch. It sets the planar location for new 2D and 3D geometry in a 3D sketch.
Sets the orientation for sketching geometry in a 3D sketch. It sets the planar location for new 2D and 3D geometry in a 3D sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetWorkingPlaneOrientation( _
   ByVal OriginX As System.Double, _
   ByVal OriginY As System.Double, _
   ByVal OriginZ As System.Double, _
   ByVal XAxisX As System.Double, _
   ByVal XAxisY As System.Double, _
   ByVal XAxisZ As System.Double, _
   ByVal YAxisX As System.Double, _
   ByVal YAxisY As System.Double, _
   ByVal YAxisZ As System.Double, _
   ByVal NormalX As System.Double, _
   ByVal NormalY As System.Double, _
   ByVal NormalZ As System.Double _
) As System.Boolean
```

```

Dim instance As ISketch
Dim OriginX As System.Double
Dim OriginY As System.Double
Dim OriginZ As System.Double
Dim XAxisX As System.Double
Dim XAxisY As System.Double
Dim XAxisZ As System.Double
Dim YAxisX As System.Double
Dim YAxisY As System.Double
Dim YAxisZ As System.Double
Dim NormalX As System.Double
Dim NormalY As System.Double
Dim NormalZ As System.Double
Dim value As System.Boolean
 
value = instance.SetWorkingPlaneOrientation(OriginX, OriginY, OriginZ, XAxisX, XAxisY, XAxisZ, YAxisX, YAxisY, YAxisZ, NormalX, NormalY, NormalZ)
```

```

System.bool SetWorkingPlaneOrientation( 
   System.double OriginX,
   System.double OriginY,
   System.double OriginZ,
   System.double XAxisX,
   System.double XAxisY,
   System.double XAxisZ,
   System.double YAxisX,
   System.double YAxisY,
   System.double YAxisZ,
   System.double NormalX,
   System.double NormalY,
   System.double NormalZ
)
```

```

System.bool SetWorkingPlaneOrientation( 
   System.double OriginX,
   System.double OriginY,
   System.double OriginZ,
   System.double XAxisX,
   System.double XAxisY,
   System.double XAxisZ,
   System.double YAxisX,
   System.double YAxisY,
   System.double YAxisZ,
   System.double NormalX,
   System.double NormalY,
   System.double NormalZ
) 
```

#### Parameters

*OriginX*
:   x coordinate of the origin of the axis

*OriginY*
:   y coordinate of the origin of the axis

*OriginZ*
:   z coordinate of the origin of the axis

*XAxisX*
:   x coordinate of the x vector direction

*XAxisY*
:   y coordinate of the x vector direction

*XAxisZ*
:   z coordinate of the x vector direction

*YAxisX*
:   x coordinate of the y vector direction

*YAxisY*
:   y coordinate of the y vector direction

*YAxisZ*
:   z coordinate of the y vector direction

*NormalX*
:   x coordinate of the normal to the planar direction

*NormalY*
:   y coordinate of the normal to the planar direction

*NormalZ*
:   z coordinate of the normal to the planar direction

#### Return Value

True if the orientation is set, false if not

Remarks

This method sets the planar location for new 2D and 3D geometry in a 3D sketch.

Example

[Create 3D Sketch Plane (C#)](Create_3D_Sketch_Plane_Example_CSharp.htm)  
[Create 3D Sketch Plane (VB.NET)](Create_3D_Sketch_Plane_Example_VBNET.htm)  
[Create 3D Sketch Plane (VBA)](Create_3D_Sketch_Plane_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)
