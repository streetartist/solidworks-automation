# ICreateOLEObject Method (ISheet)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~ICreateOLEObject`

Obsolete. Superseded by IModelDocExtension::CreateOLEObject and IModelDocExtension::ICreateOLEObject.
Obsolete. Superseded by [IModelDocExtension::CreateOLEObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateOLEObject.md) and [IModelDocExtension::ICreateOLEObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ICreateOLEObject.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateOLEObject( _
   ByVal Aspect As System.Integer, _
   ByRef Position As System.Double, _
   ByVal ByteCount As System.Integer, _
   ByRef Buffer As System.Byte _
) As System.Boolean
```

```

Dim instance As ISheet
Dim Aspect As System.Integer
Dim Position As System.Double
Dim ByteCount As System.Integer
Dim Buffer As System.Byte
Dim value As System.Boolean
 
value = instance.ICreateOLEObject(Aspect, Position, ByteCount, Buffer)
```

```

System.bool ICreateOLEObject( 
   System.int Aspect,
   ref System.double Position,
   System.int ByteCount,
   ref System.byte Buffer
)
```

```

System.bool ICreateOLEObject( 
   System.int Aspect,
   System.double% Position,
   System.int ByteCount,
   System.byte% Buffer
) 
```

#### Parameters

*Aspect*

*Position*

*ByteCount*

*Buffer*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)
