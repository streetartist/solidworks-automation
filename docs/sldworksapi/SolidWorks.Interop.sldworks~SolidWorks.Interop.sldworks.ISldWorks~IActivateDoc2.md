# IActivateDoc2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActivateDoc2`

Obsolete. Superseded by ISldWorks::ActivateDoc2 and ISldWorks::IActivateDoc3.
Obsolete. Superseded by [ISldWorks::ActivateDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateDoc2.md) and [ISldWorks::IActivateDoc3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActivateDoc3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IActivateDoc2( _
   ByVal Name As System.String, _
   ByVal Silent As System.Boolean, _
   ByRef Errors As System.Integer _
) As ModelDoc
```

```

Dim instance As ISldWorks
Dim Name As System.String
Dim Silent As System.Boolean
Dim Errors As System.Integer
Dim value As ModelDoc
 
value = instance.IActivateDoc2(Name, Silent, Errors)
```

```

ModelDoc IActivateDoc2( 
   System.string Name,
   System.bool Silent,
   out System.int Errors
)
```

```

ModelDoc^ IActivateDoc2( 
   System.String^ Name,
   System.bool Silent,
   [Out] System.int Errors
) 
```

#### Parameters

*Name*

*Silent*

*Errors*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
