# IGetBCurveParamsSize3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize3`

Gets the b-curve size.
Gets the b-curve size.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBCurveParamsSize3( _
   ByVal WantCubicIn As System.Boolean, _
   ByVal WantNRational As System.Boolean, _
   ByVal ForceNonPeriodic As System.Boolean _
) As System.Integer
```

```

Dim instance As ICurve
Dim WantCubicIn As System.Boolean
Dim WantNRational As System.Boolean
Dim ForceNonPeriodic As System.Boolean
Dim value As System.Integer
 
value = instance.IGetBCurveParamsSize3(WantCubicIn, WantNRational, ForceNonPeriodic)
```

```

System.int IGetBCurveParamsSize3( 
   System.bool WantCubicIn,
   System.bool WantNRational,
   System.bool ForceNonPeriodic
)
```

```

System.int IGetBCurveParamsSize3( 
   System.bool WantCubicIn,
   System.bool WantNRational,
   System.bool ForceNonPeriodic
) 
```

#### Parameters

*WantCubicIn*
:   True for cubic curves, false if not

*WantNRational*
:   True for non-rational curves, false if not

*ForceNonPeriodic*
:   True converts the curve to nonperiodic and returns parameters, false does not

#### Return Value

Size of the data set returned by [ICurve::IGetBCurveParams3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams3.md)

Remarks

Use this method to control the type of information returned in the subsequent call to [ICurve::IGetBCurveParams3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams3.md).

To control the accuracy of the curve data, see [IModeler::SetToleranceValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetToleranceValue.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::GetBCurveParams3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams3.md)
