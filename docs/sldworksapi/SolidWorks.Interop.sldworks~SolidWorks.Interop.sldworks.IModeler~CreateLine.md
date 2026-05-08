# CreateLine Method (IModeler)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLine`

Creates a line.
Creates a line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateLine( _
   ByVal RootPoint As System.Object, _
   ByVal Direction As System.Object _
) As System.Object
```

```

Dim instance As IModeler
Dim RootPoint As System.Object
Dim Direction As System.Object
Dim value As System.Object
 
value = instance.CreateLine(RootPoint, Direction)
```

```

System.object CreateLine( 
   System.object RootPoint,
   System.object Direction
)
```

```

System.Object^ CreateLine( 
   System.Object^ RootPoint,
   System.Object^ Direction
) 
```

#### Parameters

*RootPoint*
:   Array containing 3 doubles (x, y, z) for the start point of the line

*Direction*
:   Array containing 3 doubles (x, y, z) for the end point of the line

#### Return Value

Newly created [line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Remarks

If your application uses [ISurface::CreateTrimmedSheet4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateTrimmedSheet4.md) or [ISurface::ICreateTrimmedSheet4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICreateTrimmedSheet4.md), then your application must also use [ICurve::CreateTrimmedCurve2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.md) for the curves created by [IModeler::CreateArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateArc.md) or [IModeler::ICreateArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateArc.md) and IModeler::CreateLine or [IModeler::ICreateLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateLine.md).

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
[IModeler::CreateEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateEllipse.md)  
[IModeler::ICreateEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateEllipse.md)
