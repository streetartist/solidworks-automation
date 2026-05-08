# IReverseEvaluate Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IReverseEvaluate`

Gets the UV parameters for the given XYZ location on this face.
Gets the UV parameters for the given XYZ location on this face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IReverseEvaluate( _
   ByVal PositionX As System.Double, _
   ByVal PositionY As System.Double, _
   ByVal PositionZ As System.Double _
) As System.Double
```

```

Dim instance As IFace2
Dim PositionX As System.Double
Dim PositionY As System.Double
Dim PositionZ As System.Double
Dim value As System.Double
 
value = instance.IReverseEvaluate(PositionX, PositionY, PositionZ)
```

```

System.double IReverseEvaluate( 
   System.double PositionX,
   System.double PositionY,
   System.double PositionZ
)
```

```

System.double IReverseEvaluate( 
   System.double PositionX,
   System.double PositionY,
   System.double PositionZ
) 
```

#### Parameters

*PositionX*
:   X coordinate of this location on the face

*PositionY*
:   Y coordinate of this location on the face

*PositionZ*
:   Z coordinate of this location on the face

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles for the U and V parameters
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

This method returns corrected UV parameters for periodic surfaces; thus, you should use this method when dealing with periodic surfaces.

For example, you can have a cylindrical surface that extends from 0 to 2pi in the Udir. The face related to this surface in some cases extends from 0 to pi, then from 0 to pi again. In this case, neither [ISurface::IReverseEvaluate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IReverseEvaluate.md) nor [ISurface::ReverseEvaluate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ReverseEvaluate.md) will work for values greater than pi (the returned U value will be greater than Maximum U for the face). However, IFace2::IReverseEvaluate, and [IFace2::ReverseEvaluate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ReverseEvaluate.md), will return the correct values.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[ICurve::ReverseEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ReverseEvaluate.md)
