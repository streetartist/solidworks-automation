# RemoveUserMenu Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveUserMenu`

Obsolete. Superseded by ISldWorks::RemoveMenu.
Obsolete. Superseded by [ISldWorks::RemoveMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenu.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveUserMenu( _
   ByVal DocType As System.Integer, _
   ByVal MenuIdIn As System.Integer, _
   ByVal ModuleName As System.String _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim DocType As System.Integer
Dim MenuIdIn As System.Integer
Dim ModuleName As System.String
Dim value As System.Boolean
 
value = instance.RemoveUserMenu(DocType, MenuIdIn, ModuleName)
```

```

System.bool RemoveUserMenu( 
   System.int DocType,
   System.int MenuIdIn,
   System.string ModuleName
)
```

```

System.bool RemoveUserMenu( 
   System.int DocType,
   System.int MenuIdIn,
   System.String^ ModuleName
) 
```

#### Parameters

*DocType*

*MenuIdIn*

*ModuleName*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
