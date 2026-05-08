# SetSystemValue2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue2`

Obsolete. Superseded by IDimension::SetSystemValue3.
Obsolete. Superseded by [IDimension::SetSystemValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSystemValue2( _
   ByVal NewValue As System.Double, _
   ByVal WhichConfigurations As System.Integer _
) As System.Integer
```

```

Dim instance As IDimension
Dim NewValue As System.Double
Dim WhichConfigurations As System.Integer
Dim value As System.Integer
 
value = instance.SetSystemValue2(NewValue, WhichConfigurations)
```

```

System.int SetSystemValue2( 
   System.double NewValue,
   System.int WhichConfigurations
)
```

```

System.int SetSystemValue2( 
   System.double NewValue,
   System.int WhichConfigurations
) 
```

#### Parameters

*NewValue*

*WhichConfigurations*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)
