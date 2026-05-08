# CreateToroidalSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateToroidalSurface`

Creates an untrimmed toroidal surface from the specified arguments.
Creates an untrimmed toroidal surface from the specified arguments.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateToroidalSurface( _
   ByVal Center As System.Object, _
   ByVal Axis As System.Object, _
   ByVal RefDirection As System.Object, _
   ByVal MajorRadius As System.Double, _
   ByVal MinorRadius As System.Double _
) As System.Object
```

```

Dim instance As IModeler
Dim Center As System.Object
Dim Axis As System.Object
Dim RefDirection As System.Object
Dim MajorRadius As System.Double
Dim MinorRadius As System.Double
Dim value As System.Object
 
value = instance.CreateToroidalSurface(Center, Axis, RefDirection, MajorRadius, MinorRadius)
```

```

System.object CreateToroidalSurface( 
   System.object Center,
   System.object Axis,
   System.object RefDirection,
   System.double MajorRadius,
   System.double MinorRadius
)
```

```

System.Object^ CreateToroidalSurface( 
   System.Object^ Center,
   System.Object^ Axis,
   System.Object^ RefDirection,
   System.double MajorRadius,
   System.double MinorRadius
) 
```

#### Parameters

*Center*
:   Array containing 3 doubles (see **Remarks**)

*Axis*
:   Array containing 3 doubles (see **Remarks**)

*RefDirection*
:   Array containing 3 doubles (see **Remarks**)

*MajorRadius*
:   See **Remarks**

*MinorRadius*
:   See **Remarks**

#### Return Value

Untrimmed toroidal [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)

Remarks

Input arguments:

- Center XYZ location that represents the center of the spherical surface.
- Axis XYZ direction of the axis of the spherical surface.
- RefDirection XYZ direction of the reference axis of the spherical surface; it must be perpendicular to the axis.
- MajorRadius major radius of the toroidal surface.
- MinorRadius minor radius of the toroidal surface.

The resulting surface can be trimmed using a method like [ISurface::CreateTrimmedSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateTrimmedSheet.md) to generate a sheet body.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::CreateConicalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateConicalSurface2.md)  
[IModeler::CreateCoonsBSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCoonsBSurface.md)  
[IModeler::CreateCylindricalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCylindricalSurface2.md)  
[IModeler::CreateExtrusionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrusionSurface.md)  
[IModeler::CreateLoftSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLoftSurface.md)  
[IModeler::CreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateOffsetSurface.md)  
[IModeler::CreatePlanarSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePlanarSurface2.md)  
[IModeler::CreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateRuledSurface.md)  
[IModeler::CreateSphericalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSphericalSurface2.md)  
[IModeler::CreateSweptSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptSurface.md)  
[IModeler::ICreateBsplineSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBsplineSurface.md)  
[IModeler::ICreateConicalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateConicalSurface2.md)  
[IModeler::ICreateCylindricalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateCylindricalSurface2.md)  
[IModeler::ICreateExtrusionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateExtrusionSurface.md)  
[IModeler::ICreateLoftSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateLoftSurface.md)  
[IModeler::ICreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateOffsetSurface.md)  
[IModeler::ICreatePlanarSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePlanarSurface2.md)  
[IModeler::ICreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateRuledSurface.md)  
[IModeler::ICreateSweptSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSweptSurface.md)  
[IModeler::ICreateToroidalSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateToroidalSurface.md)  
[ISurface::IsTorus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsTorus.md)  
[ISurface::TorusParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~TorusParams.md)
