# IGetCustomProperties Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetCustomProperties`

Obsolete. Superseded by IConfiguration::CustomPropertyManager.
Obsolete. Superseded by [IConfiguration::CustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CustomPropertyManager.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetCustomProperties( _
   ByVal NumProps As System.Integer, _
   ByRef PropNames As System.String, _
   ByRef PropValues As System.String, _
   ByRef PropTypes As System.Integer _
) 
```

```

Dim instance As IConfiguration
Dim NumProps As System.Integer
Dim PropNames As System.String
Dim PropValues As System.String
Dim PropTypes As System.Integer
 
instance.IGetCustomProperties(NumProps, PropNames, PropValues, PropTypes)
```

```

void IGetCustomProperties( 
   System.int NumProps,
   out System.string PropNames,
   out System.string PropValues,
   out System.int PropTypes
)
```

```

void IGetCustomProperties( 
   System.int NumProps,
   [Out] System.String^ PropNames,
   [Out] System.String^ PropValues,
   [Out] System.int PropTypes
) 
```

#### Parameters

*NumProps*

*PropNames*

*PropValues*

*PropTypes*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)
