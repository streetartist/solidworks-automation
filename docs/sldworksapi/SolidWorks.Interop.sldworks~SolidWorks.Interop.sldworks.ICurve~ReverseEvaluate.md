# ReverseEvaluate Method (ICurve)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ReverseEvaluate`

Gets the U parameter for the given XYZ location on this curve.
Gets the U parameter for the given XYZ location on this curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReverseEvaluate( _
   ByVal PositionX As System.Double, _
   ByVal PositionY As System.Double, _
   ByVal PositionZ As System.Double _
) As System.Double
```

```

Dim instance As ICurve
Dim PositionX As System.Double
Dim PositionY As System.Double
Dim PositionZ As System.Double
Dim value As System.Double
 
value = instance.ReverseEvaluate(PositionX, PositionY, PositionZ)
```

```

System.double ReverseEvaluate( 
   System.double PositionX,
   System.double PositionY,
   System.double PositionZ
)
```

```

System.double ReverseEvaluate( 
   System.double PositionX,
   System.double PositionY,
   System.double PositionZ
) 
```

#### Parameters

*PositionX*
:   X coordinate of this location on the curve

*PositionY*
:   Y coordinate of this location on the curve

*PositionZ*
:   Z coordinate of this location on the curve

#### Return Value

U parameter value for this location on the curve

Example

[Get UV Parameters for XYZ Location (VBA)](Get_UV_Parameters_For_XYZ_Location_Example_VB.htm)  
[Get UV Parameters for XYZ Location (VB.NET)](Get_UV_Parameters_For_XYZ_Location_Example_VBNET.htm)  
[Get UV Parameters for XYZ Location (C#)](Get_UV_Parameters_For_XYZ_Location_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[IFace2::ReverseEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ReverseEvaluate.md)  
[IFace2::IReverseEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IReverseEvaluate.md)
