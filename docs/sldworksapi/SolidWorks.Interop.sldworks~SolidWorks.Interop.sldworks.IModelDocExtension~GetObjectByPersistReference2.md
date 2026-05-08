# GetObjectByPersistReference2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectByPersistReference2`

Obsolete. Superseded by IModelDocExtension::GetObjectByPersistReference3.
Obsolete. Superseded by [IModelDocExtension::GetObjectByPersistReference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectByPersistReference3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetObjectByPersistReference2( _
   ByVal PersistId As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim PersistId As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object
 
value = instance.GetObjectByPersistReference2(PersistId, ErrorCode)
```

```

System.object GetObjectByPersistReference2( 
   System.object PersistId,
   out System.int ErrorCode
)
```

```

System.Object^ GetObjectByPersistReference2( 
   System.Object^ PersistId,
   [Out] System.int ErrorCode
) 
```

#### Parameters

*PersistId*

*ErrorCode*
:   v

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
