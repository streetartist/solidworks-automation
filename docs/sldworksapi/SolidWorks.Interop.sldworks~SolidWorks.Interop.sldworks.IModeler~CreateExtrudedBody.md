# CreateExtrudedBody Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrudedBody`

Creates a temporary extruded body.
Creates a temporary extruded body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateExtrudedBody( _
   ByVal SheetBody As Body2, _
   ByVal Direction As MathVector, _
   ByVal Length As System.Double _
) As Body2
```

```

Dim instance As IModeler
Dim SheetBody As Body2
Dim Direction As MathVector
Dim Length As System.Double
Dim value As Body2
 
value = instance.CreateExtrudedBody(SheetBody, Direction, Length)
```

```

Body2 CreateExtrudedBody( 
   Body2 SheetBody,
   MathVector Direction,
   System.double Length
)
```

```

Body2^ CreateExtrudedBody( 
   Body2^ SheetBody,
   MathVector^ Direction,
   System.double Length
) 
```

#### Parameters

*SheetBody*
:   Sheet body that defines the profile for the temporary extruded body (see **Remarks**)

*Direction*
:   Direction of the axis for the temporary extruded body

*Length*
:   Length of the temporary extruded body

#### Return Value

Temporary extruded [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

Before calling this method:

1. Call [IModeler::CreateArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateArc.md), [IModeler::ICreateArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateArc.md), [IModeler::CreateEllipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateEllipse.md), [IModeler::ICreateEllipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateEllipse.md), [IModeler::CreateLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLine.md), or [IModeler::ICreateLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateLine.md) to create curves that define the profile of the body that you want to extrude.
2. Call [ICurve::CreateTrimmedCurve2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.md) to trim the curves of arcs and lines only.
3. Call [ISurface::CreateTrimmedSheet4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateTrimmedSheet4.md) or [ISurface::ICreateTrimmedSheet4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICreateTrimmedSheet4.md) to create the profile body, passing in either trimmed arcs and lines or untrimmed elliptical curves.
4. Set SheetBody to the profile body.

After calling this method, call [IBody2::Display3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Display3.md) to display the extrusion.

Example

[Create Temporary Elliptical Extrusion (C#)](Create_Temporary_Elliptical_Extrusion_CSharp.htm)  
[Create Temporary Elliptical Extrusion (VB.NET)](Create_Temporary_Elliptical_Extrusion_VBNET.htm)  
[Create Temporary Elliptical Extrusion (VBA)](Create_Temporary_Elliptical_Extrusion_Example_VB.htm)  
[Create Temporary Extruded Body (C#)](Create_Temporary_Extruded_Body_Example_CSharp.htm)  
[Create Temporary Extruded Body (VB.NET)](Create_Temporary_Extruded_Body_Example_VBNET.htm)  
[Create Temporary Extruded Body (VBA)](Create_Temporary_Extruded_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::CreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets2.md)  
[IModeler::CreateBodyFromBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox.md)  
[IModeler::CreateBodyFromCone Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCone.md)  
[IModeler::CreateBodyFromCyl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCyl.md)  
[IModeler::CreateBodyFromFaces2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromFaces2.md)  
[IModeler::CreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody3.md)  
[IModeler::CreateSweptBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptBody.md)  
[IModeler::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateWireBody.md)  
[IModeler::ICreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.md)  
[IModeler::ICreateBodyFromBox2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromBox2.md)  
[IModeler::ICreateBodyFromCone2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCone2.md)  
[IModeler::ICreateBodyFromCyl2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCyl2.md)  
[IModeler::ICreateBodyFromFaces3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces3.md)  
[IModeler::ICreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody3.md)  
[IModeler::ICreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateWireBody.md)
