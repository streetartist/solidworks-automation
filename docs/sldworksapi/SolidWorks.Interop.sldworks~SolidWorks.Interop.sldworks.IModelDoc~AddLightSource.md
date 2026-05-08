# AddLightSource Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~AddLightSource`

Obsolete. Superseded by IModelDoc2::AddLightSource.
Obsolete. Superseded by [IModelDoc2::AddLightSource](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightSource.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddLightSource( _
   ByVal IdName As System.String, _
   ByVal LTyp As System.Integer, _
   ByVal UserName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim IdName As System.String
Dim LTyp As System.Integer
Dim UserName As System.String
Dim value As System.Boolean
 
value = instance.AddLightSource(IdName, LTyp, UserName)
```

```

System.bool AddLightSource( 
   System.string IdName,
   System.int LTyp,
   System.string UserName
)
```

```

System.bool AddLightSource( 
   System.String^ IdName,
   System.int LTyp,
   System.String^ UserName
) 
```

#### Parameters

*IdName*

*LTyp*

*UserName*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
