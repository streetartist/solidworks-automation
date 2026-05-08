# ICreateBsplineSurface Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreateBsplineSurface`

Obsolete. Superseded by IBody2::ICreateBsplineSurface.
Obsolete. Superseded by [IBody2::ICreateBsplineSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBsplineSurface.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateBsplineSurface( _
   ByVal Props As System.Object, _
   ByVal UKnots As System.Object, _
   ByVal VKnots As System.Object, _
   ByVal CtrlPtCoords As System.Object _
) As Surface
```

```

Dim instance As IBody
Dim Props As System.Object
Dim UKnots As System.Object
Dim VKnots As System.Object
Dim CtrlPtCoords As System.Object
Dim value As Surface
 
value = instance.ICreateBsplineSurface(Props, UKnots, VKnots, CtrlPtCoords)
```

```

Surface ICreateBsplineSurface( 
   System.object Props,
   System.object UKnots,
   System.object VKnots,
   System.object CtrlPtCoords
)
```

```

Surface^ ICreateBsplineSurface( 
   System.Object^ Props,
   System.Object^ UKnots,
   System.Object^ VKnots,
   System.Object^ CtrlPtCoords
) 
```

#### Parameters

*Props*

*UKnots*

*VKnots*

*CtrlPtCoords*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
