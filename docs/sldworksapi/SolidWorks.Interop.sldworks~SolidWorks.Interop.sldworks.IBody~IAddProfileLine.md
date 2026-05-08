# IAddProfileLine Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IAddProfileLine`

Obsolete. Superseded by IBody2::IAddProfileLine.
Obsolete. Superseded by [IBody2::IAddProfileLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileLine.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddProfileLine( _
   ByVal RootPoint As System.Object, _
   ByVal Direction As System.Object _
) As Curve
```

```

Dim instance As IBody
Dim RootPoint As System.Object
Dim Direction As System.Object
Dim value As Curve
 
value = instance.IAddProfileLine(RootPoint, Direction)
```

```

Curve IAddProfileLine( 
   System.object RootPoint,
   System.object Direction
)
```

```

Curve^ IAddProfileLine( 
   System.Object^ RootPoint,
   System.Object^ Direction
) 
```

#### Parameters

*RootPoint*

*Direction*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
