# GetBSurfParams3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetBSurfParams3`

Gets the parameterization data for a B-spline surface.
Gets the parameterization data for a B-spline surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBSurfParams3( _
   ByVal WantCubic As System.Boolean, _
   ByVal WantNonRational As System.Boolean, _
   ByVal VP0 As System.Object, _
   ByVal Tolerance As System.Double, _
   ByRef Sense As System.Boolean _
) As BSurfParamData
```

```

Dim instance As ISurface
Dim WantCubic As System.Boolean
Dim WantNonRational As System.Boolean
Dim VP0 As System.Object
Dim Tolerance As System.Double
Dim Sense As System.Boolean
Dim value As BSurfParamData
 
value = instance.GetBSurfParams3(WantCubic, WantNonRational, VP0, Tolerance, Sense)
```

```

BSurfParamData GetBSurfParams3( 
   System.bool WantCubic,
   System.bool WantNonRational,
   System.object VP0,
   System.double Tolerance,
   out System.bool Sense
)
```

```

BSurfParamData^ GetBSurfParams3( 
   System.bool WantCubic,
   System.bool WantNonRational,
   System.Object^ VP0,
   System.double Tolerance,
   [Out] System.bool Sense
) 
```

#### Parameters

*WantCubic*
:   True if cubic is needed, false if not; specifying true converts any surface to a cubic B-spline surface

*WantNonRational*
:   True if non-rational is needed, false if not; specifying true converts any surface to a non-rational B-spline surface; if you specify true, then you should only use this method for surfaces that are of B-spline or blend type; otherwise, the underlying call is not made and the values returned from this are not initialized, or they contain the values from the last call

*VP0*
:   [ISurfaceParameterizationData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData.md)

*Tolerance*
:   Tolerance, in meters, between the approximated B-spline surface and the underlying surface; the default value is 0.01 and should generally be reduced to the tolerance desired

*Sense*
:   Approximated B-spline surface is not always in the same direction as the original surface; if Sense is true, then the underlying surface and the B-spline surface are in the same direction

#### Return Value

An [IBSurfParamData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData.md) object

Remarks

Before calling this method, call [ISurface:Parameterization2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~Parameterization2.md) to populate VP0.

If you want to use the B-spline surface in combination with its trim curves, you should use the [IFace2::GetTrimCurves2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurves2.md) method to extract both the trim curves and the B-spline surface. The [IFace2::GetTrimCurves2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurves2.md) method provides much better alignment of the trim curves with the B-spline surface, because they are both generated at the same time.

Example

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)  
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)  
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::IGetBSurfParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetBSurfParams.md)  
[ISurface::IGetBSurfParamsSize3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetBSurfParamsSize3.md)
