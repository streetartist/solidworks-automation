# GetUVBounds Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetUVBounds`

Gets the values that describe the U, V bounds of this face.
Gets the values that describe the U, V bounds of this face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUVBounds() As System.Object
```

```

Dim instance As IFace2
Dim value As System.Object
 
value = instance.GetUVBounds()
```

```

System.object GetUVBounds()
```

```

System.Object^ GetUVBounds(); 
```

#### Return Value

Array (see **Remarks**)

Remarks

The return values bound an area of the surface in which the face is defined. You can determine the surface U, V bounds using [ISurface::Parameterization](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~Parameterization.md) or [ISurface::IParameterization](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IParameterization.md).

The returned data is an array of 4 doubles arranged in the following order:

retval[0] - Minimum U parameter of this face

retval[1] - Maximum U parameter of this face

retval[2] - Minimum V parameter of this face

retval[3] - Maximum V parameter of this face

The minimum parameters are always less than the maximum parameters, and the range (for example, retval[1] - retval[0] and retval[3]-retval[2]) is always less than or equal to the U and V range of the underlying surface.

For surfaces with periodic parameters, the face parameter box can never be larger than the period of the corresponding surface parameter.

uRange[0] <= retval[0] < uRange[1]

vRange[0] <= retval[2] < vRange[1]

where uRange and vRange describe the UV range of the surface

Therefore, a face that straddles the boundary of a periodic parameter has an upper parameter value for the face that is greater than the upper parameter range of the surface.

Example

[Create Trimmed Curve (VBA)](Return_Untrimmed_Curve_Example_VB.htm)  
[Create Trimmed Curve (VB.NET)](Return_Untrimmed_Curve_Example_VBNET.htm)  
[Create Trimmed Curve (C#)](Return_Untrimmed_Curve_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::IGetUVBounds Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetUVBounds.md)  
[IBody2::GetProcessedBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBody2.md)
