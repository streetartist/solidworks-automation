# IAddTrimmingLoop Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IAddTrimmingLoop`

Obsolete. Superseded by ISurface::IAddTrimmingLoop2.
Obsolete. Superseded by [ISurface::IAddTrimmingLoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IAddTrimmingLoop2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IAddTrimmingLoop( _
   ByVal CurveCount As System.Integer, _
   ByRef Order As System.Integer, _
   ByRef Dim As System.Integer, _
   ByRef Periodic As System.Integer, _
   ByRef NumKnots As System.Integer, _
   ByRef NumCtrlPoints As System.Integer, _
   ByRef Knots As System.Double, _
   ByRef CtrlPointDbls As System.Double _
) 
```

```

Dim instance As ISurface
Dim CurveCount As System.Integer
Dim Order As System.Integer
Dim Dim As System.Integer
Dim Periodic As System.Integer
Dim NumKnots As System.Integer
Dim NumCtrlPoints As System.Integer
Dim Knots As System.Double
Dim CtrlPointDbls As System.Double
 
instance.IAddTrimmingLoop(CurveCount, Order, Dim, Periodic, NumKnots, NumCtrlPoints, Knots, CtrlPointDbls)
```

```

void IAddTrimmingLoop( 
   System.int CurveCount,
   ref System.int Order,
   ref System.int Dim,
   ref System.int Periodic,
   ref System.int NumKnots,
   ref System.int NumCtrlPoints,
   ref System.double Knots,
   ref System.double CtrlPointDbls
)
```

```

void IAddTrimmingLoop( 
   System.int CurveCount,
   System.int% Order,
   System.int% Dim,
   System.int% Periodic,
   System.int% NumKnots,
   System.int% NumCtrlPoints,
   System.double% Knots,
   System.double% CtrlPointDbls
) 
```

#### Parameters

*CurveCount*

*Order*

*Dim*

*Periodic*

*NumKnots*

*NumCtrlPoints*

*Knots*

*CtrlPointDbls*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)
