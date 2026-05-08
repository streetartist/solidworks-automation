# AddLightSourceExtProperty Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~AddLightSourceExtProperty`

Obsolete. Superseded by IModelDoc2::AddLightSourceExtProperty.
Obsolete. Superseded by [IModelDoc2::AddLightSourceExtProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightSourceExtProperty.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddLightSourceExtProperty( _
   ByVal ID As System.Integer, _
   ByVal PropertyExtension As System.Object _
) As System.Integer
```

```

Dim instance As IModelDoc
Dim ID As System.Integer
Dim PropertyExtension As System.Object
Dim value As System.Integer
 
value = instance.AddLightSourceExtProperty(ID, PropertyExtension)
```

```

System.int AddLightSourceExtProperty( 
   System.int ID,
   System.object PropertyExtension
)
```

```

System.int AddLightSourceExtProperty( 
   System.int ID,
   System.Object^ PropertyExtension
) 
```

#### Parameters

*ID*

*PropertyExtension*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
