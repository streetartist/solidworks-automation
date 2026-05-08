# ISetUserValueIn2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetUserValueIn2`

Obsolete. Superseded by IDimension::ISetUserValueIn3.
Obsolete. Superseded by [IDimension::ISetUserValueIn3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetUserValueIn3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetUserValueIn2( _
   ByVal Doc As ModelDoc, _
   ByVal NewValue As System.Double, _
   ByVal WhichConfigurations As System.Integer _
) As System.Integer
```

```

Dim instance As IDimension
Dim Doc As ModelDoc
Dim NewValue As System.Double
Dim WhichConfigurations As System.Integer
Dim value As System.Integer
 
value = instance.ISetUserValueIn2(Doc, NewValue, WhichConfigurations)
```

```

System.int ISetUserValueIn2( 
   ModelDoc Doc,
   System.double NewValue,
   System.int WhichConfigurations
)
```

```

System.int ISetUserValueIn2( 
   ModelDoc^ Doc,
   System.double NewValue,
   System.int WhichConfigurations
) 
```

#### Parameters

*Doc*

*NewValue*

*WhichConfigurations*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)
