# GetOLEObjectSettings Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetOLEObjectSettings`

Obsolete. Superseded by ISwOLEObjectAspect, ISwOLEObject::Boundaries, ISWOLEObject::IGetBoundaries, ISwOLEObject::ISetBoundaries, ISwOLEObject::IGetBuffer, and ISwOLEObject::Buffer.
Obsolete. Superseded by I[SwOLEObjectAspect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~Aspect.md), [ISwOLEObject::Boundaries](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~Boundaries.md), [ISWOLEObject::IGetBoundaries](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~IGetBoundaries.md), [ISwOLEObject::ISetBoundaries](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~ISetBoundaries.md), [ISwOLEObject::IGetBuffer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~IGetBuffer.md), and [ISwOLEObject::Buffer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~Buffer.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetOLEObjectSettings( _
   ByVal Index As System.Integer, _
   ByRef ByteCount As System.Integer, _
   ByRef Aspect As System.Integer _
) As System.Object
```

```

Dim instance As ISheet
Dim Index As System.Integer
Dim ByteCount As System.Integer
Dim Aspect As System.Integer
Dim value As System.Object
 
value = instance.GetOLEObjectSettings(Index, ByteCount, Aspect)
```

```

System.object GetOLEObjectSettings( 
   System.int Index,
   out System.int ByteCount,
   out System.int Aspect
)
```

```

System.Object^ GetOLEObjectSettings( 
   System.int Index,
   [Out] System.int ByteCount,
   [Out] System.int Aspect
) 
```

#### Parameters

*Index*

*ByteCount*

*Aspect*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)
