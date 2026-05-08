# GetSystemValue2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemValue2`

Obsolete. See IDimension::GetSystemValue3 and IDimension::IGetSystemValue3.
Obsolete. See [IDimension::GetSystemValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemValue3.md) and [IDimension::IGetSystemValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetSystemValue3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSystemValue2( _
   ByVal ConfigName As System.String _
) As System.Double
```

```

Dim instance As IDimension
Dim ConfigName As System.String
Dim value As System.Double
 
value = instance.GetSystemValue2(ConfigName)
```

```

System.double GetSystemValue2( 
   System.string ConfigName
)
```

```

System.double GetSystemValue2( 
   System.String^ ConfigName
) 
```

#### Parameters

*ConfigName*
:   Name of configuration

#### Return Value

Value in system units

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)
