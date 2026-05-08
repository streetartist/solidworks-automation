# IGetObjectByPersistReference2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference2`

Obsolete. Superseded by IModelDocExtension::IGetObjectByPersistReference3.
Obsolete. Superseded by [IModelDocExtension::IGetObjectByPersistReference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetObjectByPersistReference2( _
   ByVal Count As System.Integer, _
   ByRef PersistId As System.Byte, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim Count As System.Integer
Dim PersistId As System.Byte
Dim ErrorCode As System.Integer
Dim value As System.Object
 
value = instance.IGetObjectByPersistReference2(Count, PersistId, ErrorCode)
```

```

System.object IGetObjectByPersistReference2( 
   System.int Count,
   ref System.byte PersistId,
   out System.int ErrorCode
)
```

```

System.Object^ IGetObjectByPersistReference2( 
   System.int Count,
   System.byte% PersistId,
   [Out] System.int ErrorCode
) 
```

#### Parameters

*Count*

*PersistId*

*ErrorCode*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
