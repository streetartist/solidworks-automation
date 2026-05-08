# OpenDoc2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc2`

Obsolete. Superseded by ISldWorks::OpenDoc6.
Obsolete. Superseded by [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function OpenDoc2( _
   ByVal FileName As System.String, _
   ByVal Type As System.Integer, _
   ByVal ReadOnly As System.Boolean, _
   ByVal ViewOnly As System.Boolean, _
   ByVal Silent As System.Boolean, _
   ByRef Errors As System.Integer _
) As System.Object
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim Type As System.Integer
Dim ReadOnly As System.Boolean
Dim ViewOnly As System.Boolean
Dim Silent As System.Boolean
Dim Errors As System.Integer
Dim value As System.Object
 
value = instance.OpenDoc2(FileName, Type, ReadOnly, ViewOnly, Silent, Errors)
```

```

System.object OpenDoc2( 
   System.string FileName,
   System.int Type,
   System.bool ReadOnly,
   System.bool ViewOnly,
   System.bool Silent,
   out System.int Errors
)
```

```

System.Object^ OpenDoc2( 
   System.String^ FileName,
   System.int Type,
   System.bool ReadOnly,
   System.bool ViewOnly,
   System.bool Silent,
   [Out] System.int Errors
) 
```

#### Parameters

*FileName*

*Type*

*ReadOnly*

*ViewOnly*

*Silent*

*Errors*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
