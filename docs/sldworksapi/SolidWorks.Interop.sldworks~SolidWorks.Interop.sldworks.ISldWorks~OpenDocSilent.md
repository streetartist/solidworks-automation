# OpenDocSilent Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDocSilent`

Obsolete. Superseded by ISldWorks::OpenDoc6.
Obsolete. Superseded by [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function OpenDocSilent( _
   ByVal FileName As System.String, _
   ByVal Type As System.Integer, _
   ByRef Errors As System.Integer _
) As System.Object
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim Type As System.Integer
Dim Errors As System.Integer
Dim value As System.Object
 
value = instance.OpenDocSilent(FileName, Type, Errors)
```

```

System.object OpenDocSilent( 
   System.string FileName,
   System.int Type,
   out System.int Errors
)
```

```

System.Object^ OpenDocSilent( 
   System.String^ FileName,
   System.int Type,
   [Out] System.int Errors
) 
```

#### Parameters

*FileName*

*Type*

*Errors*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
