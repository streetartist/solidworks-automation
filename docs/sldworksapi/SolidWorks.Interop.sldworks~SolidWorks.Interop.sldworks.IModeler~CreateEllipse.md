# CreateEllipse Method (IModeler)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateEllipse`

Creates a temporary elliptical curve.
Creates a temporary elliptical curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateEllipse( _
   ByVal Center As System.Object, _
   ByVal MajorRadius As System.Double, _
   ByVal MinorRadius As System.Double, _
   ByVal MajorAxis As System.Object, _
   ByVal MinorAxis As System.Object _
) As System.Object
```

```

Dim instance As IModeler
Dim Center As System.Object
Dim MajorRadius As System.Double
Dim MinorRadius As System.Double
Dim MajorAxis As System.Object
Dim MinorAxis As System.Object
Dim value As System.Object
 
value = instance.CreateEllipse(Center, MajorRadius, MinorRadius, MajorAxis, MinorAxis)
```

```

System.object CreateEllipse( 
   System.object Center,
   System.double MajorRadius,
   System.double MinorRadius,
   System.object MajorAxis,
   System.object MinorAxis
)
```

```

System.Object^ CreateEllipse( 
   System.Object^ Center,
   System.double MajorRadius,
   System.double MinorRadius,
   System.Object^ MajorAxis,
   System.Object^ MinorAxis
) 
```

#### Parameters

*Center*
:   Array of 3 doubles describing the center of the ellipse

*MajorRadius*
:   Major radius of ellipse

*MinorRadius*
:   Minor radius of ellipse

*MajorAxis*
:   Array of 3 doubles describing the major axis of the ellipse

*MinorAxis*
:   Array of 3 doubles describing the minor axis of the ellipse

#### Return Value

[Curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Example

[Create Temporary Elliptical Extrusion (VBA)](Create_Temporary_Elliptical_Extrusion_Example_VB.htm)  
[Create Temporary Elliptical Extrusion (VB.NET)](Create_Temporary_Elliptical_Extrusion_VBNET.htm)  
[Create Temporary Elliptical Extrusion (C#)](Create_Temporary_Elliptical_Extrusion_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::CreateArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateArc.md)  
[IModeler::ICreateArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateArc.md)  
[IModeler::CreateLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLine.md)  
[IModeler::ICreateLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateLine.md)  
[IModeler::ICreateEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateEllipse.md)  
[IModeler::CreateExtrudedBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrudedBody.md)
