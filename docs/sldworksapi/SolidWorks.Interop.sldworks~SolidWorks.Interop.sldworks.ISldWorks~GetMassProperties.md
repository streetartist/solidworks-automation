# GetMassProperties Method (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMassProperties`

Obsolete. Superseded by ISldWorks::GetMassProperties2 and ISldWorks::IGetMassProperties2.
Obsolete. Superseded by [ISldWorks::GetMassProperties2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMassProperties2.md) and [ISldWorks::IGetMassProperties2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetMassProperties2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMassProperties( _
   ByVal FilePathName As System.String, _
   ByVal ConfigurationName As System.String _
) As System.Object
```

```

Dim instance As ISldWorks
Dim FilePathName As System.String
Dim ConfigurationName As System.String
Dim value As System.Object
 
value = instance.GetMassProperties(FilePathName, ConfigurationName)
```

```

System.object GetMassProperties( 
   System.string FilePathName,
   System.string ConfigurationName
)
```

```

System.Object^ GetMassProperties( 
   System.String^ FilePathName,
   System.String^ ConfigurationName
) 
```

#### Parameters

*FilePathName*

*ConfigurationName*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
