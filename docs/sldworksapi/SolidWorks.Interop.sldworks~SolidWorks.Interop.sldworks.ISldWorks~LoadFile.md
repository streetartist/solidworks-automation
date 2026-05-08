# LoadFile Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile`

Obsolete. Superseded by ISldWorks::LoadFile4.
Obsolete. Superseded by [ISldWorks::LoadFile4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function LoadFile( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.LoadFile(FileName)
```

```

System.bool LoadFile( 
   System.string FileName
)
```

```

System.bool LoadFile( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
