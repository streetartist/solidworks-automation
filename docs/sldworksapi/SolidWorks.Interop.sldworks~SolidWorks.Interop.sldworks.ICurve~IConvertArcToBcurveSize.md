# IConvertArcToBcurveSize Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertArcToBcurveSize`

Gets the b-curve size for the arc's conversion given the coordinates of the two end points of a line.
Gets the b-curve size for the arc's conversion given the coordinates of the two end points of a line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IConvertArcToBcurveSize( _
   ByRef Center As System.Double, _
   ByRef Axis As System.Double, _
   ByRef Start As System.Double, _
   ByRef End As System.Double _
) As System.Integer
```

```

Dim instance As ICurve
Dim Center As System.Double
Dim Axis As System.Double
Dim Start As System.Double
Dim End As System.Double
Dim value As System.Integer
 
value = instance.IConvertArcToBcurveSize(Center, Axis, Start, End)
```

```

System.int IConvertArcToBcurveSize( 
   ref System.double Center,
   ref System.double Axis,
   ref System.double Start,
   ref System.double End
)
```

```

System.int IConvertArcToBcurveSize( 
   System.double% Center,
   System.double% Axis,
   System.double% Start,
   System.double% End
) 
```

#### Parameters

*Center*
:   Pointer to an array of doubles (x, y, z), the coordinates of the arc center

*Axis*
:   Pointer to an array of doubles (x, y, z), the normal vector of the arc

*Start*
:   Pointer to an array of doubles (x, y, z), the coordinates of the arc start point

*End*
:   Pointer to an array of doubles (x, y, z), the coordinates of the arc end point

#### Return Value

Size of the data necessary for the conversion to a b-curve

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::ConvertArcToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertArcToBcurve.md)  
[ICurve::ExtentCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ExtentCurve.md)  
[ICurve::GetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams.md)  
[ICurve::IGetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams.md)  
[ICurve::IGetBCurveParamsSize2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize2.md)  
[ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.md)  
[ICurve::MakeBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve.md)  
[ICurve::SimplifyBCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~SimplifyBCurve.md)  
[ICurve::IConvertLineToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertLineToBcurveSize.md)  
[ICurve::IConvertPcurveToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertPcurveToBcurveSize.md)  
[ICurve::ConvertLineToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertLineToBcurve.md)
