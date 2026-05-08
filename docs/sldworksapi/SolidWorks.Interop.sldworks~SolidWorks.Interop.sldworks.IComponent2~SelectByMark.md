# SelectByMark Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SelectByMark`

Obsolete. Superseded by IComponent2::Select3.
Obsolete. Superseded by [IComponent2::Select3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Select3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SelectByMark( _
   ByVal AppendFlag As System.Boolean, _
   ByVal Mark As System.Integer _
) As System.Boolean
```

```

Dim instance As IComponent2
Dim AppendFlag As System.Boolean
Dim Mark As System.Integer
Dim value As System.Boolean
 
value = instance.SelectByMark(AppendFlag, Mark)
```

```

System.bool SelectByMark( 
   System.bool AppendFlag,
   System.int Mark
)
```

```

System.bool SelectByMark( 
   System.bool AppendFlag,
   System.int Mark
) 
```

#### Parameters

*AppendFlag*

*Mark*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)
