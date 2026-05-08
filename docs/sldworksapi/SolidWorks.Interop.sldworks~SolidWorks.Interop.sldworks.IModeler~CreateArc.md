# CreateArc Method (IModeler)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateArc`

Creates an arc.
Creates an arc.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateArc( _
   ByVal Center As System.Object, _
   ByVal Axis As System.Object, _
   ByVal Radius As System.Double, _
   ByVal StartPoint As System.Object, _
   ByVal EndPoint As System.Object _
) As System.Object
```

```

Dim instance As IModeler
Dim Center As System.Object
Dim Axis As System.Object
Dim Radius As System.Double
Dim StartPoint As System.Object
Dim EndPoint As System.Object
Dim value As System.Object
 
value = instance.CreateArc(Center, Axis, Radius, StartPoint, EndPoint)
```

```

System.object CreateArc( 
   System.object Center,
   System.object Axis,
   System.double Radius,
   System.object StartPoint,
   System.object EndPoint
)
```

```

System.Object^ CreateArc( 
   System.Object^ Center,
   System.Object^ Axis,
   System.double Radius,
   System.Object^ StartPoint,
   System.Object^ EndPoint
) 
```

#### Parameters

*Center*
:   Array containing 3 doubles for location of the center of the arc (x,y,z )

*Axis*
:   Array containing 3 doubles (x,y,z)

*Radius*
:   Arc radius

*StartPoint*
:   Array of 3 doubles (x,y,z)

*EndPoint*
:   Array of 3 doubles (x,y,z)

#### Return Value

[Curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Remarks

If your application uses [ISurface::CreateTrimmedSheet4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateTrimmedSheet4.md) or [ISurface::ICreateTrimmedSheet4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICreateTrimmedSheet4.md), then your application must also use [ICurve::CreateTrimmedCurve2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.md) for the curves created by IModeler::CreateArc or [IModeler::ICreateArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateArc.md) and [IModeler::CreateLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLine.md) or [IModeler::ICreateLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateLine.md).

Example

[Create Temporary Extruded Body (C#)](Create_Temporary_Extruded_Body_Example_CSharp.htm)  
[Create Temporary Extruded Body (VB.NET)](Create_Temporary_Extruded_Body_Example_VBNET.htm)  
[Create Temporary Extruded Body (VBA)](Create_Temporary_Extruded_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IBody2::AddProfileArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileArc.md)  
[IBody2::IAddProfileArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileArc.md)  
[IModeler::CreateEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateEllipse.md)  
[IModeler::ICreateEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateEllipse.md)
