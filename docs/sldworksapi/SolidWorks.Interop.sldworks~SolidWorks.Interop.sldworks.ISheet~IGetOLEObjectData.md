# IGetOLEObjectData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetOLEObjectData`

Obsolete. Superseded by ISwOLEObject.
Obsolete. Superseded by [ISwOLEObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetOLEObjectData( _
   ByVal Index As System.Integer, _
   ByRef Buffer As System.Byte _
) As System.Boolean
```

```

Dim instance As ISheet
Dim Index As System.Integer
Dim Buffer As System.Byte
Dim value As System.Boolean
 
value = instance.IGetOLEObjectData(Index, Buffer)
```

```

System.bool IGetOLEObjectData( 
   System.int Index,
   out System.byte Buffer
)
```

```

System.bool IGetOLEObjectData( 
   System.int Index,
   [Out] System.byte Buffer
) 
```

#### Parameters

*Index*

*Buffer*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)
