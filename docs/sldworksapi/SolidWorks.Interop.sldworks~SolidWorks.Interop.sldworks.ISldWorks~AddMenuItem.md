# AddMenuItem Method (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem`

Obsolete. Superseded by ISldWorks::AddMenuItem3.
Obsolete. Superseded by [ISldWorks::AddMenuItem3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddMenuItem( _
   ByVal DocType As System.Integer, _
   ByVal Menu As System.String, _
   ByVal Postion As System.Integer, _
   ByVal CallbackModuleAndFcn As System.String _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim DocType As System.Integer
Dim Menu As System.String
Dim Postion As System.Integer
Dim CallbackModuleAndFcn As System.String
Dim value As System.Integer
 
value = instance.AddMenuItem(DocType, Menu, Postion, CallbackModuleAndFcn)
```

```

System.int AddMenuItem( 
   System.int DocType,
   System.string Menu,
   System.int Postion,
   System.string CallbackModuleAndFcn
)
```

```

System.int AddMenuItem( 
   System.int DocType,
   System.String^ Menu,
   System.int Postion,
   System.String^ CallbackModuleAndFcn
) 
```

#### Parameters

*DocType*

*Menu*

*Postion*

*CallbackModuleAndFcn*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
