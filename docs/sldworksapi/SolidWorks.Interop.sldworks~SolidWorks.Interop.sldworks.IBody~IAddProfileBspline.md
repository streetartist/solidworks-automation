# IAddProfileBspline Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IAddProfileBspline`

Obsolete. Superseded by IBody2::IAddProfileBspline.
Obsolete. Superseded by [IBody2::IAddProfileBspline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileBspline.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddProfileBspline( _
   ByVal Props As System.Object, _
   ByVal Knots As System.Object, _
   ByVal CtrlPtCoords As System.Object _
) As Curve
```

```

Dim instance As IBody
Dim Props As System.Object
Dim Knots As System.Object
Dim CtrlPtCoords As System.Object
Dim value As Curve
 
value = instance.IAddProfileBspline(Props, Knots, CtrlPtCoords)
```

```

Curve IAddProfileBspline( 
   System.object Props,
   System.object Knots,
   System.object CtrlPtCoords
)
```

```

Curve^ IAddProfileBspline( 
   System.Object^ Props,
   System.Object^ Knots,
   System.Object^ CtrlPtCoords
) 
```

#### Parameters

*Props*

*Knots*

*CtrlPtCoords*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
