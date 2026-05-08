# IAddComponent3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IAddComponent3`

Obsolete. Superseded by IAssemblyDoc::AddComponent4.
Obsolete. Superseded by [IAssemblyDoc::AddComponent4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponent4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddComponent3( _
   ByVal CompName As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As Component2
```

```

Dim instance As IAssemblyDoc
Dim CompName As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As Component2
 
value = instance.IAddComponent3(CompName, X, Y, Z)
```

```

Component2 IAddComponent3( 
   System.string CompName,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

Component2^ IAddComponent3( 
   System.String^ CompName,
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*CompName*

*X*

*Y*

*Z*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
