# ICreateEllipse Method (IModeler)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateEllipse`

Creates a temporary elliptical curve.
Creates a temporary elliptical curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateEllipse( _
   ByRef Center As System.Double, _
   ByVal MajorRadius As System.Double, _
   ByVal MinorRadius As System.Double, _
   ByRef MajorAxis As System.Double, _
   ByRef MinorAxis As System.Double _
) As Curve
```

```

Dim instance As IModeler
Dim Center As System.Double
Dim MajorRadius As System.Double
Dim MinorRadius As System.Double
Dim MajorAxis As System.Double
Dim MinorAxis As System.Double
Dim value As Curve
 
value = instance.ICreateEllipse(Center, MajorRadius, MinorRadius, MajorAxis, MinorAxis)
```

```

Curve ICreateEllipse( 
   ref System.double Center,
   System.double MajorRadius,
   System.double MinorRadius,
   ref System.double MajorAxis,
   ref System.double MinorAxis
)
```

```

Curve^ ICreateEllipse( 
   System.double% Center,
   System.double MajorRadius,
   System.double MinorRadius,
   System.double% MajorAxis,
   System.double% MinorAxis
) 
```

#### Parameters

*Center*
:   - in-process, unmanaged C++: Pointer to an array of 3 doubles describing the location of the center of the ellipse

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*MajorRadius*
:   Major radius of ellipse

*MinorRadius*
:   Minor radius of ellipse

*MajorAxis*
:   - in-process, unmanaged C++: Pointer to an array of 3 doubles describing the major axis of the ellipse

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*MinorAxis*
:   - in-process, unmanaged C++: Pointer to an array of 3 doubles describing the minor axis of the ellipse
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

[Curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::CreateEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateEllipse.md)  
[IModeler::CreateArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateArc.md)  
[IModeler::ICreateArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateArc.md)  
[IModeler::CreateLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLine.md)  
[IModeler::ICreateLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateLine.md)  
[IModeler::CreateExtrudedBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrudedBody.md)
