# AddTrimmingLoop Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~AddTrimmingLoop`

Obsolete. Superseded by ISurface::AddTrimmingLoop2.
Obsolete. Superseded by [ISurface::AddTrimmingLoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~AddTrimmingLoop2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddTrimmingLoop( _
   ByVal NCrvs As System.Integer, _
   ByVal VOrder As System.Object, _
   ByVal VDim As System.Object, _
   ByVal VPeriodic As System.Object, _
   ByVal VNumKnots As System.Object, _
   ByVal VNumCtrlPoints As System.Object, _
   ByVal VKnots As System.Object, _
   ByVal VCtrlPointDbls As System.Object _
) As System.Boolean
```

```

Dim instance As ISurface
Dim NCrvs As System.Integer
Dim VOrder As System.Object
Dim VDim As System.Object
Dim VPeriodic As System.Object
Dim VNumKnots As System.Object
Dim VNumCtrlPoints As System.Object
Dim VKnots As System.Object
Dim VCtrlPointDbls As System.Object
Dim value As System.Boolean
 
value = instance.AddTrimmingLoop(NCrvs, VOrder, VDim, VPeriodic, VNumKnots, VNumCtrlPoints, VKnots, VCtrlPointDbls)
```

```

System.bool AddTrimmingLoop( 
   System.int NCrvs,
   System.object VOrder,
   System.object VDim,
   System.object VPeriodic,
   System.object VNumKnots,
   System.object VNumCtrlPoints,
   System.object VKnots,
   System.object VCtrlPointDbls
)
```

```

System.bool AddTrimmingLoop( 
   System.int NCrvs,
   System.Object^ VOrder,
   System.Object^ VDim,
   System.Object^ VPeriodic,
   System.Object^ VNumKnots,
   System.Object^ VNumCtrlPoints,
   System.Object^ VKnots,
   System.Object^ VCtrlPointDbls
) 
```

#### Parameters

*NCrvs*

*VOrder*

*VDim*

*VPeriodic*

*VNumKnots*

*VNumCtrlPoints*

*VKnots*

*VCtrlPointDbls*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)
