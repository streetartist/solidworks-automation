# AddProfileLine Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~AddProfileLine`

Obsolete. Superseded by IBody2::AddProfileBLine.
Obsolete. Superseded by [IBody2::AddProfileBLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileLine.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddProfileLine( _
   ByVal RootPoint As System.Object, _
   ByVal Direction As System.Object _
) As System.Object
```

```

Dim instance As IBody
Dim RootPoint As System.Object
Dim Direction As System.Object
Dim value As System.Object
 
value = instance.AddProfileLine(RootPoint, Direction)
```

```

System.object AddProfileLine( 
   System.object RootPoint,
   System.object Direction
)
```

```

System.Object^ AddProfileLine( 
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
