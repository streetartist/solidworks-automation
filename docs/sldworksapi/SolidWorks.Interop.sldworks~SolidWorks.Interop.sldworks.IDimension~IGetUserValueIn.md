# IGetUserValueIn Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetUserValueIn`

Obsolete. Superseded by IDimension::IGetUserValueIn2.
Obsolete. Superseded by [IDimension::IGetUserValueIn2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetUserValueIn2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetUserValueIn( _
   ByVal Doc As ModelDoc _
) As System.Double
```

```

Dim instance As IDimension
Dim Doc As ModelDoc
Dim value As System.Double
 
value = instance.IGetUserValueIn(Doc)
```

```

System.double IGetUserValueIn( 
   ModelDoc Doc
)
```

```

System.double IGetUserValueIn( 
   ModelDoc^ Doc
) 
```

#### Parameters

*Doc*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)
