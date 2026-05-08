# GetLightSourceExtProperty Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetLightSourceExtProperty`

Obsolete. Superseded by IModelDoc2::GetLightSourceExtProperty.
Obsolete. Superseded by [IModelDoc2::GetLightSourceExtProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceExtProperty.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLightSourceExtProperty( _
   ByVal ID As System.Integer, _
   ByVal PropertyId As System.Integer _
) As System.Object
```

```

Dim instance As IModelDoc
Dim ID As System.Integer
Dim PropertyId As System.Integer
Dim value As System.Object
 
value = instance.GetLightSourceExtProperty(ID, PropertyId)
```

```

System.object GetLightSourceExtProperty( 
   System.int ID,
   System.int PropertyId
)
```

```

System.Object^ GetLightSourceExtProperty( 
   System.int ID,
   System.int PropertyId
) 
```

#### Parameters

*ID*

*PropertyId*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
