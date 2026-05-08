# IGetObjectByPersistReference Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference`

Obsolete. Superseded by IModelDocExtension::IGetObjectByPersistReference3.
Obsolete. Superseded by [IModelDocExtension::IGetObjectByPersistReference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetObjectByPersistReference( _
   ByVal Count As System.Integer, _
   ByRef PersistId As System.Byte _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim Count As System.Integer
Dim PersistId As System.Byte
Dim value As System.Object
 
value = instance.IGetObjectByPersistReference(Count, PersistId)
```

```

System.object IGetObjectByPersistReference( 
   System.int Count,
   ref System.byte PersistId
)
```

```

System.Object^ IGetObjectByPersistReference( 
   System.int Count,
   System.byte% PersistId
) 
```

#### Parameters

*Count*

*PersistId*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
