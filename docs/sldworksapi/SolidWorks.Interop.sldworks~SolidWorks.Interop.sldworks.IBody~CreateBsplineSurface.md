# CreateBsplineSurface Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~CreateBsplineSurface`

Obsolete. Superseded by IBody2::CreateBsplineSurface.
Obsolete. Superseded by [IBody2::CreateBsplineSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBsplineSurface.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateBsplineSurface( _
   ByVal Props As System.Object, _
   ByVal UKnots As System.Object, _
   ByVal VKnots As System.Object, _
   ByVal CtrlPtCoords As System.Object _
) As System.Object
```

```

Dim instance As IBody
Dim Props As System.Object
Dim UKnots As System.Object
Dim VKnots As System.Object
Dim CtrlPtCoords As System.Object
Dim value As System.Object
 
value = instance.CreateBsplineSurface(Props, UKnots, VKnots, CtrlPtCoords)
```

```

System.object CreateBsplineSurface( 
   System.object Props,
   System.object UKnots,
   System.object VKnots,
   System.object CtrlPtCoords
)
```

```

System.Object^ CreateBsplineSurface( 
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
