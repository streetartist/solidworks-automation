# CircleParams Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CircleParams`

Gets the parameters of a curve that is a circle.
Gets the parameters of a curve that is a circle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property CircleParams As System.Object
```

```

Dim instance As ICurve
Dim value As System.Object
 
value = instance.CircleParams
```

```

System.object CircleParams {get;}
```

```

property System.Object^ CircleParams {
   System.Object^ get();
}
```

#### Property Value

Array of doubles (see **Remarks**)

Remarks

To determine if a circular edge is a complete circle or an arc, use [IEdge::GetCurveParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.md).

The return value is the following array of 7 double values:

[ center.x, center.y, center.z, axis.x, axis.y, axis.z, radius ]

Center and radius values are in meters.

Example

[Get Entities Attached to Cosmetic Thread (VBA)](Get_Entities_Attached_To_Cosmetic_Thread_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::IsCircle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsCircle.md)  
[ICurve::ICircleParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ICircleParams.md)  
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.md)
