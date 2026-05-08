# IGetMassProperties Method (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetMassProperties`

Obsolete. Superseded by ISldWorks::GetMassProperties2 and ISldWorks::IGetMassProperties2.
Obsolete. Superseded by [ISldWorks::GetMassProperties2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMassProperties2.md) and [ISldWorks::IGetMassProperties2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetMassProperties2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetMassProperties( _
   ByVal FilePathName As System.String, _
   ByVal ConfigurationName As System.String, _
   ByRef MPropsData As System.Double _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim FilePathName As System.String
Dim ConfigurationName As System.String
Dim MPropsData As System.Double
Dim value As System.Boolean
 
value = instance.IGetMassProperties(FilePathName, ConfigurationName, MPropsData)
```

```

System.bool IGetMassProperties( 
   System.string FilePathName,
   System.string ConfigurationName,
   ref System.double MPropsData
)
```

```

System.bool IGetMassProperties( 
   System.String^ FilePathName,
   System.String^ ConfigurationName,
   System.double% MPropsData
) 
```

#### Parameters

*FilePathName*

*ConfigurationName*

*MPropsData*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
