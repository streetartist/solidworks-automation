# OpenDoc Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc`

Obsolete. Superseded by ISldWorks::OpenDoc6.
Obsolete. Superseded by [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function OpenDoc( _
   ByVal Name As System.String, _
   ByVal Type As System.Integer _
) As System.Object
```

```

Dim instance As ISldWorks
Dim Name As System.String
Dim Type As System.Integer
Dim value As System.Object
 
value = instance.OpenDoc(Name, Type)
```

```

System.object OpenDoc( 
   System.string Name,
   System.int Type
)
```

```

System.Object^ OpenDoc( 
   System.String^ Name,
   System.int Type
) 
```

#### Parameters

*Name*

*Type*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
