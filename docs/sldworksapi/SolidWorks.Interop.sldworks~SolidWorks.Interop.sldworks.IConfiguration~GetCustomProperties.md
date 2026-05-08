# GetCustomProperties Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetCustomProperties`

Obsolete. Superseded by IConfiguration::CustomPropertyManager.
Obsolete. Superseded by [IConfiguration::CustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CustomPropertyManager.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCustomProperties( _
   ByRef PropNames As System.Object, _
   ByRef PropValues As System.Object, _
   ByRef PropTypes As System.Object _
) As System.Integer
```

```

Dim instance As IConfiguration
Dim PropNames As System.Object
Dim PropValues As System.Object
Dim PropTypes As System.Object
Dim value As System.Integer
 
value = instance.GetCustomProperties(PropNames, PropValues, PropTypes)
```

```

System.int GetCustomProperties( 
   out System.object PropNames,
   out System.object PropValues,
   out System.object PropTypes
)
```

```

System.int GetCustomProperties( 
   [Out] System.Object^ PropNames,
   [Out] System.Object^ PropValues,
   [Out] System.Object^ PropTypes
) 
```

#### Parameters

*PropNames*

*PropValues*

*PropTypes*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)
