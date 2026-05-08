# IOpenDoc5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IOpenDoc5`

Obsolete. Superseded by ISldWorks::OpenDoc6.
Obsolete. Superseded by [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IOpenDoc5( _
   ByVal FileName As System.String, _
   ByVal Type As System.Integer, _
   ByVal Options As System.Integer, _
   ByVal Configuration As System.String, _
   ByRef Errors As System.Integer _
) As ModelDoc2
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim Type As System.Integer
Dim Options As System.Integer
Dim Configuration As System.String
Dim Errors As System.Integer
Dim value As ModelDoc2
 
value = instance.IOpenDoc5(FileName, Type, Options, Configuration, Errors)
```

```

ModelDoc2 IOpenDoc5( 
   System.string FileName,
   System.int Type,
   System.int Options,
   System.string Configuration,
   out System.int Errors
)
```

```

ModelDoc2^ IOpenDoc5( 
   System.String^ FileName,
   System.int Type,
   System.int Options,
   System.String^ Configuration,
   [Out] System.int Errors
) 
```

#### Parameters

*FileName*

*Type*

*Options*

*Configuration*

*Errors*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
