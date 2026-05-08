# IAddProfileLineDLL Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IAddProfileLineDLL`

Obsolete. Superseded by IBody2::IAddProfileLineDLL.
Obsolete. Superseded by [IBody2::IAddProfileLineDLL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileLineDLL.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddProfileLineDLL( _
   ByRef RootPoint As System.Double, _
   ByRef Direction As System.Double _
) As Curve
```

```

Dim instance As IBody
Dim RootPoint As System.Double
Dim Direction As System.Double
Dim value As Curve
 
value = instance.IAddProfileLineDLL(RootPoint, Direction)
```

```

Curve IAddProfileLineDLL( 
   ref System.double RootPoint,
   ref System.double Direction
)
```

```

Curve^ IAddProfileLineDLL( 
   System.double% RootPoint,
   System.double% Direction
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
