# CreateOLEObject Method (ISheet)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~CreateOLEObject`

Obsolete. Superseded by IModelDocExtension::CreateOLEObject and IModelDocExtension::ICreateOLEObject.
Obsolete. Superseded by [IModelDocExtension::CreateOLEObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateOLEObject.md) and [IModelDocExtension::ICreateOLEObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ICreateOLEObject.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateOLEObject( _
   ByVal Aspect As System.Integer, _
   ByVal Position As System.Object, _
   ByVal Buffer As System.Object _
) As System.Boolean
```

```

Dim instance As ISheet
Dim Aspect As System.Integer
Dim Position As System.Object
Dim Buffer As System.Object
Dim value As System.Boolean
 
value = instance.CreateOLEObject(Aspect, Position, Buffer)
```

```

System.bool CreateOLEObject( 
   System.int Aspect,
   System.object Position,
   System.object Buffer
)
```

```

System.bool CreateOLEObject( 
   System.int Aspect,
   System.Object^ Position,
   System.Object^ Buffer
) 
```

#### Parameters

*Aspect*

*Position*

*Buffer*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)
