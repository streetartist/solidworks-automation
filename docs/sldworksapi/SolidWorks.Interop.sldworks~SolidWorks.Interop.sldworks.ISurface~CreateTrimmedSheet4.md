# CreateTrimmedSheet4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateTrimmedSheet4`

Obsolete. Superseded by ISurface::CreateTrimmedSheet5.
Obsolete. Superseded by [ISurface::CreateTrimmedSheet5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateTrimmedSheet5.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateTrimmedSheet4( _
   ByVal Curves As System.Object, _
   ByVal PreserveAnalyticCurves As System.Boolean _
) As System.Object
```

```

Dim instance As ISurface
Dim Curves As System.Object
Dim PreserveAnalyticCurves As System.Boolean
Dim value As System.Object
 
value = instance.CreateTrimmedSheet4(Curves, PreserveAnalyticCurves)
```

```

System.object CreateTrimmedSheet4( 
   System.object Curves,
   System.bool PreserveAnalyticCurves
)
```

```

System.Object^ CreateTrimmedSheet4( 
   System.Object^ Curves,
   System.bool PreserveAnalyticCurves
) 
```

#### Parameters

*Curves*
:   Array of [curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) that represent the boundary of the sheet

*PreserveAnalyticCurves*
:   True to preserve analytic curves, false to store all trimming curves as SP-curves

#### Return Value

Temporary sheet [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

The array of curves represents all of the curves required to add the appropriate trimming loops to the surface. A null entry in the array represents the separation between loops.

The curves supplied are assumed to lie on the surface. If the curves are 2D curves, then they should be created using this surface.

If your application is creating a trimmed sheet body from a periodic surface without trimming curves, then the curve array must contain one entry: null or Nothing.

Before calling this method, trim the curves created by [IModeler::CreateArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateArc.md) and [IModeler::CreateLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLine.md) by calling [ICurve::CreateTrimmedCurve2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.md). Elliptical curves created by [IModeler::CreateEllipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateEllipse.md) do not need to be trimmed before calling this method.

Example

[Create Temporary Elliptical Extrusion (VBA)](Create_Temporary_Elliptical_Extrusion_Example_VB.htm)  
[Create Temporary Elliptical Extrusion (VB.NET)](Create_Temporary_Elliptical_Extrusion_VBNET.htm)  
[Create Temporary Elliptical Extrusion (C#)](Create_Temporary_Elliptical_Extrusion_CSharp.htm)  
[Fill Holes in Part (C#)](Fill_Holes_in_Part_Example_CSharp.htm)  
[Fill Holes in Part (VB.NET)](Fill_Holes_in_Part_Example_VBNET.htm)  
[Fill Holes in Part (VBA)](Fill_Holes_in_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::ICreateTrimmedSheet4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICreateTrimmedSheet4.md)
