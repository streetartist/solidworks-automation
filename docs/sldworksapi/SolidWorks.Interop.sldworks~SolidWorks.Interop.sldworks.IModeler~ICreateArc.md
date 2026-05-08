# ICreateArc Method (IModeler)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateArc`

Creates an arc.
Creates an arc.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateArc( _
   ByRef Center As System.Double, _
   ByRef Axis As System.Double, _
   ByVal Radius As System.Double, _
   ByRef StartPoint As System.Double, _
   ByRef EndPoint As System.Double _
) As Curve
```

```

Dim instance As IModeler
Dim Center As System.Double
Dim Axis As System.Double
Dim Radius As System.Double
Dim StartPoint As System.Double
Dim EndPoint As System.Double
Dim value As Curve
 
value = instance.ICreateArc(Center, Axis, Radius, StartPoint, EndPoint)
```

```

Curve ICreateArc( 
   ref System.double Center,
   ref System.double Axis,
   System.double Radius,
   ref System.double StartPoint,
   ref System.double EndPoint
)
```

```

Curve^ ICreateArc( 
   System.double% Center,
   System.double% Axis,
   System.double Radius,
   System.double% StartPoint,
   System.double% EndPoint
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

If your application uses [ISurface::CreateTrimmedSheet4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateTrimmedSheet4.md) or [ISurface::ICreateTrimmedSheet4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICreateTrimmedSheet4.md), then your application must also use [ICurve::CreateTrimmedCurve2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.md) for the curves created by [IModeler::CreateArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateArc.md) or IModeler::ICreateArc and [IModeler::CreateLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLine.md) or [IModeler::ICreateLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateLine.md).

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
