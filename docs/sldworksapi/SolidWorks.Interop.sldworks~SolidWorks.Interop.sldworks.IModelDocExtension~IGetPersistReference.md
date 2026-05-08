# IGetPersistReference Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetPersistReference`

Obsolete. Superseded by IModelDocExtension::IGetPersistReference3.
Obsolete. Superseded by [IModelDocExtension::IGetPersistReference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetPersistReference3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetPersistReference( _
   ByVal DipsObj As System.Object, _
   ByVal Count As System.Integer _
) As System.Byte
```

```

Dim instance As IModelDocExtension
Dim DipsObj As System.Object
Dim Count As System.Integer
Dim value As System.Byte
 
value = instance.IGetPersistReference(DipsObj, Count)
```

```

System.byte IGetPersistReference( 
   System.object DipsObj,
   System.int Count
)
```

```

System.byte IGetPersistReference( 
   System.Object^ DipsObj,
   System.int Count
) 
```

#### Parameters

*DipsObj*

*Count*

#### Return Value

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
