# AddFileOpenItem2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddFileOpenItem2`

Obsolete. Superseded by ISldWorks::AddFileOpenItem3.
Obsolete. Superseded by [ISldWorks::AddFileOpenItem3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddFileOpenItem3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddFileOpenItem2( _
   ByVal Cookie As System.Integer, _
   ByVal MethodName As System.String, _
   ByVal Description As System.String, _
   ByVal Extension As System.String _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim MethodName As System.String
Dim Description As System.String
Dim Extension As System.String
Dim value As System.Boolean
 
value = instance.AddFileOpenItem2(Cookie, MethodName, Description, Extension)
```

```

System.bool AddFileOpenItem2( 
   System.int Cookie,
   System.string MethodName,
   System.string Description,
   System.string Extension
)
```

```

System.bool AddFileOpenItem2( 
   System.int Cookie,
   System.String^ MethodName,
   System.String^ Description,
   System.String^ Extension
) 
```

#### Parameters

*Cookie*

*MethodName*

*Description*

*Extension*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
