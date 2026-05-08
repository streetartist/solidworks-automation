# SetToleranceValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetToleranceValue`

Sets tolerances governing geometry output.
Sets tolerances governing geometry output.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetToleranceValue( _
   ByVal ToleranceID As System.Integer, _
   ByVal NewToleranceValue As System.Double _
) As System.Double
```

```

Dim instance As IModeler
Dim ToleranceID As System.Integer
Dim NewToleranceValue As System.Double
Dim value As System.Double
 
value = instance.SetToleranceValue(ToleranceID, NewToleranceValue)
```

```

System.double SetToleranceValue( 
   System.int ToleranceID,
   System.double NewToleranceValue
)
```

```

System.double SetToleranceValue( 
   System.int ToleranceID,
   System.double NewToleranceValue
) 
```

#### Parameters

*ToleranceID*
:   Type of tolerance you want to set as defined in [swTolerances\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolerances_e.html)

*NewToleranceValue*
:   New tolerance value in meters for the specified tolerance type

#### Return Value

Original value of the specified tolerance type

Remarks

The default tolerance setting for 3D geometry output is 0.01 meters, while 2D geometry uses a 1e-4 dimensionless tolerance value. If your 3D trim curves are coming out too far from the surfaces they are trimming or are not close to the 2D trim curves, then you might want to tighten the tolerance. Set the tolerances before any extraction of geometry.

The tolerance values can be reset by other AddIns such as IGES. Make sure that they are set to your values when you need them. The tolerance settings only affect other AddIn applications. However, you should be careful to reset the tolerances so that other AddIn applications are not affected by your choice of tolerance.

The swUVCurveOutputTol tolerance is used during the extraction of UV (SP) trim curves. The [IFace2::GetTrimCurves2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurves2.md) method is affected by this setting. This tolerance value represents a fraction of the characteristic small dimension of a face (the tolerance is dimensionless). For example, if you set the swUVCurveOutputTol tolerance value to 3e-6 and the smallest dimension of the face is 0.4 meters, then the largest deviation of the trim curve will be:

(0.4 x 3e-6) meters

For reference, the SOLIDWORKS IGES processor lets you control the swUVCurveOutputTol tolerance setting in the user preferences area. The normal setting under IGES uses a tolerance of 1e-4, while the high setting changes this tolerance to 3e-6. The IGES setting does not affect your application. Higher tolerance settings can increase processing time and the size of any output results.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::GetToleranceValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetToleranceValue.md)  
[IModeler::UnsetTolerances Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~UnsetTolerances.md)
