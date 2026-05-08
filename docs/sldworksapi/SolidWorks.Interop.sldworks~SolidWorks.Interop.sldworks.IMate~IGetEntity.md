# IGetEntity Method (IMate)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate~IGetEntity`

Obsolete. Superseded by IMate2::MateEntity.
Obsolete. Superseded by [IMate2::MateEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MateEntity.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEntity( _
   ByVal WhichOne As System.Integer _
) As Entity
```

```

Dim instance As IMate
Dim WhichOne As System.Integer
Dim value As Entity
 
value = instance.IGetEntity(WhichOne)
```

```

Entity IGetEntity( 
   System.int WhichOne
)
```

```

Entity^ IGetEntity( 
   System.int WhichOne
) 
```

#### Parameters

*WhichOne*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate.md)  
[IMate Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate_members.md)
