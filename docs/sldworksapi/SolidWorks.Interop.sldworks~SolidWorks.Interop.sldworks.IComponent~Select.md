# Select Method (IComponent)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~Select`

Obsolete. Superseded by IComponent2::Select3.
Obsolete. Superseded by [IComponent2::Select3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Select3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select( _
   ByVal AppendFlag As System.Boolean _
) As System.Boolean
```

```

Dim instance As IComponent
Dim AppendFlag As System.Boolean
Dim value As System.Boolean
 
value = instance.Select(AppendFlag)
```

```

System.bool Select( 
   System.bool AppendFlag
)
```

```

System.bool Select( 
   System.bool AppendFlag
) 
```

#### Parameters

*AppendFlag*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.md)  
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.md)
